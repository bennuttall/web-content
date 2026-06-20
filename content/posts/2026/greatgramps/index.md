Last year I came across a few paper family trees from different sections of my family my Gran had
collected, and I decided to look for a way to digitise them and bring them all together. Firstly I
scanned them all in to make digital copies, and then I looked to see if Ubuntu had any family tree
software. I found [GRAMPS](https://www.gramps-project.org/), the brilliantly backronymed
*Genealogical Research and Analysis Management Programming System*.

I spent some time entering all the names and dates into GRAMPS, combining the data from five
different trees. I quickly got the hang of GRAMPS, and found it quite a useful tool for visualising
and navigating the tree. I proceeded to ask my parents for more info on family members, filling in
gaps and adding detail. I then went into the [family history helpdesk at Manchester Central
Library](https://mlfhs.uk/helpdesk) to learn about how to conduct research and go further back than
the paper trees did. I got some guidance and continued my research at home using
[FreeBMD](https://www.freebmd.org.uk/), [FamilySearch](https://www.familysearch.org/) and
later, [Ancestry](https://www.ancestry.co.uk/).

I found Ancestry useful for finding actual records, but I found myself having to maintain a separate
tree online as well as my GRAMPS tree on my computer, in order for Ancestry to be useful. Ancestry
also requires a subscription to access records, and it's not a lot of use without one. It's well
worth paying for a subscription on a month-by-month basis while you have the time and inclination to
do some research, but if Ancestry was the only place you could access the data, that's no use
either. Ancestry being on the web means you can share it with others, but even if you have a
subscription, your family can't see the records you've collected without their own subscription.

Ancestry does let you download the images of records you've found, such as birth, baptism, marriage,
death and buirial records, and Census returns. I made an effort to download any records relating to
direct ancestors, and keep them organised, but I didn't originally bother to associate them with
events in GRAMPS because it didn't seem worth the effort.

Recently, I wondered how easy it would be to access the data in my GRAMPS database with Python, and
potentially make a static site from the data. I guided [Claude](https://claude.ai) in the experiment
and like usual, made quick progress and it soon became obvious I would be able to build something
useful. I aimed to build a static site generator so I could host a browsable tree I could share with
family. This was not just possible but *easy* because GRAMPS itself is written in Python, and has a
Python library for accessing data from a database, so there was no reverse-engineering or guesswork.

I created a homepage with an overview of the family tree, individual pages for each person in the
tree, then added lists of ancestors and descendants, tree views, maps of event locations and quickly
got something I could click around and explore. I found with it being a generated static site,
clicking around is lightning fast — there's nothing to compute and nothing to wait for.

While building out the features I wanted, step-by-step with Claude, I tried creating events for a
few Census returns and attached the images I got from Ancestry. It allowed me to view them within a
person's life events in a way I thought would be worth adding, so I began to do this for as many
ancestors as possible. In doing so I ended up scripting automations for common tasks, which
eleviated the workload I'd have doing this in the GRAMPS UI. I had a command to create a Census
event with an image, one to list someone's children, and one to add people in bulk to an event,
which would give me a preview to indicate the ages at the time so I could verify from the Ancestry
record and the image itself. I did this for a few different tasks and turned it into a CLI.

I kept adding features to the interface, and I'm pleased with what I've ended with — I have a
private self-hosted site I can share with my family, and it's inspired me to add more detail to the
tree because I can see images and maps alongside the data. Hopefully it will be useful to other
people, and maybe even inspire people to create their own family tree in GRAMPS.

I also put together a demo tree generator, so I could build a website for a fake tree showcasing
the features.

As well as the CLI for reading from and managing data in GRAMPS, I also added a PDF tree generator
so I can generate [ancestor](https://gramps.bennuttall.com/ancestors.pdf),
[descendant](https://gramps.bennuttall.com/descendants.pdf) and
[hourglass](https://gramps.bennuttall.com/hourglass.pdf) charts as printable PDFs.

<figure>
<img src="images/greatgramps_32-34.webp" />
</figure>

I've released this as a library called **greatgramps**:

- [PyPI](https://pypi.org/project/greatgramps/)
- [GitHub](https://github.com/bennuttall/greatgramps)
- [Documentation](https://greatgramps.readthedocs.io/)
- [Demo](https://gramps.bennuttall.com/I0000/people/I0000/)

The library is in three parts, which require different dependencies:

- The CLI — the `grgr` command-line tool
- Static site builder — commands for generating the static site
- PDF generator — the `grgr pdf` commands for generating PDF trees

See the docs for more info.

<figure>
<img src="images/greatgramps_44-02.webp" />
<figcaption>I have traced 195 ancestors and they're pretty much all from Yorkshire and Lancashire</figcaption>
</figure>

<figure>
<img src="images/greatgramps_42-29.webp" />
<figcaption>Generational progress bars</figcaption>
</figure>

Some screenshots from my demo tree:

<div class="gallery">

<figure id="gallery-2">
<img src="images/greatgramps_30-00.webp" />
</figure>

<figure id="gallery-3">
<img src="images/greatgramps_30-09.webp" />
</figure>

<figure id="gallery-4">
<img src="images/greatgramps_30-20.webp" />
</figure>

<figure id="gallery-5">
<img src="images/greatgramps_30-26.webp" />
</figure>

<figure id="gallery-6">
<img src="images/greatgramps_30-30.webp" />
</figure>

<figure id="gallery-7">
<img src="images/greatgramps_30-33.webp" />
</figure>

<figure id="gallery-8">
<img src="images/greatgramps_30-36.webp" />
</figure>

<figure id="gallery-9">
<img src="images/greatgramps_30-39.webp" />
</figure>

<figure id="gallery-10">
<img src="images/greatgramps_30-45.webp" />
</figure>

<figure id="gallery-11">
<img src="images/greatgramps_30-59.webp" />
</figure>

<figure id="gallery-12">
<img src="images/greatgramps_31-19.webp" />
</figure>

<div class="gallery-thumbs">
<a href="#gallery-2"><img src="images/greatgramps_30-00.webp" /></a>
<a href="#gallery-3"><img src="images/greatgramps_30-09.webp" /></a>
<a href="#gallery-4"><img src="images/greatgramps_30-20.webp" /></a>
<a href="#gallery-5"><img src="images/greatgramps_30-26.webp" /></a>
<a href="#gallery-6"><img src="images/greatgramps_30-30.webp" /></a>
<a href="#gallery-7"><img src="images/greatgramps_30-33.webp" /></a>
<a href="#gallery-8"><img src="images/greatgramps_30-36.webp" /></a>
<a href="#gallery-9"><img src="images/greatgramps_30-39.webp" /></a>
<a href="#gallery-10"><img src="images/greatgramps_30-45.webp" /></a>
<a href="#gallery-11"><img src="images/greatgramps_30-59.webp" /></a>
<a href="#gallery-12"><img src="images/greatgramps_31-19.webp" /></a>
</div>
</div>