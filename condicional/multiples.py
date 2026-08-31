'''
Write a program that reads two integers and determines whether one number is a multiple of the other. The
numbers can be entered in any order.
'''

integer1 = int(input("Integer 1: "))
integer2 = int(input("Integer 2: "))

if integer1 and integer2 % 2 == 0:
    print("There are multiple")
else:
    print("Are not multiples")