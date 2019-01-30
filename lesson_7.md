# Evil Python Lesson 7: More Games!

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

## Assignments

1. Make <a href="https://zsiegel92.github.io/evilpython/Games/rock_paper_scissors_skeleton.py" download="rock_paper_scissors_skeleton.py">This Rock-Paper-Scissors 'Skeleton'</a> --- ([view code](https://github.com/zsiegel92/evilpython/blob/master/Games/rock_paper_scissors_skeleton.py)) into a functioning Rock-Paper-Scissors game that tells you who won! Then,
	* Add a move-timer
	* Make the game keep score based on how many wins each player has, and print the score after each round
	* Add a score limit, which ends the game after a certain score!

```python
from pynput import keyboard

p1_move = False
p2_move = False

def press_callback(key):
	global p1_move,p2_move
	if not p1_move:
		if key.char == 'a':
			p1_move = 'rock'
		elif key.char == 's':
			p1_move = 'paper'
		elif key.char == 'd':
			p1_move = 'scissors'
	if not p2_move:
		if key.char == 'j':
			p2_move = 'rock'
		elif key.char == 'k':
			p2_move = 'paper'
		elif key.char == 'l':
			p2_move = 'scissors'
	print("\n"*50) # Hides previous move by moving command prompt
	if p1_move and p2_move:
		return False

def play():
	global p1_move,p2_move
	p1_move = False
	p2_move = False
	l = keyboard.Listener(on_press=press_callback)
	l.start()
	print("\n\n\nReady!")
	print("Player 1 presses 'a','s', and 'd' to play rock-paper-scissors")
	print("Player 2 presses 'j','k', and 'l' to play rock-paper-scissors")
	l.join()
	print(f"\n\n\nPlayer 1 played {p1_move} and Player 2 played {p2_move}")

while True:
	play()
```
