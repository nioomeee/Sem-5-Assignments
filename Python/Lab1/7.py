# Given a list of integers, write a Python program to remove all duplicates without
# using set(), and preserve the original order.

og_list = []
unique_nums = []

input_str = input("Enter the numbers separated by commas: ")

try:
    str_list = input_str.split(',')

    for item in str_list:
        num = int(item.strip())
        og_list.append(num)

    print(f"Original list: {og_list}")

    for num in og_list:
        if num not in unique_nums:
            unique_nums.append(num)

    print(f"Unique numbers: {unique_nums}")

except ValueError:
    print("Invalid input! Make sure only use numbers enclosed by commas")