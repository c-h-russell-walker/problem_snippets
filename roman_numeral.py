"""
To Run:
python3 -m roman_numeral
"""

from collections import namedtuple

NumeralData = namedtuple(
    'NumeralData',
    [
        'string_value',
        'integer_value',
    ]
)


def int_to_roman_numeral(integer: int):
    roman_numeral_data = [
        NumeralData('M', 1000),
        NumeralData('CM', 900),
        NumeralData('D', 500),
        NumeralData('CD', 400),
        NumeralData('C', 100),
        NumeralData('LC', 90),
        NumeralData('L', 50),
        NumeralData('XL', 40),
        NumeralData('X', 10),
        NumeralData('IX', 9),
        NumeralData('V', 5),
        NumeralData('IV', 4),
        NumeralData('I', 1),
    ]

    answer_chars = []

    for numeral_data in roman_numeral_data:
        amount = numeral_data.integer_value
        if integer >= amount:
            char_count = integer // amount
            answer_chars.append(numeral_data.string_value * char_count)
            integer -= amount * char_count

    return ''.join(answer_chars)


def main():
    assert(int_to_roman_numeral(1) == 'I')
    assert(int_to_roman_numeral(10) == 'X')
    assert(int_to_roman_numeral(1000) == 'M')
    assert(int_to_roman_numeral(39) == 'XXXIX')
    assert(int_to_roman_numeral(246) == 'CCXLVI')
    assert(int_to_roman_numeral(421) == 'CDXXI')
    assert(int_to_roman_numeral(160) == 'CLX')
    assert(int_to_roman_numeral(207) == 'CCVII')
    assert(int_to_roman_numeral(1066) == 'MLXVI')
    assert(int_to_roman_numeral(1776) == 'MDCCLXXVI')
    assert(int_to_roman_numeral(1954) == 'MCMLIV')
    assert(int_to_roman_numeral(2019) == 'MMXIX')
    print('All tests passed.')


if __name__ == '__main__':
    main()
