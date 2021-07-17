def to_decimal(number: str, base: int):
    """
    This function converts a given number is in binary, octal or hexadecimal base
    to decimal base.

    Parameters:
        number (str): The value you want convert.
        base (int): The numerical base what you want convert.

    Returns:
        int: A number is in decimal base.
    """

    if not base == 2 or base == 8 or base == 16:
        raise ValueError(f"O valor {base} não é um valor de base numérica válido.")

    hexadecimal_values = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    result = 0

    if not base == 16:
        for symbol in number:
            expoent = (len(number) - 1) - number.index(symbol)
            result += int(symbol) * (base ** expoent)
    else:
        for symbol in number:
            expoent = (len(number) - 1) - number.index(symbol)
            try:
                result += int(symbol) * (base ** expoent)
            except TypeError:
                result += hexadecimal_values[symbol] * (base ** expoent)

    return result

def from_decimal(number: str, base: int):
    """
    This function converts a given number is in decimal base to a
    binary, octal or hexadecimal base.

    Parameters:
        number (str): The value you want convert.
        base (int): The numerical base what you want convert.

    Returns:
        str: A number is in numerical base what you wanted.
    """

    if not base == 2 or base == 8 or base == 16:
        raise ValueError(f"O valor {base} não é um valor de base numérica válido.")

    hexadecimal_values = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    result = ""

    while number >= base:
        rest = str(number % base)
        result += str(rest)
        number = number // base

    result += str(number)
    result = result[::-1]

    return result
