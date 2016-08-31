'''
This module’s purpose is to provide a textual UI to interact with the Contact Manager. You will import contact_manager.py. Take a look at the last lecture’s exercise Part 2 to help you through this.
The UI(user-interface) menu will have the following options for a user to choose from running with a while loop:
"0 - Main Menu"
"1 - Show all contacts"
"2 - Add a new contact"
"3 - Edit a contact"
"4 - Delete a contact"
"5 - Exit the program."
Bonus Challenges
'''
import contact_manager

def menu():
    while True:
        print ""
        print "Select a Menu Option:"
        print "		0 - Main Menu"
        print "     1 - Show all contacts"
        print "     2 - Add a new contact"
        print "     3 - Edit a contact"
        print "     4 - Delete a contact"
        print "     5 - Exit the program"
        choice = raw_input("-->  ")
        if choice not in str(range(6)):
            print "'" + str(choice) + "' was not a menu item."
        else:
            return int(choice)
def main():
    choice = None
    while choice != 5:
        choice = menu()
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        else:
            print "Goodbye."

if __name__ == '__main__':
    main()