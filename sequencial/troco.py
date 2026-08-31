preco_unitario = float(input("preço unitário do produto: "))
qt_comprada = int(input("quantidade comprada: "))
dinheiro_recebido = float(input("dinheiro recebido: "))
valor_total = preco_unitario*qt_comprada
troco = dinheiro_recebido-valor_total
print(f"troco: {troco}")