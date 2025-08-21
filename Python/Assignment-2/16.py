# Create a dictionary of student names and a list of their marks in 3 subjects.
# Calculate and store the average for each student. Display the dictionary
# with names and averages.

student_marks = {
    "Alisha" : [35, 64, 52],
    "Brinda" : [58, 22, 45],
    "Carrie" : [85, 76, 56],
    "Demi" : [86, 69, 94],
    "Elena" : [50, 67, 85] 
}

student_averages = {
    name: sum(marks) / len(marks)
    for name, marks in student_marks.items()
}

print(f"Initial data(marks): {student_marks}")
print(f"Final data(average): {student_averages}")