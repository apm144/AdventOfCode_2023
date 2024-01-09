import copy
import numpy as np
import itertools

# Read in data, new item for each line
f = open(r'..\inputs\input_day15.txt')
lines = f.readlines()
f.close()
lines = [i.strip() for i in lines]

test_1 = [
    'HASH',
]
test_2 = [
    'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
]
test_answer_1 = 52
test_answer_2 = 1320
test_answer_3 = 145


def solve_day_part_1(data):

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
print('Output equal to test_1 output for part 1, ', output_test_1 == test_answer_1)
output_test_2 = solve_day_part_1(test_2)
print('Output equal to test_1 output for part 1, ', output_test_2 == test_answer_2)
output = solve_day_part_1(lines)
# output_test_2 = solve_day_part_2(test_1)
# print('Output equal to test_1 output for part 2, ', output_test_2 == test_answer_2)
# output_2 = solve_day_part_2(lines)
