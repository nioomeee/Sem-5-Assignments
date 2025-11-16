# Write a Python program that counts how many times a value appears in a tuple.

my_tuple = (8, 6, 3, 8, 6, 4, 1, 8, 2, 6)

try: 
    value_to_find = int(input("Enter the number to find it's occurence in the tuple: "))

    count = my_tuple.count(value_to_find)

    print(f"Frequency of {value_to_find} in the tuple = {count}")

except ValueError:
    print("Invalid input")
