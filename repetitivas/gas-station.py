'''
A gas station wants to determine which of its products is preferred by its customers.
Write an algorithm to read the type of fuel dispensed (coded as follows:
1. Ethanol 2. Gasoline 3. Diesel 4. End). If the user enters an invalid code (outside the range of 1 through
4), they must be prompted to enter a new code (until a valid one is entered). The program will terminate when the
code entered is 4, at which point it should display the message “THANK YOU VERY MUCH,” as well
as the quantities of each fuel.
'''

alcool = 0
gasoline = 0
diesel = 0

cod = int(input("Enter a code (1 (Alcool), 2 (Gasoline), 3 (Diesel)) or 4 to stop:"))
while cod !=4 and cod < 4:
    if cod == 1:
        alcool += 1
    elif cod == 2:
        gasoline += 1
    elif cod == 3:
        diesel += 1
    cod = int(input("Enter a code (1, 2, 3) or 4 to stop:"))

print("Thank you very much!")
print(f'''Alcool: {alcool}\
    Gasoline: {gasoline}\
    Diesel: {diesel}''')