print("*****************************************")

print("Welcome to Validate Combination of Brackets")

print("*****************************************")
print("")
def is_valid_string(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping.values():  # Opening bracket
            stack.append(char)
        elif char in mapping.keys():  # Closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack) == 0

while True:
    # Take input from the user
    input_string = input("Enter a string of brackets (q to quit): ")

    if input_string.lower() == 'q':
        break

    # Check if the string is valid
    if is_valid_string(input_string):
        print("The input string is valid.")
    else:
        print("The input string is invalid.")

print("Exiting the program.")
