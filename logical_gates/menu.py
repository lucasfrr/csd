from logical_gates import functions


def logical_gates_menu():

    while True:
        print("1 - NOT")
        print("2 - AND")
        print("3 - OR")
        print("4 - NAND")
        print("5 - NOR")
        print("6 - XOR")

        choice = int(input("Selecione uma porta ou digite (0) para voltar: "))

        if choice == 0:
            break
        elif choice not in [1, 2, 3, 4, 5, 6]:
            print("Opção inválida, escolha novamente.")
        else:
            input_binary = str(input("Digite valor de entrada em binário: "))
            if choice == 1:
                print("Saída será igual a " + functions.not_gate(input_binary))
            elif choice == 2:
                print("Saída será igual a " + functions.and_gate(input_binary))
            elif choice == 3:
                print("Saída será igual a " + functions.or_gate(input_binary))
            elif choice == 4:
                print("Saída será igual a " + functions.nand_gate(input_binary))
            elif choice == 5:
                print("Saída será igual a " + functions.nor_gate(input_binary))
            elif choice == 6:
                print("Saída será igual a " + functions.xor_gate(input_binary))
