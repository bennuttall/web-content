Ever wanted to know how many visitors you've had to your website? Or wanted to know which pages,
articles or downloads are the most popular? If you're self-hosting your blog or website, whether you
use Apache, nginx or even IIS (yes, really), [lars](https://lars.readthedocs.io/en/latest/) is here
to help.

Lars is a web server log toolkit for Python. That means you can use Python to parse log files
retrospectively (or in real time), using simple code, and do whatever you want with the data – store
it in a database, save it as a CSV file, or analyze it right away using more Python.

Lars is another hidden gem written by [Dave Jones](https://twitter.com/waveform80/). I first saw
Dave present lars to a little group at the Python user group in Manchester. Then a few years later
we started using it in the [piwheels](https://www.piwheels.org/) project, to read in the Apache logs
and insert rows into our postgres database. In real-time, as Raspberry Pi users download Python
packages from piwheels.org, we log the filename, timestamp, system architecture (Arm version),
distro name/version, Python version and so on. Since it's a relational database we can join these
results onto other tables to get more contextual information about the file.

You can install lars with:

```
pip install lars
```

To get started, find a single web access log and make a copy of it. You'll want to download the log
file onto your computer to play around with. I'll be using Apache logs in my examples but with some
small (and obvious) alterations you can use nginx or IIS. On a typical web server you'll find Apache
logs in /var/log/apache2/ then usually `access.log`, `ssl_access.log` (for HTTPS), or gzipped
rotated logfiles like `access-20200101.gz` or `ssl_access-20200101.gz`.

To get started, find a single web access log and make a copy of it. You'll want to download the log
file onto your computer to play around with. I'll be using Apache logs in my examples but with some
small (and obvious) alterations you can use nginx or IIS.

First of all, what does a log entry look like?

```
81.174.152.222 - - [30/Jun/2020:23:38:03 +0000] "GET / HTTP/1.1" 200 6763 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0"
```

This is a request showing the IP address of the origin of the request, the timestamp, the requested
file path (in this case `/`, the homepage, the HTTP status code, the user agent (Firefox on Ubuntu)
and so on.

Your log files will be full of entries like this, not just every single page hit, but every file and
resource served — every CSS stylesheet, JavaScript file and image, every 404, every redirect, every
bot crawl. To get any sensible data out of your logs, you need to parse, filter and sort the
entries. That's what lars is for. This example will open a single log file and print the contents of
every row:

```python
with open('ssl_access.log') as f:
    with ApacheSource(f) as source:
        for row in source:
            print(row)
```

Which will show results like this for every log entry:

```python
Row(remote_host=IPv4Address('81.174.152.222'), ident=None, remote_user=None, time=DateTime(2020, 6, 30, 23, 38, 3), request=Request(method='GET', url=Url(scheme='', netloc='', path_str='/', params='', query_str='', fragment=''), protocol='HTTP/1.1'), status=200, size=6763)
```

You can see that it's parsed the log entry and put the data into a structured format. The entry has
become a [namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple)
with attributes relating to the entry data, so for example you can access the status code with
`row.status` and the path with `row.request.url.path_str`:

```python
with open('ssl_access.log') as f:
    with ApacheSource(f) as source:
        for row in source:
            print(f'hit {row.request.url.path_str} with status code {row.status}')
```

If you wanted to show only the 404s, you could do:

```python
with open('ssl_access.log') as f:
    with ApacheSource(f) as source:
        for row in source:
            if row.status == 404:
                print(row.request.url.path_str)
```

You might want to de-duplicate these and print the number of unique pages with 404s:

```python
s = set()
with open('ssl_access.log') as f:
    with ApacheSource(f) as source:
        for row in source:
            if row.status == 404:
                s.add(row.request.url.path_str)
print(len(s))
```

Dave and I have been working on expanding piwheels' logger to include web page hits, package
searches and more, and it's been a piece of cake thanks to lars. It's not going to tell us any
answers about our users – we still have to do the data analysis, but it's taken it from an awkward
file format and put it into our database in a way we can make best use of it.

Check out the [lars documentation](https://lars.readthedocs.io/en/latest/api.html) to see how to
read Apache, nginx and IIS logs, and what more you can do with it. Thanks yet again to Dave for
another great tool!
