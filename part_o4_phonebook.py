# Use a dict to store at least 5 contacts. Make a menu in a loop: 1) add, 2) search, 3) delete,
# 4) show all, 5) exit. Searching for a missing name must print “Not found”, not crash (use
# .get() or in ).
#dict to store contacts
contacts = {
    "Ali": "03331234567",
    "Babar": "03001234567",
    "Shab": "03421234567",
    "fahad": "03211234567",
    "Jan": "03121234567"
}
#menu loop
while True:
    print("1) Add contact")
    print("2) Search contact")
    print("3) Delete contact")
    print("4) Show all contacts")
    print("5) Exit")
    #input from user for choice
    choice = input("Enter your choice: ")
    #selecting the choice and performing the corresponding action
    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        #adding the contact to the dictionary   
        contacts[name] = number
        print("Contact sucessfully added.")
    elif choice == "2":
        name = input("Enter name to search: ")
        #using .get() method to search for the contact and print the result
        number = contacts.get(name)
        #checking if the contact exists and printing the result
        if number:
            print(f"{name}: {number}")
        else:
            print("Not found.")
    elif choice == "3":
        name = input("Enter name to delete: ")
        #using 'in' to check if the contact exists and delete it if found
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Not found.")
    elif choice == "4":
        #printing all contacts using a for loop,
        for name, number in contacts.items():
            print(f"{name}: {number}")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")