# Accept a number from the user and reverse it using a while loop (without
# converting it into a string).
num = int(input("Enter a number: "))
n = num
rev = 0
rem = 0

while n > 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10

print(f"Entered number: {num}")
print(f"Reversed number: {rev}")


