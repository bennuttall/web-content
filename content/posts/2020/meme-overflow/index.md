A few months ago I was looking through questions posted to the [Raspberry Pi Stack Exchange
site](https://raspberrypi.stackexchange.com/). If you're not familiar, [Stack
Exchange](https://stackexchange.com/) provides Q&A sites like Stack Overflow for specific areas,
such as particular programming languages, technologies or other topics. And while observing the
erratic nature of the way people post questions to the site, I thought "wouldn't it be funny to take
questions from Stack Exchange and put them on meme templates?" and it seemed like a trivial enough
task to automate, so I started googling things, and typing stuff into a Python shell, and within an
hour or so I had it working. The results were random and hilarious, as I expected.

<div class="gallery">
<figure id="gallery-18">
<img src="images/WhatsApp-Image-2019-02-20-at-12.24.38-AM-1.webp" />
</figure>

<figure id="gallery-19">
<img src="images/WhatsApp-Image-2019-02-20-at-12.24.38-AM-2.webp" />
</figure>

<figure id="gallery-20">
<img src="images/WhatsApp-Image-2019-02-20-at-12.24.38-AM-3.webp" />
</figure>

<figure id="gallery-21">
<img src="images/WhatsApp-Image-2019-02-20-at-12.24.38-AM.webp" />
</figure>

<div class="gallery-thumbs">
<a href="#gallery-18"><img src="images/WhatsApp-Image-2019-02-20-at-12.24.38-AM-1.webp" /></a>
<a href="#gallery-19"><img src="images/WhatsApp-Image-2019-02-20-at-12.24.38-AM-2.webp" /></a>
<a href="#gallery-20"><img src="images/WhatsApp-Image-2019-02-20-at-12.24.38-AM-3.webp" /></a>
<a href="#gallery-21"><img src="images/WhatsApp-Image-2019-02-20-at-12.24.38-AM.webp" /></a>
</div>
</div>

Sometimes ideas like this seem simple in theory, but in practice there's some complexity you didn't
think of that gets in the way. But with this idea, everything was smooth sailing. I found the [Stack
Exchange API](https://api.stackexchange.com/) easy to use, and came across the
[imgflip](https://imgflip.com/) site, which provides an [API](https://api.imgflip.com/). All I
needed to be able to do was retrieve question titles from a particular Stack Exchange site, and to
add text to a random meme template. Both of these things were trivial, and as I've done a lot of
things using web APIs in Python lately, all the skills were [well
practised](https://en.wikipedia.org/wiki/Kata), which helps a lot.

Once the concept was proven, I decided to set up a Twitter account for the memes. I added code to
tweet the images. Again, this is something I've done a lot of, so no hassle. I forget how long it
took to get the app approved and the bot working, but before long,
[@pi_stack](https://twitter.com/pi_stack/) was tweeting out memes autonomously.

## Hit and miss

Meme templates are chosen randomly, so obviously not every question / meme combination will work.
Some will never be funny, some won't be a good match, some will end up on a template that doesn't
really work. Over time I got to see which meme templates would never work, and blacklisted them. I
also made sure that text was placed in the correct position for most effect: some templates work
better with the text in the second or third position than the first – and as I only have one piece
of text to add, this makes all the difference.

Later I decided to add some logic to choose the right meme template based on simple rules like
"starts with X", or to use a different template if it "doesn't end in Y". This seemed to make a big
difference, though it's still very hit-and-miss.

## The test suite

I decided to create a test suite so I could more confidently make changes to the library without
risking breaking things. Even though this is a silly side project, it's been another way for me to
exercise good practice which makes it easier when you need to do this stuff for real.

In [gpiozero](https://github.com/gpiozero/gpiozero) we have a mock pin interface which allows us to
test the workings of the library without running on real Raspberry Pi hardware. And in the test
suite we use patch to mock behaviour. I had to learn some new techniques for mocking things like web
requests, image uploads and even tweets. I'm sure my methods are far from perfect but it's a decent
attempt with good coverage. Check out the
[tests](https://github.com/bennuttall/meme-overflow/tree/master/tests) and
[coverage](https://codecov.io/github/bennuttall/meme-overflow).

## Instances

I started with the Raspberry Pi Stack Exchange, and later added other instances:

- [@pi_stack](https://twitter.com/pi_stack) (Raspberry Pi)
- [@overflow_meme](https://twitter.com/overflow_meme) (Stack Overflow)
- [@worldbuildingme](https://twitter.com/worldbuildingme) (World Building)
- [@askubuntumemes](https://twitter.com/askubuntumemes) (Ask Ubuntu)
- [@stackamemia](https://twitter.com/stackamemia) (Academia)

If you're not familiar with the concept of "world building", it's for people who are designing
worlds for books, stories, games and such – and have questions like "[What is keeping my Terror Bird
from being the size of a T.
Rex?](https://worldbuilding.stackexchange.com/questions/124928/what-is-keeping-my-terror-bird-from-being-the-size-of-a-t-rex)"
which are perfect for this project.

I've tried to set up more (there are so many great Stack Exchange sites) but Twitter is not letting
me authenticate more accounts with the same mobile number.

## Best in show

Here are some examples that worked well:

<div class="gallery">
<figure id="gallery-1">
<img src="images/D0jcpZKXgAEGmr4.webp" />
</figure>

<figure id="gallery-2">
<img src="images/D_cgx6DWwAM9Ee2.webp" />
</figure>

<figure id="gallery-3">
<img src="images/Dz3SAxFWwAIDglN.webp" />
</figure>

<figure id="gallery-5">
<img src="images/ECF8KEBXkAARLkQ.webp" />
</figure>

<figure id="gallery-6">
<img src="images/EFiUDafXYAAZjvt.webp" />
</figure>

<figure id="gallery-7">
<img src="images/EFpkFuJWsAAyjGT-700x467.webp" />
</figure>

<figure id="gallery-8">
<img src="images/EORlxwoX4AAJuTY.webp" />
</figure>

<figure id="gallery-9">
<img src="images/EOuZpfXXUAACDUV.webp" />
</figure>

<figure id="gallery-10">
<img src="images/EPPToZ5WAAAyTU4.webp" />
</figure>

<figure id="gallery-11">
<img src="images/EQ_7k9uWoAYHbZG.webp" />
</figure>

<figure id="gallery-12">
<img src="images/ER-Oi2WsAAMYw2.webp" />
</figure>

<figure id="gallery-13">
<img src="images/ERDLAYpWoAActNe.webp" />
</figure>

<figure id="gallery-14">
<img src="images/ERGqxv6WAAETFHH.webp" />
</figure>

<figure id="gallery-16">
<img src="images/ERTUd0BWoAEFmf_.webp" />
</figure>

<figure id="gallery-17">
<img src="images/ERxLGs3W4AEuKZ_.webp" />
</figure>

<div class="gallery-thumbs">
<a href="#gallery-1"><img src="images/D0jcpZKXgAEGmr4.webp" /></a>
<a href="#gallery-2"><img src="images/D_cgx6DWwAM9Ee2.webp" /></a>
<a href="#gallery-3"><img src="images/Dz3SAxFWwAIDglN.webp" /></a>
<a href="#gallery-5"><img src="images/ECF8KEBXkAARLkQ.webp" /></a>
<a href="#gallery-6"><img src="images/EFiUDafXYAAZjvt.webp" /></a>
<a href="#gallery-7"><img src="images/EFpkFuJWsAAyjGT-700x467.webp" /></a>
<a href="#gallery-8"><img src="images/EORlxwoX4AAJuTY.webp" /></a>
<a href="#gallery-9"><img src="images/EOuZpfXXUAACDUV.webp" /></a>
<a href="#gallery-10"><img src="images/EPPToZ5WAAAyTU4.webp" /></a>
<a href="#gallery-11"><img src="images/EQ_7k9uWoAYHbZG.webp" /></a>
<a href="#gallery-12"><img src="images/ER-Oi2WsAAMYw2.webp" /></a>
<a href="#gallery-13"><img src="images/ERDLAYpWoAActNe.webp" /></a>
<a href="#gallery-14"><img src="images/ERGqxv6WAAETFHH.webp" /></a>
<a href="#gallery-16"><img src="images/ERTUd0BWoAEFmf_.webp" /></a>
<a href="#gallery-17"><img src="images/ERxLGs3W4AEuKZ_.webp" /></a>
</div>
</div>

One of the best ones ever was extremely unlikely. It was a template that almost never works, because
it really requires two pieces of text to make sense. But in this one case, it was perfect. In the
RPi.GPIO library, Python warnings are switched on by default, and you have to turn them off. Most
people find them annoying and include the line that disables them. The problem with Python warnings
is that they look like errors/exceptions – people see red text and think there's something wrong
with their program – when really it's working fine but it's just letting them know something
unimportant like they've already configured that pin. So someone on Raspberry Pi asked about the
warning message, posting just the warning text (verbatim) as the question title, where the desired
outcome is that no warning is output. And – by chance – this subtle genius comes out of Meme
Overflow:

<figure class="wp-block-image">
<img src="images/EAG__56XsAI8VJ0.webp" />
<figcaption>The perfect RPi.GPIO meme</figcaption>
</figure>

Another recent one was from World Building. Again, completely random:

<figure class="wp-block-image">
<img src="images/ERQK46XW4Acpk9H.webp" />
</figure>

## Is anyone following?

The Stack Overflow bot is the most popular, with nearly 500 followers at the time of writing.
Raspberry Pi and Ask Ubuntu have over 100 each.

## Run your own instance

If you want to run your own bot following a particular Stack Exchange site, you can
[`pip install memeoverflow`](https://pypi.org/project/memeoverflow/) and use the example script,
following the [simple guide](https://github.com/bennuttall/meme-overflow/blob/main/README.md).

If you want to run a modified version, you can either [fork the
project](https://github.com/bennuttall/meme-overflow) or subclass the provided class.

<figure class="wp-block-image">
<img src="images/EPPToZ5WAAAyTU4.webp" />
<figcaption>docker exec(utive order)</figcaption>
</figure>
