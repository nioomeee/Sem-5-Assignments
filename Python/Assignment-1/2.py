# Create a Python program that will have one string variable =“ Welcome to Python”.
# Perform following operations:
#     • Print whole string
#     • Print only first character of string
#     • Print 3rdcharacter to -1 character of string using slicing operator
#     • Print string from 4thcharacter to the end of string using slicing operator
#     • Print whole string 5 times using appropriate operator.• Count the occurance of “to”
#     • Print length of string• Convert the string to lowecase• Find the substring “Python”
#     • Remove leading space from string• Check whether string is ending with “is” or not.

my_string = " Welcome to Python"

print(f"Orginal string = {my_string} \n")
print("---Let's get started!---\n")

# 1. Print whole string
print("1. The whole string is: ")
print(my_string)
print("-" * 20)

# 2. Print only first character of string
print("2. First character of string is: ")
print(my_string[0])
print("-" * 20)

# 3. Print 3rdcharacter to -1 character of string using slicing operator
print("3. 3rd character to -1 character of string using slicing operator: ")
print(my_string[2: -1])
print("-" * 20)

# 4. Print string from 4thcharacter to the end of string using slicing operator
print("4. 4th character to the end of string using slicing operator: ")
print(my_string[3:])
print("-" * 20)

# 5. Print whole string 5 times using appropriate operator
print("5. Whole string 5 times using appropriate operator: ")
print(my_string * 5)
print("-" * 20)

# 6. Count the occurance of “to”
print("6. The sub-string “to” appears: ")
print(f"{my_string.count('to')} times")
print("-" * 20)

# 7. Print length of string
print("7. Length of string: ")
print(len(my_string))
print("-" * 20)

# 8. Convert the string to lowercase
print("8. The entered string in lowercase is: ")
print(my_string.lower())
print("-" * 20)

# 9. Find the substring “Python”
print("9. The substring “Python” starts at index: ")
print(my_string.find("Python"))
print("-" * 20)

# 10. Remove leading space from string
print("10. Removed leading space from string: ")
print(my_string.lstrip())
print("-" * 20)

# 11. Check whether string is ending with “is” or not.
print("11. Does string end with “is” or not: ")
print(my_string.endswith("is"))
print("-" * 20)


