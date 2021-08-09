from unit_computer_memory.functions import convert_from_bytes, convert_to_bytes


def unit_computer_memory_menu():

    while True:
        unit_from = ""
        unit_to = ""

        print("1 - Bytes")
        print("2 - Kilobytes")
        print("3 - Megabytes")
        print("4 - Gigabytes")
        print("5 - Terabytes")

        choice = int(
            input(
                "Selecione de qual unidade você quer converter ou digite (0) para voltar:"
            )
        )

        if choice == 0:
            break
        elif choice == 1:
            unit_from = "Bytes"
        elif choice == 2:
            unit_from = "Kilobytes"
        elif choice == 3:
            unit_from = "Megabytes"
        elif choice == 4:
            unit_from = "Gigabytes"
        elif choice == 5:
            unit_from = "Terabytes"

        value = float(input("Digite o valor a ser convertido ou (0) para sair: "))
        formated_value = format(value, ".2f")

        if choice == 0:
            break

        print("1 - Bytes")
        print("2 - Kilobytes")
        print("3 - Megabytes")
        print("4 - Gigabytes")
        print("5 - Terabytes")

        choice_2 = int(
            input(
                "Selecione para qual unidade você quer converter ou digite (0) para voltar:"
            )
        )

        if choice_2 == 0:
            break
        elif choice_2 == 1:
            unit_to = "Bytes"
        elif choice_2 == 2:
            unit_to = "Kilobytes"
        elif choice_2 == 3:
            unit_to = "Megabytes"
        elif choice_2 == 4:
            unit_to = "Gigabytes"
        elif choice_2 == 5:
            unit_to = "Terabytes"

        if choice == 0 or choice_2 == 0:
            break
        elif choice == choice_2:
            print("Não é possível converter um número para mesma unidade")
        elif choice_2 == 1:
            result = convert_to_bytes(formated_value, unit_from)
            print(
                f"O valor {formated_value} {unit_from} em {unit_to} é igual a {result}"
            )
        elif choice_2 in [2, 3, 4, 5]:
            partial_result = convert_to_bytes(formated_value, unit_from)
            result = convert_from_bytes(partial_result, unit_to)
            print(
                f"O valor {formated_value} {unit_from} em {unit_to} é aproximadamente {result}"
            )
