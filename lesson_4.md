# Evil Python Lesson 2: Executing Shell Commands from Python!

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

The default `start` of a slice is `0`. The default `end` of a slice is the end of a string. If we leave either one blank, we will slice from or to the default value.

```python

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

##

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Hs_v7rGAdKc?rel=0&amp;start=52" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## Assignments

1.
	Complete [this challenge](http://www.acsl.org/acsl/sample_ques/c_3_palindrome_sr.pdf) from the American Computer Science League!

