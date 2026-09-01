'''
Write a program to read an unspecified number of data points, each containing the age of an
individual. The last data point, which will not be included in the calculations, contains a negative age value. Calculate
and print the average age of this group of individuals. If a negative value is entered the first time,
display the message “UNABLE TO CALCULATE.”
'''

sum = 0
count = 0

age = int(input("Age: "))

while age >= 0:
    sum += age
    count += 1

    age = int(input("Age: "))

if count == 0:
    print("UNABLE TO CALCULATE")
else:
    mean = sum/count
    print(f"Media: {mean:.2f}")