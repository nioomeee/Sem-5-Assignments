# Write a Python program to demonstrate the use of random function.
import random

print("\n---Welcome to Random Zone---\n")

# 1. random.randint(a,b)
dice_roll = random.randint(1, 6)
print(f"1. Rolling a 6-sided dice... you got a {dice_roll}")

# 2. random.random()
random_float = random.random()
print(f"2. Generating a random float: {random_float:.4f}")

# 3. random.choice(sequence)
subjects = ["Maths", "Science", "English", "Social"]
winner = random.choice(subjects)
print(f"3. Random Subject: {winner}")

# 4. random.shuffle(list)
print(f"Subjects before shuffling: {subjects}")
random.shuffle(subjects)
print(f"4. Newly shuffled subjects = {subjects}")
