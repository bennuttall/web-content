A few months ago I was looking through questions posted to the [Raspberry Pi Stack Exchange
site](https://raspberrypi.stackexchange.com/). If you're not familiar, [Stack
Exchange](https://stackexchange.com/) provides Q&A sites like Stack Overflow for specific areas,
such as particular programming languages, technologies or other topics. And while observing the
erratic nature of the way people post questions to the site, I thought "wouldn't it be funny to take
questions from Stack Exchange and put them on meme templates?" and it seemed like a trivial enough
task to automate, so I started googling things, and typing stuff into a Python shell, and within an
hour or so I had it working. The results were random and hilarious, as I expected.

<figure class="wp-block-gallery columns-3 is-cropped wp-block-gallery-4 is-layout-flex wp-block-gallery-is-layout-flex"><ul class="blocks-gallery-grid"><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2601" data-full-url="https://bennuttall.com/wp-content/uploads/2020/02/WhatsApp-Image-2019-02-20-at-12.24.38-AM-1.jpeg" data-id="2601" data-link="https://bennuttall.com/?attachment_id=2601" decoding="async" height="333" loading="lazy" sizes="auto, (max-width: 500px) 100vw, 500px" src="images/WhatsApp-Image-2019-02-20-at-12.24.38-AM-1.jpeg" width="500"/></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2602" data-full-url="https://bennuttall.com/wp-content/uploads/2020/02/WhatsApp-Image-2019-02-20-at-12.24.38-AM-2.jpeg" data-id="2602" data-link="https://bennuttall.com/?attachment_id=2602" decoding="async" height="720" loading="lazy" sizes="auto, (max-width: 363px) 100vw, 363px" src="images/WhatsApp-Image-2019-02-20-at-12.24.38-AM-2.jpeg" width="363"/></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2603" data-full-url="https://bennuttall.com/wp-content/uploads/2020/02/WhatsApp-Image-2019-02-20-at-12.24.38-AM-3.jpeg" data-id="2603" data-link="https://bennuttall.com/?attachment_id=2603" decoding="async" height="1024" loading="lazy" sizes="auto, (max-width: 460px) 100vw, 460px" src="images/WhatsApp-Image-2019-02-20-at-12.24.38-AM-3-460x1024.jpeg" width="460"/></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2604" data-full-url="https://bennuttall.com/wp-content/uploads/2020/02/WhatsApp-Image-2019-02-20-at-12.24.38-AM.jpeg" data-id="2604" data-link="https://bennuttall.com/?attachment_id=2604" decoding="async" height="600" loading="lazy" sizes="auto, (max-width: 423px) 100vw, 423px" src="images/WhatsApp-Image-2019-02-20-at-12.24.38-AM.jpeg" width="423"/></figure></li></ul><figcaption class="blocks-gallery-caption">First attempts</figcaption></figure>

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

<figure class="wp-block-gallery aligncenter columns-3 is-cropped wp-block-gallery-5 is-layout-flex wp-block-gallery-is-layout-flex"><ul class="blocks-gallery-grid"><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2605" data-full-url="https://bennuttall.com/wp-content/uploads/2020/03/D_cgx6DWwAM9Ee2.jpg" data-id="2605" data-link="https://bennuttall.com/?attachment_id=2605" decoding="async" height="375" loading="lazy" sizes="auto, (max-width: 500px) 100vw, 500px" src="images/D_cgx6DWwAM9Ee2.jpg" width="500"/></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2606" data-full-url="https://bennuttall.com/wp-content/uploads/2020/03/D0jcpZKXgAEGmr4.jpg" data-id="2606" data-link="https://bennuttall.com/?attachment_id=2606" decoding="async" height="500" loading="lazy" sizes="auto, (max-width: 500px) 100vw, 500px" src="images/D0jcpZKXgAEGmr4.jpg" width="500"/></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2607" data-full-url="https://bennuttall.com/wp-content/uploads/2020/03/Dz3SAxFWwAIDglN.jpg" data-id="2607" data-link="https://bennuttall.com/?attachment_id=2607" decoding="async" height="414" loading="lazy" sizes="auto, (max-width: 552px) 100vw, 552px" src="images/Dz3SAxFWwAIDglN.jpg" width="552"/></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2608" data-full-url="https://bennuttall.com/wp-content/uploads/2020/03/ECF8KEBXkAARLkQ.jpg" data-id="2608" data-link="https://bennuttall.com/?attachment_id=2608" decoding="async" height="350" loading="lazy" sizes="auto, (max-width: 500px) 100vw, 500px" src="images/ECF8KEBXkAARLkQ.jpg" width="500"/></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2609" data-full-url="https://bennuttall.com/wp-content/uploads/2020/03/EFiUDafXYAAZjvt.jpg" data-id="2609" data-link="https://bennuttall.com/?attachment_id=2609" decoding="async" height="500" loading="lazy" sizes="auto, (max-width: 518px) 100vw, 518px" src="images/EFiUDafXYAAZjvt.jpg" width="518"/></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2610" data-full-url="https://bennuttall.com/wp-content/uploads/2020/03/EFpkFuJWsAAyjGT.jpg" data-id="2610" data-link="https://bennuttall.com/?attachment_id=2610" decoding="async" height="467" loading="lazy" sizes="auto, (max-width: 700px) 100vw, 700px" src="images/EFpkFuJWsAAyjGT-700x467.jpg" width="700"/></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2611" data-full-url="https://bennuttall.com/wp-content/uploads/2020/03/EORlxwoX4AAJuTY.jpg" data-id="2611" data-link="https://bennuttall.com/?attachment_id=2611" decoding="async" height="496" loading="lazy" sizes="auto, (max-width: 620px) 100vw, 620px" src="images/EORlxwoX4AAJuTY.jpg" width="620"/></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2612" data-full-url="https://bennuttall.com/wp-content/uploads/2020/03/EOuZpfXXUAACDUV.jpg" data-id="2612" data-link="https://bennuttall.com/?attachment_id=2612" decoding="async" height="480" loading="lazy" sizes="auto, (max-width: 640px) 100vw, 640px" src="images/EOuZpfXXUAACDUV.jpg" width="640"/></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2613" data-full-url="https://bennuttall.com/wp-content/uploads/2020/03/EPPToZ5WAAAyTU4.jpg" data-id="2613" data-link="https://bennuttall.com/?attachment_id=2613" decoding="async" height="499" loading="lazy" sizes="auto, (max-width: 610px) 100vw, 610px" src="images/EPPToZ5WAAAyTU4.jpg" width="610"/></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2614" data-full-url="https://bennuttall.com/wp-content/uploads/2020/03/EQ_7k9uWoAYHbZG.jpg" data-id="2614" data-link="https://bennuttall.com/?attachment_id=2614" decoding="async" height="500" loading="lazy" sizes="auto, (max-width: 500px) 100vw, 500px" src="images/EQ_7k9uWoAYHbZG.jpg" width="500"/></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2615" data-full-url="https://bennuttall.com/wp-content/uploads/2020/03/ER-Oi2WsAAMYw2.jpg" data-id="2615" data-link="https://bennuttall.com/?attachment_id=2615" decoding="async" height="463" loading="lazy" sizes="auto, (max-width: 620px) 100vw, 620px" src="images/ER-Oi2WsAAMYw2.jpg" width="620"/></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2616" data-full-url="https://bennuttall.com/wp-content/uploads/2020/03/ERDLAYpWoAActNe.jpg" data-id="2616" data-link="https://bennuttall.com/?attachment_id=2616" decoding="async" height="348" loading="lazy" sizes="auto, (max-width: 500px) 100vw, 500px" src="images/ERDLAYpWoAActNe.jpg" width="500"/></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2617" data-full-url="https://bennuttall.com/wp-content/uploads/2020/03/ERGqxv6WAAETFHH.jpg" data-id="2617" data-link="https://bennuttall.com/?attachment_id=2617" decoding="async" height="500" loading="lazy" sizes="auto, (max-width: 657px) 100vw, 657px" src="images/ERGqxv6WAAETFHH.jpg" width="657"/></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2619" data-full-url="https://bennuttall.com/wp-content/uploads/2020/03/ERTUd0BWoAEFmf_.jpg" data-id="2619" data-link="https://bennuttall.com/?attachment_id=2619" decoding="async" height="281" loading="lazy" sizes="auto, (max-width: 500px) 100vw, 500px" src="images/ERTUd0BWoAEFmf_.jpg" width="500"/></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-2620" data-full-url="https://bennuttall.com/wp-content/uploads/2020/03/ERxLGs3W4AEuKZ_.jpg" data-id="2620" data-link="https://bennuttall.com/?attachment_id=2620" decoding="async" height="600" loading="lazy" sizes="auto, (max-width: 423px) 100vw, 423px" src="images/ERxLGs3W4AEuKZ_.jpg" width="423"/></figure></li></ul></figure>

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
<img src="images/EAG__56XsAI8VJ0.jpg" />
</figure>

Another recent one was from World Building. Again, completely random:

<figure class="wp-block-image">
<img src="images/ERQK46XW4Acpk9H.jpg" />
</figure>

## Is anyone following?

The Stack Overflow bot is the most popular, with nearly 500 followers at the time of writing.
Raspberry Pi and Ask Ubuntu have over 100 each.

## Run your own instance

If you want to run your own bot following a particular Stack Exchange site, you can
[`pip install memeoverflow`](https://pypi.org/project/memeoverflow/) and use the example script,
following the [simple guide](https://github.com/bennuttall/meme-overflow/blob/master/README.md).

If you want to run a modified version, you can either [fork the
project](https://github.com/bennuttall/meme-overflow) or subclass the provided class.

<div class="wp-block-image">
<figure class="aligncenter size-large">
<img alt="" class="wp-image-2613" decoding="async" height="499" loading="lazy" sizes="auto, (max-width: 610px) 100vw, 610px" src="images/EPPToZ5WAAAyTU4.jpg" width="610"/>
<figcaption>Mr President</figcaption>
</figure>
</div>
