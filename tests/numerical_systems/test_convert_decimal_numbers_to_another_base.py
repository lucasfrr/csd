from numerical_systems.functions import convert_from_decimal


def test_convert_15_decimal_to_binary():
    assert convert_from_decimal("15", 2) == "1111"


def test_convert_26_decimal_to_binary():
    assert convert_from_decimal("26", 2) == "11010"


def test_convert_8_decimal_to_binary():
    assert convert_from_decimal("8", 2) == "1000"


def test_convert_26_decimal_to_octal():
    assert convert_from_decimal("26", 8) == "32"


def test_convert_26_decimal_to_hexadecimal():
    assert convert_from_decimal("26", 16) == "1A"


def test_convert_9_decimal_to_hexadecimal():
    assert convert_from_decimal("9", 16) == "9"


def test_convert_32_decimal_to_hexadecimal():
    assert convert_from_decimal("32", 16) == "20"
