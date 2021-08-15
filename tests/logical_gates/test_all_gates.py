from logical_gates.functions import (
    and_gate,
    or_gate,
    nand_gate,
    nor_gate,
    not_gate,
    xor_gate,
    xnor_gate,
)


def test_and_gate_get_zeros_and_ones_return_zero():
    assert and_gate("101") == "0"


def test_and_gate_get_zeros_return_zero():
    assert and_gate("0000") == "0"


def test_and_gate_return_one():
    assert and_gate("11") == "1"


def test_or_gate_return_zero():
    assert or_gate("000") == "0"


def test_or_gate_get_zeros_and_ones_return_one():
    assert or_gate("1010") == "1"


def test_or_gate_return_one():
    assert or_gate("111") == "1"


def test_nand_gate_get_zeros_and_ones_return_one():
    assert nand_gate("101") == "1"


def test_and_gate_get_zeros_return_one():
    assert nand_gate("0000") == "1"


def test_nand_gate_return_zero():
    assert nand_gate("11") == "0"


def test_nor_gate_return_one():
    assert nor_gate("000") == "1"


def test_nor_gate_get_zeros_and_ones_return_zero():
    assert nor_gate("1010") == "0"


def test_nor_gate_return_zero():
    assert nor_gate("111") == "0"


def test_not_gate_return_zero():
    assert not_gate("1") == "0"


def test_not_gate_return_one():
    assert not_gate("0") == "1"


def test_xor_gate_return_zero():
    assert xor_gate("11") == "0"


def test_xor_gate_return_one():
    assert xor_gate("01") == "1"


def test_xnor_gate_return_one():
    assert xnor_gate("11") == "1"


def test_xnor_gate_return_zero():
    assert xnor_gate("01") == "0"
