'''
Write a program that reads a positive integer N (maximum = 10) and then N integers,
and stores them in a vector. Next, display all the negative numbers that were read on the screen.
'''

n = int(input("How many numbers will you enter: "))
vector = []

for i in range(n):
    value = int(input("Enter a number: "))
    vector.append(value)

print("números negativos:")

for value in vector:
    if value < 0:
        print(value)
