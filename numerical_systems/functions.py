from numerical_systems.hexadecimals_conversions import decimal_to_hexadecimal


bases = (2, 8, 16,)

def convert_to_decimal(number: str, base: int) -> str:
    """
    This function converts a given number is in binary, octal or hexadecimal base
    to decimal base.

    Parameters:
        number (str): The value you want convert.
        base (int): The numerical base what you want convert.

    Returns:
        str: A number is in decimal base.
    """

    if base not in bases:
        raise ValueError(f"O valor {base} não é um valor de base numérica válido.")

    hexadecimal_values = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    result = 0
    iteration = 0

    if not base == 16:
        for symbol in number:
            iteration += 1
            expoent = len(number) - iteration
            result += int(symbol) * (base ** expoent)
    else:
        for symbol in number:
            iteration += 1
            expoent = len(number) - iteration

            if symbol not in hexadecimal_values.keys():
                result += int(symbol) * (base ** expoent)
            else:
                result += hexadecimal_values[symbol] * (base ** expoent)

    return str(result)


def convert_from_decimal(number: str, base: int) -> str:
    """
    This function converts a given number is in decimal base to a
    binary, octal or hexadecimal base.

    Parameters:
        number (str): The value you want convert.
        base (int): The numerical base what you want convert.

    Returns:
        str: A number is in numerical base what you wanted.
    """

    if base not in bases:
        raise ValueError(f"O valor {base} não é um valor de base numérica válido.")

    if base == 16:
        return decimal_to_hexadecimal(number)

    result, number = "", int(number)

    while number >= base:
        rest = number % base
        result += str(rest)
        number = number // base

    result += str(number)
    return result[::-1]