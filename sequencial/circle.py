'''
Write a program to read the value “r” for the radius of a circle, and then display the area of the
circle to three decimal places. The formula for the area of a circle is as follows: 𝑎𝑟𝑒𝑎 = 𝜋 𝑟. You can
use the value of 𝜋 provided by your programming language’s library, or, if you prefer, use
the value 3.14159 directly.
'''

radius = float(input("Value of the circle's radius: "))
area = 3.14159*radius**2
print(f"Area: {area:.3f}")