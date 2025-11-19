# Write a Python script that does the following:

# Setup: Import os, csv, and datetime.

# Encryption Function: Create a function encrypt(text, shift) that uses a 
# simple Caesar Cipher (shift each character code by +shift).

# CSV Writer:

# Check if a file named secret_log.csv exists using os.path.exists().

# If it doesn't exist, create it and write the header: ['Timestamp', 'Original', 'Encrypted'].

# If it does exist, append a new row.

# The Operation:

# Get the current time using datetime.datetime.now().

# Take a user input string (e.g., "Attack at dawn").

# Encrypt it using your function.

# Write the {Time, Original, Encrypted} row to the CSV file.

import os
import csv
import datetime

def encrypt(text, shift):
    result = ""

    for char in text:
        ascii_val = ord(char)
        ascii_char = chr(ascii_val + shift)

        result += ascii_char
    return result

filename = "secret_log.csv"

header = ["Timestamp", "Orginal", "Encrypted"]

shift_key = 3

text = input("Enter message to log: ")
current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

encrypted_msg = encrypt(text, shift_key)

# File handling

file_exists = os.path.exists(filename)

with open(filename, mode='a', newline='') as f:
    writer = csv.writer(f)

    if not file_exists:
        writer.writerow(header)
        print("New log file created with header")

    writer.writerow([current_time, text, encrypted_msg])
    print("\nEntry logged successfully")