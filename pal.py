"""
To Run:
python3 -m pal
"""


def _format_char(char: str, case_sensitive: bool = False) -> str:
    if case_sensitive:
        return char
    else:
        return char.lower()


def pal(word: str, case_sensitive: bool = False) -> bool:
    """
    Case insensitive (by default) palindrome checker
    Also removes whitespace

    TODO: Check for and/or remove punctuation
    """
    is_palindrome = False
    if type(word) != str:
        return is_palindrome

    word = word.replace(' ', '')

    if word == '':
        is_palindrome = True
    elif len(word) == 1:
        is_palindrome = True
    else:
        is_palindrome = True

        middle = int(len(word) / 2)
        first_half = word[:middle]
        second_half = word[middle:]

        for idx in range(middle):
            if (
                _format_char(first_half[idx], case_sensitive) !=
                _format_char(second_half[-(idx + 1)], case_sensitive)
            ):
                is_palindrome = False
                break

    return is_palindrome


def test(word: str, case_sensitive: bool = False) -> bool:
    print(f'Testing {word}')
    return pal(word, case_sensitive)


def main():
    # False - not strings
    assert not test(None)
    assert not test(2)
    assert not test([])
    assert not test({})
    assert not test(Exception)

    # False
    assert not test('AS')
    assert not test('asd')
    assert not test('ASD')
    assert not test('🐊croc🐊')
    assert not test('abA', case_sensitive=True)
    assert not test('abBa', case_sensitive=True)

    # True (case insensitive)
    assert test('')
    assert test('a')
    assert test('A')
    assert test('aA')
    assert test('aAa')
    assert test('aba')
    assert test('aba', case_sensitive=True)
    assert test('abA')
    assert test('abba')
    assert test('abba', case_sensitive=True)
    assert test('abBa')
    assert test('1aba1')
    assert test('1abba1')
    assert test('111111')
    assert test('🐊')
    assert test('🐊🐊')
    assert test('🐊aha🐊')
    assert test('A Santa stops pots at NASA')
    assert test('Saippuakivikauppias')
    assert test('f' * 555)

    print('All tests passed.')


if __name__ == '__main__':
    main()
