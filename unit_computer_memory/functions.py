def convert_to_bytes(number: str, unit: str):
    """Convert a value in Kilobytes, Megabytes, Gigabytes or Terabytes to bytes

    Args:
        number (int): Value to be converted
        unit (str): Unit of value

    Returns:
        str: Return a string with converted value
    """
    number = float(number)
    if number < 0:
        return "Número inválido"

    if unit == "Kilobytes":
        result = number * 1024
        return str(format(result, ".2f"))
    elif unit == "Megabytes":
        result = number * 1048576
        return str(format(result, ".2f"))
    elif unit == "Gigabytes":
        result = number * 1073741824
        return str(format(result, ".2f"))
    elif unit == "Terabytes":
        result = number * 1099511627776
        return str(format(result, ".2f"))
    else:
        return "Unidade inválida ou indisponível."


def convert_from_bytes(number: str, unit: str):
    """Convert a value in bytes to Kilobytes, Megabytes, Gigabytes or Terabytes

    Args:
        number (int): Value to be converted
        unit (str): Unit to be converted

    Returns:
        str: Resturn a string with converted value
    """
    number = float(number)
    if number < 0:
        return "Número inválido"

    if unit == "Kilobytes":
        result = number / 1024
        return str(format(result, ".2f"))
    elif unit == "Megabytes":
        result = number / 1048576
        return str(format(result, ".2f"))
    elif unit == "Gigabytes":
        result = number / 1073741824
        return str(format(result, ".2f"))
    elif unit == "Terabytes":
        result = number / 1099511627776
        return str(format(result, ".2f"))
    else:
        return "Unidade inválida ou indisponível."
