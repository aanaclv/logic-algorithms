'''
Write a program that reads the grades for a student's two exams. Calculate and print the
semester average. Ensure that the algorithm only accepts valid grades (a valid grade must fall within the
interval [0,10]). Each grade must be validated separately.
'''

grade1 = float(input("Grade 1: "))
grade2 = float(input("Grade 2: "))

while not (0 <= grade1 <= 10):
    print("Invalid value! Please try again: ")
    grade1 = float(input("nota 1: "))

while not(0 <= grade2 <= 10):
    print("Invalid value! Please try again: ")
    grade2 = float(input("nota 2: "))


mean = (grade1+grade2)/2
print(f"Mean: {mean}")
