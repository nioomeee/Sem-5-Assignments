# Create a Python program that will have 3 variables which stores integer, float and
# complex value. Display its value and also demonstrate its datatype class using type().
u_int = int(input("Enter a whole number: "));

u_float = float(input("Enter a decimal number: "))

u_complex = complex(input("Enter a complex number: "))

print("\nHere's what you entered: \n")

print(f"The value is: {u_int}\n")
print(f"The data type = {type(u_int)}\n")

print(f"\nThe entered number = {u_float}\n")
print(f"The data type = {type(u_float)}\n")

print(f"\nThe entered number = {u_complex}\n")
print(f"The data type = {type(u_complex)}\n")