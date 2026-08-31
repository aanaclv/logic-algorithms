'''
Write a program to read the two grades a student received in the first and second semesters of
a year-long course. Then, display the student’s final grade (to one decimal place) for the
year along with an explanatory message. If the student’s final grade is less than 60.00, display the
message “FAILED.”
'''

grade1 = int(input("Number 1: "))
grade2 = int(input("Number 2: "))

if grade1 and grade2 % 2 == 0:
    print("There are multiple")
else:
    print("Are not multiples")