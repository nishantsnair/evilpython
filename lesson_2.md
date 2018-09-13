# Evil Python Lesson 2: Executing Shell Commands from Python!

[All Lessons](https://zsiegel92.github.io/evilpython/)

[TOC]


## Python Review

In Python, we can easily implement all basic programming constructs, like:

* [**loops**](https://zsiegel92.github.io/Eitan_S/Lessons/Lesson_3_Loops/Python3.html)
* [**functions**](https://zsiegel92.github.io/Eitan_S/Lessons/Lesson_5_Functions/Python5.html)
* [**string manipulation**](https://zsiegel92.github.io/Eitan_S/Lessons/Lesson_4_Strings/Python4.html)
* [**list data structures**](https://zsiegel92.github.io/Eitan_S/Lessons/Lesson_6_Lists/Python6.html)

and more! **Please review any you don't feel 100% comfortable using**.

## Shell meets Python: `subprocess` package!

> We will be using the Python package `subprocess`. [Read about it here](https://docs.python.org/3.7/library/subprocess.html).

Create a new Python file called `shell_commands.py`. Add the following code:


```python
import subprocess
subprocess.run(['ls'])
```
This function imports the `subprocess` package and uses its function `subprocess.run` to execute a shell command, `ls`! **This runs a *shell* command from *Python***!

### Capturing Shell Output in Python

What if we want to capture the output of `ls` and use it in Python?

```python
import subprocess
output = subprocess.run(['ls'],capture_output=True).stdout
print(output)
```

> `capture_output=True` prevents commands from sending their output to the console, and instead stores the output in the command's `stdout` property, which we store in the Python variable `output`.

This command should have sent some *UGLY* output to the console! Something like

```shell
b'file1.txt\nfile2.txt\na_folder\nshell_commands.py\n'
```

From the [**string manipulation**](https://zsiegel92.github.io/Eitan_S/Lessons/Lesson_4_Strings/Python4.html) lesson, you should know that **`\n` is the *newline* character**. The `b` in front of the output means that Python is storing this as a `bytes` (*byte string*) not a regular `str` variable.

Let's modify our code to improve our output:

```python
import subprocess
output = subprocess.run(['ls'],capture_output=True).stdout.decode().splitlines()
print(output)
```

> Every Python `bytes` variable has the `decode` method, which we can call to convert our output to a standard Python `str` variable. Every Python `str` variable has the `splitlines` function, which separates the string on *newline* characters (`'\n'`), and stores the separate strings in a Python `list`.

Now your output should look nicer, kind of like this:

```shell
['file1.txt', 'file2.txt', 'a_folder', 'shell_commands.py']
```

Much better!

Since we will use this "cleaning up" so many times, let's create a Python function taht does this for us:


```python
import subprocess

def clean_run(cmd):
	output = subprocess.run([cmd],capture_output=True,shell=True).stdout.decode().splitlines()
	print(output)
	return output

clean_run("ls")
clean_run("pwd")
```

> [This script](https://github.com/zsiegel92/evilpython/blob/master/shell_commands.py) defines a function called `clean_run`. The `clean_run` function takes input `cmd`, which should store a valid shell command as a Python `str` variable. The function `clean_run` executes `cmd` using the function `subprocess.run`, `print`s its output, and `return`s its output.

> The `shell=True` argument tells `subprocess.run` to execute these commands as though you were executing them from your own shell, which allows `run` to execute commands more flexibly. For now, just include it in your `clean_run` function.

By storing our command in a tidy function, we can call it twice very easily!


### Using Python to Execute Complicated Shell Commands

What does the following Python script do?

```python
import subprocess

def clean_run(cmd):
	output = subprocess.run([cmd],capture_output=True,shell=True).stdout.decode().splitlines()
	print(output)
	return output

i = 0
while i < 5:
	clean_run("touch file_" + str(i) + ".txt")
	i = i + 1
```

> Note that in Python, `'hello' + 5` does NOT return the concatenated `str` variable `'hello5'` (unlike in Javascript). In Python, to concatenate a `str` to a variable that is not an `str` variable, we need to tell Python to turn that other variable into a `str` using the `str(other_variable)` command. This is known as **casting**, and is discussed in [**the string manipulation lesson**](https://zsiegel92.github.io/Eitan_S/Lessons/Lesson_4_Strings/Python4.html).

[Download it](https://github.com/zsiegel92/evilpython/blob/master/iterate_shell.py) and test out your idea!

### Shell Syntax Review: Multiple Shell Commands Combined with `&&`

In the shell, type

```shell
cd ~/Desktop && ls
```

> Remember to change the `/` to `\` when using Windows!

This command `cd`s to the `/home/<username>/Desktop` folder and then executes `ls`. The `&&` symbol instructs to wait for the previous command to execute before executing the next command.

Now, run this Python file, and think about how `&&` can be used in our Python workflow!

```python
import subprocess

def clean_run(cmd):
	output = subprocess.run([cmd],capture_output=True,shell=True).stdout.decode().splitlines()
	print(output)
	return output

clean_run("cd ~/Desktop && ls")
```

## Assignments

1.
	Create a Python script called `iterate_shell.py` that creates ten *files* called `file1.txt`, `file2.txt`, etc, **in the current folder**.

	If your directory looks like this:

	```shell
	.
	├── iterate_shell.py
	└── some_file
	```

	It should now look like this:

	```shell
	.
	├── file_0.txt
	├── file_1.txt
	├── file_2.txt
	├── file_3.txt
	├── file_4.txt
	├── file_5.txt
	├── file_6.txt
	├── file_7.txt
	├── file_8.txt
	├── file_9.txt
	├── iterate_shell.py
	└── some_file
	```
2.
	Create a Python script called `iterate_shell_desktop.py` that creates ten *files* **on your Desktop**. (Then delete them so your family isn't annoyed).

3.
	Create a Python script called `iterate_shell_subfolder.py` that creates ten *folders* **in the current directory**, each of which contains an empty file called `content.txt`.
