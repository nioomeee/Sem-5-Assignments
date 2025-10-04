# Write a program to divide one number from another number 
# with exception handling and show ZeroDivisionError.
print("----- Number Division Program -----")

try:
    numerator = float(input("Enter the numerator (The number on top): "))
    denominator = float(input("Enter the denominator (The number on bottom): "))

    result = numerator / denominator
except ZeroDivisionError:
    # this block runs only if ZeroDivsionError encountered in try block
    print("\n Error! You can't divide by Zero! Please Try again.")
else:
    # This block only runs if the try block runs w/o any errors
    print(f"\n Success! The result is {result}")
finally:
    # This block ALWAYS runs
    print("\n ----- Program has finished -----")