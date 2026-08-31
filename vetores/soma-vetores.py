n = int(input("quantos valores vai ter cada vetor: "))
a = []
b = []
soma = []

for i in range(n):
    n_a = int(input("digite os valores do vetor A: "))
    a.append(n_a)

for i in range(n):
    n_b = int(input("digite os valores do vetor B: "))
    b.append(n_b)


for i in range(n):
   soma.append(a[i] + b[i])

print(f"soma dos vetores: {soma}")
