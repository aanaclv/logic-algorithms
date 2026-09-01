'''
Write a program to read two vectors, A and B, each containing N elements. Then, generate a
third vector, C, where each element of C is the sum of the corresponding elements of A and B. Print
the generated vector C.
'''

n = int(input("quantos valores vai ter cada vetor: "))
a = []
b = []
sum = []

for i in range(n):
    n_a = int(input("Enter the values of vector A: "))
    a.append(n_a)

for i in range(n):
    n_b = int(input("Enter the values of vector B: "))
    b.append(n_b)


for i in range(n):
   sum.append(a[i] + b[i])

print(f"vector sum: {sum}")
