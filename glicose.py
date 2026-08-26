qt_glicose = float(input("Quantidade de glicose no sangue: "))

if qt_glicose <= 100:
    print("Normal")

elif qt_glicose > 100 and qt_glicose <= 140:
    print("Elevado")

else:
    print("Diabetes")
