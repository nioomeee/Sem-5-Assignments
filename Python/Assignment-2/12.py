# Input a paragraph and count the number of words, vowels, and consonants.
# Store word frequencies in a dictionary.
import string

paragraph = input("Enter a paragraph: ")

vowel_count = 0
consonant_count = 0
word_frequencies = {}
vowels = "aeiou"

for char in paragraph.lower():
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

translator = str.maketrans("", "", string.punctuation)
cleaned_para = paragraph.translate(translator)

words = cleaned_para.lower().split()

for word in words:
    word_frequencies[word] = word_frequencies.get(word, 0) + 1

print("\n--- Analysis Results ---")
print(f"Vowel count = {vowel_count}")
print(f"Consonant count = {consonant_count}")
print("\n--- Word frequencies ---")

for word, count in word_frequencies.items():
    print(f"Word: {word}, frequency: {count}")

print("-" * 15)

