import random
import string

print("**********************************")
print("Welcome to Generate Password ")
print("**********************************")
print("")


while True:

 digits = list(string.digits)

 user_name= input("Please enter a user name: ")

 password = []
 for i in range(3):
		password.append(random.choice(user_name))

 for i in range(4):
		password.append(random.choice(digits))


 print("".join(password))
 x=input("If you want to exit from program please type  exit or press enter to continue : ")
 if x=="exit" or x=="Exit":
   print("Exiting the program... Good Bye")
   break