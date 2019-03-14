"""
To Run:
python3 -m char_count

Given a string, please write a function that returns the characters in the
string with a count of how many times each character appears.

Example: "hello" -> 'h' - 1, 'e' - 1, 'l' - 2, 'o' - 1
"""


from collections import Counter


def char_count(string):
    counter = Counter(string)
    return counter


if __name__ == '__main__':
    print(char_count('hello'))
