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
