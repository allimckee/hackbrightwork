contacts = {("Diana", "Banana"): "888-888-4568", ("M.J.", "Grey"): "888-879-7893", ("Ryan", "Gunnar"): "415-346-7895"}  

def addcontact_changenum(person_name, phone_number):
	contacts[person_name]=phone_number 

def change_lastname():
	name_list = contacts.keys()
	for name in name_list:
		print name[0], name[1]
	


#{"Diana Banana": "888-888-4568", "M.J. Grey": "888-879-7893", "Ryan Gunnar": "415-346-7895"} 

def main():
	change_lastname()

if __name__ == '__main__':
 	main()