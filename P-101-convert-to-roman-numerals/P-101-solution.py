print("*****************************************")

print("Welcome to  Convert to Roman Numerals")

print("*****************************************")
print("")
while True:


 num=(input('Please enter a number between 1 and 3999: '))
 try:
    val = int(num)

    if 0 >= int(num) :
      print("Please enter a number bigger than zero")
    elif int(num) > 3999 :
     print("Please enter a number lower than 4000") 
    else :
     def solve(num):
        res = ""
        table = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        for cap, roman in table:
            d, m = divmod(int(num), cap)
            res += roman * d
            num = m

        return res
     print('Result: ' + (solve(num)))
    
 except ValueError:
    print("Not Valid Input !")
 x=input("If you want to exit from program please type  Exit or press enter for continue : ")
 if x=="Exit" or x=="exit":
   print("Exiting the program... Good Bye")
   break