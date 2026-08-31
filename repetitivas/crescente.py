x = int(input("valor 1:"))
y = int(input("valor 2:"))

while x != y:
    if x < y:
        print("crescente")
        print(x,y)
    else:
        print("decrescente")
        print(x,y)

    break