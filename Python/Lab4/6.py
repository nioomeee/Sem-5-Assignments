# Write a program to demonstrate the use of finally with exception.

print(" ----- Number Division -----")

try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    result = numerator / denominator
    print(f"\n Succes! The reuslt is {result:.2f}")

except ZeroDivisionError:
    print("\n Error cannot divide by Zero!")

finally:
    print("\n ----- Program terminated -----")
