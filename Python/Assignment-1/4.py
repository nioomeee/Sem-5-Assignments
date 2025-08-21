# Create a Python program that will have one tuple of vegetables with values = (‘Potato’,
# ‘Brinjal’,‘Tomato’,‘Cabbage’, ‘Cauliflower’). Perform following operations:
#     • Print whole tuple
#     • Print only first element of tuple
#     • Prints elements starting from 2ndtill4th
#     • Prints elements starting from 2ndelement till last
#     • Print whole tuple twice using appropriate operator.

Vegetables = ["Potato", "Brinjal", "Tomato", "Cabbage", "Cauliflower"]

# 1. Print whole tuple
print("\n1. Whole tuple: ")
print(Vegetables)
print("-" * 30)

# 2. Print only first element of tuple
print("2. Print only first element of tuple: ")
print(Vegetables[0])
print("-" * 30)

# 3. Prints elements starting from 2nd till 4th
print("3. Prints elements starting from 2nd till 4th: ")
print(Vegetables[1:4])
print("-" * 30)

# 4. Prints elements starting from 2ndelement till last
print("4. Prints elements starting from 2ndelement till last: ")
print(Vegetables[1:])
print("-" * 30)

# 5. Print whole tuple twice using appropriate operator.
print("5. Print whole tuple twice using appropriate operator.")
print(f"{Vegetables} \n" * 2)
print("-" * 30)
