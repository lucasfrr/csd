from numerical_systems.functions import convert_to_decimal


def test_convert_binary_to_decimal():
    assert convert_to_decimal("101", 2) == "5"


def test_convert_octal_to_decimal():
    assert convert_to_decimal("32", 8) == "26"


def test_convert_hexadecimal_to_decimal():
    assert convert_to_decimal("CAF", 16) == "3247"
