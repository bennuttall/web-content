The [ternary operator](http://en.wikipedia.org/wiki/Ternary_operation) is a shorthand way of writing
an if/else statement where a particular action occurs in both cases, but the value associated with
that action depends on the condition stated.

For example, the traditional if/else construct (C/Java/JavScript syntax):  

```javascript
if (a > b) {
   result = x;
}
else {
   result = y;
}
```
  
can be rewitten as:  

```javascript
result = a > b ? x : y;
```
  
This in itself is a huge benefit to clean, concise code. I use it wherever possible. Here's an
example in PHP:  

```php
<?php

echo 'User is ' . $user['loggedin'] ? 'online' : 'offline';
```

A particularly cool Python example utilising the idea of a function of a list comprehension:

```python
vowels = 'aeiou'
print sum(j in vowels for j in 'stringy cheese') > 5
# returns False because the sum of the values in the resultant list is 4
```

```python
vowels += 'y'
print all([j in vowels for j in 'you'])
# returns True because all the values in the resultant list are True
```
  
If you want to return/echo true or false depending on the condition, there is no need for the
ternary operator as a shorter operator is available: simply echo the boolean result of the
condition, i.e. rather than:  

```python
def sum_digits_greater_than_ten(n):
   return True if sum([int(j) for j in str(n)]) > 10 else False
```
  
This will produce the same output:  

```python
def sum_digits_greater_than_ten(n):
   return sum([int(j) for j in str(n)]) > 10
```
  
There are various other implementations of this idea in different languages, but the reason for this
blog post is because while talking about these with my colleague
[Mike](http://twitter.com/mgldev) and I came up with an interesting manipulation of this on the
train to work the other day. I had a program which incremented a value by 1 if and only if a
condition was true:  

```python
var += 1 if x > 0 else 0
```
  
In my opinion this is good because it's on one line, but bad because the `else 0` should be
unnecessary. Unfortunately Python requires an `else` here. The obvious alternative doesn't use a `+0`
but requires 2 lines:

```python
if x > 0:
   var += 1
```

Anyway, the thing we thought of was to increment by the integer value of the boolean, i.e. 
`1 if True`, `0 if False`:

```python
var += x>0
```
  
Evaluating a condition, say `x>0`, returns `True` or `False`, which when added to an integer is
equal to 1. Another implementation of this is to multiply the value of the condition by a scaling
factor:  

```python
var += 2*(x>0) # increment by 2 if (and only if) true
var += x*(x>0) # increment by x if (and only if) true
var += y*(x>0) # increment by y if (and only if) true
```
