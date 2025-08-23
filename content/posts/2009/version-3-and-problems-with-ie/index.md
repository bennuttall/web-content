I decided I needed a new website template so I made one. Much better, don't you think?  
  
It's compliant with [W3C](http://www.w3c.org/) Web Standards ([XHTML 1.0
Strict](http://validator.w3.org/check?uri=http://www.bennuttall.com/) and [CSS
2.1](http://jigsaw.w3.org/css-validator/validator?uri=http://www.bennuttall.com/)) and I'm even
using PHP to render it using Server Side Includes, as well as a PHP email form on the
[contact](http://www.blogger.com/contact/) page. I've learned so much these last few months; a great
resource for web developers (beginner/intermediate/expert) is
[W3Schools](http://www.w3schools.com/) - it gives you all the information you need about every
single tag, every single CSS style, how each browser renders each element, and which tags and
attributes are permitted under each of the levels of markup (HTML/XHTML and
Frameset/Transitional/Strict).
  
The World Wide Web Consortium (W3C) is the international standards organization for the World
Wide Web, founded and headed by [Tim Berners-Lee](http://en.wikipedia.org/wiki/Tim_Berners-Lee).
  
Of all the people who converted to Firefox from Internet Explorer (IE), most of them know it's
better but they don't really know why. One of the main reasons it's better is that IE does not
comply with official W3C standards - it literally just ignores how things are supposed to work, and
does it its own way. Firefox, Chrome and the other browsers all comply which means that when someone
designs a website following the proper standards, as they're supposed to, it will look fine in
Firefox, Chrome, or whatever they're using, but then they open it in IE, some of the elements will
be displayed differently - something small like the spacing following a set of a bullet points - in
the good browsers there will be a reasonable space immediately after a set of bullets, but in IE
there will be no space. This can be resolved by adding the space manually using CSS, but that will
double the space shown in the good browsers - and why should they suffer because of IE's
incompetence? It should also be noted that if a website's code is valid, it will generally load
faster, run smoother on all browsers and systems, and (along with other factors) increase a site's
search engine optimisation.
  
One of the more famous bugs in IE is known as the [Internet Explorer box model
bug](http://en.wikipedia.org/wiki/Internet_Explorer_box_model_bug). This is a problem with the way
IE interprets the markup and style differently to the W3C standards; when you set the width of an
element, and then apply a margin, some padding and a border, IE will subtract the width of the
border and padding and the content width will be whatever is left, whereas the W3C way is to declare
the width, then add the padding, border and margin to it. IE's way means that if the sum of the
margin, border and padding is greater than half of the width (half because it counts on both sides
so can be doubled) then you are left with a negative width, which is impossible, so it just
disappears! The diagram below should explain this clearer:

<figure class="wp-block-image">
<a href="http://upload.wikimedia.org/wikipedia/commons/b/bd/W3C_and_Internet_Explorer_box_models.png"><img src="http://upload.wikimedia.org/wikipedia/commons/b/bd/W3C_and_Internet_Explorer_box_models.png" /></a>
</figure>
  
It's things like this that make web design much harder than it should be, because although everyone
should use good browsers like Chrome or Firefox (or even Safari), unfortunately the web browser
market is clearly dominated by IE with 66% because most people know no other way because they are
trapped in Microsoft land. That will change, eventually, I hope.  