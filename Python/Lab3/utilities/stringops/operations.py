# Create a package utilities with a sub-package stringops 
# containing a module which performs any 5 string operations.
# Import the function in another program and test it with a sample string.

def to_uppercase(text):
    return text.upper()

def to_lowercase(text):
    return text.lower()

def reverse_string(text):
    return text[::-1]

def count_words(text):
    words = text.split()
    return len(words)

def isPalindrome(text):
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]

