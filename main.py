from numerical_systems.conversions import from_decimal, to_decimal


def main():
    while True:
        print("#### CONVERSOR DE BASES ####")
        print("Que tipo de conversão você deseja realizar?")
        print("1 - Decimal para binário")
        print("2 - Decimal para octal")
        print("3 - Decimal para hexadecimal")
        print("4 - Binário para decimal")
        print("5 - Binário para hexadecimal")
        print("6 - Binário para octal")
        print("7 - Octal para decimal")
        print("8 - Octal para hexadecimal")
        print("9 - Octal para binário")
        print("10 - Hexadecimal para decimal")
        print("11 - Hexadecimal para binário")
        print("12 - Hexadecimal para octal")

        choice = input("Digite a opção ou (s) para sair: ")
        if choice == 's' or choice == 'S':
            break

        value = input("Digite o valor a ser convertido ou (s) para sair: ")

        if value == 's' or value == 'S':
            break
        elif choice == '1':
            result = from_decimal(int(value), 2)
            print(f"O número {value} na base 10 é equivalente a {result} em binário")
        elif choice == '2':
            result = from_decimal(int(value), 8)
            print(f"O número {value} na base 10 é equivalente a {result} em octal")
        elif choice == '3':
            result = from_decimal(int(value), 16)
            print(f"O número {value} na base 10 é equivalente a {result} em hexadecimal")
        elif choice == '4':
            result = to_decimal(int(value), 2)
            print(f"O número {value} na base 2 é equivalente a {result} em decimal")
        elif choice == '5':
            partial_result = to_decimal(int(value), 2)
            result = from_decimal(partial_result, 16)
            print(f"O número {value} na base 2 é equivalente a {result} em hexadecimal")
        elif choice == '6':
            partial_result = to_decimal(int(value), 2)
            result = from_decimal(partial_result, 8)
            print(f"O número {value} na base 2 é equivalente a {result} em octal")
        elif choice == '7':
            result = to_decimal(int(value), 8)
            print(f"O número {value} na base 8 é equivalente a {result} em decimal")
        elif choice == '8':
            partial_result = to_decimal(int(value), 8)
            result = from_decimal(partial_result, 16)
            print(f"O número {value} na base 8 é equivalente a {result} em hexadecimal")
        elif choice == '9':
            partial_result = to_decimal(int(value), 8)
            result = from_decimal(partial_result, 2)
            print(f"O número {value} na base 8 é equivalente a {result} em binário")
        elif choice == '10':
            result = to_decimal(int(value), 16)
            print(f"O número {value} na base 16 é equivalente a {result} em decimal")
        elif choice == '11':
            partial_result = to_decimal(int(value), 16)
            result = from_decimal(partial_result, 2)
            print(f"O número {value} na base 16 é equivalente a {result} em binário")
        elif choice == '12':
            partial_result = to_decimal(int(value), 16)
            result = from_decimal(partial_result, 8)
            print(f"O número {value} na base 16 é equivalente a {result} em octal")

if __name__ == '__main__':
    main()
