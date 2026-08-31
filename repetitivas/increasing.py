'''
Read an unspecified number of pairs of integers X and Y. For each pair of X and Y, print a
message indicating whether these values were entered in ascending or descending order. The
program should terminate when two equal values are entered.
'''

x = int(input("Value 1:"))
y = int(input("Value 2:"))

while x != y:
    if x < y:
        print("increasing")
        print(x,y)
    else:
        print("decreasing")
        print(x,y)

    break