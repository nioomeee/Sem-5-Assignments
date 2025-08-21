# Write a program to input a list of 10 names and check if there are any
# duplicate entries. If yes, display the duplicates.

names = []

print("Please enter 10 names 1 by 1: ")

for i in range(10):
    name = input(f"Enter name {i+1}: ").strip().title()
    names.append(name)

# for findinding duplicates
uniques = set()
duplicates = set()

for name in names: 
    if name in uniques:
        duplicates.add(name)
    else: 
        uniques.add(name)

if duplicates:
    print("Duplicate names found: " + ", " .join(duplicates))
else:
    print("No duplicates found")

print("-" * 25)