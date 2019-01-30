# Evil Python Lesson 6: Keyboard Input!

[All Lessons](https://zsiegel92.github.io/evilpython/)

[TOC]


## Review

### Python `input`

The function `input` returns a variable of type `str`. If `x = input()` is executed and `5` <kbd>Enter</kbd> is typed, then `type(x)` will yield `<class 'str'>`.

```python
>>> x = input()
5
>>> x
'5'
>>> type(x)
<class 'str'>
```
> Notice that the variable `age` stores a number but its type is `str`.

### Continuous Input: `pynput`

Recall from [the previous lesson's assignments](https://zsiegel92.github.io/evilpython/lesson_5.html#assignments) that games can be created using Python's built-in `input` function, while more advanced (and more fun) games can be created in which the user does not have to press <kbd>Enter</kbd> after every key press.


### Installing `pynput`

The `pynput` package allows Python to "listen" to keyboard input continuously.

To install `pynput`, complete the following:

* Navigate to folder containing the `.py` file using `cd foldername1/foldername2`, etc.
* Read the **PACKAGE INSTALL NOTE** below, then type `pip install pynput`
* Run a game called (for example) `filename.py` using `python filename.py`.
	* If you get an error that contains the words <span style="color:red">`user`</span> or <span style="color:red">`permissions`</span>, run the program using `sudo python filename.py`. You may be prompted for a password.

> **PACKAGE INSTALL NOTE**: This installs the `pynput` package on your computer. If you instead just want to download and run the `pynput` package in the folder you're in to easily drag to the trash later, or if you have an error, such as <span style="color:red">`Could not find an activated virtualenv (required)`</span>, do the following:
>
> * Type `python -m venv venv`
> * Type `source venv/bin/activate`
> * Type `pip install pynput`
>
> Then, every time you navicate to the folder with the game, you have to type `source venv/bin/activate` before running your program.

## Overview: "Listening" to Input

So far, we have written Python code that prompts the user for textual input through the command prompt with the built-in Python `input` function. While typing our responses into the command prompt, we can navigate away from the window or type and erase, and Python won't know the difference until we press <kbd>Enter</kbd>.

By contrast, `pynput` is a ***keyboard listener***, which means it interacts with your operating system (*Windows*, *Mac OS*, or *Linux*) so that it knows about all keyboard actions. In fact, `pynput` can even *control* the keyboard and trigger automated key-presses.

<img alt="Keyboard typing on its own 'PLAY AGAIN?'" src="keyboard_moving.gif">

You can view the official `pynput` keyboard documentation [here](https://pynput.readthedocs.io/en/latest/keyboard.html).

## *Events* and *Callbacks*

The way `pynput` handles keyboard input is by being aware of all keyboard actions, called "*events*", and to respond to them by executing functions, called "*callbacks*".

The *events* that `pynput` can respond to are ***key-presses*** and ***key-releases***.

A very simple key-press callback function that prints the pressed key looks like this:

```python
def press_callback(key):
	print('{} was pressed'.format(key))
```
> Callbacks take a parameter - here it is called `key`. When we register this function as a callback, `pynput` sends the identity of the pressed key as an argument to this function when it executes.

To register this function as a callback, we create an object of the the `pynput.keyboard.Listener` class and its `start` and `join` method. For now, just copy this syntax to implement a keyboard listener:

```python
from pynput import keyboard

def press_callback(key):
	print('{} was pressed'.format(key))

l = keyboard.Listener(on_press=press_callback)
l.start()
l.join()
```

The `keyboard.Listener` method takes a keyword parameter called `on_press`, which is here set to our callback `press_callback`. This function is executed whenever any key is pressed, with an argument that gives the identity of the pressed key, which becomes the parameter of the callback, `key`.

## Keyboard Listening: `pynput.keyboard.Listener`

### "Press" and "Release": `on_press` and `on_release`

We can implement a more complicated listener that responds to key-presses as well as key-releases.

```python
from pynput import keyboard

def press_callback(key):
	print('{} was pressed'.format(key))

def release_callback(key):
	print('{} released'.format(key))

l = keyboard.Listener(on_press=press_callback,on_release=release_callback)
l.start()
l.join()
```

### The `key` Variable is not a Python String: `key.char`

We used the following key-press callback:

```python
def press_callback(key):
	print('{} was pressed'.format(key))
```

When we use `str.format` to print the pressed key, the `key` variable automatically returns a Python string to be printed (using a `__str__` method). But if we had tried:

```python
def press_callback(key):
	print(key + " was pressed")
```

we would see <span style="color:red">`TypeError: unsupported operand type(s) for +: 'KeyCode' and 'str'`</span>.

So, the `key` variable holds more than just a string identifying the key. However, that's usually what we want. To access the `str` identifier for the pressed key, you can use the `key.char` attribute:

```python
def press_callback(key):
	print(key.char + " was pressed")
```
> Note that in the first version of the code, we would see output like:
> ```
> g'g' was pressed
> ```
> whereas now it looks like:
> ```
> gg was pressed
> ```
> That's because `key.__str__` returns a nicely-formatted string identifying the key pressed, whereas `key.char` contains just the character associated with that key.

Unfortunately, `key.char` can only be called for keys that are associated with a character (like <kbd>A</kbd>, <kbd>5</kbd>, and <kbd>=</kbd>). If `key` is referring to the <kbd>Enter</kbd> key, for example, then `key` simply *does not have the attribute* `char`.

Python has a built-in function called `hasattr` ("has attribute") that checks whether a variable has a certain attribute, and it comes in handy here:

```python
def press_callback(key):
	if hasattr(key,'char'):
		print('The character "{}" was pressed'.format(key.char))
	else:
		print('The special key "{}" was pressed'.format(key))
```

### Responding To Individual Keys

Using `key.char`, we can respond to individual keypresses:

```python
def press_callback(key):
	if hasattr(key,'char'):
		if key.char == "z":
			print('Thanks for pressing "z"! That\'s my favorite character!')
```

Some special keys, like <kbd>esc</kbd>, have special `pynput` variables associated with them:

```python
def press_callback(key):
	if key == keyboard.Key.esc:
		print('You pressed "escape"! You must want to quit really badly...')
```

### Stop Listening to Me!

We can always stop a keyboard listener by returning `False` from a callback function:

```python
def press_callback(key):
    print('{} was pressed'.format(key))
    if key == keyboard.Key.esc:
    	return False
```


## Keyboard Control: `pynput.keyboard.Controller`

We can instruct `pynput` to press a key with the following:

```python
from pynput import keyboard

c = keyboard.Controller()

c.press('a')
c.release('a')
```
> Make sure to **always release** keys that you press using code!

The possibilities are great by just pressing character keys, but we can also press special keys:

```python
from pynput import keyboard

c = keyboard.Controller()
keys = keyboard.Key

c.press(keys.space)
c.release(keys.space)
```

Pressing a key once is no big deal, but code lets us iterate!

```python
from pynput import keyboard

c = keyboard.Controller()
keys = keyboard.Key

i = 0
while i < 100:
	c.press('a')
	c.release('a')
	i += 1
```

Even better? There is a `type` function that will type a whole string:

```python
from pynput import keyboard

c = keyboard.Controller()
keys = keyboard.Key

c.type("hello")
```

## Controling and Listening

This code autocompletes a word!

```python
from pynput import keyboard
from pynput.keyboard import Controller, Listener
c = Controller()

def press_callback(key):
	if key.char == 'c':
		c.type("ool, dude!")
		return False

l = Listener(on_press=press_callback)
l.start()
l.join()

```

## Assignments

1. Describe what the following code does:

	```python
	from pynput import keyboard
	from pynput.keyboard import Controller
	c = Controller()

	def press_callback(key):
		if key.char == 'b':
			c.press("l")
			c.release("l")
			c.press("a")
			c.release("a")
			c.press("h")
			c.release("h")

	l = Listener(on_press=press_callback)
	l.start()
	l.join()
	```

2. Make an **autocomplete** tool. Write some code so that when you type the first letter of your name, the rest of your name is typed out. If your name contains two copies of the letter it starts with, you will have difficulty, so pick another word!

	* Try Making code that autocompletes only after you've typed the first TWO letters of your name!

3. Return to [the previous lesson's assignment 3](https://zsiegel92.github.io/evilpython/games.html#assignments) and mod some of the advanced games with continuous input!

	* <a href="https://zsiegel92.github.io/evilpython/Games/treasure_continuous.py" download="treasure_continuous.py">Treasure Walker (continuous input)</a> --- ([view code](https://github.com/zsiegel92/evilpython/blob/master/Games/treasure_continuous.py))
		* Add **hazards** so that when certain locations are accessed, the player loses
			* Make sure the hazards are not placed atop the treasure!
			* Add a variable called `num_hazards` that controls the **number of hazards**
		* Add scorekeeping to keep track of the number of treasures found
		* Add a timer using the Python `time` module (`import time`)
		* Change the game so that every 5 rounds, the symbols denoting player, treasure, and boundaries change
	* <a href="https://zsiegel92.github.io/evilpython/Games/snake_continuous.py" download="snake_continuous.py">Snake (continuous input)</a> --- ([view code](https://github.com/zsiegel92/evilpython/blob/master/Games/snake_continuous.py))
		* Add scorekeeping
		* Add timekeeping
		* Change the game so that every 5 rounds, the symbols denoting snake, the food, and the boundaries change
	* <a href="https://zsiegel92.github.io/evilpython/Games/runner_continuous.py" download="runner_continuous.py">Runner (continuous input)</a> --- ([view code](https://github.com/zsiegel92/evilpython/blob/master/Games/runner_continuous.py))
		* Add scorekeeping
		* Add timekeeping
		* Change the game so that every 5 rounds, the symbols denoting player, the obstacles, and the boundaries change


<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
