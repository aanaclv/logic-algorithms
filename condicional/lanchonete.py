codigo_produto = int(input("Código do produto: "))
quantidade = int(input("Quantidade: "))

if codigo_produto == 1:
    print(f'''Código do produto comprado: {codigo_produto}\\
    Quantidade comprada: {quantidade}\\
    Total: {quantidade*5:.2f}
    ''')
if codigo_produto == 2:
    print(f'''Código do produto comprado: {codigo_produto}\\
    Quantidade comprada: {quantidade}\\
    Total: {quantidade*3.50:.2f}
    ''')
if codigo_produto == 3:
    print(f'''Código do produto comprado: {codigo_produto}\\
    Quantidade comprada: {quantidade}\\
    Total: {quantidade*4.80:.2f}
    ''')

if codigo_produto == 4:
    print(f'''Código do produto comprado: {codigo_produto}\\
    Quantidade comprada: {quantidade}\\
    Total: {quantidade*8.90:.2f}
    ''')

if codigo_produto == 5:
    print(f'''Código do produto comprado: {codigo_produto}\\
    Quantidade comprada: {quantidade}\\
    Total: {quantidade*7.32:.2f}
    ''')