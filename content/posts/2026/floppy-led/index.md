During the first COVID lockdown, stuck at home, bored, I had a silly idea: could I use the insertion
of a floppy disk as a trigger to control something from a Raspberry Pi? I bought a sleek USB floppy
drive and a brand new 10-pack of disks.

Although I managed to mount the floppy and read files from it, I struggled to get udev events
working and quite quickly gave up. The floppy drive and disks have lived in a drawer ever since, but
my intention to one day make this silly dream a reality never wavered.

Some six years later, with a Raspberry Pi and a HAT out on the desk fresh from some gpiozero hacking
(see [last week's post](/blog/2026/07/gpiozero-flow/)), I decided it was time to try something
whacky with floppy disks. And I had no excuse this time, because I had [Claude](https://claude.ai/)
on hand to help if I hit any blockers.

This is what I came up with:

<iframe width="560" height="315" src="https://www.youtube.com/embed/P3FClzeb3GM?si=Oj2ct5e9klG9cBwv" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Since I had a HAT with traffic lights on it, I thought it would be fun to have differently coloured
floppy disks light up a matching LED - so I wrote a file containing "red", "yellow" or "green" to
each of three disks, and labelled them with a coloured sticker to match.

A udev monitor in Python detects the floppy drive event, reads the text file to determine the
colour, and (using gpiozero, obviously) lights up the appropriate LED.

Claude figured out the part I'd got stuck on last time:

> No native media-change signalling. USB floppy bridges don't tell Linux when a disk is swapped, so
> detection relies on udisks2's periodic polling of removable drives (it re-probes every couple of
> seconds and fires a fresh change uevent when the state changes).

See the instructions and code on GitHub:
[github.com/bennuttall/floppy-led](https://github.com/bennuttall/floppy-led)