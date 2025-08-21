# Write a program to input a tuple of strings and find how many strings
# contain only vowels.
strings = ("Aeiou", "rhythm", 'o', "education", '', "Himalayas")

vowels = "aeiou"

vowel_count = 0

for item in strings:
    if item and all(char.lower() in vowels for char in item):
        print(f"Found a vowel only string: {item}")
        vowel_count +=1

print(f"Total number of strings containing only vowels: {vowel_count}")