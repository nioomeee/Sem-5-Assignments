# Recursion: Define a function recursive_sum(n) that adds numbers from 0 to n

def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n-1)

try:
    num = int(input("\n Enter a number: "))
    result = recursive_sum(num)

    print(f"\n The recurive sum of {num} = {result}")

except ValueError as e:
    print(f"\n Invalid input: {e}")
