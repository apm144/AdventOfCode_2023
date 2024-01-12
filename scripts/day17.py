import copy
import numpy as np
import itertools

# Read in data, new item for each line
f = open(r'..\inputs\input_day17.txt')
lines = f.readlines()
f.close()
lines = [i.strip() for i in lines]

test_1 = [
    '2413432311323',
    '3215453535623',
    '3255245654254',
    '3446585845452',
    '4546657867536',
    '1438598798454',
    '4457876987766',
    '3637877979653',
    '4654967986887',
    '4564679986453',
    '1224686865563',
    '2546548887735',
    '4322674655533',
]
test_answer_1 = 102

# Sample code from https://www.redblobgames.com/pathfinding/a-star/
# Copyright 2014 Red Blob Games <redblobgames@gmail.com>
#
# Feel free to use this code in your own projects, including commercial projects
# License: Apache v2.0 <http://www.apache.org/licenses/LICENSE-2.0.html>

# from __future__ import annotations
# some of these types are deprecated: https://www.python.org/dev/peps/pep-0585/
from typing import Protocol, Iterator, Tuple, TypeVar, Optional
T = TypeVar('T')

Location = TypeVar('Location')
class Graph(Protocol):
    def neighbors(self, id: Location) -> list[Location]: pass


def solve_day_part_1(data):

    data_grid = []
    for row in data:
        data_grid.append(np.array([int(i) for i in row]))
    data_grid = np.array(data_grid)

    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current


    init_seq = data[0].split(',')
    # Loop over the input rows

    seq_results = []
    for seq in init_seq:
        curr_val = 0
        for character in seq:
            curr_val += ord(character)
            curr_val *= 17
            curr_val = curr_val % 256
        seq_results.append(curr_val)

    print('Sum of initialization sequence, ', sum(seq_results))
    return sum(seq_results)


def solve_day_part_2(data):

    # Loop over the input rows
    grid_north = []
    rock_coordinates = []
    for row_id, row in enumerate(data):
        cube_rock_row = []
        for col_id, char in enumerate(row):
            # If character is a 'O' (rolling rock), save the coordinates
            if char == 'O':
                cube_rock_row.append(0)
                rock_coordinates.append([row_id, col_id])
            # If character is '#' (cube rock), set grid as 1
            elif char == '#':
                cube_rock_row.append(1)
            else:
                cube_rock_row.append(0)
        grid_north.append(cube_rock_row)

    return True

output_test_1 = solve_day_part_1(test_1)
# print('Output equal to test_1 output for part 1, ', output_test_1 == test_answer_1)
# output = solve_day_part_1(lines)
# output_test_2 = solve_day_part_2(test_1)
# print('Output equal to test_1 output for part 2, ', output_test_2 == test_answer_2)
# output_2 = solve_day_part_2(lines)
