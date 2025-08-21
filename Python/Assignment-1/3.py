# Create a Python program that will have one list with values = 
# [‘Navratri’, ‘Diwali’,‘Holi’, ‘Rakshabandhan’,’Bakri Id’, ‘Muharram’ ]. 
# Perform following operations:
#     • Print whole list
#     • Print only first element of list
#     • Prints elements starting from 2nd till 3rd
#     • Prints elements starting from 2ndelement till last
#     • Print whole list 4 times using appropriate operator.

festivals = ["Navratri", "Diwali", "Holi", "Rakshabandhan", "Bakri Id", "Muharram"]

print(f"\nOrginal list: {festivals}")
print("\n---Let's go!---\n")

# 1. Print whole list
print("1. whole list is: ")
print(festivals)
print("-" * 25)

# 2. Print only first element of list
print("2. First element of list is: ")
print(festivals[0])
print("-" * 25)

# 3. Prints elements starting from 2nd till 3rd
print("3. Elements starting from 2nd till 3rd: ")
print(festivals[1:3])
print("-" * 25)

# 4. Prints elements starting from 2ndelement till last
print("4. Elements starting from 2nd element till last: ")
print(festivals[1:])
print("-" * 25)

# 5. Print whole list 4 times using appropriate operator.
print("5. Printing whole list 4 times using appropriate operator: ")
print(f"{festivals} \n" * 5)
print("-" * 25)
