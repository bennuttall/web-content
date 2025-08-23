This trick was inspired by [Brian Suda](http://twitter.com/briansuda) who I saw speak at [Whisky
Web](/blog/2012/04/whisky-web/).

1.  Take a string, any string.
2.  Hash it using [MD5](http://en.wikipedia.org/wiki/MD5).
3.  Substring the hash to get a 6-digit hex code.
4.  Take a look at what colour that hex code represents.

A really simple, really cool way of generating seemingly random colours, that can be used to
represent things.

I had a play with this idea and used it to generate a simple flag for any input string:  

```php
<?php

$thing = $_GET['thing'];

$md5 = md5($thing);

$col1 = substr($md5, 0, 6);
$col2 = substr($md5, 6, 6);
$col3 = substr($md5, 12, 6);

echo
    "<div style='float:left;width:100px;height:200px;background:#{$col1}'></div>\n" .
    "<div style='float:left;width:100px;height:200px;background:#{$col2}'></div>\n" 
    "<div style='float:left;width:100px;height:200px;background:#{$col3}'></div>";
```
  
This takes an input string via the GET method variable 'thing' and turns it in to a 3-stripe flag.
Examples:

(empty string):

<div style="float: left; width: 100px; height: 200px; background: #d41d8c;"></div>
<div style="float: left; width: 100px; height: 200px; background: #d98f00;"></div>
<div style="float: left; width: 100px; height: 200px; background: #b204e9;"></div>
<div style="clear: both;"></div>

`ben`:

<div style="float: left; width: 100px; height: 200px; background: #7fe477;"></div>
<div style="float: left; width: 100px; height: 200px; background: #1c008a;"></div>
<div style="float: left; width: 100px; height: 200px; background: #22eb76;"></div>
<div style="clear: both;"></div>

`bennuttall`:

<div style="float: left; width: 100px; height: 200px; background: #0d06cd;"></div>
<div style="float: left; width: 100px; height: 200px; background: #0fb632;"></div>
<div style="float: left; width: 100px; height: 200px; background: #c94f57;"></div>
<div style="clear: both;"></div>

`bennuttall.com`:

<div style="float: left; width: 100px; height: 200px; background: #3013b2;"></div>
<div style="float: left; width: 100px; height: 200px; background: #956149;"></div>
<div style="float: left; width: 100px; height: 200px; background: #dd4525;"></div>
<div style="clear: both;"></div>

The code is on GitHub:
[github.com/bennuttall/MD5-Flag-Generator/](https://github.com/bennuttall/MD5-Flag-Generator/)

Check out Brian's book *[Designing With Data](http://www.designingwithdata.com/)*