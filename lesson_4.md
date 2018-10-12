# Evil Python Lesson 4: String-Integer Challenge

[All Lessons](https://zsiegel92.github.io/evilpython/)

[TOC]


## Python Review

In the [4th Python Lesson (about `str`s)](https://zsiegel92.github.io/Eitan_S/Lessons/Lesson_4_Strings/Python4.html), we saw how to **concatenate** using `+`, how to check from **substrings** using `in`, how to **index** characters in a string using `[]`, how to **split** and **join** `str` and `list` variables using `str.join` and `str.split`, and how to **format** strings using `str.format`.

We also learned about variable **type** in [the 2nd Python Lesson (about variables)](https://zsiegel92.github.io/Eitan_S/Lessons/Lesson_2_Variables_and_Conditionals/Python2.html). We know **casting** is the process of creating a variable from a variable with another **type**.

In the [6th Python Lesson (about `list`s)](https://zsiegel92.github.io/Eitan_S/Lessons/Lesson_6_Lists/Python6.html#indexing-and-slicing) we learned about **list slicing**. We also saw slicing, like indexing, works with both `list` variables and `str` variables!

### String Indexing and Slicing Examples

```python
>>> x = "Sup, World"
>>> x[4]
' '
>>> x[0:8]
'Sup, Wor'
```
> Note that the slicing in `x[0:8]` takes a *start* and an *end* index, and that *the end index is **not** included in the slice!*

#### Slicing with an *Increment*

Slicing of a variable `x` usually looks like `x[start:end]`, where `start` and `end` are the *start* and *end* indices of the slice (the *end* index is not included in the slice).

But *slicing has a third parameter - the *increment*!* We can specify the *increment* of a slice using `x[start:end:increment]`. The increment controls how many characters the slice jumps ahead after it reads each one. The **default increment** is 1, so `x[start:end:1]` is equivalent to `x[start:end]`, which means

Observe:

```python
>>> x = "Sup, World"
>>> x[0:8:1]
'Sup, Wor'
>>> x[0:8:2]
'Sp o'
```

**The increment can be negative to produce a *backwards* slice!**

```python
>>> x = "Sup, World"
>>> x[8:0:-1]
'lroW ,pu'
```
> Remember that the *end* of a slice is **not** included in the slice, so if the *end of our *backwards* slice is set to `0`, the *zeroth* (first) character of our string will not be included in the backwards slice.

#### Blank Slice Arguments

The default *start* of a slice is `0`, the beginning of the `str` or `list` from which we are slicing. The default *end* of a slice is the end of a string. If we leave either one blank, we will slice from or to the default value.

```python
>>> x = "Sup, World"
>>> x[0:] # start is 0 and end is blank/default
'Sup, World'
>>> x[:] # start AND end are blank/default
'Sup, World'
```

The default *increment* of a slice is `1`, assigned when the increment is blank (or the second `:` is omitted):

```python
>>> x = "Sup, World"
>>> x[0:5:1] # increment is 1
'Sup, '
>>> x[0:5:] # increment is blank, defaults to 1
'Sup, '
>>> x[0:5] # the second : symbol is omitted, increment defaults to 1
'Sup, '
```

If *start* and *end* are left blank/default, but *increment* is set to `-1` (or any negative integer), slicing will occur in the *negative direction*, namely from the back of the string or list.

```python
>>> x = 'Sup, World'
>>> x[::-1] # start and end are blank and default
'dlroW ,puS'
>>> x[-1::-1] # start is -1 (the default value), end is blank and defaults
'dlroW ,puS'
```


#### "Reversing" a `str` or `list` Variable

Using the above slicing syntax, a Python `str` or `list` variable `x` can be reversed using `x[::-1]`.

```python
>>> x = '12345'
>>> x[::-1]
'54321'
>>> y = [1,2,3,4,5]
>>> y[::-1]
[5, 4, 3, 2, 1]
```


### Casting Examples

#### Casting `int` as `str`

```python
>>> x = 5
>>> y = 6
>>> x + y
11
>>> str(x) + str(y)
'56'
```

#### Casting `str` as `int`

```python
>>> x = "5"
>>> y = "2"
>>> x + y
'52'
>>> int(x) + int(y)
7
>>> int(x + y)
52
```

And more! **Please review any you don't feel 100% comfortable using**.

### "Reversing" an `int` Variable!

By combining *casting* and *slicing*, we can reverse `int` variables!

```python
>>> x = 12345
>>> str(x)[::-1] # casts int as str, then reverses using slicing
'54321'
>>> int(str(x)[::-1]) # casts int as str, reverses using slicing, then casts back to int
54321
```


## Assignments

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Hs_v7rGAdKc?rel=0&amp;start=52" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
> Missy Elliott's 2002 hit *Work It* includes the lines:
> > Put my thing down, flip it, and reverse it.
>
> > Ti esrever dna ti pilf, nwod gniht ym tup.
>
> This video plays the lines forward and in reverse.
>
> Clearly, Ms. Elliott is a master of palindromes and string manipulation.

You will complete [this challenge](http://www.acsl.org/acsl/sample_ques/c_3_palindrome_sr.pdf) from the American Computer Science League!

Start by creating a file called `palindrome.py`.

1. Write a function called `reverse` that takes an `int` argument and returns the "reversed" integer.

	This should get you started:
	```python
	def reverse(x):
		return int(str(x)[::-1])
	print(reverse(521)) # should return 125
	```
	> Actually, this function is fully formed. For now, just get `palindrome.py` running and test this function out with several inputs.

2. Write a function called `is_pal` that returns `True` if its argument is an `int` variable that is a palindrome, and returns `False` otherwise. You can use the `reverse` function you've already written.

	This should get you started:
	```python
	def is_pal(x):
		y = reverse(x)
		if x == y:
			return True
		else:
			return False
	```

3. Write a function called `add_to_reverse` that takes an `int` argument, then adds it to its "reverse", and returns the sum.

	This should get you started:
	```python
	def add_to_reverse(x):
		# DO SOMETHING HERE!
		return # RETURN SOMETHING
	```

4. Write a function called `pal_count` that takes an `int` argument, then adds it to its "reverse" several times until a palindrome is produced (see [challenge](http://www.acsl.org/acsl/sample_ques/c_3_palindrome_sr.pdf)). When a palindrome is produced, the function should return the number of times the addition was performed.

	```python
	def pal_count(x):
		count = 0
		while not is_pal(x):
			x = add_to_reverse(x)
			count += 1
		return # RETURN SOMETHING
	```

5. Change `pal_count` so that a number that takes more than 10 iterations of `add_to_reverse` to produce a palindrome causes `pal_count` to return something special, like `-1`, to indicate that the process failed.
