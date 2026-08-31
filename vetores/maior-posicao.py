n = int(input("quantos números você vai digitar: "))
vetor = []
for i in range(n):
    valores = int(input("digite um número: "))
    vetor.append(valores)

maximo = max(vetor)
print(f"maior valor: {maximo}")

posicao = vetor.index(max(vetor))
print(f"posição de maior valor: {posicao}")