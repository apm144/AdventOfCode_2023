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


# Function the looks for reflection and returns number of rows above reflection
# Optional Boolean argument 'mirror' used to control whether looking for true reflection (part 1)
# or a reflection that is off by one character (part 2).
def get_pattern_sum(pattern, mirror=True):
    # Loop over each row but the last one
    for row_id_above in range(len(pattern) - 1):
        # Create the pattern above in reverse from original orientation because it will be compared to pattern below
        pattern_above = pattern[0: row_id_above + 1][::-1]
        # Create the pattern below
        pattern_below = pattern[row_id_above + 1:]
        # Look for minimum length between the two - will truncate larger pattern.
        min_id = min(len(pattern_above), len(pattern_below))
        pattern_above = pattern_above[0: min_id]
        pattern_below = pattern_below[0: min_id]
        # If looking for true reflection (part 1)
        if mirror:
            # If two patterns match, return number of rows above
            if pattern_above == pattern_below:
                return row_id_above + 1
        # If looking for patterns that are one off (part 2)
        else:
            num_diff = 0
            # Loop over each row in pattern_above and pattern_below, and sum up how many times they are different
            for row_pattern_id in range(len(pattern_above)):
                num_diff += sum([pattern_above[row_pattern_id][i] != pattern_below[row_pattern_id][i] for i in
                                 range(len(pattern_above[row_pattern_id]))])
            # If they are different by only one value, return number of rows above
            if num_diff == 1:
                return row_id_above + 1
    return 0


# Method for solving by expanding the grid by 1
def solve_day(data, mirror=True):

    # Loop over the input rows
    round_rock_grid = []
    cube_rock_grid = []
    for row in data:
        round_rock_row = []
        cube_rock_row = []
        for i, char in enumerate(row):
            if char == 'O':
                round_rock_row.append(1)
                cube_rock_row.append(0)
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

    new_round_grid = np.zeros(round_rock_grid.shape).astype(int)
    for row in range(round_rock_grid.shape[0]):
        for col in range(round_rock_grid.shape[1]):
            if round_rock_grid[row, col] == 1:
                # If in first row, stays there
                if row == 0:
                    new_round_grid[row, col] = 1
                # No cube between rock and end
                if sum(cube_rock_grid[0:row, col]) == 0:
                    new_round_grid[sum(new_round_grid[0:row, col]), col] = 1
                else:
                    cube_row = [i for i in range(len(cube_rock_grid[0:row, col])) if cube_rock_grid[i, col] == 1][-1]
                    new_round_grid[sum(new_round_grid[cube_row:row, col]) + cube_row + 1, col] = 1

    total_load = sum(np.sum(new_round_grid, axis=1) * np.arange(1, new_round_grid.shape[0] + 1)[::-1])

    print('Total load, ', total_load)
    return total_load


# output_test = solve_day(test_1)
# print('Output equal to test_1 output for part 1, ', output_test == test_answer_1)
output = solve_day(lines)
# output_test_2 = solve_day(test_1, mirror=False)
# print('Output equal to test_1 output for part 2, ', output_test_2 == test_answer_2)
# output_2 = solve_day(lines, mirror=False)
