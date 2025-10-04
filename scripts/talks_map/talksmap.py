#!/usr/bin/env python3
"""
Generate a map of talk locations from tables embedded in:
content/pages/talks/index.md

Supports:
 - HTML <table> blocks
 - Markdown pipe tables

Outputs:
 - talks_map.html
 - geocode_cache.json
"""

import json
import re
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import folium
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim

# ---------- CONFIG ----------
INPUT_FILE = Path("../content/pages/talks/index.md")
CACHE_FILE = Path("geocode_cache.json")
OUTPUT_FILE = Path("talks_map.html")
CENTER = [54.5, -3]  # roughly UK centre
ZOOM = 5
SLEEP_BETWEEN_GEOCODES = 1.0  # seconds
# ----------------------------


def load_cache() -> Dict[str, List[float]]:
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text())
        except Exception:
            return {}
    return {}


def save_cache(cache: Dict[str, List[float]]):
    CACHE_FILE.write_text(json.dumps(cache, indent=2))


# --- HTML table extraction (unchanged) ---
def extract_talks_from_html(html_text: str) -> List[Dict]:
    soup = BeautifulSoup(html_text, "html.parser")
    talks = []
    for table in soup.find_all("table"):
        for row in table.select("tbody tr"):
            cols = row.find_all("td")
            if len(cols) < 4:
                continue
            title = cols[0].get_text(strip=True)
            event = cols[1].get_text(strip=True)
            location = cols[2].get_text(strip=True)
            date = cols[3].get_text(strip=True)
            slides = None
            video = None
            if len(cols) > 4 and cols[4].find("a"):
                slides = cols[4].find("a").get("href")
            if len(cols) > 5 and cols[5].find("a"):
                video = cols[5].find("a").get("href")
            talks.append(
                {
                    "title": title,
                    "event": event,
                    "location": location,
                    "date": date,
                    "slides": slides,
                    "video": video,
                }
            )
    return talks


# --- Markdown table extraction ---
def is_md_table_separator(line: str) -> bool:
    # a separator line looks like: | ---- | :---: | --- |
    # we'll split and ensure each cell contains only - and optional leading/trailing :
    if "|" not in line:
        return False
    parts = [p.strip() for p in line.strip().strip("|").split("|")]
    if not parts:
        return False
    for p in parts:
        if not re.fullmatch(r":?-{3,}:?", p):
            return False
    return True


def extract_markdown_table_blocks(md_text: str) -> List[Tuple[str, List[str]]]:
    lines = md_text.splitlines()
    blocks = []
    i = 0
    while i < len(lines) - 1:
        line = lines[i]
        next_line = lines[i + 1] if i + 1 < len(lines) else ""
        if "|" in line and is_md_table_separator(next_line):
            header = line
            i += 2
            rows = []
            while i < len(lines) and ("|" in lines[i] and lines[i].strip() != ""):
                rows.append(lines[i])
                i += 1
            blocks.append((header, rows))
        else:
            i += 1
    return blocks


def extract_cells_from_md_row(line: str) -> List[str]:
    # strip leading/trailing pipe if present, then split
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return cells


def extract_link_from_markdown(cell: str) -> Optional[str]:
    # [text](url) or plain url inside
    m = re.search(r"\[.*?\]\((https?://[^\s)]+)\)", cell)
    if m:
        return m.group(1)
    m2 = re.search(r"(https?://[^\s\)]+)", cell)
    if m2:
        return m2.group(1).rstrip(".,)")
    return None


def map_headers_to_fields(headers: List[str]) -> Dict[int, str]:
    mapping = {}
    for i, h in enumerate(headers):
        key = h.strip().lower()
        key = re.sub(r"\s+", " ", key)
        if "talk" in key and "title" in key or key == "title" or "talk title" in key:
            mapping[i] = "title"
        elif "event" in key:
            mapping[i] = "event"
        elif "location" in key:
            mapping[i] = "location"
        elif "date" in key:
            mapping[i] = "date"
        elif "slide" in key:
            mapping[i] = "slides"
        elif "video" in key:
            mapping[i] = "video"
        else:
            mapping[i] = None
    return mapping


def extract_talks_from_markdown(md_text: str) -> List[Dict]:
    blocks = extract_markdown_table_blocks(md_text)
    talks = []
    for header, rows in blocks:
        headers = extract_cells_from_md_row(header)
        header_map = map_headers_to_fields(headers)
        for row in rows:
            cells = extract_cells_from_md_row(row)
            # pad cells if fewer than headers
            if len(cells) < len(headers):
                cells += [""] * (len(headers) - len(cells))
            data = {
                "title": None,
                "event": None,
                "location": None,
                "date": None,
                "slides": None,
                "video": None,
            }
            for idx, val in enumerate(cells):
                field = header_map.get(idx)
                if not field:
                    continue
                text = val.strip()
                if field in ("slides", "video"):
                    url = extract_link_from_markdown(text)
                    data[field] = url if url else (text if text.startswith("http") else None)
                else:
                    data[field] = text or None
            # require at least title, event, location, date
            if data["title"] and data["location"] and data["date"]:
                talks.append(data)
    return talks


# --- Combine & dedupe talks ---
def extract_all_talks(md_text: str) -> List[Dict]:
    # HTML tables may be embedded. Grab them and parse.
    html_tables = re.findall(r"<table.*?>.*?</table>", md_text, flags=re.DOTALL | re.IGNORECASE)
    html_talks = []
    for t in html_tables:
        html_talks.extend(extract_talks_from_html(t))

    # Markdown tables
    md_talks = extract_talks_from_markdown(md_text)

    # Combine & dedupe by (title,event,location,date)
    seen = set()
    combined = []
    for t in html_talks + md_talks:
        key = (
            (t.get("title") or "").strip(),
            (t.get("event") or "").strip(),
            (t.get("location") or "").strip(),
            (t.get("date") or "").strip(),
        )
        if key in seen:
            continue
        seen.add(key)
        combined.append(t)
    return combined


# --- Geocoding ---
def geocode_locations(talks: List[Dict]) -> List[Dict]:
    cache = load_cache()
    geolocator = Nominatim(user_agent="talks-map-script")
    for talk in talks:
        loc_text = (talk.get("location") or "").strip()
        if not loc_text:
            continue
        if loc_text in cache:
            talk["coords"] = cache[loc_text]
            continue
        try:
            result = geolocator.geocode(loc_text)
            if result:
                coords = [result.latitude, result.longitude]
                talk["coords"] = coords
                cache[loc_text] = coords
                print(f"✓ Geocoded: {loc_text} -> {coords}")
            else:
                print(f"✗ No geocode result for: {loc_text}")
        except Exception as e:
            print(f"⚠ Error geocoding '{loc_text}': {e}")
        save_cache(cache)
        time.sleep(SLEEP_BETWEEN_GEOCODES)
    return talks


# --- Grouping & Map building ---
def group_talks_by_coords(talks: List[Dict]) -> Dict[Tuple[float, float], List[Dict]]:
    grouped = {}
    for t in talks:
        if "coords" not in t:
            continue
        lat, lon = t["coords"][0], t["coords"][1]
        key = (round(lat, 6), round(lon, 6))
        grouped.setdefault(key, []).append(t)
    return grouped


def build_map(talks: List[Dict]):
    m = folium.Map(location=CENTER, zoom_start=ZOOM)
    grouped = group_talks_by_coords(talks)
    for (lat, lon), items in grouped.items():
        # Build popup HTML
        location_name = items[0].get("location") or ""
        lines = [f"<div><strong>{location_name}</strong><br><br>"]
        for idx, t in enumerate(items):
            lines.append(f"<strong>{t.get('title') or 'No title'}</strong><br>")
            if t.get("event"):
                lines.append(f"{t.get('event')}<br>")
            if t.get("date"):
                lines.append(f"{t.get('date')}<br>")
            links = []
            if t.get("slides"):
                links.append(f'<a href="{t["slides"]}">Slides</a>')
            if t.get("video"):
                links.append(f'<a href="{t["video"]}">Video</a>')
            if links:
                lines.append(" | ".join(links) + "<br>")
            if idx != len(items) - 1:
                lines.append("<hr>")
        lines.append("</div>")
        popup_html = "".join(lines)
        folium.Marker(
            location=(lat, lon),
            popup=folium.Popup(popup_html, max_width=450),
            tooltip=location_name,
        ).add_to(m)
    m.save(OUTPUT_FILE)
    print(f"Map saved to: {OUTPUT_FILE.resolve()}")


# --- Main ---
def main():
    if not INPUT_FILE.exists():
        print(f"Input file not found: {INPUT_FILE}")
        return

    md_text = INPUT_FILE.read_text()
    # quick counts for debug
    html_tables = re.findall(r"<table.*?>.*?</table>", md_text, flags=re.DOTALL | re.IGNORECASE)
    md_blocks = extract_markdown_table_blocks(md_text)
    print(f"Found {len(html_tables)} HTML table(s) and {len(md_blocks)} Markdown table(s).")

    talks = extract_all_talks(md_text)
    print(f"Extracted {len(talks)} talk(s) after deduplication.")

    if not talks:
        print("No talks found. Are your tables using a header row + separator like:")
        print("| A | B | C |")
        print("|---|---|---|")
        return

    talks = geocode_locations(talks)
    found_coords = sum(1 for t in talks if "coords" in t)
    print(f"Geocoded {found_coords}/{len(talks)} talk location(s).")

    build_map(talks)


if __name__ == "__main__":
    main()
