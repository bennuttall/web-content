Today I saw [fixubuntu.com](https://fixubuntu.com/) featured on [Hacker
News](https://news.ycombinator.com/). I assumed it was to be yet another rant about why you should
use distro X instead of Ubuntu, and how Canonical are ruining it. I was half-right. I clicked the
link to see what it was about and found a large box containing a list of Linux commands, with the
instruction to copy and paste the block in to your Terminal and hit enter:

```
gsettings set com.canonical.Unity.Lenses remote-content-search none; if [ "`/usr/bin/lsb_release -rs`" \< '13.10' ]; then sudo apt-get remove -y unity-lens-shopping; else gsettings set com.canonical.Unity.Lenses disabled-scopes "['more_suggestions-amazon.scope', 'more_suggestions-u1ms.scope', 'more_suggestions-populartracks.scope', 'music-musicstore.scope', 'more_suggestions-ebay.scope', 'more_suggestions-ubuntushop.scope', 'more_suggestions-skimlinks.scope']"; fi; echo | sudo tee -a /etc/hosts; echo 127.0.0.1 productsearch.ubuntu.com | sudo tee -a /etc/hosts;
```

The instructions were followed with "Enjoy your privacy" and an explanation of what the code does
underneath. It explained that it is designed to turn off the remote search (so your Dash searches
aren't sent to the internet) and other Dash scopes, to uninstall Amazon ads built in to Ubuntu, and
block connections to Ubuntu's ad server "just in case".

It also explained what the problem they're trying to solve is – that with default settings in
Ubuntu, each search you type in the Dash (to search your computer for files and apps), your searches
are sent to third parties. It expressed that Ubuntu should protect its users' privacy by default.

As an Ubuntu user (and advocate), I had mixed feelings about this. I do believe there are genuinely
useful purposes for the Dash as a desktop based web search tool – as developers strive to invent and
innovate for the future of technology, the most obvious move at the moment is the move towards an
integration of desktop and the web. The lenses in Unity have potential uses – for example hitting a
YouTube icon from the Dash searching for videos could be useful (see other examples on
[askubuntu](http://askubuntu.com/questions/38772/what-lenses-for-unity-are-available)), and the
technology is still young and yet to be proven – it's probably used by a very small percentage of
Ubuntu users right now. One way Ubuntu have aimed to demonstrate its potential is to include an
Amazon search – and enable it by default. Searching "Moby Dick" and seeing results where you can buy
the book – naïvely looking at this, one might "that's cool" but most people would find this
intrusive and pushy – particularly with it being Amazon (see [Richard Stallman's notes on
Amazon](http://stallman.org/amazon.html)). I did disable this feature once I considered that *every
search keystroke *I typed in to the Dash was actually sent to Ubuntu's server and on to third party
ones such as Amazon. For me, if I wanted this feature, it should be opt-in on both being enabled at
all, and per use (i.e. clicking a particular lens icon).

I don't have a problem with Ubuntu's development process, nor with Canonical's directive, nor with
third party partnerships in general – but these should be options for users, and I believe better
choices could have been made when implementing demonstrative default lenses. Ubuntu and Canonical
are getting a *lot* of stick from the open source community at the moment for things like this, and
should be doing their best to preserve their reputation as being a user-friendly Linux distribution.
Privacy issues and general careless manipulations of user data should be avoided.

I still believe Ubuntu to be the best all-round Linux distro – and will continue to use, recommend
and advocate it. But I will be keeping an eye on things like this and disabling invasive defaults.

So it looks like the author of this page has similar views to mine. He's not just whining. I imagine
he wants to continue to use Ubuntu the way he wants and feels safe – and encouraging others to do
the same.
