'''
Write a program that reads N real numbers and stores them in a vector. Then:
- Print all the elements of the vector
- Display the sum and the average of the vector's elements on the screen

'''

n = int(input("How many numbers will you enter: "))
vector = []

for i in range(n):
    value = int(input("Enter a number: "))
    if value % 2 == 0:
        vector.append(value)
    quantity = len(vector)

print(f'''Even numbers:: {vector}
    {quantity}''')
