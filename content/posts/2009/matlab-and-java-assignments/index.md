I've had a hectic week this week trying to get all my assignments in. I had a MATLAB assignment due
in on Thursday and a Java one due in today.

The MATLAB one involved two questions: the first was a banking system which calculated interest and
mortgage payments; the second was an animation of a sporting event. The first question involved a
switch statement to begin, so the user was prompted to choose one of four options, each one taking
them to a certain part of the code and allowing them to perform their chosen banking task. Within
each of those I had to use nested for loops and if statements, taking input values and getting the
loops to work out how to calculate the answer based on their inputs (for instance if the user
entered 10 years, the loop would have to run 10 times), which was kind of fiddly but fairly easy. If
you don't know what a for loop is, it's quite common in many programming languages, and here's a
brief explanation:

```matlab
for i = 1:10
    a = 2*i
end
```

This means that the loop runs 10 times (for i=1, for i=2, ..., for i=10) and does the code in between
each time. So the first time it runs, the variable i=1, so when i is multiplied by 2, a = 2 (in
MATLAB this would return the answer each time). The second time, i=2 so a=4, then each time i
increments by 2 until i=10 and a=20. This is a very basic example but there are many applications
this can be used for.

For the animation, I had to draw the figures using x- and y-coordinates of polygons, filling them in
with a chosen colour, and then use a for loop to change their coordinates (i.e. move all the
x-coordinates one space to the left every time the loop runs). It started off as a simple yacht
animation, but I got carried away when I added the second yacht and made it into a pirate chase with
a bullet being fired.

It actually sailed smoother before I added the movement up-and-down, but the code to make it do this
was rather complex and imaginative so I left it in to get more marks. I nested an if statement
within the for loop:

```
for j = 0:120
    ...
    if rem(j,2) == 0
        yboat = yboat + 1
    else
        yboat = yboat - 1
    end
    ...
end
```

So every time the loop ran (the ellipsis doesn't show the bits of code that get the x-coordinates to
move the the left), the if statement checks to see whether j is divisible by 2: if it is, the
y-coordinates increment by 1; if not, they decrement. This makes the boat (and all its related
shapes, again not shown) move up and down alternately. The assignment handout included a video of an
animation worth 90% and it was much simpler than mine so I should have scored fairly well.

Once I had this finished and submitted I had to get on with my Java assignment: to make a simple
sketching program in Java, as an applet for HTML. About 24 hours before the deadline I hadn't done
much, only the very basics, and then spent most of the afternoon helping 3 other people to get that
far, went to have a beak for about an hour and a half and went to train, then did a little more
before going out to see the Inbetweeners at a club in Manchester, then woke at 10:00 the next
morning to carry on with it, just 2 hours before the de this was only enough to get 40%. I worked on
it every second for the next two hours, trying bits of code to get it to do more advanced functions,
I added colours, a reset button, a change background colour function, different shapes, a text
field, another text field, a change size field, and so on, until I had completed the list of
functions to include, which were given with percentages of how much you would get if you did them,
up to 70% (a First Class), and it said extra marks would be awarded for extra features and for the
general 'look and feel' of the applet, so I should have done pretty well. I submitted at 11:59. Just
in time.

Java and MATLAB seem to be very similar in what you can do and the code you use to do it, but
MATLAB's syntax is much simpler. Next year's Java will be much more complex, with a much stronger
emphasis on objects. As for MATLAB, I specifically chose the units which included MATLAB
programming, one of which was about computer graphics and virtual environments, and most people who
aren't interested in programming will have gone elsewhere so it should get much more hardcore.
