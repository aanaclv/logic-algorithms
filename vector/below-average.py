'''
Write a program to read an integer N and then a vector of N real numbers. Next,
display the arithmetic mean of all elements on the screen, rounded to three decimal places. Then display all
the elements of the vector that are below the mean, each rounded to one decimal place.
'''

import statistics

n = int(input("How many elements will the vector have: "))
vector = []

for i in range(n):
    value = int(input("Enter a value: "))
    vector.append(value)

mean = statistics.mean(value)
print(f"Mean: {mean}")