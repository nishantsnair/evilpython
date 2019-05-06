# Evil Python Lesson 11: User Engagement

[All Lessons](https://zsiegel92.github.io/evilpython/)

[TOC]

## Review: Sending Emails

Please review [Lesson 3: Email](https://zsiegel92.github.io/evilpython/lesson_3.html) and [Lesson 10: Mail Merge](https://zsiegel92.github.io/evilpython/lesson_10.html) from this tutorial.


## Tracking User Engagement

Now that you can mail-merge some content to your users (or customers, or friends, *or enemies*), you can start to manage their engagement with your services. We will send unique links with mail-merged emails so that you can track


### Sending Customized Emails


Make sure you have an emailing interface set up:

**Create a file called `emailer.py`**. Add this code:

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

Then, run this code from another file in the same directory to send an email:

```python
from emailer import send_email

message = "Click this link: http://127.0.0.1:5000/"
subject = "THIS IS A TEST! And this is the subject."

send_email(
           'your_own_email@host.domain',
           message,
           subject
           )
```

### Server Responses to Clicked Links

Before sending your email, create and run a Python file called `app.py` with the following code:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def basic_response():
	print("Someone clicked this link!")
	return "This is a website!"

app.run(host='0.0.0.0')
```
> Run this using `python app.py` or by setting environment variables using the following commands:
>
> `export FLASK_APP=app.py` (mac)
> `$env:FLASK_APP = "hello.py"` (Windows Powershell)
> `set FLASK_APP=app.py` (Windows Command Prompt)
>
> Then, you can run the app with the command:
> `flask run`
>
> **Note**: If the *Flask* micro-framework package is not installed on your computer, run the following command then repeat the steps above:
> `pip install flask`


When you run this script, you will be hosting a website! It will only be visible on your home network, which makes it safer. You should see something in your console like:

```bash
$ python app.py
 * Tip: There are .env files present. Do "pip install python-dotenv" to use them.
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

If your URL, in this case `https://127.0.0.1:5000/` is different from the one here, make sure to include the correct link in the email you send.

#### Custom Links

Your emails are customizable in many ways (see previous lesson), and we can tell the server exactly who clicked the emailed link.

Change your email to the following:

```python
from emailer import send_email
from urllib import parse

name = "Zach Siegel"
message = "Click this link: http://127.0.0.1:5000/click/{}".format(parse.quote(name))
subject = "THIS IS A TEST! And this is the subject."

send_email(
           'your_own_email@host.domain',
           message,
           subject
           )
```
> The function `urllib.parse.quote` turns a Python `str` variable into a valid URL argument. For example, URLs typically do not include spaces (although they can), so the url `http://127.0.0.1:5000/click/Zach Siegel` would be changed to `http://localhost:5000/click/Zach%20Siegel`, which the Flask server decodes automatically.

Now, change your app to have the following code:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def basic_response():
	print("Someone clicked this link!")
	return "This is a Website!"

@app.route("/click/<user>")
def name_response(user):
	print("{} clicked this link!".format(user))
	return "This is a Website!"

app.run(host='0.0.0.0')
```

## Storing User Interactions in a Database

**More on this next time**!

## Formatting with Jinja2

Jinja 2 is a Python package tht allows formatting with much more precision than the Python built-in `format` function. **More on this next time**!

## Reading data from a spreadsheet

**More on this next time**!

## Assignments
