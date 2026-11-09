'''
develop a program that reads 10 integers and stores them in a list. Then, create a new list containing no duplicate elements, while preserving the order of the first occurrence of each number.
example:
original list: [4, 2, 4, 7, 2, 9]
new list: [4, 2, 7, 9]
'''

def read_number(n):
    while True:
        try:
            return int(input(n))
        except ValueError:
            print(f"[error]: enter a valid integer: ")

def main():
    numbers_oficial = []
    
    for i in range(1,11):
        numbers_oficial.append(read_number("enter the {i}º integer number: "))

    new_numbers = []
    for number in numbers_oficial:
        if number not in new_numbers:
            new_numbers.append(number)

    print(f"list origin: {numbers_oficial}")
    print(f"list with no duplicates: {new_numbers}")

if __name__ == "__main__":
    main()

