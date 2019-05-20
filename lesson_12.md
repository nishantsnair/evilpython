# Evil Python Lesson 12: Cloud-Based User Engagement Platform

[All Lessons](https://zsiegel92.github.io/evilpython/)

[TOC]

## Overview

In this lesson, we will create a cloud-hosted webapp that collects user engagement.

## Install Necessary Software

### Set up Git

* Create a [GitHub](https://github.com/) account
	* Follow the on-screen instructions to create your GitHub account.
* Install Git
	* [Download Git](https://git-scm.com/downloads)
	* Follow instructions to install Git, a command-line tool for version control.

### Set up Heroku

* Sign up for [Heroku](heroku.com)
* Install Heroku CLI (*Command Line Interface*)
	* [Download](https://devcenter.heroku.com/articles/heroku-cli)
	* Follow instructions to install Heroku CLIS

## Create a New Repository

### Local Repository

* Create a folder called `app` or `webapp`
* Make it into a **git repository** ("repo") by typing `git init`.
	* This will create an invisible folder called `/.git` and an invisible
* Type `echo >> .gitignore`. **This will create an empty (invisible) file that keeps track of the stuff you don't want to sync with Git**.
* Type `echo # Test App! >> README`
	* This will create a basic `README` file with only a header taht says "Test App!". You can make it say whatever you want.
		* The `README` file will be interpreted in the **Markdown** language. [Read more about Markdown here](https://en.wikipedia.org/wiki/Markdown). (This website was created using Markdown.)
* Type `git add .`
	* the "`.`" refers to *the current directory*. The command `git add .` adds all files in the current directory (only the `README` at this point) to the git file tracking. Changes to those files will be eligible for commitment to the repository.
* Type `git commit -m "First commit!"`
	* The command `git commit` is how you commit changes to the local (not online) version of your repository
	* The `-m "some message"` is how you give an informative "commit message" for your commit, describing the changes. This is actually necessary (if you omit the `-m "some message"`, you will be forced to write one in your command prompt's default text editor, which is usually a pain).

### Upload to GitHub

* Visit [Github](https://github.com), click the "**+**" sign and click "**New Repository**".
* Name the repository something similar (or identical) to the folder you created (like "app" or "webapp").
* Give an informative description for the repository.
	* For this repo, the following works well: "A web application hosted on Heroku".
* Click "**Create Repository**"
* You will see some on-screen instructions to "**push an existing repository from the command line**". That's what you want to do! The instructions will be easy to spot on GitHub, with the correct URL, so you should copy them from there.
	* If your GitHub username is `<username>` and your repository is called `<my_repo>`, you'll be asked to use these commands:
	* 
		```
			git remote add origin https://github.com/<username>/<my_repo>.git
			git push -u origin master
		```
	* You may be asked to log into GitHub the first time you use the command line interface.

## Create an App, Associate it with your Repository

* Visit the [Heroku Dashboard](https://dashboard.heroku.com)
* Click on "**New**" and select "**Create new app**"
	* Follow the directions - enter an app name. Unlike GitHub repositories, different users can't create Heroku apps with the same name. So, you may need to call your app something like `testapp-may-2019` or add a number at the end.
* Once you've created the app, click on "**Connect to GitHub**" and connect your account. Then, type in the name of your repository in the box that says `repo-name`, and select it.
* Click the box that says "**Enable Automatic Deploys**", then click "**Deploy Branch**". At this point, deployment should fail. Our goal is to make it succeed.

## Create a Basic Web Application

Create the **most basic possible web application** using Python's Flask. Copy the following into a file called `app.py`:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "Success! Welcome to this web app."

app.run()
```
> You may need to type `pip install flask` before typing `python app.py` to install Flask.

Make sure this runs properly on your computer. Now, to run properly on Heroku, we will need to change it to this:


```python
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
	return "Success! Welcome to this web app."

port = int(os.environ.get("PORT", 33507))
app.run(host='0.0.0.0', port=port)
```
> Changing the `host` and `port` are necessary to make the app work properly on Heroku.

### Giving "Run Instructions" for Heroku

Heroku mainly uses two files to run your code on its cloud computers: a **procfile** ("process file") and a **requirements file**.

#### Procfile

Heroku machines have several different "process types", but we will only use one: a "web dyno", which runs a web application.

To tell Heroku how to run your code on a web dyno, create a file called `Procfile` (not `Procfile.txt` or anything with a file extension or a lowercase "p"!). Open your procfile and add only the following command:

```
web: python app.py
```
> This just means "run my code with the command `python app.py` on a web dyno type of machine".

#### Requirements File

Type `pip freeze` and you should see a list of Python packages (and their versions) installed on your machine. We want the cloud machine to install all of these packages so that it can run your code the same way you do. Create a file called `requirements.txt` and copy the output of `pip freeze` into that file.

You can do this with one slick command:

`pip freeze >> requirements.txt`

## Push Your Webapp!

Push your changes to GitHub. If you turned on "Automatic Deploy" on Heroku, Heroku will immmediately start updating your app on its server.

* Type `git add .`
* Type `git commit -m "app is set up"`
* Type `git push origin master`

If you are at the [Heroku Dashboard](dashboard.heroku.com) and click on your app, you should see some activity that says your app is being "built".

## Scale Your Webapp

Our procfile notes what type of machine our app should run on. If you click on "Resources" in the [Heroku Dashboard](dashboard.heroku.com), you should see the contents of your `Procfile`. By default, your app will be running on a "free Heroku web dyno", which means that when you don't access it for 30 minutes, it goes to sleep, and it will then take 2-15 seconds to start back up when you visit it. It can be awake no more than 18 hours per day or so.

Note the slider - you can upgrade  your cloud machine to be (much, much) more powerful than the most powerful home computers. You could technically use Heroku to run a full instance of Windows or Linux and host a game server that you connect to with your friends!
> Potentially great for those who don't want to buy Xbox Live.

### Visit App/Troubleshooting

Click on "Activity" and you should see the option to "View build log" for the most recent upload. At the bottom of that build log, you'll see a URL where you can visit your application.

If your app is called `<my-app>`, your URL will be

```
https://<my-app>.herokuapp.com/
```

### Fully Utlizing the CLI (Command Line Interface)

Note that on [blog.heroku.com](https://blog.heroku.com/python_and_django) there are instructions to launch a Flask web application like we did **fully from the command line**:


```bash

$ heroku create --stack cedar
Creating young-fire-2556... done, stack is cedar
http://young-fire-2556.herokuapp.com/ | git@heroku.com:young-fire-2556.git
Git remote heroku added

$ git push heroku master
Counting objects: 5, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 495 bytes, done.
Total 5 (delta 0), reused 0 (delta 0)

$ git push heroku master
Counting objects: 5, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 495 bytes, done.
Total 5 (delta 0), reused 0 (delta 0)

-----> Heroku receiving push
-----> Python app detected
-----> Preparing virtualenv version 1.6.1
   New python executable in ./bin/python2.7
   Also creating executable in ./bin/python
   Installing setuptools............done.
   Installing pip...............done.
-----> Installing dependencies using pip version 1.0.1
   Downloading/unpacking Flask==0.7.2 (from -r requirements.txt (line 1))
   ...
   Successfully installed Flask Werkzeug Jinja2
   Cleaning up...
-----> Discovering process types
   Procfile declares types -> web
-----> Compiled slug size is 3.5MB
-----> Launching... done, v2
   http://young-fire-2556.herokuapp.com deployed to Heroku

To git@heroku.com:young-fire-2556.git
 * [new branch]      master -> master

```
> `heroku create --stack cedar` creates an app with a random name (in this case it turned out to be "`young-fire-2556`") on Heroku's "cedar" servers.
>
> If you want to create an app called `example and you don't care what servers it's on (you probably don't), juse use the command:
>
> `heroku create example`

 You can even access your app from the command line! If your app is called `my-app`, you would enter the following, and see the following output from our app:

 ```
 $ curl http://my-app.herokuapp.com/
 "Success! Welcome to this web app."
 ```

## Setting Environment Variables in the Heroku CLI

Type `heroku login` in your command prompt to ensure you are logged in.

Type `heroku apps` to view a list of your current applications. You should see the name of your app. Every command that refers to a specific app called `my-app` needs to contain the option `--app my-app` somewhere.

To set an environment variable called `var1` to have the value `value1` on an app called `my-app`, you will have to type:

`heroku config:set var1=value1 --app my-app`
> If `value1` was instead a value with multiple space-separated words, you'd have to wrap it in quotes.
>
> For example, on my app `testapp-may2019`, to change the `owner` environment variable to `Zach Siegel`, I'd type:
> ```
> heroku config:set owner="Zach Siegel" --app testapp-may2019
> ```

To view your environment variables for the app `my-app`, you have to type:

```
heroku config --app my-app
```

For example, running this for `testapp-may2019` gives the following output:

```
heroku config --app testapp-may2019
=== testapp-may2019 Config Vars
owner: Zach Siegel
var1:  value1
```

## Assignment

1. Create a Heroku webapp. Set the environment variables `EMAIL` and `PASSWORD` to the email and password of the "*burner*" email account you made. not an email address you care about! 
	> What we're doing is safe, but it's very easy to accidentally save a password in a Git repository and upload it for the whole world. There are bots that are constantly prowling GitHub for password to steal.

	In your app, you can access environment variables by using `import os` and, for example:

	```python
	os.environ.get("EMAIL")
	```

	Make the webapp send some emails (any emails) when you visit the link with route `/send_emails`.

	Push your changes using:

	```
	git add .
	git commit -m "commit messaage"
	git push origin master
	```
