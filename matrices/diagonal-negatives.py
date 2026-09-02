'''
Write a program to read an integer N (maximum = 10) and an N×N square matrix
containing integers. Then, display the main diagonal and the number of negative values
in the matrix.
'''

order = int(input("Matrix's order: "))

matrix = []

for i in range(order):
    line = list(map(int, input().split()))
    matrix.append(line)

print("Principal diagonal:")
for i in range(order):
    print(matrix[i][i], end=" ")
print()

negatives = 0

for i in range(order):
    for j in range(order):
        if matrix[i][j] < 0:
            negatives += 1

print(f"negatives = {negatives}")