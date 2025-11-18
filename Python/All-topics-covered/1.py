# The "DataCleaner" Module (String & List Mastery)
# Goal: Write a Python script that processes a messy list of product codes. raw_data = [" Apple-101 ", "banana_202", "Orange-303", " grape-404", "apple-101"] (Note the duplicates and spaces).

# Create a function clean_data(data_list) that:

# Removes leading/trailing spaces.

# Converts all strings to lowercase.

# Removes duplicates without using set() (to preserve order).

# Use list comprehension to create a new list containing only items that endswith "101" or "303".

# Print the final list and the type() of the first element.


# The Why: Tests strip() , lower() , manual duplicate removal , endswith() , type() , and List Comprehension.

def clean_data(data_list):
    unique_list = []

    for item in data_list:
        clean_item  = item.strip().lower()
        
        if clean_item not in unique_list:
            unique_list.append(clean_item)

    filtered_list = [x for x in unique_list if x.endswith("101") or x.endswith("303")]

    return filtered_list

raw_data = [" Apple-101 ", "banana_202", "Orange-303", " grape-404", "apple-101"]
print(f"Raw data: {raw_data}")

result = clean_data(raw_data)

print(f"\n Final list: {result}")

if result:
    print(f"\n Type of first element: {type(result[0])}")   