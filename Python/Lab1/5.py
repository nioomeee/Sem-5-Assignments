# Write a python program to Count the total number of digits in a number.
num_str = input("Enter a number: ")
try:

    num = int(num_str)
    num = abs(num)
    count = len(str(num))

    print(f"The number {num_str} has {count} digits")
except ValueError:
    print("Invalid Input")