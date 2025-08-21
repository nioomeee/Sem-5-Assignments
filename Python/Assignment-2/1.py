# Write a Python program to input a list of student marks, 
# find average, and print 'Pass with Distinction' 
# if average ≥ 85, 
# 'Pass' if ≥ 50, 
# else 'Fail'. 
# Also,count how many subjects are failed (<35).

marks = []

num = int(input("ENter the number of subjects you want: "))

print("Enter marks for each subject 1 by 1: ")

for i in range(num):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

if marks:
    total_marks = sum(marks)
    average = total_marks / num

count = 0

for m in marks:
    if m < 50:
        count += 1

print("\n ---Student report card---\n")

print(f"Marks entered: {marks}")
print(f"Average marks: {average:.2f}")

if average >= 85:
    print("Result: Pass With Distinction")
elif average >= 50:
    print("Result: Average")
else:
    print("Result: Fail")

print(f"\nNumber of subjects failed: {count}\n")
