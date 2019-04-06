"""
To Run:
python3 -m conway

Write a program that simulates Conway’s Game of Life.
Wikipedia article:
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

A simple 2-dimensional automata where each cell can be either alive or dead.
Each “clock tick” updates the live/dead status of each cell based on the
following rules:

 * Any live cell with fewer than two live neighbors dies, as if by
    underpopulation.
 * Any live cell with two or three live neighbors lives on to the next
    generation.
 * Any live cell with more than three live neighbors dies, as if by
    overpopulation.
 * Any dead cell with exactly three live neighbors becomes a live cell, as if
    by reproduction.

"""

import os
from copy import deepcopy
from time import sleep


class ConwayGame(object):

    def __init__(self, initial_state):
        width = len(initial_state)
        height = len(initial_state[0])
        self.width = width
        self.width_limit = width - 1
        self.height = height
        self.height_limit = height - 1
        self.matrix = initial_state

    def play(self, delay=1.0):
        self.print_matrix()
        while True:
            self.step()
            os.system('clear')
            self.print_matrix()
            if delay:
                sleep(delay)

    def step(self):
        matrix_copy = deepcopy(self.matrix)
        for y in range(self.height):
            for x in range(self.width):
                alive = False
                neighbor_count = self.get_neighbor_count(x, y)

                if self.matrix[x][y] and neighbor_count in [2, 3]:
                    alive = True
                elif not self.matrix[x][y] and neighbor_count == 3:
                    alive = True

                matrix_copy[x][y] = int(alive)

        self.matrix = matrix_copy

    def get_neighbor_count(self, x, y):
        neighbor_count = 0
        if y < self.height_limit:
            neighbor_count += self.matrix[x][y + 1]

        if y > 0:
            neighbor_count += self.matrix[x][y - 1]

        if x > 0:
            neighbor_count += self.matrix[x - 1][y]
            if y > 0:
                neighbor_count += self.matrix[x - 1][y - 1]
            if y < self.height_limit:
                neighbor_count += self.matrix[x - 1][y + 1]

        if x < self.width_limit:
            neighbor_count += self.matrix[x + 1][y]
            if y > 0:
                neighbor_count += self.matrix[x + 1][y - 1]
            if y < self.height_limit:
                neighbor_count += self.matrix[x + 1][y + 1]

        return neighbor_count

    def print_matrix(self, display_as_ints=False):
        """
        Optionally display as the integer values - helpful for debugging
        """
        icon_map = {
            0: '-',
            1: '*',
        }
        matrix_string = '\n'.join(
            [
                ''.join(
                    [
                        '{:3}'.format(
                            item if display_as_ints else icon_map[item]
                        )
                        for item in row
                    ]
                ) for row in self.matrix
            ]
        )
        print(matrix_string)


def main():
    # 'Blinker'
    # TODO - Add more examples to test with
    blinker = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]
    second_generation = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    third_generation = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]

    test_game = ConwayGame(blinker)
    test_game.step()
    assert(test_game.matrix == second_generation)
    test_game.step()
    assert(test_game.matrix == third_generation)

    print('Tests passed.\n')

    # 'Toad'
    toad = [
        [0, 0, 0, 0],
        [0, 1, 1, 1],
        [1, 1, 1, 0],
        [0, 0, 0, 0],
    ]

    toad_game = ConwayGame(toad)

    yes_no = input('Play game on loop?\ny/n\n\nEnter `ctrl-c` to stop.\n\n')
    if yes_no.lower() == 'y':
        try:
            os.system('clear')
            toad_game.play()
        except KeyboardInterrupt:
            print('\nGame stopped.')


if __name__ == '__main__':
    main()
