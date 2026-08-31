'''
Write a program to calculate the change when paying for a product at a grocery store.
The program must read the unit price of the product, the number of units purchased,
and the amount of cash given by the customer (assume there is enough cash). Your program must
display the amount of change to be returned to the customer.
'''

unit_price = float(input("Unit price of product: "))
quantity = int(input("Quantity: "))
money_received = float(input("Money Received: "))
total_value = unit_price*quantity
change = money_received-total_value
print(f"Change: {change}")