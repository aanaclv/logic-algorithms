'''
Write a program to read an employee's name, their hourly wage, and the
number of hours they worked. At the end, display the employee's pay amount along with
an explanatory message, as shown in the example.
'''
name = input("Name: ")
hourly_rate = float(input("Hourly rate: "))
hours_worked = int(input("Hours worked: "))
salary = hourly_rate*hourly_rate
print(f"The payment to {name} should be {salary:.2f}$")