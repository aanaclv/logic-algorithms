width = float(input("Enter the width of the lot: "))
length = float(input("Enter the length of the lot: "))
square_meter = float(input("Enter the price per square meter: "))

area = width*length
print(f"Lot area =  {area:.2f}")

land_price = area * square_meter
print(f"Land price = {land_price:.2f}$")