n = int(input("quantos números você vai digitar?"))
vetor = []

for i in range(n):
    numero = int(input("digite um número: "))
    vetor.append(numero)

print("números negativos:")

for numero in vetor:
    if numero < 0:
        print(numero)
