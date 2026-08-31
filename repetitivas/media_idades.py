soma = 0
cont = 0

idade = int(input("idade: "))

while idade >= 0:
    soma += idade
    cont += 1

    idade = int(input("idade: "))

if cont == 0:
    print("impossível calcular")
else:
    media = soma/cont
    print(f"Média: {media:.2f}")