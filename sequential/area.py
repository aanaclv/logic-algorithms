'''
Write a program to read the width and length of a rectangular plot of land, each with one
decimal place, as well as the price per square meter of the plot, with two decimal places. 
The program should then display the area of the plot and the price of the plot, both with two decimal places.
'''

width = float(input("Enter the width of the lot: "))
length = float(input("Enter the length of the lot: "))
square_meter = float(input("Enter the price per square meter: "))

area = width*length
print(f"Lot area =  {area:.2f}")

land_price = area * square_meter
print(f"Land price = {land_price:.2f}$")