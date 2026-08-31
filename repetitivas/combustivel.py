alcool = 0
gasolina = 0
diesel = 0

codigo = int(input("informe um código (1,2,3) ou 4 para parar: "))
while codigo !=4:
    if codigo == 1:
        alcool += 1
    elif codigo == 2:
        gasolina += 1
    elif codigo == 3:
        diesel += 1

    codigo = int(input("informe um código (1,2,3) ou 4 para parar: "))

print("obrigado!")
print(f'''álcool: {alcool}\
    gasolina: {gasolina}\
    diesel: {diesel}''')