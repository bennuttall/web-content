*One year ago today, I
[started](https://github.com/RPi-Distro/python-gpiozero/commit/272747238f54aa9939a88872a1c1324321de3810)
the GPIO Zero project. We now have a core team of three (Dave Jones, Andrew Scheller and me). There
have been 587 commits, we've released four major versions, and [published a
book](https://bennuttall.com/simple-electronics-gpio-zero-book/). The library has great coverage of
GPIO devices, and contains features I never even dreamed of. In the last year I've delivered
workshops and given talks about it at conferences and events around the UK, the US and even in
[Russia](https://speakerdeck.com/bennuttall/physical-computing-with-python-and-raspberry-pi-pycon-russia).
It's being used in [Raspberry Pi's learning resources](https://www.raspberrypi.org/resources/), and
[teacher training](https://www.raspberrypi.org/picademy/) and by hobbyists around the world. Read on
to find out what's new in the latest release.*

GPIO Zero v1.3 is out now! Install it (or upgrade) with:

```python
sudo apt-get update
sudo apt-get install python3-gpiozero python-gpiozero
```

What does this release bring?

- New `ButtonBoard` class
- New `Servo` and `AngularServo` classes
- New `CPUTemperature` class
- Improved remote GPIO support
- Plenty of behind-the-scenes changes
- Lots of [new recipes](http://gpiozero.readthedocs.io/en/v1.3.1/recipes.html)

### ButtonBoard

The new [`ButtonBoard`](http://gpiozero.readthedocs.io/en/v1.3.1/api_boards.html#buttonboard) class
is a composite device representing multiple buttons. The idea being you can pass the value set from
a collection of buttons into another collection of the same size: e.g. matching buttons to LEDs. You
can also process the value set to get the information you want, for example the number of buttons
pressed; any pressed, all pressed, proportion pressed or more. We're currently discussion options
for documenting these examples and possibly extending the features of this class in
[Issue #425](https://github.com/RPi-Distro/python-gpiozero/issues/425).

### Servo

The [long-discussed](https://github.com/RPi-Distro/python-gpiozero/issues/248) Servo classes have
now arrived! [Servo](http://gpiozero.readthedocs.io/en/v1.3.1/api_output.html#servo) allows you to
move a servo between its minimum, maximum and mid-point positions:

```python
from gpiozero import Servo
from time import sleep

servo = Servo(17)
while True:
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)
```

[AngularServo](http://gpiozero.readthedocs.io/en/v1.3.1/api_output.html#angularservo) allows you to
move a servo to specific angles:

```python
from gpiozero import Servo
from time import sleep

s = AngularServo(17, min_angle=-45, max_angle=45)

s.angle = 0.0
sleep(1)
s.angle = 15
sleep(1)
s.angle = 45
sleep(1)
s.angle = -45
```

We're currently [discussing](https://github.com/RPi-Distro/python-gpiozero/issues/419) what else
should be added to the servo classes for different use cases.

### CPUTemperature

We introduced some internal devices which act like regular GPIO Zero classes. `CPUTemperature`
allows you to access the Pi's CPU temperature, and use it to control other devices:

```python
from gpiozero import LEDBarGraph, CPUTemperature

temp = CPUTemperature(min_temp=50, max_temp=90)
graph = LEDBarGraph(5, 6, 13, 19, 25, pwm=True)
graph.source = temp.values
```

Now the LEDs will light up according to the temperature: at 50 degrees all the LEDs will be off; at
90 degrees they'll all be on; at 70 degrees half will be on; and anything in-between. There's also a
`TimeOfDay` class provided but it's not working properly at the moment so I'll cover that in the
next release post.

### Remote GPIO support

I talked about this last time. It's really exciting. It was amazing to see this working in v1.2 but
support wasn't really very good, so its use was limited. However, significant work has gone into
remote GPIO support since then and it's going to be really powerful. Thanks to a
[pigpio](https://github.com/joan2937/pigpio), a C library from GitHub user joan2937, we can set up
GPIO Zero devices connected to pins on Pis over a network. Easily.

Usually, you'd set up an LED like so:

```python
from gpiozero import LED

led = LED(17)

led.blink()
```

Where the 17 refers to pin 17 on the Pi you're executing the code. You can also do this:

```python
from gpiozero import LED
from gpiozero.pins import PiGPIOPin

pin = PiGPIOPin(17, host='192.168.1.4')
led = LED(pin)

led.blink()
```

Here, rather than simply specifying the number 17, we've provided a reference to a pin on another Pi
on the network. This means you can remotely control the LED connected to that other Pi.

However, an easier method is to supply the Pi's IP address in an environment variable. Before
running the python shell, IPython, IDLE or whatever you're using, simply set the `PIGPIO_ADDR`
environment variable:

```
$ PIGPIO_ADDR=192.168.1.4 python my_script.py
```

to run a file, or:

```
$ PIGPIO_ADDR=192.168.1.4 ipython3
```

to run the IPython shell, for example. Each of these will be set up so that when you type
`led = LED(17)`, it uses pin 17 on that remote Pi. Note: you'll need to enable Remote GPIO, start
the pigpio daemon, and install the pigpio python client on your host machine. See full instructions
in [this gist](https://gist.github.com/bennuttall/572789b0aa5fc2e7c05c7ada1bdc813e).

Of course, you can mix these methods and use a default pin factory but also specify pins on other
Pis.

To set this up, you need the pigpio Python library installed on the device you're running the code,
and the pigpio daemon running on the remote Pi (and remote GPIO enabled in raspi-config). Read the
[pins documentation](http://gpiozero.readthedocs.io/en/v1.3.1/api_pins.html) for more info.

Did I mention you can run this on any PC, not just on a Pi? That's right. You can install GPIO Zero
on your laptop and run GPIO Zero code which communicates with a Pi on the network. The *Python* code
is running on your laptop, which communicates with the pigpio daemon using sockets. The daemon does
all the GPIO stuff. I've seen this working on Linux, Mac and Windows. Admittedly, we need to provide
much more solid instructions for getting this working if we want it to be seen as a viable solution
for schools, Code Clubs and such. But it's a start. Please give feedback if you're using it (if you
have any issues or not – we'd love to know). There's also some interesting stuff around. If you know
your way around installing with pip on Windows and Mac, we could use your help! See
[Issue #434](https://github.com/RPi-Distro/python-gpiozero/issues/434).

## What's next?

We didn't complete all the things we had on the list for this release, but we decided to push it out
anyway, and leave the rest to the next release. As well as lots of minor improvements, we intend to
add I2C support, including I2C expander chips (and probably SPI expander chips while we're at it),
which will be really handy. You'll be able to set up an expander chip, and index it to refer to each
pin, and create regular device objects on those pins, something like this:

```python
from gpiozero import IOExtender, LED

ext = IOExtender()
led = LED(ext[0])

led.on()
```

Then there's temperature sensors, different types of motors, servos and more. Feature requests
welcome on [GitHub](https://github.com/RPi-Distro/python-gpiozero)! We're also aiming to establish a
release schedule for future releases.

## Thanks

Again, thanks to Dave Jones and Andrew Scheller for all their hard work in the last release, and to
everyone who provided useful feedback on GitHub. Keep it coming!

## PyCon UK

Dave and I will be giving a talk together on GPIO Zero at PyCon UK this week. <s>The video will be
available shortly after the conference</s> (unfortunately the recording failed). We're also running
a sprint on GPIO Zero, welcoming new developers to the library. Come and have a go if you're
available, and we'll show you where to start.
