print("*****************************************")

print("Welcome to Find the Largest Number ")

print("*****************************************")
print("")

while True:

 a=input("Please Enter first number: ")
 b=input("Please Enter second number: ")
 c=input("Please Enter third number: ")
 d=input("Please Enter forth number: ")
 e=input("Please Enter fifth number: ")

 list1 = [int(a),int(b),int(c),int(d),int(e)]

 list1.sort()
 print("Largest element is:", list1[-1])

 x=input("If you want to exit from program please type  exit or press enter to continue : ")
 if x=="exit" or x=="Exit" :
   print("Exiting the program... Good Bye")
   break
