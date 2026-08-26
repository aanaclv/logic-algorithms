preco_unitario = float(input("Preço unitário do produto: "))
qt_comprada = int(input("quantidade comprada: "))
valor_recebido = float(input("Valor recebido: "))
total_compra = preco_unitario * qt_comprada

if total_compra < valor_recebido:
    troco = valor_recebido - total_compra
    print(f"Troco: {troco}")
else:
    valor_faltante = total_compra - valor_recebido
    print(f"Falta {valor_faltante}")