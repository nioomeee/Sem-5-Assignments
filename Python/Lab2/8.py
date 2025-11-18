# Given a list of numbers, use `enumerate()` to print index and value. Use
# `all()` to check if all elements are positive, and `any()` to check if any is a
# multiple of 7.

n = int(input("Enter the number of elements you want: "))

try:
    numbers = [int(input(f"Enter {i+1} number: ")) for i in range(n)]
    print(f"List of numbers you entered: {numbers}")

    for index, value in enumerate(numbers):
       print(f"Index: {index}, Value: {value}")
    
    all_pos = all(num > 0 for num in numbers)
    print(f"Are all the numbers in the list positive? {all_pos}")

    multiple = any(num % 7 == 0 for num in numbers)
    print(f"Is any number multiple of 7? {multiple}")

except ValueError:
    print("Invalid input")
