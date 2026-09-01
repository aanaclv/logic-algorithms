'''
Write a program to read the base and height of a rectangle. Then, display the value
of the area and perimeter of this rectangle, rounded to four decimal places.
'''

rectangular_base = float(input("Enter the base of the rectangle: "))
rectangular_height = float(input("Enter the height of the rectangle: "))
area = rectangular_base*rectangular_height

perimeter = 2*(rectangular_base+rectangular_height)

print(f'Area = {area:.4f}')
print(f'Perimeter = {perimeter:.4f}')
