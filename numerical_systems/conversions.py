def to_decimal(number: int, base: int):
    """
    This function converts a given number is in binary, octal or hexadecimal base
    to decimal base.

    Parameters:
        number (int): The value you want convert.
        base (int): The numerical base what you want convert.

    Returns:
        int: A number is in decimal base.
    """

    if not base == 2 or base == 8 or base == 16:
        raise ValueError(f"O valor {base} não é um valor de base numérica válido.")

    number = str(number) if base != 16 else number
    hexadecimal_values = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    result = 0

    if not base == 16:
        for symbol in number:
            result += int(symbol) * (base ** number.index(symbol))
    else:
        for symbol in number:
            try:
                result += int(symbol) * (base ** number.index(symbol))
            except TypeError:
                result += hexadecimal_values[symbol] * (base ** number.index(symbol))

    return result

def from_decimal(number: int, base: int):
    """
    This function converts a given number is in decimal base to a
    binary, octal or hexadecimal base.

    Parameters:
        number (int): The value you want convert.
        base (int): The numerical base what you want convert.

    Returns:
        int: A number is in numerical base what you wanted.
    """

    if not base == 2 or base == 8 or base == 16:
        raise ValueError(f"O valor {base} não é um valor de base numérica válido.")

    hexadecimal_values = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    result = list()

    while number > base:
        rest = str(number % base)
        result.append(rest)
        number = number // base

    result = "".join(item for item in result)
    result + str(number)

    return result if base == 16 else int(result)
