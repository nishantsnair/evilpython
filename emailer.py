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