print("**********************************")
print("Welcome to Phonebook Application")
print("**********************************")
print("")

def welcome():
    
    entry = int(input(""" 
                    >>>Py Contact Book commands are: 1,2 and 3 <<<
                    >>>What would you like to do?<<<
                    1. Find phone number
                    2. Insert a phone number
                    3. Delete a person from the phonebook 
                    4. Terminate
                    Select operation on Phonebook App (1/2/3) :  """))
    
   
    return entry



def phonebook():
    
    contact = {}
    
    
    while True:
        
        
        entry = welcome()
        
        
        if entry == 1:
            
            if bool(contact) != False:
                for isim, numara  in contact.items():
                    print(isim, ':', numara)
            else:
                print('You have an empty phonebook! Go back to the menu to add a new contact')
        elif entry == 2:
            phone_number = input('Please Enter a number: ')
            contact_name = input('What would you like to Save the name as? Enter in the format "FirstName,LastName".: ')
            
            if phone_number not in contact.items():
                contact.update({contact_name:phone_number})
                print('Contact successfully saved')
                print('Your updated phonebook is Shown below: ')
                for isim , numara in contact.items():
                    print( isim , ':', numara)
            else:
                print('That contact already exits in your Phonebook')
                
        
        elif entry == 3:
            name = input('Enter the name of the contact you wish to delete: ')
            if name in contact:
                print('The contact is',name,':',contact[name])
                
            else:
                print('That contact does not exist! Return to the main menu to enter the contact')
            
            
            confirm = input('Are you sure you wish to delete this contact? Yes/No: ')
            if confirm.capitalize() == 'Yes':
                contact.pop(name,None)
                for isim, numara in contact.items():
                    print('Your Updated Phonebook is shown below:')
                    print(isim , ':', numara )
            
            else:
                print('Return to Main Menu')
           
        elif entry == 4:
            print('Thanks for using the Phonebook Application')
            break
            
          
        else:
            print('Incorrect Entry!')
            
            
        

    

phonebook()