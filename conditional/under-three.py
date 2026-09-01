'''
Write a program to read three integers. Then, display the smallest of the three
numbers read. In the event of a tie, display it only once.
'''

first_value = int(input("First value: "))
second_value = int(input("Second value: "))
third_value = int(input("Third: "))

if first_value < second_value:
    if first_value < third_value:
        print(first_value)
elif second_value < third_value:
    print(second_value)
else:
    print(third_value)