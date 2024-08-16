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

    # '????#??##.????? 1,5,2',
    # '..#???.??.. 4,1',
    # '??.??????? 1,4,1',
    # '#??.????#??. 2,1,2,1',
    # '?#????##..#????? 8,1,1,1',
    # '???????#??#.??????? 3,2,2,1,2',
]
test_answer_1 = 21
test_answer_2 = 525152


# Method for solving by expanding the grid by 1
def solve_day_part_1(data):

    # Loop over the input rows
    row_data = []
    counters = []
    for row in data:
        row_split = row.split()
        string_data = [i for i in row_split[0]]
        orig_string_data = string_data.copy()
        number_data = [int(i) for i in row_split[1].split(',')]
        unknown_indices = [i for i, j in enumerate(string_data) if j == '?']
        combos = list(itertools.product([0, 1], repeat=len(unknown_indices)))
        counter = 0
        for combo in combos:
            string_data = orig_string_data.copy()
            for idx, sym_type in zip(unknown_indices, combo):
                string_data[idx] = '.' if sym_type == 0 else '#'
            string_test = ''.join(string_data).replace('.', ' ').split()
            if len(string_test) == len(number_data):
                if all([len(string_test[i]) == number_data[i] for i in range(len(string_test))]):
                    counter += 1
        counters.append(counter)

    # Return sum of shortest paths
    print('Sum of possible arrangements, ', sum(counters))
    return sum(counters)


def solve_day_part_2(data):

    # Loop over the input rows
    row_data = []
    counters = []
    for row in data:
        row_split = row.split()
        string_data = [i for i in row_split[0]]
        orig_string_data = string_data.copy()
        number_data = [int(i) for i in row_split[1].split(',')]
        unknown_indices = [i for i, j in enumerate(string_data) if j == '?']
        pound_indices = [i for i, j in enumerate(string_data) if j == '#']
        num_new_pounds_needed = sum(number_data) - len(pound_indices)
        combos = list(itertools.combinations(unknown_indices, num_new_pounds_needed))

        # combos = list(itertools.product([0, 1], repeat=len(unknown_indices)))
        counter = 0
        for combo in combos:
            string_data = orig_string_data.copy()
            for idx in unknown_indices:
                if idx in combo:
                    string_data[idx] = '#'
                else:
                    string_data[idx] = '.'
            string_test = ''.join(string_data).replace('.', ' ').split()
            if len(string_test) == len(number_data):
                if all([len(string_test[i]) == number_data[i] for i in range(len(string_test))]):
                    counter += 1
        counters.append(counter)

    # Return sum of shortest paths
    print('Sum of possible arrangements, ', sum(counters))
    return sum(counters)


def solve_day_part_3(data):

    # Loop over the input rows
    row_data = []
    counters = []
    for row in data:
        row_split = row.split()
        string_data = [i for i in row_split[0]]
        # string_data = string_data + ['?'] + string_data + ['?'] + string_data + ['?'] + string_data + ['?'] +string_data
        orig_string_data = string_data.copy()
        # number_data = [int(i) for i in row_split[1].split(',')] * 5
        number_data = [int(i) for i in row_split[1].split(',')]
        number_data_orig = number_data.copy()


        # combos = list(itertools.product([0, 1], repeat=len(unknown_indices)))
        total_counter = 0
        count_track = []
        # for i, orig_string_data_loop in enumerate([orig_string_data + ['?'] + orig_string_data + ['?'] + orig_string_data,
        #                                            orig_string_data + ['?'] + orig_string_data + ['?'] + orig_string_data]):
        # for i, orig_string_data_loop in enumerate([orig_string_data + ['?'],
        #                                            ['?'] + orig_string_data + ['?'],
        #                                            ['?'] + orig_string_data,
        #                                            orig_string_data + ['?'] + orig_string_data]):
        # for i, orig_string_data_loop in enumerate([['?'] + orig_string_data + ['?']]):
        orig_string_data_loop = ['?'] + orig_string_data + ['?']
        # number_data = number_data_orig + number_data_orig if i == 3 else number_data_orig.copy()
        # number_data = number_data_orig + number_data_orig + number_data_orig
        unknown_indices = [i for i, j in enumerate(orig_string_data_loop) if j == '?']
        pound_indices = [i for i, j in enumerate(orig_string_data_loop) if j == '#']
        num_new_pounds_needed = sum(number_data) - len(pound_indices)
        combos = list(itertools.combinations(unknown_indices, num_new_pounds_needed))
        counter = 0
        good_combos = []
        for combo in combos:
            string_data = orig_string_data_loop.copy()
            for idx in unknown_indices:
                if idx in combo:
                    string_data[idx] = '#'
                else:
                    string_data[idx] = '.'
            string_test = ''.join(string_data).replace('.', ' ').split()
            if len(string_test) == len(number_data):
                if all([len(string_test[i]) == number_data[i] for i in range(len(string_test))]):
                    counter += 1
                    good_combos.append(combo)
        count_track.append(counter)
        # if i == 0:
        #     total_counter = counter
        # elif i == 1:
        #     total_counter *= counter * counter * counter
        # else:
        #     total_counter *= counter

        leading_valid = 0
        mid_valid = 0
        ending_valid = 0

        # new_string = orig_string_data + ['?'] + orig_string_data + ['?']
        # unknown_indices = [i for i, j in enumerate(new_string) if j == '?']
        # new_numbers = number_data + number_data
        # for combo in good_combos:
        #     if combo[0] == 0:
        #         continue
        #     combo = tuple([i - 1 for i in combo])
        #     for combo2 in good_combos:
        #         combo2 = tuple([i + len(orig_string_data) for i in combo2])
        #         for idx in unknown_indices:
        #             if idx in combo + combo2:
        #                 new_string[idx] = '#'
        #             else:
        #                 new_string[idx] = '.'
        #         string_test = ''.join(new_string).replace('.', ' ').split()
        #         if len(string_test) == len(new_numbers):
        #             if all([len(string_test[i]) == new_numbers[i] for i in range(len(string_test))]):
        #                 leading_valid += 1
        #
        # new_string = ['?'] + orig_string_data + ['?'] + orig_string_data
        # unknown_indices = [i for i, j in enumerate(new_string) if j == '?']
        # new_numbers = number_data + number_data
        # for combo in good_combos:
        #     if combo[-1] == len(orig_string_data) + 1:
        #         continue
        #     combo = tuple([i + len(orig_string_data) + 1 for i in combo])
        #     for combo2 in good_combos:
        #         # combo2 = tuple([i + len(orig_string_data) for i in combo2])
        #         for idx in unknown_indices:
        #             if idx in combo + combo2:
        #                 new_string[idx] = '#'
        #             else:
        #                 new_string[idx] = '.'
        #         string_test = ''.join(new_string).replace('.', ' ').split()
        #         if len(string_test) == len(new_numbers):
        #             if all([len(string_test[i]) == new_numbers[i] for i in range(len(string_test))]):
        #                 ending_valid += 1



        valid_k = []
        valid_j = []
        new_string = orig_string_data + ['?'] + orig_string_data
        unknown_indices = [i for i, j in enumerate(new_string) if j == '?']
        new_numbers = number_data + number_data
        for k, combo in enumerate(good_combos):
            if len(combo) == 0:
                valid_k = [0]
                valid_j = [0]
                break
            if combo[0] == 0:
                continue
            combo = tuple([i - 1 for i in combo])
            for j, combo2 in enumerate(good_combos):
                if combo2[-1] == len(orig_string_data) + 1:
                    continue
                combo2 = tuple([i + len(orig_string_data) for i in combo2])
                for idx in unknown_indices:
                    if idx in combo + combo2:
                        new_string[idx] = '#'
                    else:
                        new_string[idx] = '.'
                string_test = ''.join(new_string).replace('.', ' ').split()
                if len(string_test) == len(new_numbers):
                    if all([len(string_test[i]) == new_numbers[i] for i in range(len(string_test))]):
                        valid_k.append(k)
                        valid_j.append(j)

        total_counter = len(np.unique(valid_k)) * len(np.unique(valid_j)) * max([len(np.unique(valid_k)),
                                                                                 len(np.unique(valid_j))]) ** 3

        # print(len(np.unique(valid_k)) * len(np.unique(valid_j)) * max([len(np.unique(valid_k)), len(np.unique(valid_j))]) ** 3)

        # if count_track[0] * count_track[2] == count_track[3]:
        #     total_counter = count_track[0] * count_track[2] * count_track[1] ** 3
        # else:
        #     print(row, count_track)

        counters.append(total_counter)

        # string_data = orig_string_data.copy()
        # new_string = string_data + ['?'] + string_data + ['?'] + string_data + ['?'] + string_data + ['?'] + string_data
        # new_number_data = number_data * 5



    # Return sum of shortest paths
    print('Sum of possible arrangements, ', sum(counters))
    return sum(counters)


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


# output_test = solve_day_part_1(test_1)
# print('Output equal to test_1 output for part 1, ', output_test == test_answer_1)
# output = solve_day_part_1(lines)
# output_test = solve_day_part_2(test_1)
# print('Output equal to test_1 output for part 1, ', output_test == test_answer_1)
# output = solve_day_part_2(lines)
output_test_2 = solve_day_part_3(test_1)
print('Output equal to test_1 output for part 1, ', output_test_2 == test_answer_2)
output_test_2 = solve_day_part_3(lines)
# too low - 753032410026
# output_test_1 = solve_day_part_2(test_1, 2)
# print('Output equal to test_1 output for part 1, ', output_test_1 == test_answer_1)
# output_test_2 = solve_day_part_2(test_1, 10)
# print('Output equal to test_2 output for part 2, ', output_test_2 == test_answer_2)
# output_test_3 = solve_day_part_2(test_1, 100)
# print('Output equal to test_3 output for part 2, ', output_test_3 == test_answer_3)
# output_2 = solve_day_part_2(lines, 1000000)