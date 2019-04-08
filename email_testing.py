from emailer import Emailer
import os

username = input("Enter username")
password = input("Enter password")

to_address = input("To whom should a message be sent?")

os.environ['EMAIL'] = username
os.environ['EMAIL_PASSWORD'] = password

emailer = Emailer()
emailer.email(to_address,message="generic_emailer_message",subject="generic_emailer_subject")
