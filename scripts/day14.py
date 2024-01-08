import copy

import numpy as np
import itertools

# Read in data, new item for each line
f = open(r'..\inputs\input_day14.txt')
lines = f.readlines()
f.close()
lines = [i.strip() for i in lines]

test_1 = [
    'O....#....',
    'O.OO#....#',
    '.....##...',
    'OO.#O....O',
    '.O.....O#.',
    'O.#..O.#.#',
    '..O..#O..O',
    '.......O..',
    '#....###..',
    '#OO..#....',
]
test_answer_1 = 136
test_answer_2 = 64


def get_new_coordinates(rock_coordinates, cube_rock_grid):
    new_round_grid = np.zeros(cube_rock_grid.shape).astype(int)
    new_coordinates = []

    for row_id, col_id in rock_coordinates:
        # No cube between rock and end
        if sum(cube_rock_grid[0:row_id, col_id]) == 0:
            new_row_id = sum(new_round_grid[0:row_id, col_id])
        else:
            cube_row = [i for i in range(len(cube_rock_grid[0:row_id, col_id]))
                        if cube_rock_grid[i, col_id] == 1][-1]
            new_row_id = sum(new_round_grid[cube_row:row_id, col_id]) + cube_row + 1
        new_round_grid[new_row_id, col_id] = 1
        new_coordinates.append([new_row_id, col_id])

    return new_coordinates


# 90 degree clockwise
def rotate_clockwise(coordinates, len_grid):
    new_coor = []
    for row_id_orig, col_id_orig in coordinates:
        new_coor.append([col_id_orig, len_grid - 1 - row_id_orig])
    return new_coor


def get_cycle_coordinates(coordinates, grids):
    for grid in grids:
        output_coor = get_new_coordinates(coordinates, grid)
        output_coor = rotate_clockwise(output_coor, len(grid))
        output_coor = sorted(output_coor)
        coordinates = copy.deepcopy(output_coor)
    return coordinates


def solve_day_part_1(data):

    # Loop over the input rows
    grid_north = []
    rock_coordinates = []
    for row_id, row in enumerate(data):
        cube_rock_row = []
        for col_id, char in enumerate(row):
            if char == 'O':
                cube_rock_row.append(0)
                rock_coordinates.append([row_id, col_id])
            elif char == '#':
                cube_rock_row.append(1)
            else:
                cube_rock_row.append(0)
        grid_north.append(cube_rock_row)

    grid_north = np.array(grid_north)

    loads = list(range(1, len(grid_north) + 1))[::-1]
    load_map = {i: j for i, j in enumerate(loads)}

    new_coordinates = get_new_coordinates(rock_coordinates, grid_north)

    total_load = sum([load_map[i[0]] for i in new_coordinates])

    print('Total load, ', total_load)
    return total_load


def solve_day_part_2(data, mirror=True):

    # Loop over the input rows
    # round_rock_grid = []
    grid_north = []
    rock_coordinates = []
    # cube_coordinates = []
    for row_id, row in enumerate(data):
        # round_rock_row = []
        cube_rock_row = []
        for col_id, char in enumerate(row):
            if char == 'O':
                # round_rock_row.append(1)
                cube_rock_row.append(0)
                rock_coordinates.append([row_id, col_id])
            elif char == '#':
                # round_rock_row.append(0)
                cube_rock_row.append(1)
                # cube_coordinates.append([row_id, col_id])
            else:
                # round_rock_row.append(0)
                cube_rock_row.append(0)
        # round_rock_grid.append(round_rock_row)
        grid_north.append(cube_rock_row)

    # round_rock_grid = np.array(round_rock_grid)
    grid_north = np.array(grid_north)
    grid_west = np.rot90(grid_north, -1)
    grid_south = np.rot90(grid_west, -1)
    grid_east = np.rot90(grid_south, -1)

    loads = list(range(1, len(grid_north) + 1))[::-1]
    load_map = {i: j for i, j in enumerate(loads)}

    orig_coor = copy.deepcopy(rock_coordinates)
    coor = copy.deepcopy(orig_coor)

    load_tracker = [0]

    for cycle in range(1, 100):
        coor = get_cycle_coordinates(coor, [grid_north, grid_west, grid_south, grid_east])
        print(cycle, sum([load_map[i[0]] for i in coor]))
        load_tracker.append(sum([load_map[i[0]] for i in coor]))

    total_load = sum([load_map[i[0]] for i in coor])

    print('Total load, ', total_load)
    return total_load


# output_test_1 = solve_day_part_1(test_1)
# print('Output equal to test_1 output for part 1, ', output_test_1 == test_answer_1)
# output = solve_day_part_1(lines)
output_test_2 = solve_day_part_2(test_1)
# print('Output equal to test_1 output for part 2, ', output_test_2 == test_answer_2)
# output_2 = solve_day(lines, mirror=False)
