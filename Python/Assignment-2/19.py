# Create a list of 10 random numbers and remove all elements greater than
# the average of the list. Display final list.

import random

numbers = [random.randint(1, 100) for _ in range(10)]
print(f"Original list: {numbers}")

if numbers: 
    average = sum(numbers) / len(numbers)
    print(f"Average: {average:.2f}")

final_list = [num for num in numbers if num <= average]

print(f"Final List after calculation: {final_list}")