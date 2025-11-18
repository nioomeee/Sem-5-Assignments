# binary to decimal and vice-versa

binary_string = '101'

decimal_int = int(binary_string, base=2)

print(" ----- Binary to decimal ----- \n")
print(f" Input: {binary_string}")
print(f" Output: {decimal_int}")

decimal_input = 5
binary_string_full = bin(decimal_input)
binary_cleaned = binary_string_full[2:]
print("\n ----- Decimal to Binary ----- \n")
print(f" Input: {decimal_input}")
print(f" Intermediary binary: {binary_string_full}")
print(f" Cleaned binary: {binary_cleaned}")