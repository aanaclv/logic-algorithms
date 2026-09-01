'''
Write a program to read three measurements, A, B, and C. Then, calculate and display (print the data
to four decimal places):
a) the area of the square with side length A
b) the area of the right triangle with base A and height B
c) the area of the trapezoid with bases A and B, and height C
'''

a = float(input("Enter the measurement for  A: "))
b = float(input("Enter the measurement for B: "))
c = float(input("Enter the measurement for C: "))

square_area = a*4
rectangle_area = (a*b)/2
trapeze_area = ((a+b)*c)/2

print(f'''
        Square of area: {square_area:.4f}
         Rectangle of area: {rectangle_area:.4f}
          Trapeze of area: {trapeze_area:.4f}
''')