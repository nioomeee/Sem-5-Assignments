# Write a Python program that calculates the factorial of a number using a while loop.

try:

    number = int(input("Enter a number: "));
    factorial = 1;

    if number < 0:
        print("Factorial doesn't exist for negative numbers")
    elif number == 0:
        print("Factorial of 0 = 1")
    else:
        i = number
        while i > 0:
            factorial *= i;
            i -= 1;
        print(f"Factorial of {number} = {factorial}")
    
except ValueError:
    print("Invalid input");