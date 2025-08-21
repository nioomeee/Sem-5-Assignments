# Create a set of vowels found in a user-given sentence. Then convert the set
# to a frozenset and try to remove an element (handle the exception).

sentence = input("Enter a sentence to find the vowels in it: ")

vowels = "aeiou"

vowels_found = {char for char in sentence.lower() if char in vowels}

print(f"Mutable set of vowels found: {vowels_found}")

frozen_vowels = frozenset(vowels_found)

print(f"Immutable frozenset of vowels found: {frozen_vowels}")

try:
    frozen_vowels.remove('i')
except AttributeError as e:
    print("Operation failed! you can't modify a frozen set")
    print(f"Error details: {e}")