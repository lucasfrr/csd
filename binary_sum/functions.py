def sum_binary(number_01: str, number_02: str) -> str:
    """
    This funciton makes a sum of two binary numbers.

    Parameters:
        number_01 (str)
        number_02 (str)

    Returns:
        str: Result of sum.
    """

    return bin(int(number_01, 2) + int(number_02, 2))[2:]
