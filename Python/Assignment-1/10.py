# Write a Python program that will demonstrate the use of Identity Operators.
# is , is not

x = 1006.56
y = 1006.56

print("---Checking 2 simple numbers: ---")
print(f"Are x and y equal (x == y) => {x == y}")
print(f"Are x and y the same object (x is y) => {x is y}")
print("-" * 25)


list_a = [1, 2, 3]
list_b = [1, 2, 3]

print("---Checking 2 Lists---")
print(f"Are list_a and list_b equal (list_a == list_b) => {list_a == list_b}")
print(f"Are list_a and list_b the same object (list_a is list_b) => {list_a is list_b}")
print("-" * 25)


# Assigning 1 variable to another
list_c = list_a
print("---Comparing a list to it's alias---")
print(f"Are list_a and list_c exact same object (list_a is list_c) => {list_a is list_c}")
print("-" * 25)


print("\n Now let's change list_a by adding a number...")
list_a.append(56)
print("-" * 25)

print(f"list_a is now: {list_a}")
print(f"list_c is now: {list_c}")
print("They both changed because they're the same object!")
print("-" * 25)
