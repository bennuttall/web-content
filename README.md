# Web content

The source of web content for my website [bennuttall.com](https://bennuttall.com) which is built
using my own static site generator called [beemo](https://github.com/bennuttall/beemo).

## Content

This repo contains content, static files and
[Chameleon](https://chameleon.readthedocs.io/en/latest/) templates for my website.

## Build

Requires [beemo](https://github.com/bennuttall/beemo) with the `logs` extra installed.

```bash
make build          # build the site
make logs           # process Apache logs into CSV
make analytics         # generate analytics report
make serve          # serve the site locally on port 8000
make serve-analytics   # serve the analytics report on port 8001
```

## Licences

Text content of posts in [content/posts](content/posts/) is Copyright Ben Nuttall, licenced under
[CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).

The site template and static files are copyright Ben Nuttall, with the exception of static files
from [WordPress](https://wordpress.org/) and [Foundation](https://get.foundation/).