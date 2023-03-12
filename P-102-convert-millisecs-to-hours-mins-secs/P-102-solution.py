print("************************************************************************")

print("Welcome to Converting Milliseconds into Hours, Minutes, and Seconds ")

print("***********************************************************************")
print("")
while True:


 millis=input("Please enter time in milliseconds: ")
 try:
    val = int(millis)
 

    if 0 >= int(millis) :
      print("Please enter a number bigger than zero")
    elif int(millis) < 999 :
     print("Just" , int(millis) , "millisecond/s") 
    else :
      seconds=(int(millis)/1000)%60
      seconds = int(seconds)
      minutes=(int(millis)/(1000*60))%60
      minutes = int(minutes)
      hours=(int(millis)/(1000*60*60))%24
 
      print("Hours:Minutes:Seconds")
      print ("%d:%d:%d" % (hours, minutes, seconds))
      
    
 except ValueError:
    print("Not Valid Input !")
 x=input("If you want to exit from program please type  exit or press enter to continue : ")
 if x=="exit" or x=="Exit":
   print("Exiting the program... Good Bye")
   break