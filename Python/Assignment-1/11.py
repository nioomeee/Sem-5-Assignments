# Write a Python program that will demonstrate the use of Membership Operators.
# in and not in 

subjects = ["Programming", "Data Structures", "Cryptography", "Networking", "Databases"]

print(f"Your subjects are: {subjects}\n")

print("1. check for cryptography: ")
if "Cryptography" in subjects:
    print("Yes! It's on the list.")
else:
    print("Nope, it's not on the list")

print("-" * 30)

# 2. Biology
print("2. Checking for biology: ")
if "Biology" in subjects: 
    print("Yes it's on the list")
else:
    print("Nope, it's not on the list")
print("-" * 30)

# 3.not in for ARTS
print("Let's confirm Arts is not your subject")

if "Arts" not in subjects:
    print("Correct! Arts is not your subject")
else: 
    print("Looks like it's on the list")

print("-" * 30)

# Also works for strings
my_string = "Welcome to Python"

print("Does the string include the word 'Python' ")

if "Python" in my_string:
    print("Yes")
else:
    print("No")

print("-" * 30)