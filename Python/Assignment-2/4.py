# Accept a tuple of integers and count how many elements are divisible by 3
# but not by 5. Also, calculate their sum.
input_string = input("Enter a series of number separated by spaces: ")

numbers = tuple(int(num) for num in input_string.split())

count = 0
total_sum = 0

for num in numbers:
    if num % 3 == 0 and num % 5 != 0:
        count += 1
        total_sum += num

print(f"Originl tuple: {numbers}")
print(f"Count of numbers divisible by 3 and not by 5: {count}")
print(f"Sum of these numbers: {total_sum}")
 