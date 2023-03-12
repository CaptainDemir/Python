print("*****************************************")

print("Welcome to Validate Combination of Brackets")

print("*****************************************")
print("")

string=input("Please enter your combination of brackets: ")

open_list = ["[","{","("]
close_list = ["]","}",")"]

def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "false"
    if len(stack) == 0:
        return "true"
    else:
        return "false"
  
  

print(string,"-", check(string))
  
