import numpy as np
import os
import re

# Read in data, new item for each line
f = open(r'..\inputs\input_day3.txt')
lines = f.readlines()
f.close()
lines = [i.strip() for i in lines]

test = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..',
]
test_answer = 4361


def solve_day(data):

    # Get number and halo coordinates
    # number_dict = {}
    number_list = []
    coordinate_list = []
    number_list_2 = []
    subdata_list = []
    for row_id, row in enumerate(data):
        numbers = re.findall(r'\d+', row)
        numbers = list(np.unique(numbers))
        # number_patterns = re.findall(r'[^0-9]\d+[^0-9]|\d+[^0-9]|[^0-9]\d+', row)  # non-number of both sides of number
        for num in numbers:
            coordinates = []
            col_id = [index.start() for index in re.finditer(num, row)]
            if len(col_id) > 1:
                # print('here_bad')
                valid_col_id = []
                for id in col_id:
                    valid_bool = True
                    if id != 0 and row[id - 1].isnumeric():
                        valid_bool = False
                    if id + len(num) != len(row) and row[id + len(num)].isnumeric():
                        valid_bool = False
                    if valid_bool:
                        valid_col_id.append(id)
                if len(valid_col_id) > 1:
                    print('here_bad_2')
            else:
                valid_col_id = col_id.copy()

            # col_id = col_id[0]

            # if not num[0].isnumeric():
            #     col_id = col_id + 1
            #     num = num[1:]
            # num = num if num[-1].isnumeric() else num[0:-1]

            for col_id in valid_col_id:

                start_col = col_id if col_id == 0 else col_id - 1
                end_col = col_id + len(num) - 1 if col_id + len(num) == len(row) else col_id + len(num)
                start_row = row_id if row_id == 0 else row_id - 1
                end_row = row_id if row_id == len(data) - 1 else row_id + 1
                sub_data = [data[i][start_col:end_col + 1] for i in range(start_row, end_row + 1)]

                number_list_2.append(int(num))
                subdata_list.append(sub_data.copy())

                # print(row_id, num, [data[i][start_col:end_col + 1] for i in range(start_row, end_row + 1)])

                if row_id != 0:
                    coordinates.extend([(row_id - 1, i) for i in range(start_col, end_col + 1)])
                if row_id != len(data) - 1:
                    coordinates.extend([(row_id + 1, i) for i in range(start_col, end_col + 1)])
                if col_id != 0:
                    coordinates.append((row_id, col_id - 1))
                if col_id + len(num) != len(row):
                    coordinates.append((row_id, col_id + len(num)))
                # if num in number_dict.keys():
                #     print('here_badder')
                # number_dict[int(num)] = coordinates.copy()
                number_list.append(int(num))
                coordinate_list.append(coordinates.copy())

    # Get symbol coordinates
    sym_coordinates = []
    for row_id, row in enumerate(data):
        sym_coordinates.extend([(row_id, i) for i, j in enumerate(row) if (not j.isnumeric() and j != '.')])


    part_numbers = []
    for part_num, halo in zip(number_list, coordinate_list):  # number_dict.items():
        for coordinate in halo:
            if coordinate in sym_coordinates:
                part_numbers.append(part_num)
                break
    num_strings = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    part_numbers_2 = []
    is_not_partnum = []
    wtf = []
    for part_num, subdata in zip(number_list_2, subdata_list):  # number_dict.items():
        temp = []
        temp_2 = []
        for row in subdata:
            temp.extend([i in num_strings or i == '.' for i in row])
            if str(part_num) not in row:
                temp_2.extend([i in num_strings for i in row])
        is_not_partnum.append(all(temp))
        if any(temp_2):
            wtf.append(part_num)
        if not all(temp):
            # if part_num not in part_numbers_2:
            part_numbers_2.append(part_num)


    print('Sum of part numbers, ', sum(part_numbers))
    print('Sum of part numbers, ', sum(part_numbers_2))

    return sum(part_numbers_2)


output_test = solve_day(test)
print('Output equal to test output, ', output_test == test_answer)
output = solve_day(lines)

