'''
A telephone company charges 50.00$ for a basic plan that includes 100 minutes of
talk time. Each minute that exceeds the 100-minute allowance costs 2.00$. Write a program to
determine the number of minutes a person has used and then display the amount to be paid.
'''

minuty = int(input("Quantity of minuts: "))
amount_paid = 50

if minuty > 100:
    amount_paid = amount_paid + 2 * (minuty - 100)
    print(f"Amount due: {amount_paid}")
print(amount_paid)