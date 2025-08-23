Last month I attended [Hack Manchester](http://www.hackmanchester.com/) – a 24 coding event as part
of the [Manchester Science Festival](http://www.manchestersciencefestival.com/), held at
[MOSI](http://www.mosi.org.uk). Having only arranged to team up with
[Mike](http://twitter.com/m1ke), we ended up joining two
guys [Shaf](http://twitter.com/hashpointfive) introduced us to, his colleagues from the
[BBC](http://www.bbc.co.uk/), by the names of [Jack](http://twitter.com/jackpalf) and Tom. The four
of us formed a team, and after browsing the challenges set, we liked the idea of
[Intechnica](http://www.intechnica.co.uk/)'s [Bacon Number
problem](http://intechnicahackmcr.azurewebsites.net/) the most, but rather than just solve the
[Bacon Number problem](http://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon), we derived the
challenge and set off to build a tool to find the film set with the largest [birthday
party](http://2.bp.blogspot.com/_Fw8biBy5Ras/Sb-QFSl36lI/AAAAAAAAA5o/ax1QpmNx6yU/s400/vintage+birthday+party.jpg)
(most common birthday per film, among actors in the same film).

We decided the [data provided](ftp://ftp.sunet.se/pub/tv+movies/imdb/) was too poorly formatted, and
because any alternatives (such as the [Open Movie Database](http://www.omdb.org/movie)) required
sign-up and prior approval, we ended up scraping [IMDB](http://www.imdb.com/) for the [actor
birthday data](http://www.imdb.com/date/). I wrote a [Python](http://www.python.org/) script using
[Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) which worked really well, it hit
every day page on IMDB and stored each of the actor's names in a MongoDB collection in the following
format:  

```
{
    birthday: '27-10',
    name: 'John Cleese'
}
```
  
I ran the script for the 1st Jan page, to see that it worked – and I had a number of records stored,
all with `01-01` as the date, so it seemed to be working ok. I wrapped a loop around it to hit every
day of every month. I started running the script, with no idea how long it would take. I quit it
quite early and added a print statement on every new month for indication as to where it was up to.
Just how I used to solve most of the number crunching [Project Euler](http://projecteuler.net/)
problems! I watched it run, and it seemed to take about a minute and a half per month, so it took
about 20 mins to run in total (it also crashed out at one point when it got a 500 error from IMDB –
I deleted all from the collection from May (incomplete) and ran it from there again, in order not to
get duplicates, or miss any out!). Also, I should point out that we were having to run off tethering
from my phone, because the Hack Manchester wifi only had 100 IPs to dish out (not ideal for a
hackathon with 250 geeks with ~4 devices each!) – a real shame as I'm sure the
[organ](http://twitter.com/ruby_gem)[isers](http://twitter.com/seanhandley) did all they could to
reassure the providers that they would *need* a lot of connected devices. Quite a lot of data ran
through my phone that night – hundreds of hits at IMDB, various packages (such as Beautiful Soup,
the Mongo libraries, the IMDB text file data, etc.)

I sanity-checked this data, by looking at the number of records held in each of the dates in the
collection. I noticed that 1 January had a *significant *number more than all the other dates. I
assumed I had left the data in from when I initially ran it on 1st Jan to test the script – although
it was more than 2, even 3 (actually about 10) times all the other days. I deleted Jan 1st and ran
it on that day again, and got the same number. I looked at the [IMDB page for 1st
Jan](http://www.imdb.com/date/01-01/births) and there were genuinely a lot more than for any other
day. I asked around my team mates for an idea – someone suggested that people aim for 1st January as
a birth date, but I said it's not distributed among nearby dates, and that didn't really make sense
anyway. Of course (you probably already deduced this – please excuse us – we were tired), it was
that 1st January would have been the default value if no date was entered, or maybe this list
included actors without a birth date given.

I committed this code at around 1:45am, and about 45 minutes later, while browsing the team's work
on github, I noticed the commit times for some files. The times, given in a friendly time-relative
human-readable way were:  

```
30 minutes ago
in 16 minutes
27 minutes ago
an hour ago
5 hours ago
```
  
What's that? I committed the file ... in 16 minutes? As in, in the future? How is that so? Well of
course, Hack Manchester happened overnight on the day in the year when [daylight
saving](http://en.wikipedia.org/wiki/Daylight_saving_time) reverts back and we move from
[BST](http://en.wikipedia.org/wiki/British_Summer_Time) to
[GMT](http://en.wikipedia.org/wiki/Greenwich_Mean_Time), and this happens at 2am, when it goes back
to 1am. So every 'time' between 01:00 and 01:59 happened twice. I thought this was rather amusing :)

We then had a searchable database of actors and their birthday. Jack whipped up a [Twitter
Bootstrap](http://twitter.github.com/bootstrap/) web interface, in to which I added some PHP code
(using the [PHP MongoDB library](http://www.php.net/manual/en/class.mongodb.php)) to display a list
of actors with a given birthday, or show a given actor's birthday. At this point we have no movies
stored, so we had [limited functionality](http://www.hawkenking.com/img.skill.cgpainting/mouse.jpg).

Meanwhile, Mike had been writing a bunch of PHP classes containing methods for looking up the data.
He'd also started writing a [Ruby](http://www.ruby-lang.org/) script to extract film-actor data from
some text files he found somewhere. He'd had real trouble extracting out the data in a way it would
be useful to us. It was tab-separated and had referenced films by random alphanumeric IDs rather
than film names, and also contained a ridiculous number of porno films. Later on, Jack and I adapted
this code to try to get it to insert the data in to our existing MongoDB collection. It was quite
fiddly, and we weren't really sure how accurately the data was being collated, but worth a try!

At this point we had a discussion about how we would store the data. Someone suggested:

> We need another table to store the films, and another to store the film-actor relations

Erm, that's not how Mongo works. I'm no expert, and my solution may not have been the best, or
Mongo-est, but I know you can store lists as values (making multiple 'tables', or collections or
whatever, unnecessary), so I suggested we would be fine to add a 'movies' field to the existing
actor storage, which would be a list of films they'd been in, e.g:  

```
{
    birthday: '18-12',
    name: 'Brad Pitt',
    movies: ['Fight Club', 'Inglourious Basterds']
}
```
  
We managed to figure out how to add the movie field to an actor, and how to append a movie to list
already containing one, and we wrote this in to the script and let it run. We left in a print
statement to see what was happening, which obviously slowed the process down a lot. Think about how
many movies there are, and think about how many actors there are. Now think about how many instances
of an actor being in a movie. That's a lot. It took bloody ages. And didn't seem to work. We were
out of time by this point (in fact time was almost up when the program started running). Doing this
properly we'd have tested it better, and ensured all data was being entered correctly. We were just
having a bash at getting it to work.

All of us completely exhausted, we awaited the event closing and awards ceremony. Mike and I had
stayed in the museum all night – each attempting a short nap on a couple of occasions, rather
unsuccessfully in a room full of geeks bashing away at their respective keyboards. Tom had a prior
engagement, so he shot off early evening, and Jack headed home later on due to problems with the
wifi, and worked on setting us up an amazon instance to host the project from home.

Among the hackers were many friends of mine – including a team consisting of [Michael
Heap](http://twitter.com/mheap) and [Tim Hastings](http://twitter.com/timhastings); an
[MMU](http://www.mmu.ac.uk/) team with [Farkie](http://twitter.com/farkie "MORNING BEN"); a
[Manchester Girl Geeks](http://manchester.girlgeekdinners.com/) team; a couple of
[Laterooms](http://www.laterooms.com/) team including
[Mark/Kirsty](http://twitter.com/markkirschstein), [Jim](http://twitter.com/jimmbob) &
[Andy](http://twitter.com/moorcroftlad); a [Thoughtworks](http://www.thoughtworks.com/) team with
[Daley](http://twitter.com/dchetwynd), and so on. I had plenty of people to chat to while taking
breaks (I drank a lot of coffee) – and met a bunch of new people too.

It came to the closing and the winners of each category was named, and had a chance to give a short
demo of their project. Some amazing stuff went on show – it was great to see so much innovation from
so many teams. By chance, no-one else had chosen the Bacon Number challenge, so we won by default! A
bit lame, I know, but the way I see it is that we weren't so awful that they decided to withdraw! I
count that as a win. And what was the prize? A brand new [512MB Raspberry
Pi](http://www.raspberrypi.org/archives/2180) each! Can't complain! Huge thanks to
[Intechnica](http://www.intechnica.co.uk/) for the prizes :)

Also a great big thanks to [Gemma](http://twitter.com/ruby_gem) and
[Sean](http://twitter.com/seanhandley) for putting the event on. It was fantastic! I will definitely
enter events like this in future, even without a team – you can always group up with people and get
something done. I was worried about working with people who used different languages or frameworks
and that we wouldn't be able to get things done, but we pooled ideas and skills together and managed
to build some cool stuff! Also thanks to [MOSI](http://www.mosi.org.uk/) for the use of the space
(all through the night!) during the science festival.

The code from our hack is available at
[GitHub](https://github.com/hackmanchester/test_can_rename_repo) – it may or may not get
updated/fixed in future, but at the time of writing was as we left at the end of the event

Also check out Farkie's blog post on the Magma Digital blog – [Hack Manchester
2012](http://www.magmadigital.co.uk/hack-manchester-2012/)
