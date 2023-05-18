print("**********************************")
print("Welcome to Phonebook Application")
print("**********************************")
print("")

phonebook = {}  # Empty phonebook

def find_contact():
    name = input("Enter the name to find the phone number: ")
    if name in phonebook:
        print("Phone number:", phonebook[name])
    else:
        print("Contact not found.")

def insert_contact():
    name = input("Enter the name to insert: ")
    number = input("Enter the phone number: ")
    phonebook[name] = number
    print("Contact inserted successfully.")

def delete_contact():
    name = input("Enter the name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def terminate():
    print("Phonebook application terminated.")
    exit()

while True:
    print("Welcome to the phonebook application")
    print("1. Find phone number")
    print("2. Insert a phone number")
    print("3. Delete a person from the phonebook")
    print("4. Terminate")
    choice = input("Select operation on Phonebook App (1/2/3/4): ")

    if choice == "1":
        find_contact()
    elif choice == "2":
        insert_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        terminate()
    else:
        print("Invalid choice. Please try again.")
