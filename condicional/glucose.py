'''
Write a program to read a person's blood glucose level
and then display on the screen the
classification of that glucose level according to the
reference table
'''

glucose_quantity = float(input("Blood glucose level: "))

if glucose_quantity <= 100:
    print("Normal")

elif glucose_quantity > 100 and glucose_quantity <= 140:
    print("High")

else:
    print("Diabetes")
