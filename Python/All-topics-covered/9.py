# gcd (greatest common divisor)

import math

# pythonic way
def gcd_pythonic(a, b):
    return math.gcd(a, b)

def gcd_manual(a, b):
    while b:
        a, b = b, a % b
    
    return a

try:
    num1 = int(input("\n Enter number 1: "))
    num2 = int(input("\n Enter number 2: "))

    print(f"\n GCD({num1}, {num2}) using math.gcd = {gcd_pythonic(num1, num2)}")
    print(f"\n GCD ({num1}, {num2}) using Euclidean algorithm = {gcd_manual(num1, num2)}")

except ValueError as e:
    print(f"\n Invalid input: {e}")