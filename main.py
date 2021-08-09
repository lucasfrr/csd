from numerical_systems.menu import numerical_system_menu
from unit_computer_memory.menu import unit_computer_memory_menu


def main():
    while True:
        print("Que tipo de conversão você deseja realizar?")
        print("1 - CONVERSOR DE BASES")
        print("2 - CONVERSOR DE UNIDADE DE MEMÓRIA COMPUTACIONAL")

        choice = int(input("Digite a opção ou (0) para sair: "))

        if choice == 0:
            break
        elif choice == 1:
            numerical_system_menu()
        elif choice == 2:
            unit_computer_memory_menu()


if __name__ == "__main__":
    main()
