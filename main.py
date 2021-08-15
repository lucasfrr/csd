from numerical_systems.menu import numerical_system_menu
from unit_computer_memory.menu import unit_computer_memory_menu
from logical_gates.menu import logical_gates_menu
from binary_sum.menu import binary_sum_menu


def main():
    while True:
        print("Que tipo de conversão você deseja realizar?")
        print("1 - CONVERSOR DE BASES")
        print("2 - CONVERSOR DE UNIDADE DE MEMÓRIA COMPUTACIONAL")
        print("3 - PORTAS LÓGICAS")
        print("4 - SOMAS BINÁRIAS")

        choice = int(input("Digite a opção ou (0) para sair: "))

        if choice == 0:
            break
        elif choice == 1:
            numerical_system_menu()
        elif choice == 2:
            unit_computer_memory_menu()
        elif choice == 3:
            logical_gates_menu()
        elif choice == 4:
            binary_sum_menu()
        else:
            print("Escolha inválida")


if __name__ == "__main__":
    main()
