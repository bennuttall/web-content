[structa](https://github.com/waveform80/structa) is a hidden gem. It's one of many great utilities
created by [Dave Jones](https://twitter.com/waveform80). It's a command line tool for analysing JSON
files. Sometimes you need to inspect the structure of a large nested JSON file, and it's too
unwieldy to work out what kind of data it contains. structa is perfect for showing you.

The [People in Space API](http://open-notify.org/Open-Notify-API/People-In-Space/) shows the number
of people currently in space, and their names and craft name:

```
wget http://api.open-notify.org/astros.json
structa astros.json
```

Output:

```
├─ 'number': 5
├─ 'message': success
└─ 'people': [
   ├─ 'craft': ISS
   └─ 'name': {Doug Hurley|Bob Behnken|Chris Cassidy|Anatoly...}
]
```

As you can see, most of this data is static – so the values are just given as is. But the `people`
value is an array, so it shows the keys and the data types. Again, since `craft` is the same every
time, it's just given, but `name` varies, so the value is given as a set of the variations.

The [Python Package Index](https://pypi.org/) (PyPI) provides a JSON API for packages:

```
wget https://pypi.org/pypi/numpy/json -O numpy.json
structa numpy.json
```

Output:

```
├─ 'last_serial': 7391399
├─ 'urls': [
   ├─ 'requires_python': >=3.5
   ├─ 'filename': <str>
   ├─ 'yanked_reason': None
   ├─ 'comment_text':
   ├─ 'python_version': {cp36|source|cp35|cp38|cp37}
   ├─ 'md5_digest': <str 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh'>
   ├─ 'size': <int 5.2M..19.6M>
   ├─ 'downloads': -1
   ├─ 'url': <URL>
   ├─ 'has_sig': False
   ├─ 'upload_time': <datetime '%Y-%m-%dT%H:%M:%S' 2020-06-04 00:10:51..2020-06-04 00:27:58>
   ├─ 'upload_time_iso_8601': <str '2020-06-04T00:dd:dd.ddddddZ'>
   ├─ 'digests':
   │  ├─ 'md5': <str 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh'>
   │  └─ 'sha256': <str ...>
   ├─ 'packagetype': {sdist|bdist_wheel}
   └─ 'yanked': False
]
├─ 'info':
│  └─ <str>: <value>
└─ 'releases':
   └─ <str>: [
      ├─ 'requires_python': {>=3.5|>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*|>=3.6|None}
      ├─ 'filename': <str>
      ├─ 'yanked_reason': None
      ├─ 'comment_text': {|Simple installer, no SSE instructions. |Simple windows...}
      ├─ 'python_version': <str>
      ├─ 'md5_digest': <str 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh'>
      ├─ 'size': <int 1.8M..23.4M>
      ├─ 'downloads': -1
      ├─ 'url': <URL>
      ├─ 'has_sig': {False|True}
      ├─ 'upload_time': <datetime '%Y-%m-%dT%H:%M:%S' 2006-12-02 02:07:43..2020-06-04 00:35:35>
      ├─ 'upload_time_iso_8601': <str>
      ├─ 'digests':
      │  ├─ 'md5': <str 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh'>
      │  └─ 'sha256': <str ...>
      ├─ 'packagetype': {bdist_wheel|bdist_wininst|sdist}
      └─ 'yanked': False
   ]
```

Here you can see a wide variety of helpful information inferred from the data, including:

- Under `urls`:
  - `filename` is a string (too many options to show as a set)
  - `python_version` is always one of: `{cp36|source|cp35|cp38|cp37}`
  - `size` is an integer between 5.2 million and 19.6 million (bytes)
  - `md5_digest` is a 32-character hex string
  - `url` is detected as being a URL
  - `upload_time` is a datetime string in the format `'%Y-%m-%dT%H:%M:%S'` ranging between
    `2020-06-04 00:10:51` and `2020-06-04 00:27:58`
  - `packagetype` is either `sdist` or `bdist_wheel`
- Under `info`:
  - There's a variable `key` name, which contains a variety of values
- Under `releases`:
  - There's a variable key name, which contains an array...

Unfortunately, structa is not published on PyPI yet, so for now you have to install it from
[GitHub](https://github.com/waveform80/structa):

```
git clone https://github.com/waveform80/structa
cd structa
pip install .
```
