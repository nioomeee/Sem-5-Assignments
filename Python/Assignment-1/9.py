# Write a Python program that will demonstrate the use of Bitwise Operators.

a = 10 # Binary(10) = 1010
b = 4 # Binary(4) = 0100

print(f"1st number: {a} Binary = 1010 and 2nd number: {b} Binary = 0100")

# 1. Bitwise AND
#     1010
#    &0100
#     0000 which is 0 in decimal
result_and = a & b
print(f"1. Bitwise AND (a & b): {result_and}")
print("-" * 20)

# 2. BITWISE OR
result_or = a | b
print(f"2. BITWISE Or (a | b): {result_or}")
print("-" * 20)

# 3. BITWISE XOR(^)
result_xor = a ^ b
print(f"3. BITWISE XOR (a ^ b): {result_xor}")
print("-" * 20)

# 4. BITWISE NOT(~)
result_not = ~a
print(f"4. BITWISE NOT (~a) : {result_not}")
print("-" * 20)

# 5. BITWISE Left Shift (<<)
result_ls = a << 2
print(f"5. BITWISE Left Sift (a << 2): {result_ls}")
print("-" * 20)

# 6. BITWISE Right Shift (>>)
result_rs = a >> 2
print(f"6. BITWISE Right shift (a >> 2) : {result_rs}")
print("-" * 20)

