import statistics

n = int(input("quantos elementos vai ter o vetor: "))
vetor = []

for i in range(n):
    valor = int(input("digite um número: "))
    vetor.append(valor)

media = statistics.mean(vetor)
print(f"méida: {media}")