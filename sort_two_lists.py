"""
To Run:
python3 -m sort_two_lists

Given 2 lists that are sorted return one list sorted of all values
We're making the assumption that the lists contain only integers (pos. or neg.)

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
        if not list_one and not list_two:
            return []
        elif not list_one:
            return list_two
        elif not list_two:
            return list_one

        answer = []
        min_val = min([list_one[0], list_two[0]])
        max_val = max([list_one[-1], list_two[-1]])
        for val in range(min_val, max_val + 1):
            while list_one and list_one[0] == val:
                answer.append(val)
                del list_one[0]
            while list_two and list_two[0] == val:
                answer.append(val)
                del list_two[0]
        return answer


def main():
    first_list_one = [3, 4, 4, 5]
    first_list_two = [2, 3, 6, 7, 8]
    first_answer = [2, 3, 3, 4, 4, 5, 6, 7, 8]

    assert(
        sort_lists(first_list_one, first_list_two) == first_answer
    ), sort_lists(first_list_one, first_list_two)
    assert(
        sort_lists(first_list_one, first_list_two, False) == first_answer
    ), sort_lists(first_list_one, first_list_two, False)

    second_list_one = [-3, 0, 4, 4, 5]
    second_list_two = [2, 3, 6, 7, 8, 111_111]
    second_answer = [-3, 0, 2, 3, 4, 4, 5, 6, 7, 8, 111_111]

    assert(
        sort_lists(second_list_one, second_list_two) == second_answer
    ), sort_lists(second_list_one, second_list_two)
    assert(
        sort_lists(second_list_one, second_list_two, False) == second_answer
    ), sort_lists(second_list_one, second_list_two, False)

    assert(sort_lists([], []) == [])
    assert(sort_lists([], [], False) == [])

    assert(sort_lists([], [3], False) == [3])
    assert(sort_lists([3], [], False) == [3])
    assert(sort_lists([3], [3], False) == [3, 3])
    assert(sort_lists([1, 2, 3], [], False) == [1, 2, 3])

    print('All tests passed.')


if __name__ == '__main__':
    main()
