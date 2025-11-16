# Write a Python program to create a dictionary with 3 key-value pairs and print each
# key and its corresponding value.

user_profile = {
    "username": "codergirl123",
    "level": 5,
    "email": "coder@example.com"
}

for key, value in user_profile.items():
    print(f"Key: {key} | Value: {value}")