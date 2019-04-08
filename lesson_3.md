# Evil Python Lesson 3: Email!

[All Lessons](https://zsiegel92.github.io/evilpython/)

[TOC]

## What is email?


<img alt="How email works." src="email_overview.png">


>"The diagram to the right shows a typical sequence of events that takes place when sender Alice transmits a message using a mail user agent (MUA) addressed to the email address of the recipient.[28]
>
>Email operation
>
><ol>
	<li> The MUA formats the message in email format and uses the submission protocol, a profile of the Simple Mail Transfer Protocol (SMTP), to send the message content to the local mail submission agent (MSA), in this case smtp.a.org. </li>
	<li>The MSA determines the destination address provided in the SMTP protocol (not from the message header), in this case bob@b.org which is a fully qualified domain address (FQDA). The part before the @ sign is the local part of the address, often the username of the recipient, and the part after the @ sign is a domain name. The MSA resolves a domain name to determine the fully qualified domain name of the mail server in the Domain Name System (DNS).</li>
	<li>The DNS server for the domain b.org (ns.b.org) responds with any MX records listing the mail exchange servers for that domain, in this case mx.b.org, a message transfer agent (MTA) server run by the recipient's ISP.[29]</li>
	<li>smtp.a.org sends the message to mx.b.org using SMTP. This server may need to forward the message to other MTAs before the message reaches the final message delivery agent (MDA).</li>
	<li>The MDA delivers it to the mailbox of user bob.</li>
	<li>Bob's MUA picks up the message using either the Post Office Protocol (POP3) or the Internet Message Access Protocol (IMAP)." - *[Wikipedia "Email"](https://en.wikipedia.org/wiki/Email#Operation)*</li>
	</ol>

### Making an Email Account for Development

When programatically sending emails, **SECURITY IS OF THE UTMOST IMPORTANCE!**.

1. Start by [creating a "dummy" email account with GMail](https://accounts.google.com/signup) using a real email account as the "backup" for the account.
2. **Create a secure password, and WRITE IT DOWN!**
3. In your inbox, click the user badge, and select "Google Account" (top right-hand corner of the page). Click on "Security" on the left.
4. Go down to "Less secure app access" and TURN IT ON! We are building a "less secure" app.

## Environment Variables

Try running the following command in the shell (NOT in Python):

* `export hello="sup"`
* `echo $hello`
> On Windows, you may need to use `set hello="sup"`.

Clearly the shell saves those variables somewhere! These are called ***environment variables***.

### Access Environment Variables from Python?

#### Getting Environment Variables

```python
import os

print(os.environ['hello'])
```
> If you are on Windows, you may need to use `os.getenv('hello')`.

#### Setting Environment Variables

```python
import os

os.environ['hello'] = "Sup, my friend?"
print(os.environ['hello'])
```
> On Windows, you may need to use `os.putenv('hello','Sup, my friend?')` and `print(os.getenv('hello'))`.

#### Python Doesn't Change the Outer Environment

Run this snippet from Python, then quit Python and, from the shell, type `echo hello`. ***Nothing changed! Why?***

Python's interaction with the environment variables is one-way. You can read and alter the environment variables within a Python environment, but they will revert once Python quits.


#### Never Store Credentials in Code!!

***Never store login credentials in code!*** Your code might get backed up, synced to a cloud server, uploaded to a version control manager (like GitHub), might float around the internet forever in potentially insecure ways, etc. So, **do not store credentials in code!!**.

How to use credentials in code:

1. Okay: `pasword = input("Please enter your password")`
2. Better: `password = os.getenv('PASSWORD')`
3. Even Better: store password in encrypted database.
4. Best: Require all logins to use 2-factor authentication. Then, whenever code tries to use your login, you will just authorize the access from a separate device (phone, email, etc).



## Email Client

There is [a fully-functional email client here](https://github.com/zsiegel92/evilpython/blob/master/emailer.py). We will now make one ourselves!

### Goal: Sending Email using Email Client

```python
from emailer import Emailer
import os

username = input("Enter username")
password = input("Enter password")
to_address = input("To whom should a message be sent?")

# Set environment variables.
# The Emailer object automatically reads these for credentials.
# This is relatively secure.
os.environ['EMAIL'] = username
os.environ['EMAIL_PASSWORD'] = password

emailer = Emailer()
emailer.email(to_address,message="generic_emailer_message",subject="generic_emailer_subject")
```

### Building an Email Client Using `smtplib`

```python
import os
import smtplib

username = input("Enter username")
password = input("Enter password")
to_address = input("To whom should a message be sent?")

message = "the message"
subject = "the subject"

fullMessage = "\r\n".join([
	"From: " + username,
	"To: " + to_address,
	"Subject: " + subject,
	"",
	message
])
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(username, password)
server.sendmail(username, to_address, fullMessage)
server.close()
```

## Assignments

1. Use the above snippet to organize your code into a `class` called `Emailer` in a file called `emailer.py`, like [the one provided](https://github.com/zsiegel92/evilpython/blob/master/emailer.py).
>
> You may need to refer to [Lesson 7: Object Classes](https://zsiegel92.github.io/Eitan_S/Lessons/Lesson_7_Classes/Python7.html) from the [Web Development Tutorial](https://zsiegel92.github.io/Eitan_S/).

2. Implement any of [the games you've made](https://zsiegel92.github.io/evilpython/lesson_7.html) so that when the game is finished, you are emailed a message with your score!
