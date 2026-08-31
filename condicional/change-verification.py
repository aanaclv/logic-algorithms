'''
Write a program to calculate the change when paying for a product at a grocery store.
The program must read the unit price of the product, the number of units purchased,
and the amount of cash given by the customer. Your program must display the amount of change to be returned
to the customer.
'''

unity_price = float(input("Unity price of product: "))
quantity = int(input("Quantity: "))
amount_received = float(input("Amount received: "))
total_value = unity_price * quantity

if total_value < amount_received:
    change = amount_received - total_value
    print(f"Change: {change}")
else:
    missing_value = total_value - amount_received
    print(f"Missing {missing_value}")