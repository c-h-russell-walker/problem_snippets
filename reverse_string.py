"""
To Run:
python3 -m reverse_string
"""

import math


class NonStringException(Exception):
    pass


def reverse_string(string: str) -> str:
    if not isinstance(string, str):
        raise NonStringException(f'Passed non-string: {string}')

    # Using built-ins:
    # return string[::-1]

    # _Not_ using built-ins
    # We can ignore middle character if length is odd
    left_idx = math.floor(len(string) / 2) - 1
    right_idx = math.ceil(len(string) / 2)

    chars = [char for char in string]

    while left_idx >= 0:
        chars[left_idx], chars[right_idx] = chars[right_idx], chars[left_idx]
        left_idx -= 1
        right_idx += 1

    return ''.join(chars)


def main():
    non_string_types = [
        None,
        [],
        {},
        123,
    ]
    for type_ in non_string_types:
        try:
            reverse_string(type_)
        except NonStringException:
            print(f'Caught exception for {type_}')

    assert(reverse_string('asdf') != 'asdf')
    assert(reverse_string('asdf') == 'fdsa')
    assert(reverse_string('asddf') == 'fddsa')
    assert(reverse_string('asdfg') == 'gfdsa')
    print('All tests passed.')


if __name__ == '__main__':
    main()
