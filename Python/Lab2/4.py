# Accept a tuple of 10 integers. Count even and odd numbers. Extract
# prime numbers into a new tuple. Display max, min, and sum of the new tuple.

import math

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

try:
    numbers_tuple = tuple(int(input(f"Enter {i+1}: ")) for i in range(10))
    print(f"Numbers tuple: {numbers_tuple}")

    even = 0
    odd = 0
    prime_list = []

    for num in numbers_tuple:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

        if(is_prime(num)):
            prime_list.append(num)

    prime_tuple = tuple(prime_list)

    print(f"Tuple of prime numbers = {prime_tuple}")

    if prime_tuple:
        print(f"Maximum : {max(prime_tuple)}")
        print(f"Minimum: {min(prime_tuple)}")
        print(f"Sum: {sum(prime_tuple)}")
    else:
        print("No prime numbers found in tuple")
except ValueError:
    print("Invalid Input!")
