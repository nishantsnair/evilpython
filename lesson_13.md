# Evil Python Lesson 3: Cloud-Hosted App FUn

[All Lessons](https://zsiegel92.github.io/evilpython/)

[TOC]

## Overview

In this lesson, we will configure some interactions between a cloud-hosted webapp and a user.

## App Setup

At this point you should have the following:

* **Git repository** on GitHub containing a Flask webapp
	* Use these commands to upload changes:
		* `git add .`
		* `git commit -m "commit message here"`
		* git push origin master
* **Heroku app** configured to run the code in your GitHub repository
	* To set the default app (so you don't have to type `--app appname` all the time):
		* `heroku git:remote -a appname`
		* (replace `appname` with your app's name)
	* To view environment variables:
		* `heroku config`
	* To navigate your server using the command prompt:
		* `heroku run bash -- app appname`
* **Environment variables** set called "EMAIL" and "PASSWORD" for a gmail account that you *do not use for anything important*
	* These should be set *locally* (on your computer) using one of the following:
		* `export var1=value1` (Mac)
		* `$Env:var1=value1` (Windows Powershell)
		* `@set var1=value1` (Windows `cmder` shell)
	* These should be set *remotely* (on your Heroku server) using the following (here for an app called `appname`):
		* `heroku config:set var1=value1 --app appname`

## Emailer Package

You should have created a Python package called `emailer` in a file called `emailer.py` that can send emails with a simple command. It should look something like this:

```python
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to_address, html_body, subject):
    username = os.environ.get('EMAIL')
    password = os.environ.get('PASSWORD')

    html = f"<html><head></head><body>{html_body}</body></html>"

    msg = MIMEMultipart('alternative')
    msg['Subject']=subject
    msg['From']=username
    msg['To']=to_address
    msg.attach(MIMEText(html,'html'))

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(username, password)
    server.sendmail(username, to_address, msg.as_string())
    server.close()
```


## App So Far

Your app should have the ability to shoot off an email when you visit a URL:

```python
from flask import Flask
import os
from emailer import send_email


app = Flask(__name__)

@app.route("/")
def basic_response():
    print("Someone clicked this link!")
    return """
      Click this link to get a cool email: <a href='http://127.0.0.1:33507/send_something'>LINK</a>
    """
@app.route("/click/<user>")
def name_response(user):
    print("{} clicked this link!".format(user))
    return "This is a Website!"

@app.route("/send_something")
def send_something():
  subject = "THIS IS A TEST! And this is the subject."
  message = """
    Click <a href="http://127.0.0.1:33507/">this link</a> to return to our website.
  """
  send_email(
             'your_email@domain.com', message, subject)
  return "OKAY - email sent."


port = int(os.environ.get("PORT", 33507))
app.run(host='0.0.0.0', port=port)
```

## Custom Emails based on URL

Change your `/send_something` route to the following:

```python
@app.route("/send_something/<user_email>")
def send_something(user_email):
  subject = f"Hello, {user_email}"
  message = """
  	Hi, {username},


    Click <a href="http://127.0.0.1:33507/">this link</a> to return to our website.
  """
  message = message.format(username=user_email)
  send_email(
             user_email, message, subject)
  return f"OKAY - email sent to {user_email}"
```

Make sure you successfully receive an email when you visit `http://127.0.0.1:33507/send_something/YOUR_EMAIL_HERE` (with `YOUR_EMAIL_HERE` replaced with your email).

## HTML Template with a custom link!

Create a folder called `templates` in the same folder as `app.py`. In that folder, save the following HTML webpage in a file called `linker.html`:

```html
	<html>
	<head>
	    <title>Click my link!</title>
	</head>
	<body>

		<input type="text" id="input">
		<button type="button" id="thebutton">Click Me!</button>

		<script type="text/javascript">
			document.getElementById("thebutton").addEventListener("click", travel_to_email_link);
			function travel_to_email_link(){
		   var inputValue = document.getElementById("input").value;
		   var base_url = "http://127.0.0.1:33507"; //Local version
		   // var base_url = "http://test-app-zsze.herokuapp.com/"; // Cloud version
		   window.location.replace(base_url + "/send_to/"+inputValue);
			 }
		</script>
	</body>
	</html>
```

Now, create a route called `/contact` that looks like this:

```python
@app.route("/contact")
def name_response():
    return render_template('linker.html')
```

Run your app using `python app.py` and visit the url with the route `/contact`. **Make sure you receive an email when you click the button!!**

## Pushing changes - with versioning!

Change the `linker.html` file to include the link to the *cloud* version (some URL with `.herokuapp.com`) instead of the *local* version (some URL with `.0.0.1:33507`) by un-commenting that line.

Push your changes to the GitHub repository that your app is using and try out all the routes!

## Variable Versioning with Environment Variables!

We can use environment variables to automatically set our `base_url` in our cloud-hosted and locally-hosted app.

**Create a local environment variable called `base_url`**. It will look like this:

* `export base_url=http://127.0.0.1:33507` (Mac)
* `$Env:base_url=http://127.0.0.1:33507` (Windows Powershell)
* `@set base_url=http://127.0.0.1:33507` (Windows `cmder` shell)


Now, set this on your Heroku server (change `test-app-zeze` to your app's name):

* `heroku config:set base_url=https://test-app-zsze.herokuapp.com --app test-app-zsze`

Now, change your `/contact` route function to the following:

```python
@app.route("/contact")
def name_response():
    return render_template('linker.html',base_url=os.environ['base_url'])
```

and change your `linker.html` file to the following:

```html
<html>
<head>
    <title>Click my link!</title>
</head>
<body>

	Enter your email here to receive a cool email: <input type="text" id="input">
	<br>
	<button type="button" id="thebutton">Click Me!</button>

	<script type="text/javascript">
		document.getElementById("thebutton").addEventListener("click", travel_to_email_link);
		function travel_to_email_link(){
	   var inputValue = document.getElementById("input").value;
	   window.location.replace("{{base_url}}" + "/send_something/"+inputValue);
		 }
	</script>
</body>
</html>
```

Run this code locally, upload your changes to GitHub and test in on Heroku!

Now you don't need to maintain separate versions of your code for the *local* and *remote* (/*cloud*) versions of your app!

## Assignment

1. Make the HTML page display soemthing like: "You have entered: zsiegel@gmai" as you are entering text into the text box. Use [this example](https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_oninput) for inspiration and guidance.
