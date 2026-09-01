'''
Write a program to read the names and ages of two people. At the end, display a message with the
names and the average age of the two people, rounded to one decimal place.
'''

print("First-person data:")
name1 = str(input("Name: "))
age1 = int(input("Age: "))

print("Second-person data:")
name2 = str(input("Name: "))
age2 = int(input("Age: "))

mean = (age1+age2)/2
resultado = print(f"The average age of {name1} and {name2} is {mean} years old.")