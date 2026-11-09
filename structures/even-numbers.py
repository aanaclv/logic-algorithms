'''
read 10 integers and store them in a list.
then, create two new lists: one containing only the even numbers and another containing only the odd numbers.
finally, display the three lists and the number of elements in each one.
'''

def read_number(n):
    while True:
        try:
            return int(input(n))
        except ValueError:
            print("[error]: enter a valid integer: ")

def main():
    numbers = []

    for i in range(1,11):
        numbers.append(read_number(f"enter the {i}º integer number: "))

    even_numbers = []

    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)
    print(f"even numbers list: {even_numbers}")

if __name__ == "__main__":
    main()