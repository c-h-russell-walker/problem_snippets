"""
To Run:
python3 -m common_chars
"""


def common(word_one: str, word_two: str) -> list:
    # Returns (non-repeating values) list of characters common to both strings
    return list(set(word_one).intersection(set(word_two)))


def main():
    assert(sorted(common('asdf', 'dfgh')) == sorted(['d', 'f']))
    assert(sorted(common('asdfasdf', 'dfgh')) == sorted(['d', 'f']))
    assert(common('', 'dfgh') == [])
    assert(common('', '') == [])
    assert(common('asdf', 'dfgh') != ['d'])
    print('All tests passed.')


if __name__ == '__main__':
    main()
