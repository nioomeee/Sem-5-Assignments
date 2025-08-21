# Write a Python program that accepts 5 strings and displays the longest and
# shortest strings.
print("\n Enter 5 strings 1 by 1: ")
string_list = []

for i in range(5):
    str1 = input(f"{i+1}: ")
    string_list.append(str1)

if string_list:
    longest_string = max(string_list, key = len)
    shortest_string = min(string_list, key = len)

    print(f"Longest string = {longest_string}")
    print(f"Shortest string = {shortest_string}\n")