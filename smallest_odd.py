"""
To Run:
python3 -m smallest_odd

Given a list of integers, please write a function that returns the smallest
odd integer from that list

Example: [4, 5, 3, 6, 2, 2, 7] -> 3
"""


def smallest_odd(integers: list):
    """
    Always a list - may be empty - may have non integer values
    returns None if empty or only even integers
    """

    odd_integers = [
        int_
        for int_ in integers
        if isinstance(int_, int) and int_ % 2
    ]

    if odd_integers:
        return min(odd_integers)
    else:
        return None


def main():
    assert(smallest_odd([]) is None)
    assert(smallest_odd([4, 5, 3, 6, 2, 2, 7]) == 3)
    assert(smallest_odd([7]) == 7)
    assert(smallest_odd([7, 7]) == 7)
    assert(smallest_odd([2, 4, 6]) is None)
    assert(smallest_odd([0, 2]) is None)
    assert(smallest_odd([4, 5, 3, 6, None, 'TEST!', 2, 2, 7]) == 3)
    assert(smallest_odd([4, {}, 3, 6, None, 'TEST!', 2, 2, 7]) == 3)
    print('All tests passed.')


if __name__ == '__main__':
    main()
