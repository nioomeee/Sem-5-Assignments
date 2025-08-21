# Create a program to input two lists and convert them into a dictionary
# using one as keys and one as values. Swap key-value pairs and display the
# reversed dictionary.
key_input = input("Enter keys for dictionary separated by spaces: ").split()
value_input = input("ENter values for dictionary separated by spaces: ").split()

initial_dictionary = dict(zip(key_input, value_input))

print(f"\nInitial dictionary: {initial_dictionary}")

reverse_dictionary = dict(zip(value_input, key_input))
print(f"\Reversed dictionary: {reverse_dictionary}")