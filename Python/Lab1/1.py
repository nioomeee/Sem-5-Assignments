# Write a Python program that takes a number as input and prints "Even" if the number
# is even, and "Odd" if the number is odd using an if-else statement.

try:
    number = int(input("Enter a number: "));

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Invalid input!");