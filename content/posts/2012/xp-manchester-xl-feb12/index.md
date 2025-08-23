Yesterday was [XP Manchester](http://xpmanchester.wordpress.com/)'s XL event – a Saturday coding
session of [pairing](http://en.wikipedia.org/wiki/Pair_programming),
[katas](http://en.wikipedia.org/wiki/Kata_(programming)) and a team bot tournament hosted at the
[MadLab](http://www.madlab.org.uk/).

I managed to persuade [Kris](http://twitter.com/KrisChalmers), a friend I used to work with, to come
along – it's his first experience of this sort of thing, so I'm really glad he got introduced to the
world of [XP](http://en.wikipedia.org/wiki/Extreme_programming) and
[TDD](http://en.wikipedia.org/wiki/Test-driven_development).
[Ash](http://twitter.com/wisemonkeyash) was there, [Mike](http://twitter.com/M1ke) brought a friend
along who's also new to [agile](http://en.wikipedia.org/wiki/Agile_software_development), and there
was a decent crowd of about 23 attendees which was great to say we were expecting snow that
afternoon. The day was led by [Mark](http://twitter.com/markkirschstein) with *ahem* assistance
from [Jim](http://twitter.com/JimmBob).

We started by pairing up and solving a decimal to Roman numerals problem using TDD. I did mine with
Kris to get him up to speed with what TDD was all about. We used a rather amateur if/elif construct
in Python to solve for numbers up to about 20, but it was a good way to get in to the mood and to
show Kris the methodology of thinking up a feature, writing a test, writing the code to implement
the feature, testing it, refactoring and moving on to the next feature. The emphasis of the day was
on 'release early, release often' which is a really good attitude for software development. As
Facebook founder Mark Zuckerberg said in his letter to the shareholders:

> Hackers try to build the best services over the long term by quickly releasing and learning from
> smaller iterations rather than trying to get everything right all at once. To support this, we
> have built a testing framework that at any given time can try out thousands of versions of
> Facebook. We have the words "Done is better than perfect" painted on our walls to remind ourselves
> to always keep shipping.

The next session was the opposite conversion, Roman Numerals to Decimal, which I managed to do quite
well in a pair with Mike's friend, a PHP dev with no experience of TDD. We did the kata in Python
and solved it by looping through the characters from right to left, looking up the value of each
character and adding it to the total. If a character of lower value than the previous character was
found, its value was subtracted rather than added. I thought this solution to be suitable for any
numeral using characters the program knew about. Within the set time we had tested up to 20 but it
was failing on 14, which made no sense to me. I tried to debug but found no problems so I left it to
inspect later. I got chance to take a look at it later on and with a few handy tips from
[Michael](http://twitter.com/michaelj) (assertEquals more useful than assertTrue) I managed to spot
the mistake causing it to evaluate 14 wrong. I was right to think the solution was good for all,
though, as using the value characters up to M (1000) and adding some more tests for higher numbers
in the hundreds and thousands, all tests passed.

The third pair session was the now infamous [Ordered Jobs
Kata](http://invalidcast.com/2011/09/the-ordered-jobs-kata) by
[Martin](http://twitter.com/martinrue). I did this kata in Ruby with Michael. Ruby's not one of my
preferred languages like PHP or Python but I do like the chance to work in it for exercises like
this (and I'm sure I'll be doing more of this as I'm now living with a Ruby dev). I've had a go at
the Ordered Jobs kata once before but didn't complete it, so it was interesting to have a fresh
attempt. We got off to a really slow start when we hit the first sign of difficulty (introduction of
dependencies), and took quite a while working out a strategy for holding the input data and making
sure dependencies were completed before the other jobs, and realised that although our first
solution was technically sound, that the test failed because of the order we asserted in the test.
We re-jigged our code to make the test pass and moved on. Speaking to Ash about this later, he
pointed out that we'd have been better to specify several smaller pieces of the test separately,
i.e. number of jobs in input must match number of jobs in output; all jobs in the input needed to be
in the output once; and each of the dependencies individually needed to be listed before their
respective dependants. We continued through the next stages and progressed rather well on to stage 6
which we just managed to pass by the end of the session. It turned out we'd managed to get the
furthest in the room with that one, despite our slow start.

After lunch we had a bot battle of rock-paper-scissors-waterbomb-dynamite wherein we had to program
a 'player' to play against a bot on a server built by Jim. It needed to be in C# so each of the .NET
developers in the room split off and we joined them to make teams of 3. Kris and I teamed up and our
strategy took a while to get going as we had many problems whenever our bot got loaded on to the
server we seemed to get disqualified or just fail to take its move. However once all buggy issues
resolved we devised a method of logging the opponent's name and each of its moves. This allowed us
to determine what had gone on in each round, what strategies other players (or the pre-programmed
bots) were taking, where we won and where we lost. We made a few subtle changes to our attack and
added some different approaches when we faced particular known opponents. A fun afternoon which
resulted in us coming second to Mike's team in the final round (although the bots won overall).
Interestingly, Mike's team was the only team running proper tests...

After we left the Madlab we had an extensive drinking session which involved geeky hilarity and many
OHs on twitter. Huge thanks to Mark and Jim for making the event happen – and to the Madlab for
hosting it.
