file_name = "my_diary.txt"

print(f"\n ----- Writing to '{file_name}' using 'with' -----")

try:
    with open(file_name, "w") as f:
        f.write("Dear Diary, \n")
        f.write("Today i learnt about with keyword \n")
        f.write("It cleans up after me")

    print("\n File writing completed!")

except Exception as e:
    print(f"\n An error occured: {e}")

print(f"\n ----- Reading from '{file_name}' using 'with' -----")

with open(file_name, "r") as f:
    content = f.read()
    print("File Content: \n -----")
    print(content.strip())
    print(" ------")