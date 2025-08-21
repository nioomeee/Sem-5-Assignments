# Accept an integer input and display a right-angled number triangle pattern
# using nested loops. Example for input 4:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

rows = int(input("Enter the number of rows: "))

k = 1

for i in range (rows):
    for j in range(i):
        print(k, end=" ")
        k += 1
    print()



