import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

class Emailer:

	def __init__(self):
		self.gmail_user = os.environ['EMAIL']
		self.gmail_password=os.environ['EMAIL_PASSWORD']

	def get_email(self):
		return self.gmail_user


	def email(self,toAddress=None,message="generic_emailer_message",subject="generic_emailer_subject"):
		self.direct_email(toAddress,self.gmail_user,self.gmail_password,message,subject)

	@classmethod
	def direct_email(cls,sent_to,sent_from,password,message="",subject="",error=False):
		print("in Emailer.direct_email")
		try:
			fullMessage = "\r\n".join([
				"From: " + sent_from,
				"To: " + sent_to,
				"Subject: " + subject,
				"",
				message
			])
			server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
			server.ehlo()
			server.login(sent_from, password)
			server.sendmail(sent_from, sent_to, fullMessage)
			server.close()
		except Exception as exc:
			print('Something went wrong with login.')
			print("exception: " + str(exc))
			if error is False:
				cls.direct_email(sent_from,sent_from,password,message="ERROR SENDING message to " + str(sent_to) +"!\n" + str(message),subject="ERROR MESSAGE for: " + str(subject),error=True)
		else:
			print("Message sent successfully.")


	@classmethod
	def send_from_server(cls,fromAddress,password,toAddress,message):
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(fromAddress, password)
		server.sendmail(fromAddress, toAddress, message)
		server.close()

	def send_html_body(self,toAddress,html_body,subject="",text_message=""):
		print("in Emailer.send_html_body")
		html = '<html><head></head><body>{body}</body></html>'.format(body=html_body)
		return self.send_html(toAddress,html,subject,text_message)

	def self_send_html_body(self,html_body,subject="",text_message=""):
		self.send_html_body(self.gmail_user,html_body,subject,text_message)

	def send_html(self,toAddress,html_message,subject="",text_message="",attachments={}):
		print("in Emailer.send_html")
		msg = MIMEMultipart('alternative')
		msg['Subject']=subject
		msg['From']=self.gmail_user
		msg['To']=toAddress
		html = html_message

		for content_id in attachments:
			fp = open(attachments[content_id], 'rb')
			img = MIMEImage(fp.read())
			fp.close()
			img.add_header('Content-ID', '<{}>'.format(content_id))
			msg.attach(img)

		if text_message=="":
			text = html_message
		else:
			text=text_message

		msg.attach(MIMEText(text,'plain'))
		msg.attach(MIMEText(html,'html'))


		self.send_from_server(msg['From'],self.gmail_password,msg['To'],msg.as_string())


