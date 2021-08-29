def decimal_to_hexadecimal(number: str) -> str:
    symbols = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F',}
    
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
