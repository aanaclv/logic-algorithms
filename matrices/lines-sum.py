'''
Write a program to read two integers M and N (maximum = 10). Next, read a matrix
with M rows and N columns containing real numbers. Generate a vector such that each element of the vector
is the sum of the elements in the corresponding row of the matrix. Display the generated vector.
'''

l = int(input("enter the line number: "))
c = int(input("enter the column number: "))

matrix = []

for i in range(l):
    line = list(map(float, input().split()))
    matrix.append(l)

vector = []

for i in range(l):
    sum = 0

    for j in range(c):
        sum += matrix[i][j]

    vector.append(sum)

print("vector: ")
for value in vector:
    print(value)
