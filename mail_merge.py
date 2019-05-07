from emailer import send_email

class EmailData:
	from_name = ""
	about_name = ""
	to_name = ""
	to_address = ""
	occasion = ""
	location = ""
	favorite_thing = ""

	def __init__(self,from_name,about_name,to_name,to_address,occasion,location,favorite_thing):
		self.from_name = from_name
		self.about_name = about_name
		self.to_name = to_name
		self.to_address = to_address
		self.occasion = occasion
		self.location = location
		self.favorite_thing = favorite_thing


info1 = EmailData('Zach','Ethan','Michael','michael311@gmail.com','quinceañera','The Cheesecake Factory','their pretty little cupcakes')
info2 = EmailData('Elyse','Zach','Ruth','ruth22@gmail.com','first-grade graduation','Chuck-E-Cheese','terrible pizza and sticky booths')

info_list = [info1, info2]

message_template = """
Hi {to_name},

I would like to invite you to {about_name}'s' {occasion}! We will be celebrating at {location} because, as you know, {about_name} loves {favorite_thing}.

Best wishes, {from_name}
"""
subject_template = "Hi {to_name}! You're invited..."

for info in info_list:
	message = message_template.format(
	                          to_name = info.to_name,
	                          about_name = info.about_name,
	                          occasion = info.occasion,
	                          location = info.location,
	                          favorite_thing = info.favorite_thing,
	                          from_name = info.from_name
	                          )
	subject = subject_template.format(
	                                  to_name = info.to_name
	                                  )
	send_email(
	           info.to_address,
	           message,
	           subject
	           )