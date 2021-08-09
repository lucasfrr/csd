from numerical_systems.functions import convert_to_decimal, convert_from_decimal


def numerical_system_menu():

    while True:

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

        choice = int(
            input("Digite tipo de conversão ou 0 para voltar ao menu anterior: ")
        )

        if choice == 0:
            break

        value = input(
            "Digite o valor a ser convertido ou 0 para voltar ao menu anterior: "
        )

        if choice == 0:
            break
        elif choice == 1:
            result = convert_from_decimal(str(value), 2)
            print(f"O número {value} na base 10 é equivalente a {result} em binário")
        elif choice == 2:
            result = convert_from_decimal(str(value), 8)
            print(f"O número {value} na base 10 é equivalente a {result} em octal")
        elif choice == 3:
            result = convert_from_decimal(str(value), 16)
            print(
                f"O número {value} na base 10 é equivalente a {result} em hexadecimal"
            )
        elif choice == 4:
            result = convert_to_decimal(str(value), 2)
            print(f"O número {value} na base 2 é equivalente a {result} em decimal")
        elif choice == 5:
            partial_result = convert_to_decimal(str(value), 2)
            result = convert_from_decimal(partial_result, 16)
            print(f"O número {value} na base 2 é equivalente a {result} em hexadecimal")
        elif choice == 6:
            partial_result = convert_to_decimal(str(value), 2)
            result = convert_from_decimal(partial_result, 8)
            print(f"O número {value} na base 2 é equivalente a {result} em octal")
        elif choice == 7:
            result = convert_to_decimal(str(value), 8)
            print(f"O número {value} na base 8 é equivalente a {result} em decimal")
        elif choice == 8:
            partial_result = convert_to_decimal(str(value), 8)
            result = convert_from_decimal(partial_result, 16)
            print(f"O número {value} na base 8 é equivalente a {result} em hexadecimal")
        elif choice == 9:
            partial_result = convert_to_decimal(str(value), 8)
            result = convert_from_decimal(partial_result, 2)
            print(f"O número {value} na base 8 é equivalente a {result} em binário")
        elif choice == 10:
            result = convert_to_decimal(str(value), 16)
            print(f"O número {value} na base 16 é equivalente a {result} em decimal")
        elif choice == 11:
            partial_result = convert_to_decimal(str(value), 16)
            result = convert_from_decimal(partial_result, 2)
            print(f"O número {value} na base 16 é equivalente a {result} em binário")
        elif choice == 12:
            partial_result = convert_to_decimal(str(value), 16)
            result = convert_from_decimal(partial_result, 8)
            print(f"O número {value} na base 16 é equivalente a {result} em octal")
