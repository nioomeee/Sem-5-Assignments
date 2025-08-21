# Write a program to find common elements between two tuples without
# converting them to lists or sets.

tuple1 = (10, 20, 30, 40, 50, 60)
tuple2 = (40, 50, 20, 60, 70, 80)

common = []

for item in tuple1:
    if item in tuple2 and item not in common:
        common.append(item)

common_tuple = tuple(common)

print(f"Common elements found = {common_tuple}")
