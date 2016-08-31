contacts = []

class Contact(object):
	def __init__(self, first, last, email = "", birthday = "", phone = ""):
		self.first_name = first
		self.last_name = last 
		self.email = email
		self.birthday  = birthday
		self.phone_number = phone

	def send_text(self, message):
		if len(self.phone_number) > 0: 
			print "To: %s - %s" % (self.phone_number, message)
		else:
			print "Nice try! Please add a phone number to text"

def main():
		
	contact_diana = Contact("Diana", "Smith", phone = "888-583-9875")
	contact_amy = Contact("Amy", "Wong", email = "a.while@yahoo.com")
	contact_wes = Contact("Wes", "Snow", birthday = "08/09/1987")

	contacts.append(contact_diana)
	contacts.append(contact_amy)
	contacts.append(contact_wes)

	for person in contacts:
		print person.first_name, person.last_name, person.email, person.birthday, person.phone_number
	
	for person in contacts:
		person.send_text("Hi! What's up!")


if __name__ == '__main__':
	main()