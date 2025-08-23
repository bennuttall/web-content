So you have some data. Let's say it's a record of the number of instances of some things. Let's say
it's the number of movies you own, grouped by the year they were released.

Let's say you have those data in the form of a
[dictionary](http://docs.python.org/tutorial/datastructures.html#dictionaries) in Python, like so:  

```python
years = {2000: 2, 2001: 9, 2002: 10, 2003: 9, 2004: 14, 2005: 11, 2006: 8, 2007: 10, 2008: 14, 2009: 19, 2010: 16, 2011: 17}
```
  
The following loop will print out an ASCII bar chart for a quick & easy visualisation of these data:

```python
for y in years:
    print y, years[y]*'|'
```
  
Which looks like this:  

```
2000 ||
2001 |||||||||
2002 ||||||||||
2003 |||||||||
2004 ||||||||||||||
2005 |||||||||||
2006 ||||||||
2007 ||||||||||
2008 ||||||||||||||
2009 |||||||||||||||||||
2010 ||||||||||||||||
2011 |||||||||||||||||
```

Note I used the 'pipe' character in this example. First I used 'o', which worked well, but I tried a
few others (`'O','x','X','*','@',':','/','#','[]','+','-','=','_',':)',`...) and liked this the most.

That's the end of what I wanted the blog post to show, but I may as well throw in how I got my data
in this case. I have movies saved in a folder, and by convention I name them with the year in
brackets at the end so I used [glob](http://docs.python.org/library/glob.html) to loop through the
files in this folder, extract the year, and increment the counter in my years dictionary. I have
another blog post in draft about using glob to edit filenames in batch. Coming soon.
