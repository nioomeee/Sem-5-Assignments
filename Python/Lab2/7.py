# 7 Create two sets: even and prime numbers between 1–20. Find union,
# intersection, difference, and symmetric difference. Convert one to
# frozenset and try modifying it (handle the error).
import math

def isPrime(n):
    if n <= 1:
        return False
    
    for i in range (2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    
    return True

print("Generating sets: ")

evens = {i for i in range(2, 21, 2)}
primes = {i for i in range(2, 21) if isPrime(i)}

print(f"Generated even numbers: {evens}")
print(f"Generated prime numbers: {primes}")

print("-----")

print("Set functions: ")
print(f"Union between 2 sets: {evens | primes}")
print(f"Intersection between 2 sets: {evens & primes}")
print(f"Difference between 2 sets: {evens - primes}")
print(f"Symmetric difference between 2 sets: {evens ^ primes}")
print("-----")

print("Demonstrating frozen set: ")

frozen_set = frozenset(primes)
print(f"This is a frozen set: {primes}")

try:
    print("Trying to add 21 to the frozenset...")
    frozen_set.add(21)

except AttributeError as e:
    print(f"Error caught: {e}")


