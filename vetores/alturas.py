n = int(input("quantos números vai digitar: "))
vetor = []

for i in range(n):
    valor = int(input("digite um número: "))
    if valor % 2 == 0:
        vetor.append(valor)
    quantidade = len(vetor)

print(f'''Numeros pares: {vetor}
    {quantidade}''')
