During the first COVID lockdown, stuck at home bored, I had a silly idea - I wonder if I could use
the insertion of floppy disks as a trigger to control something from a Raspberry Pi. I bought a
sleek USB floppy drive and a brand new 10-pack of disks.

Although I managed to mount the floppy and read files from it, somehow I struggled to get udev
events working and quite quickly gave up. The floppy drive and disks have lived in a drawer ever
since, and my intention to one day get around to making this silly dream a reality never wavered.

Some six years later, Raspberry Pi with a HAT out on the desk, fresh from some gpiozero hacking (see
[last week's post](/blog/2026/07/gpiozero-flow/)), I decide it's time to try something whacky with
floppy disks. And I have no excuse now, because I have [Claude](https://claude.ai/) on hand to help
if I hit any blockers.

This is what I came up with:

<iframe width="560" height="315" src="https://www.youtube.com/embed/P3FClzeb3GM?si=Oj2ct5e9klG9cBwv" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Since I had a HAT with traffic lights on it, I thought it would be fun to have different coloured
floppy disks light up a different colour - so I wrote a file with "red", "yellow" and "green" to
each of three disks, and labelled them with a coloured sticker.

We have a udev monitor in Python to detect the floppy drive event, then read the text file to
determine the colour and (using gpiozero, obviously), light up the appropriate LED.

See the instructions and code on GitHub:
[github.com/bennuttall/floppy-led](https://github.com/bennuttall/floppy-led)