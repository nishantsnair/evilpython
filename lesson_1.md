# Evil Python Lesson 1

[All Lessons](https://zsiegel92.github.io/evilpython/)

[TOC]

## Shell Review

You have opened **Terminal**, **Command Prompt**, **PowerShell** or something equivalent.

You have seen the **shell**.

You know the following **commands**:

|Command| Name| Effect|
|--|--|--|
|`pwd`|Present Working Directory|Displays the present working directory in the console|
|`ls`|List|Displays all files and folders in the peresent working directory in the console|
|`ls <foldername>` | List | Same as `ls`, but searches in the folder `<foldername>`. Note `ls .` is the same as `ls` because `.` refers to the current present working directory|
|`ls -A`| List All | Same as `ls`, but includes hidden files and folders beginning with `.` (such as `.git`)|
| `cd <foldername>`| Change Directory | If `<foldername>` is the name of a directory *inside the current directory*, change to that directory|
| `cd ..` | Change Directory | `..` means *"the directory containing the present working directory"*, so this goes "up one level" to that directory |
| `touch <filename>` | Touch | Creates a file called `<filename>` in the present working directory|
| `mkdir <foldername>`| Make Directory | Creates a folder called `<foldername>` in the present working directory |
| `echo <text>` or `echo "<text>"`| Echo | Sends `<text>` to the console. If `<text>` contains spaces, enclose it in quotes, like `echo "hello my friend"`|
| `rm <filename>` | Remove | Removes the file called `<filename>` in the present working directory if it exists|
| `rm -rf <foldername>` | Remove Recursive | Removes the folder called `<foldername>` in the present working directory, including all its contents. Cannot be undone |


### Paths

You can refer to files and folders relative to other folders with a `/` on Unix (Mac/Linux) or a `\` on Windows, such as `touch folder1/folder2/filename` (or `touch folder1\folder2\filename`) to create a file called `filename` in `folder2`, which is inside `folder1`, which is inside the current directory.

The symbol `.` is short for *"this directory"* and `..` is short for *"the directory enclosing this one"*. You can `cd ..` to leave the current directory, and you can even `cd ../..` to leave the directory containing the current directory.

Most paths are **relative** to the current directory, so `folder/file` means *"the file called `file` in the folder called `folder`, which is in the current directory"*.

Sometimes **absolute** paths are used, which are built up from the **root directory** (which is usually your `C:` drive). These paths start with a `/`. So `/folder/file` means *"The file called `file` in the folder called `folder`, which is in the root directory"*.

The symbol `~` is an alias for your user's "home" folder, which is different on different systems. On Mac, `~/Desktop` is short for `/Users/username/Desktop`, where `username` is a Mac username. On Windows, `~\Desktop` is short for `C:\Users\username` where `username` is a Windows username.

### Shell Command Assignments

Suppose your directory looks like this:

```
.
└── topfolder
    ├── file_one
    ├── file_two
    └── midfolder
        ├── deepfolder
        │   └── deep_file
        ├── file_one
        └── file_two
```

1.
	**In one command**, create a file called `hello.py` in the directory `midfolder` so that your directory looks like this:
	```
	.
	└── topfolder
	    ├── file_one
	    ├── file_two
	    └── midfolder
	        ├── deepfolder
	        │   └── deep_file
	        ├── file_one
	        ├── file_two
	        └── hello.py
	```
2.
	**In one command**, create a directory called `sup` in `midfolder` so that your directory looks like this:
	```
	.
	└── topfolder
	    ├── file_one
	    ├── file_two
	    └── midfolder
	        ├── deepfolder
	        │   └── deep_file
	        ├── file_one
	        ├── file_two
	        └── sup
	```
3.
	**In two commands**, make your directory look like this:
	```
	.
	└── topfolder
	    ├── file_one
	    ├── file_two
	    └── midfolder
	        ├── another_file
	        ├── file_one
	        └── file_two
	```
4.
	**BONUS**
	*Undo* each of the assigned changes using shell commands.

#### Solutions

[View solutions here](https://zsiegel92.github.io/evilpython/lesson_1_solutions.html).

### Causing Problems with Shell Commands

To cause problems with these basic tools, we will need to put together a long **script** consisting of many commands. Shell scripting can be frustrating, though, as shell syntax rarely is updated and can be hard to read.

Rather than struggling with basic shell scripting, **we will build a Python script, and run these commands from there in the next lesson**.



