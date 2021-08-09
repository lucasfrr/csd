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

    bases = (
        2,
        8,
        16,
    )
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

    bases = (
        2,
        8,
        16,
    )
    if base not in bases:
        raise ValueError(f"O valor {base} não é um valor de base numérica válido.")

    hexadecimal_values = {
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F",
    }
    result, number = "", int(number)

    while number >= base:
        if base != 16:
            rest = number % base
            result += str(rest)
            number = number // base
        else:
            rest = number % base
            if rest > 9 and rest <= 15:
                rest = hexadecimal_values[str(rest)]
            result += str(rest)
            number = number // base

    result += str(number)
    result = result[::-1]

    return str(result)
