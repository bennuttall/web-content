[Python](http://www.python.org/) is a wonderful [dynamic
language](http://en.wikipedia.org/wiki/Dynamic_programming_language) offering various [functional
programming](http://en.wikipedia.org/wiki/Functional_programming) features, including standard
library modules [itertools](http://docs.python.org/2/library/itertools.html) and
[functools](http://docs.python.org/2/library/functools.html) borrowed from
[Haskell](http://www.haskell.org/) and [Standard ML](http://en.wikipedia.org/wiki/Standard_ML). Some
see it as the best of both worlds as not only can you perform complex tasks with these functional
programming tools but you can do it using simple readable code thanks to Python's beautiful syntax.

Early on in my experience with Python I discovered [list
comprehension](http://en.wikipedia.org/wiki/List_comprehension). Traditionally, to generate a list
(an array) of values according to a particular rule, let's say a list of square numbers, we
initialise an empty list, and loop over the domain, square each one and add it to the list:  

```python
squares = []
for n in range(10):
    squares.append(n ** 2)
-> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

However, using list comprehension allows you to generate this list in a single (readable) line:

```python
squares = [n ** 2 for n in range(10)]
-> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
  
I really like this shorthand. It's a list definition in the assignment. Not assigning to the
variable, then building it up, just assigning it to exactly what you want it to be. Concise!

You can do list comprehension with two domains, say a rows range and a columns range:  

```python
rows = cols = range(3)
grid = [(r, c) for c in cols for r in rows]
-> [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]

grid = [(r, c) for c in cols for r in rows if r != c]
-> [(1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2)]
```
  
This example generated a single list of all the [tuples](http://en.wikipedia.org/wiki/Tuple) of
coordinates of a grid – the second ignoring the diagonal – which is equivalent to:

```python
rows = cols = range(3)
grid = []
for r in rows:
    for c in cols:
        if r != c:
            cell = (r, c)
            grid.append(cell)
-> [(1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2)]
```

The following example generates a nested list of tuples, separating each row:

```python
rows = cols = range(3)
grid = [[(r, c) for c in cols] for r in rows]

-> [[(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)]]
```

You can wrap a list comprehension in a function such as sum:

```python
sum(i ** 2 for i in range(10))
-> 285
```

An example of string generation from joining comprehended lists:

```python
msg = [['M', 'J', 'S', 'F'], ['A', 'O', 'O', 'O'], ['K', 'H', 'M', 'O'], ['E', 'N', 'E', 'D']]
' '.join(''.join(msg[j][i] for j in range(4)) for i in range(4))
-> 'MAKE JOHN SOME FOOD'
```

There are other ways you can manipulate list comprehension but this gives you the idea.

More recently I discovered it's also possible to comprehend
[dictionaries](http://docs.python.org/2/tutorial/datastructures.html#dictionaries) and
[sets](http://docs.python.org/2/tutorial/datastructures.html#sets) in the same way, using curly
braces instead of square brackets:  

```python
my_dict = {i: i ** 2 for i in range(1, 11)}
-> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
my_dict[7]
-> 49
```

```python
my_list = [i % 3 for i in range(10)]
-> [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]

my_set = {i % 3 for i in range(10)}
-> set([0, 1, 2])
```

```python
char_list = [c for c in 'abracadabra']
-> ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']

char_set = {c for c in 'abracadabra'}
-> set(['a', 'r', 'b', 'c', 'd'])
```
  
Note the sets only contain each value once, as it cannot contain duplicates.

Finally, another interesting feature is generator comprehension, known as generator expressions:  

```python
gen = (i ** i for i in range(1, 10))
print gen
-> <generator object <genexpr> at 0xfc7d20>
gen.next()
-> 1
gen.next()
-> 4
gen.next()
-> 27
gen.next()
-> 256
```
  
Generators don't keep the list in memory. Instead, each time the next() method is called on it, it
returns the next value. This can be done in custom functions by use of the keyword `yield` rather
than `return`. Return would be used to send a whole list back, whereas yield could be used to return
each value individually, when prompted. You can also request a list from a generator by wrapping it
in the list function.

Comprehension's not always the right way to do something. It's natural to want to use it for
everything once you discover it can be done, but some situations are better written longer. I tend
to follow [PEP8](http://www.python.org/dev/peps/pep-0008/) – one of the guidelines is that a line
must be shorter than 80 characters. If my list comprehension is longer than this, or I struggle to
explain it to someone, it should probably be changed. If there's any logic in the item generator, it
could be abstracted out to a separate function. Sometimes even the nested list is the way to go.

Read more on list comprehension and data structures at
[docs.python.org](http://docs.python.org/2/tutorial/datastructures.html#list-comprehensions). Note
this functionality was brought in in version 2.7.

You can discuss this article on [Hacker News](http://news.ycombinator.com/item?id=5127759).
