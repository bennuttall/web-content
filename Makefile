export BEEMO_CONFIG=config.yml

.PHONY: build logs analytics serve serve-analytics check-images

build:
	BEEMO_CONFIG=$(BEEMO_CONFIG) beemo build

logs:
	BEEMO_CONFIG=$(BEEMO_CONFIG) beemo logs

analytics:
	BEEMO_CONFIG=$(BEEMO_CONFIG) beemo analytics

serve:
	python -m http.server -d www 8000

serve-analytics:
	python -m http.server -d analytics 8000

check-images:
	@result=$$(find content static -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.gif" -o -iname "*.bmp" -o -iname "*.tiff" -o -iname "*.tif" \)); \
	if [ -n "$$result" ]; then \
		echo "Error: non-webp images found:"; \
		echo "$$result"; \
		exit 1; \
	fi