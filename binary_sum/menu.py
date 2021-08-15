from binary_sum.functions import sum_binary


def binary_sum_menu():

    input_1 = str(input("Digite o primeiro número binário: "))
    input_2 = str(input("Digite o segundo número binário: "))

    print("A soma é igual a: " + sum_binary(input_1, input_2))
