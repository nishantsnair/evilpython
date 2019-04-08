# from emailer import Emailer
# import os

# username = input("Enter username")
# password = input("Enter password")

# to_address = input("To whom should a message be sent?")

# os.environ['EMAIL'] = username
# os.environ['EMAIL_PASSWORD'] = password

# emailer = Emailer()
# emailer.email(to_address,message="generic_emailer_message",subject="generic_emailer_subject")

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
