# Write a Python program to accept marks for 5 subjects, calculate average,
# and assign grade (A/B/C/D/Fail). If any subject has marks <35, display
# “Fail due to subject back”.

try:
    marks = [int(input(f"Enter marks for subject {i+1}: ")) for i in range(5)]

    if(any(mark < 35 for mark in marks)):
        print("Fail due to subject back")
    else:
        average = sum(marks) / len(marks)

        if average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'B'
        elif average >= 70:
            grade = 'C'
        elif average >= 60:
            grade  = 'D'
        else:
            grade = "Fail"

        print("Final result: \n")
        print(f"Average: {average}\n")
        print(f"Grade: {grade}")

except ValueError:
    print("Invalid input!")
        
 