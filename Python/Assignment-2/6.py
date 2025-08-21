# Take 10 user inputs. If the number is prime, skip it (use `continue`). 
# If it is divisible by 10, stop the loop (use `break`). 
# Use `else` to confirm normal loop completion.

import math

def isPrime(num):
    """Checks if a number is prime"""
    if num <= 1:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

print("Enter 10 numbers. the loop will stop if the number is divisible by 10")

for i in range(10) :
    number = int(input(f"ENter number {i+1}: "))

    if number % 10 == 0:
        break

    if isPrime(number):
        print(f"Number {number} is prime, skipping it...")
        continue

    print(f"Processing number {number}...")

else:
    print("Loop completed normally without stopping!")