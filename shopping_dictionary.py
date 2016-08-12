'''
A menu of shopping lists that does: 
0 - Main Menu
1 - Show all lists.
2 - Show a specific list.
3 - Add a new shopping list.
4 - Add an item to a shopping list.
5 - Remove an item from a shopping list.
6 - Remove a list by nickname.
7 - Exit when you are done.  

'''
all_shopping_lists = {}
all_shopping_lists = {"safeway":["socks","soap"], "target":["toothbrush"]}

def sort_items(key):
	#alphabetize the items within the lists when they're displayed
	list_sort = all_shopping_lists[key]
	list_sort.sort()
	return list_sort
	

def display_menu():
	#printing the menu options 0 through 7 as a dictionary
	print ''' A menu of shopping lists that does: 
	0 - Main Menu
	1 - Show all lists.
	2 - Show a specific list.
	3 - Add a new shopping list.
	4 - Add an item to a shopping list.
	5 - Remove an item from a shopping list.
	6 - Remove a list by nickname.
	7 - Exit when you are done.  '''

# display_menu()	

def show_all_lists():
	#printing the dictionary that holds the lists
	#Could print just the keys, OR print keys and values
	#print all_shopping_lists.keys()
	print all_shopping_lists.items()

# show_all_lists()

def show_list(key):
	#ask the user for the key
	#print the values for that key
	print sort_items(key)

def add_new_list(key):
	#ask user the name of the new list (aka key)
	#print you've added a list for X
	#Prompt user to add items to list now
	#call the add item function, we will set the key, and then they can add items to list
	#return new list with all items
	key=key.lower()
	if key in all_shopping_lists:
		print key + " is already one of your lists."
	else:
		all_shopping_lists[key] = []
		print key + " has been added."
	
def add_item(key, item):
	#ask user for the key (aka the list)
	#then prompt user what item they want to add
	#check to see if that item exists, if it does write item already exists
	#if item doesn't exist then return list with new item
	#ask user if they want to add anything else or return to main menu, if y then call add item function again, if n, then return to main menu
	key = key.lower()
	item = item.lower()
	if key in all_shopping_lists:
		shopping_list = all_shopping_lists[key]
		if item in shopping_list:
			print "You have already added this item."
		else:
			shopping_list.append(item)
			all_shopping_lists[key] = shopping_list
			clean_list = sorted(shopping_list)
			print "Your new list contains", shopping_list
	else:
		print key + " does not exist."

def remove_item(key,item):
	#ask user for the key (aka the list)
	#then prompt user what item they want to remove
	#then return list witout that item
	#return to main menu
	pass

def remove_list(key):
	#show the user all of the lists and then prompt user what key/list they want to remove
	#then return the dictionary keys without the removed key
	#return the lists that remain
	#return to main menu
	pass

def exit_menu():
	#break out of the while loop thats from the main function
	pass

def main():
	#while loop that prompts the user to use the menu with option to break the loop
	pass