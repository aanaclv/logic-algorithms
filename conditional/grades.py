'''
Write a program to read the two grades a student received in the first and second semesters of
a year-long course. Then, display the student’s final grade (to one decimal place) for the
year along with an explanatory message. If the student’s final grade is less than 60.00, display the
message “FAILED.”
'''

grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
final_grade = (grade1 + grade2)/2

if final_grade < 60:
    print("Reproved")
else:
    print(final_grade)