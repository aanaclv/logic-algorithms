qt_min = int(input("Quantidade de minutos: "))
valor_pago = 50

if qt_min > 100:
    valor_pago = valor_pago + 2 * (qt_min - 100)
    print(f"valor a pagar: {valor_pago}")
print(valor_pago)