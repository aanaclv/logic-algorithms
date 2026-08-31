a = float(input("Digite a medida A: "))
b = float(input("Digite a medida B: "))
c = float(input("Digite a medida C: "))

area_quadrado = a*4
area_triangulo = (a*b)/2
area_trapezio = ((a+b)*c)/2

print(f'''
        Área do quadrado: {area_quadrado:.4f} \\
         Área do triângulo: {area_triangulo:.4f} \\
          Área do trapézio: {area_trapezio:.4f} \\
''')