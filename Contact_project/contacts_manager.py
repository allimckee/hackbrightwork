'''
You will create a new file called contact_manager.py. It will make use the Contact class as a module. The purpose of contact_manager is to manage the contacts list. Create a list to hold the contacts.
It can:
show current contacts
add a new one
edit an existing one
delete an existing one
Special cases:
Remember to handle special cases like upper/lower case names.
For this exercise, assume that you cannot have a duplicate contact with the same first and last name. Make sure to print out an error message when necessary.
Make sure to test your functions in a main() function.


'''

import contact

def show_all_contacts():
	#print the contact list
	#if there are no contacts print there are no contacts press 2 to add a new contact
	if len(contact.contacts) == 0: 
		print "Go out and make a friend!"
	else:
		for person in contact.contacts:
			print person.first_name, person.last_name, person.email, person.birthday, person.phone_number

def add_a_new_contact():
	#check for white spaces and upper or lower case it
	first_name = first_name.upper.strip
	last_name = last_name.upper.strip
	email = email.lower.strip
	birthday = str(birthday.strip)
	phone_number = str(phone_number.strip)
	new_contact = contact.Contact(first_name, last_name, email = email, birthday = birthday, phone_number = phone number)
	#check if contact.contacts is empty, and if so create it with this instance
	if not contact.contacts
		contact.contacts.append(new_contact)
	else:
		#check if there's a duplicate. 
			for item in contact.contacts:
				if first_name in contact.contacts.first_name == item and last_name in contact.contacts.last_name ==item
					print "Nice try, bucko. You've already added this person."
				#if so, print error
				else:
				#if not, add it
				contact.contacts.append(new_contact)

	#check to see if there is a duplicate, and you have to check the first and last name, AND also make sure that it is iterating throughout the entire contacts list before adding, AND if it finds a duplicate it can stop



	for item in contact.contacts 


	#instantiate and instance
	#print back the instance that was inputed

def edit_contact():
	pass
	#what part of the class are you editing? Pick a number from a list (first, last, email = "", birthday = "", phone = "")
	#check to see if there is a duplicate, and you have to check the first and last name, AND also make sure that it is iterating throughout the entire contacts list before adding, AND if it finds a duplicate it can stop
	#edit the list, by overwriting the old attribute with the new one
	#then print new contact, everything in it

def delete_contact():
	pass
	#delete contact (self?)



def main():
	show_all_contacts()
	

if __name__ == '__main__':
	main()