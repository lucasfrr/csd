symbols = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F',}

def decimal_to_hexadecimal(number: str) -> str:
    
    result, number = '', int(number)
    
    while True:
        if number < 16:
            break
        
        rest = number % 16
        number = number // 16
        if rest >= 10 and rest <= 15:
            result += symbols[str(rest)]
        else:
            result += str(rest)
    
    if number < 16 and number >= 10 and number <=15:
        result += symbols[str(number)]
    else:
        result += str(number) if number != 0 else ''
    
    return result[::-1]


def hexadecimal_to_decimal(number: str) -> str:
    iteration, result = 0, 0

    for symbol in number:
        iteration += 1
        expoent = len(number) - iteration

        if symbol not in symbols.keys():
            result += int(symbol) * (16 ** expoent)
        else:
            result += symbols[symbol] * (16 ** expoent)

    return str(result)
