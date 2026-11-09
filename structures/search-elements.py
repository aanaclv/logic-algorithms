'''
Crie uma lista contendo 10 números inteiros informados pelo usuário. 
Em seguida, solicite outro número e verifique se ele está presente na lista. 
Caso esteja, informe quantas vezes aparece e apresenta as posições em que foi encontrado.
'''

def read_num(n):
    while True:
        try:
            return int(input(n))
        except ValueError:
            print(f"[error]: enter a valid integer: ")


def main():
    numbers = []

    for i in range(1,11):
        numbers.append(read_num("enter the {i}º integer number: "))

    search_number = read_num("enter the value you wish to search for: ")
    position = [indice for indice, n in enumerate(numbers) if n == search_number]

    print(f"\n list; {numbers}")
    if position:
        print(f"the numer {search_number} appears {len(position)} times.")
        print(f"position 0:{position}")
    else:
        print(f"the value {search_number} is not present in the list.")

if __name__ == "__main__":
    main()