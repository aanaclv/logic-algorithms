n = int(input("quantos valores você vai digitar: "))
vetor = []

for i in range(n):
    valores = int(input("digite os números: "))
    vetor.append(valores)
    total = sum(vetor)

print(total)
