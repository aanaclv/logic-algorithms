'''
A snack bar offers several products. Each product has a code
and a price. You must write a program to read the code and the
quantity purchased of a product (assuming the code is valid), and then
display the amount to be paid, rounded to two decimal places,
'''

product_code = int(input("Product code: "))
quantity = int(input("Quantity: "))

if product_code == 1:
    print(f'''Product code of the purchased item: {product_code}
    Quantity Purchased: {quantity}
    Total: {quantity*5:.2f}$
    ''')
if product_code == 2:
    print(f'''Product code of the purchased item: {product_code}
    Quantity Purchased: {quantity}
    Total: {quantity*3.50:.2f}$
    ''')
if product_code == 3:
    print(f'''Product code of the purchased item: {product_code}
    Quantity Purchased: {quantity}
    Total: {quantity*4.80:.2f}$
    ''')

if product_code == 4:
    print(f'''Product code of the purchased item: {product_code}
    Quantity Purchased: {quantity}
    Total: {quantity*8.90:.2f}$
    ''')

if product_code == 5:
    print(f'''Product code of the purchased item: {product_code}
    Quantity Purchased: {quantity}
    Total: {quantity*7.32:.2f}$
    ''')