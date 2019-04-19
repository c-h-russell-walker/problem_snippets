"""
To Run:
python3 -m sort_two_lists

Given 2 lists that are sorted return one list sorted of all values

Example:
    [ 3, 4, 4, 5 ] [ 2, 3, 6, 7, 8] => [ 2, 3, 3, 4, 4, 5, 6, 7, 8 ]
"""


def sort_lists(
    list_one: list,
    list_two: list,
    with_builtins: bool = True,
) -> list:
    if with_builtins:
        return sorted(list_one + list_two)
    else:
        merged = list_one + list_two
        for _ in range(len(merged)):
            for j in range(len(merged) - 1):
                if merged[j] > merged[j + 1]:
                    merged[j + 1], merged[j] = merged[j], merged[j + 1]
        return merged


def main():
    list_one = [3, 4, 4, 5]
    list_two = [2, 3, 6, 7, 8]
    assert(sort_lists(list_one, list_two) == [2, 3, 3, 4, 4, 5, 6, 7, 8])
    assert(
        sort_lists(list_one, list_two, False) == [2, 3, 3, 4, 4, 5, 6, 7, 8]
    )

    assert(sort_lists([], []) == [])
    assert(sort_lists([], [], False) == [])

    assert(sort_lists([], [3]) == [3])
    assert(sort_lists([1, 2, 3], [], False) == [1, 2, 3])

    print('All tests passed.')


if __name__ == '__main__':
    main()
