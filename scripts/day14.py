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


# Method for solving by expanding the grid by 1
def solve_day(data, mirror=True):

    # Loop over the input rows
    round_rock_grid = []
    cube_rock_grid = []
    rock_coordinates = []
    for row_id, row in enumerate(data):
        round_rock_row = []
        cube_rock_row = []
        for col_id, char in enumerate(row):
            if char == 'O':
                round_rock_row.append(1)
                cube_rock_row.append(0)
                rock_coordinates.append([row_id, col_id])
            elif char == '#':
                round_rock_row.append(0)
                cube_rock_row.append(1)
            else:
                round_rock_row.append(0)
                cube_rock_row.append(0)
        round_rock_grid.append(round_rock_row)
        cube_rock_grid.append(cube_rock_row)

    round_rock_grid = np.array(round_rock_grid)
    cube_rock_grid = np.array(cube_rock_grid)

    # new_round_grid = np.zeros(round_rock_grid.shape).astype(int)
    # new_coordinates = []
    loads = list(range(1, len(cube_rock_grid) + 1))[::-1]
    load_map = {i: j for i, j in enumerate(loads)}

    new_coordinates = get_new_coordinates(rock_coordinates, cube_rock_grid)
    # for row_id, col_id in rock_coordinates:
    #     # No cube between rock and end
    #     if sum(cube_rock_grid[0:row_id, col_id]) == 0:
    #         new_row_id = sum(new_round_grid[0:row_id, col_id])
    #     else:
    #         cube_row = [i for i in range(len(cube_rock_grid[0:row_id, col_id]))
    #                     if cube_rock_grid[i, col_id] == 1][-1]
    #         new_row_id = sum(new_round_grid[cube_row:row_id, col_id]) + cube_row + 1
    #     new_round_grid[new_row_id, col_id] = 1
    #     new_coordinates.append([new_row_id, col_id])

    total_load = sum([load_map[i[0]] for i in new_coordinates])
    # total_load = sum(np.sum(new_round_grid, axis=1) * np.arange(1, new_round_grid.shape[0] + 1)[::-1])

    print('Total load, ', total_load)
    return total_load


output_test = solve_day(test_1)
print('Output equal to test_1 output for part 1, ', output_test == test_answer_1)
output = solve_day(lines)
# output_test_2 = solve_day(test_1, mirror=False)
# print('Output equal to test_1 output for part 2, ', output_test_2 == test_answer_2)
# output_2 = solve_day(lines, mirror=False)
