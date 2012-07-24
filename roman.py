roman_map = (
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
)

def to_roman(number):
    result = ''
    while number > 0:
        for key_number, roman in roman_map:
            if key_number <= number:
                result += roman
                number -= key_number
                break
            
    return result
