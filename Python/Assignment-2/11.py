# Write a Python program to print a square pattern with diagonals. Example
# for input 5:* ** *** ** *

size = int(input("Enter the size of the pattern: "))

for i in range(size):
    for j in range(size):
        if (
            i == j or # diagonal
            i+j == size-1  # anti-diagnonal 
        ):
            print("*", end = " ")
        else:
            print(" ", end = " ")

    print()
