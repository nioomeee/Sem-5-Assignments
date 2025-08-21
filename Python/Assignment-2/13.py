# Continuously accept integers until a negative number is entered. Calculate
# sum, average, and count of positive numbers entered.
numbers = []


print("Enter number 1 by 1. Enter negative number to stop!")
while True:
    num = int(input("Enter number: "))

    if num < 0:
        print(f"Negative number {num} entered. Stopping the loop")
        break

    numbers.append(num)

count = len(numbers)
total_sum = sum(numbers)

if count > 0:
    average = total_sum/count
else:
    average = 0

print("\n--- Final Results ---")
print(f"List of positive numbers entered: {numbers}")
print(f"Count of positive numbers: {count}")
print(f"Sum of positive numbers: {total_sum}")
print(f"Average of positive numbers: {average}")

