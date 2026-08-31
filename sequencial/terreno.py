l = float(input("digite a largura do terreno: "))
c = float(input("digite o comprimento do terreno: "))
m = float(input("digite o valor do metro quadrado: "))

area_terreno = l*c
print(f"area do terreno =  {area_terreno:.2f}")

preco_terreno = area_terreno * m
print(f"preco do terreno = {preco_terreno:.2f}")