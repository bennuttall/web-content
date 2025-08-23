For the last few months in BBC News Labs, I've been working on various projects involving extracting
metadata from running orders for BBC programmes such as
[Newsnight](https://www.bbc.co.uk/programmes/b006mk25) and the [R4
Today](https://www.bbc.co.uk/programmes/b006qj9z) programme.

Like many traditional broadcasters, the BBC uses the [MOS Protocol](http://mosprotocol.com/) for
communications between newsroom computers and servers where media files such as audio and video are
stored.

<figure class="wp-block-image">
<img src="images/mos.jpg" />
</figure>

Production teams create running orders using
[OpenMedia](https://www.cgi.com/en/solutions/openmedia), and every time they add details or make
changes, MOS XML messages are emitted by the newsroom computer systems. We've created a way to
process these messages to build up a machine-readable version of the running order.

We developed a general solution for dealing with MOS messages – a Python library called mosromgr.
It's based on open standards and could be useful to other broadcasting organisations, so we've
released it under an open source licence.

- The source code is available on [GitHub](https://github.com/bbc/mosromgr)
- The documentation for the library is available on [readthedocs](https://mosromgr.readthedocs.io/)
- The project is available from the [Python Package Index](https://pypi.org/project/mosromgr/)

Read more at [bbc.co.uk/opensource](https://www.bbc.co.uk/opensource/projects/project/mosromgr) and
[bbc.co.uk/rdnewslabs](https://www.bbc.co.uk/rdnewslabs/projects/mosromgr)
