'''
develop a program that asks the user for 5 integers and stores them in a list. At the end, display:
the complete list.
the largest and smallest numbers.
the sum and the average of the values.
the list in ascending order.
'''

def read_num(n):
    while True:
        try:
            return int(input(n))
        except ValueError:
            print("[error]: enter a valid integer: ")

def main():
    numbers = []

    for i in range(1,6):
        numbers.append(read_num(f"enter the {i}º integer number: "))

    print(f"complete list: {numbers}")
    print(f"largest number: {max(numbers)}")
    print(f"smallest number: {min(numbers)}")
    print(f"sum of the values: {sum(numbers)}")
    print(f"average of the values: {sum(numbers)/ len(numbers):.2f}")
    print(f"list in ascending order: {sorted(numbers)}")

if __name__ == "__main__":
    main()


