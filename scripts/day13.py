import numpy as np
import itertools

# Read in data, new item for each line
f = open(r'..\inputs\input_day13.txt')
lines = f.readlines()
f.close()
lines = [i.strip() for i in lines]

test_1 = [
    '#.##..##.',
    '..#.##.#.',
    '##......#',
    '##......#',
    '..#.##.#.',
    '..##..##.',
    '#.#.##.#.',
    '',
    '#...##..#',
    '#....#..#',
    '..##..###',
    '#####.##.',
    '#####.##.',
    '..##..###',
    '#....#..#',
]
test_answer_1 = 405
test_answer_2 = 400


# Method for solving by expanding the grid by 1
def solve_day_part_1(data):

    # Loop over the input rows
    pattern_data = []
    grid_data = []
    for row in data:
        if row == '':
            pattern_data.append(grid_data)
            grid_data = []
            continue
        grid_data.append(row)
    pattern_data.append(grid_data)

    row_sum = 0
    col_sum = 0
    for pattern in pattern_data:
        for row_id_above in range(len(pattern) - 1):
            pattern_above = pattern[0: row_id_above + 1][::-1]
            pattern_below = pattern[row_id_above + 1:]
            min_id = min(len(pattern_above), len(pattern_below))
            pattern_above = pattern_above[0: min_id]
            pattern_below = pattern_below[0: min_id]
            if pattern_above == pattern_below:
                row_sum += row_id_above + 1
                break

        pattern_t = []
        for i in range(len(pattern[0])):
            row = []
            for sublist in pattern:
                row.append(sublist[i])
            pattern_t.append(''.join(row))
        for col_id_above in range(len(pattern_t) - 1):
            pattern_above = pattern_t[0: col_id_above + 1][::-1]
            pattern_below = pattern_t[col_id_above + 1:]
            min_id = min(len(pattern_above), len(pattern_below))
            pattern_above = pattern_above[0: min_id]
            pattern_below = pattern_below[0: min_id]
            if pattern_above == pattern_below:
                col_sum += col_id_above + 1
                break

    print('Summarized notes, ', col_sum + (100 * row_sum))

    return col_sum + (100 * row_sum)


# # Method for solving by expanding by any arbitrary amount, default is 2 (expansion by 1)
def solve_day_part_2(data):

    # Loop over the input rows
    pattern_data = []
    grid_data = []
    for row in data:
        if row == '':
            pattern_data.append(grid_data)
            grid_data = []
            continue
        grid_data.append(row)
    pattern_data.append(grid_data)

    row_sum = 0
    col_sum = 0
    for pattern in pattern_data:
        for row_id_above in range(len(pattern) - 1):
            pattern_above = pattern[0: row_id_above + 1][::-1]
            pattern_below = pattern[row_id_above + 1:]
            min_id = min(len(pattern_above), len(pattern_below))
            pattern_above = pattern_above[0: min_id]
            pattern_below = pattern_below[0: min_id]
            num_diff = 0
            for row_pattern_id in range(len(pattern_above)):
                num_diff += sum([pattern_above[row_pattern_id][i] != pattern_below[row_pattern_id][i] for i in
                                 range(len(pattern_above[row_pattern_id]))])
            if num_diff == 1:
                row_sum += row_id_above + 1
                break
            # if pattern_above == pattern_below:
            #     row_sum += row_id_above + 1
            #     break

        pattern_t = []
        for i in range(len(pattern[0])):
            row = []
            for sublist in pattern:
                row.append(sublist[i])
            pattern_t.append(''.join(row))
        for col_id_above in range(len(pattern_t) - 1):
            pattern_above = pattern_t[0: col_id_above + 1][::-1]
            pattern_below = pattern_t[col_id_above + 1:]
            min_id = min(len(pattern_above), len(pattern_below))
            pattern_above = pattern_above[0: min_id]
            pattern_below = pattern_below[0: min_id]
            num_diff = 0
            for row_pattern_id in range(len(pattern_above)):
                num_diff += sum([pattern_above[row_pattern_id][i] != pattern_below[row_pattern_id][i] for i in
                                 range(len(pattern_above[row_pattern_id]))])
            if num_diff == 1:
                col_sum += col_id_above + 1
                break
            # if pattern_above == pattern_below:
            #     col_sum += col_id_above + 1
            #     break

    print('Summarized notes, ', col_sum + (100 * row_sum))

    return col_sum + (100 * row_sum)


output_test = solve_day_part_1(test_1)
print('Output equal to test_1 output for part 1, ', output_test == test_answer_1)
output = solve_day_part_1(lines)
output_test_2 = solve_day_part_2(test_1)
print('Output equal to test_1 output for part 2, ', output_test_2 == test_answer_2)
output_2 = solve_day_part_2(lines)
# print('Output equal to test_2 output for part 2, ', output_test_2 == test_answer_2)
# output_test_3 = solve_day_part_2(test_1, 100)
# print('Output equal to test_3 output for part 2, ', output_test_3 == test_answer_3)
# output_2 = solve_day_part_2(lines, 1000000)
