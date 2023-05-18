print("**********************************")
print("Welcome to Phonebook Application")
print("**********************************")
print("")

class Phonebook:
    def __init__(self):
        self.phonebook = {}

    def find_contact(self):
        name = input("Find the phone number of: ")
        if name in self.phonebook:
            print(self.phonebook[name])
        else:
            print("Couldn't find phone number of", name)

    def insert_contact(self):
        name = input("Insert name of the person: ")
        while True:
            number = input("Insert phone number of the person: ")
            if number.isdigit():
                self.phonebook[name] = number
                print("Phone number of", name, "is inserted into the phonebook.")
                break
            else:
                choice = input("Invalid input format. Press 1 to try again or 4 to terminate or 2 to back to menu: ")
                if choice == "4":
                    self.terminate()
                elif choice =="2":
                    return


    def delete_contact(self):
        name = input("Whom to delete from phonebook: ")
        if name in self.phonebook:
            del self.phonebook[name]
            print(name, "is deleted from the phonebook.")
        else:
            print("Couldn't find", name, "in the phonebook.")

    def terminate(self):
        print("Exiting Phonebook.")
        exit()

    def run_phonebook(self):
        while True:
            print("Welcome to the phonebook application")
            print("1. Find phone number")
            print("2. Insert a phone number")
            print("3. Delete a person from the phonebook")
            print("4. Terminate")
            choice = input("Select operation on Phonebook App (1/2/3/4): ")

            if choice == "1":
                self.find_contact()
            elif choice == "2":
                self.insert_contact()
            elif choice == "3":
                self.delete_contact()
            elif choice == "4":
                self.terminate()
            else:
                print("Invalid choice. Please try again.")


phonebook = Phonebook()
phonebook.run_phonebook()
