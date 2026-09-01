line = int(input("How many lines will have the matrix: "))
column = int(input("How many columns will have the matrix: "))

#creates a matrix with rows and columns
matrix = [[0 for j in range(column)] for i in range (line)]

for i in range(0,line):
    for j in range(0, column):
        matrix[i][j] = int(input(f"Element [{i},{j}]: "))

print()
print("Typed matrix:")

for i in range(0,line):
    for j in range(0,column):
        print(f"{matrix[i][j]}", end = " ")
    print()