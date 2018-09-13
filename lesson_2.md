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

> [This script]() defines a function called `clean_run`. The `clean_run` function takes input `cmd`, which should store a valid shell command as a Python `str` variable. The function `clean_run` executes `cmd` using the function `subprocess.run`, `print`s its output, and `return`s its output.

> The `shell=True` argument tells `subprocess.run` to execute these commands as though you were executing them from your own shell, which allows `run` to execute commands more flexibly. For now, just include it in your `clean_run` function.

By storing our command in a tidy function, we can call it twice very easily!

