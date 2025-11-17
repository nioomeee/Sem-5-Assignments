# Write a python program to perform following operations on string.
# • Reverse string and print it
# • count the occurance
# • Check whether the string ends with particular substring or not
# • find substring

my_string = input("Enter a string: ")
reversed = my_string[::-1]
print(f"Reverse of the string {my_string} = {reversed}")

char = input("Enter the character you wanna count: ")

print(f"Occurence of {char} in string {my_string} = {my_string.count(char)}")

text = input("Enter substring to check if the string ends with it or not: ")

result = my_string.endswith(text)

print(f"Does it end with {text}? {result}")

substr_to_find = input("Enter the substring to find: ")

index = my_string.find(substr_to_find)

if index != -1:
    print(f"Substring {substr_to_find} found at index: {index}")
else:
    print(f"Substring {substr_to_find} not found")

