'''
Write a program to read the total distance (in km) traveled by a car, as well as the total
amount of fuel consumed by the car while traveling that distance. Your program should display the car’s
average fuel consumption, rounded to three decimal places.
'''

distance_traveled = int(input("Distance traveled: "))
spent_fuel = float(input("Spent fuel: "))
average_consumption = distance_traveled/spent_fuel
print(f"Average consumption: {average_consumption:.3f}")
