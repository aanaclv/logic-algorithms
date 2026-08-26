distancia1 = float(input("Distância 1: "))
distancia2 = float(input("Distância 2: "))
distancia3 = float(input("Distância 3: "))

if distancia1 > distancia2:
     if distancia1 > distancia3:
          print(distancia1)
elif distancia2 > distancia3:
     print(distancia2)

else:
     print(distancia3)
    