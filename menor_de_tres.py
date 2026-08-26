primeiro_valor = int(input("Primeiro valor: "))
segundo_valor = int(input("Segundo valor: "))
terceiro_valor = int(input("Terceiro valor: "))

if primeiro_valor < segundo_valor:
    if primeiro_valor < terceiro_valor:
        print(primeiro_valor)
elif segundo_valor < terceiro_valor:
    print(segundo_valor)
else:
    print(terceiro_valor)