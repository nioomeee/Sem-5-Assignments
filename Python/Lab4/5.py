# Write a program to raise an exception if number is negative
def process_age(age):
    if age < 0:
        raise ValueError("Invalid Age: Age can't be negative")
    
    print("\n Age is Valid and has been processed!")

try:
    user_age = int(input("Enter your age: "))
    process_age(user_age)

except ValueError as e:
    print(f"\n An error occured: {e}")

finally:
    print("\n ----- Age Validation Complete -----")
