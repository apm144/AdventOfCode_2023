import numpy as np
import itertools

# Read in data, new item for each line
f = open(r'..\inputs\input_day12.txt')
lines = f.readlines()
f.close()
lines = [i.strip() for i in lines]

test_1 = [
    '???.### 1,1,3',
    '.??..??...?##. 1,1,3',
    '?#?#?#?#?#?#?#? 1,3,1,6',
    '????.#...#... 4,1,1',
    '????.######..#####. 1,6,5',
    '?###???????? 3,2,1',
]
test_answer_1 = 21


# Method for solving by expanding the grid by 1
def solve_day_part_1(data):

    # Loop over the input rows
    row_data = []
    for row in data:
        row_split = row.split()
        string_data = [i for i in row_split[0]]
        orig_string_data = string_data.copy()
        number_data = [int(i) for i in row_split[1].split(',')]
        unknown_indices = [i for i, j in enumerate(string_data) if j == '?']
        combos = list(itertools.product([0, 1], repeat=len(unknown_indices)))
        for combo in combos:
            string_data = orig_string_data.copy()
            for idx, sym_type in zip(unknown_indices, combo):
                string_data[idx] = '.' if sym_type == 0 else '#'
            string_test = ''.join(string_data).replace('.', ' ').split()
            print('here')
        print('here')

    return True


# # Method for solving by expanding by any arbitrary amount, default is 2 (expansion by 1)
# def solve_day_part_2(data, expansion=2):
#
#     # Loop over the input rows and make galaxies ('#') 1s.
#     grid = []
#     for row in data:
#         grid.append([1 if i == '#' else 0 for i in row])
#
#     # Get the index of the row of no galaxies
#     row_expanse = [i for i, row in enumerate(grid) if sum(row) == 0]
#     # Transpose the grid and get the index of the column of no galaxies
#     grid = np.array(grid).T.tolist()
#     col_expanse = [i for i, row in enumerate(grid) if sum(row) == 0]
#     # Transpose back to original orientation
#     grid = np.array(grid).T.tolist()
#
#     # Get original coordinates of galaxies (where = 1)
#     coordinates = []
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == 1:
#                 coordinates.append([i, j])
#
#     # Getting new coordinates after expansion
#     # Loop over each coordinate
#     for i, coor in enumerate(coordinates):
#         new_coor = coor.copy()
#         # If the coordinate is greater than index of galaxy expansion, increase
#         # coordinate by expansion amount (less 1).  This happens for each index the
#         # original coordinate is greater than, so expansion accumulates.
#         for k in row_expanse:
#             if coor[0] > k:
#                 new_coor[0] += expansion - 1
#         # Do same for columns
#         for k in col_expanse:
#             if coor[1] > k:
#                 new_coor[1] += expansion - 1
#         coordinates[i] = new_coor.copy()
#
#     # Get the shortest path length between galaxies.  Shortest length is
#     # Manhattan distance abs(diffx) + abs(diffy)
#     path_length = []
#     # Loop over each coordinate
#     for i in range(len(coordinates)):
#         # Loop over each remaining coordinate
#         for j in range(i + 1, len(coordinates)):
#             path_length.append(abs(coordinates[i][0] - coordinates[j][0]) +
#                                abs(coordinates[i][1] - coordinates[j][1]))
#
#     print('Sum of shortest paths, ', sum(path_length))
#     # Return sum of shortest paths
#     return sum(path_length)


output_test = solve_day_part_1(test_1)
# print('Output equal to test_1 output for part 1, ', output_test == test_answer_1)
# output = solve_day_part_1(lines)
# output_test_1 = solve_day_part_2(test_1, 2)
# print('Output equal to test_1 output for part 1, ', output_test_1 == test_answer_1)
# output_test_2 = solve_day_part_2(test_1, 10)
# print('Output equal to test_2 output for part 2, ', output_test_2 == test_answer_2)
# output_test_3 = solve_day_part_2(test_1, 100)
# print('Output equal to test_3 output for part 2, ', output_test_3 == test_answer_3)
# output_2 = solve_day_part_2(lines, 1000000)
