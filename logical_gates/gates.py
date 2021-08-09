def and_gate(bits: str) -> str:
    if len(bits) < 2:
        raise ValueError(
            "Uma porta n-ária não aceita como entrada uma palavra com menos de 2 bits"
        )
    if all(bit == "1" for bit in bits):
        return "1"
    return "0"


def or_gate(bits: str) -> str:
    if len(bits) < 2:
        raise ValueError(
            "Uma porta n-ária não aceita como entrada uma palavra com menos de 2 bits"
        )
    if all(bit == "0" for bit in bits):
        return "0"
    return "1"


def nand_gate(bits: str) -> str:
    if len(bits) < 2:
        raise ValueError(
            "Uma porta n-ária não aceita como entrada uma palavra com menos de 2 bits"
        )
    if all(bit == "1" for bit in bits):
        return "0"
    return "1"


def nor_gate(bits: str) -> str:
    if len(bits) < 2:
        raise ValueError(
            "Uma porta n-ária não aceita como entrada uma palavra com menos de 2 bits"
        )
    if all(bit == "0" for bit in bits):
        return "1"
    return "0"


def xor_gate(bits: str) -> str:
    if len(bits) < 2:
        raise ValueError(
            "Uma porta n-ária não aceita como entrada uma palavra com menos de 2 bits"
        )
    if all(bit == "0" for bit in bits) or all(bit == "1" for bit in bits):
        return "0"
    return "1"


def xnor_gate(bits: str) -> str:
    if len(bits) < 2:
        raise ValueError(
            "Uma porta n-ária não aceita como entrada uma palavra com menos de 2 bits"
        )
    if all(bit == "0" for bit in bits) or all(bit == "1" for bit in bits):
        return "1"
    return "0"


def not_gate(bit: str):
    if len(bit) != 1:
        raise ValueError(
            "Uma porta unária não pode receber mais de um bit como entrada"
        )
    if bit == "0":
        return "1"
    return "0"
