# Given a list of integers, print the square of even numbers and cube of odd
# numbers using `enumerate()` and list comprehension.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [
    num**2 if num % 2 == 0 else num**3
    for index, num in enumerate(numbers)
]

print(f"Original list: {numbers}")
print(f"Transformed list: {result}")