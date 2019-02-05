# Evil Python Lesson 8: File I/O

[All Lessons](https://zsiegel92.github.io/evilpython/)

[TOC]

## I/O: "Input/Output"

**File I/O** is short for "file input and output".

We have *written* to the **console** using the built-in *Python* `print` function. We have also used the *shell* command `touch` to create empty files from the command line. **We will use Python functions to *open* files and to *write* content to open files.**

We have *read* content from the **console** using the built-in *Python* `input` function, and we have captured keyboard input using the `pynput` package. **We will use Python functions to *open* and *read* content from open files**.

### Opening and Closing Files

To open a file, Python has a built-in function called `open`. We can **read** and **write** to open files. [Read about it in the Python documentation](https://docs.python.org/3/library/functions.html#open)!

* `open_file = open('some_file.txt','r')` ← Read file.
* `open_file = open('some_file.txt','w')` ← Write to file, clearing if it exists.
* `open_file = open('some_file.txt','x')` ← Create file if it doesn't exist.
* `open_file = open('some_file.txt','a')` ← Write to file, appending to the end.
* `open_file = open('some_file.txt','+')` ← Read and write to file.

When we are finished with a file, we **close** the file, using the command

```python
open_file.close()
```

### Reading File

To **read** a file and store its contents in a Python `str` variable, use the `.read` function:

```python
f = open_file('some_file.txt','r')
contents = f.read()
f.close()
print(contents)
```
> Copy this code into a file in a folder that contains another file called `some_file.txt` containing the text `Hello, World!`.

### Writing to a File

```python
f = open_file('new_file.txt','w')
f.write("Hello, World!")
f.close()
```
> Run this code and then open the file `new_file.txt`.

Remember that you can open a file with the `w` parameter to **overwrite** the file, or `a` parameter to **append** to the file.

## Assignments

1. Create a program that asks the user for their name as input, then writes to a file called `yournameis.txt`:

2. Create a program that asks the user for the name of a file, then writes `Hello!` to that file.

3. Create a program that asks the user for an integer, then prints an "asterisk triangle" with that many rows to the file `asterisk_triangle.txt`. An "asterisk triangle" with 10 rows looks like this:

```python
*
**
***
****
*****
******
*******
********
*********
**********
```


