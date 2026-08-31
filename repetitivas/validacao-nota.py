nota1 = float(input("nota 1: "))
nota2 = float(input("nota 2: "))

while not (0 <= nota1 <= 10):
    print("valor inválido: tente novamente: ")
    nota1 = float(input("nota 1: "))

while not(0 <= nota1 <= 10):
    print("valor inválido: tente novamente: ")
    nota2 = float(input("nota 2: "))


media = (nota1+nota2)/2
print(f"média: {media}")
