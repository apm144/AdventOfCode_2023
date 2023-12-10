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


def get_halos(data):
    # Get number and halo coordinates
    number_list = []
    coordinate_list = []
    coordinate_list_with_num = []
    # Loop over each row of input
    for row_id, row in enumerate(data):
        # Find all the numbers in the row
        numbers = re.findall(r'\d+', row)
        # There could be duplicates, so only selecting the unique ones,
        # duplicates will be handled below
        numbers = list(np.unique(numbers))
        # number_patterns = re.findall(r'[^0-9]\d+[^0-9]|\d+[^0-9]|[^0-9]\d+', row)  # non-number of both sides of number
        # Loop over each number found
        for num in numbers:
            # coordinates = []
            # Find the starting index for the current number
            col_id = [index.start() for index in re.finditer(num, row)]
            # There is a chance that the number is found multiple times.
            # This could happen if 1. the number is in the row twice or 2. if the current
            # number is a subset of another number
            # If 1., we want to include that number and halo, but not for 2.
            # Check if more than one index
            if len(col_id) > 1:
                valid_col_id = []
                # Loop over each index - will check for validity
                # Possible for multiple indices to be valid which is when a number
                # is repeated in a row
                for id in col_id:
                    valid_bool = True
                    # Check if preceding value is a number or not.
                    # If it is, this is a subset and is not valid
                    if id != 0 and row[id - 1].isnumeric():
                        valid_bool = False
                    # Check if succeding value is a number or not.
                    # If it is, this is a subset and is not valid
                    if id + len(num) != len(row) and row[id + len(num)].isnumeric():
                        valid_bool = False
                    # If validation does not fail, add this index as a valid index
                    if valid_bool:
                        valid_col_id.append(id)
            else:
                valid_col_id = col_id.copy()

            # Loop over each valid index to identify halo
            for col_id in valid_col_id:
                coordinates = []
                # Set starting column, which is 1 less than index unless index is first column
                start_col = col_id if col_id == 0 else col_id - 1
                # Set ending column, which is 1 more than index unless index is last column
                end_col = col_id + len(num) - 1 if col_id + len(num) == len(row) else col_id + len(num)
                # Set starting row, which is 1 less than index unless index is first row
                start_row = row_id if row_id == 0 else row_id - 1
                # Set ending row, which is 1 more than index unless index is last row
                end_row = row_id if row_id == len(data) - 1 else row_id + 1
                # Get slice of data that includes halo and number
                sub_data = [data[i][start_col:end_col + 1] for i in range(start_row, end_row + 1)]

                # Get halo part for row ABOVE index, unless current row is first row
                if row_id != 0:
                    coordinates.extend([(row_id - 1, i) for i in range(start_col, end_col + 1)])
                # Get halo part for row BELOW index, unless current row is last row
                if row_id != len(data) - 1:
                    coordinates.extend([(row_id + 1, i) for i in range(start_col, end_col + 1)])
                # Get halo part for column to left of index, unless current column is first column
                if col_id != 0:
                    coordinates.append((row_id, col_id - 1))
                # Get halo part for column to right of index, unless current column is last column
                if col_id + len(num) != len(row):
                    coordinates.append((row_id, col_id + len(num)))
                number_list.append(int(num))
                coordinate_list.append(coordinates.copy())
                coordinate_list_with_num.append(sub_data.copy())

    return number_list, coordinate_list, coordinate_list_with_num


def get_symbol_data(data):
    # Get coordinates for symbols
    sym_coordinates = []
    gear_coordinates = []
    # Loop over each row
    for row_id, row in enumerate(data):
        # Symbol is if an item is not a number or is not a '.'
        # Extend list of coordinates for those items that are a symbol in this row
        # Extend list of gear coordinates for those items that have a symbol of '*'
        sym_coordinates.extend([(row_id, i) for i, j in enumerate(row) if (not j.isnumeric() and j != '.')])
        gear_coordinates.extend([(row_id, i) for i, j in enumerate(row) if j == '*'])
    return sym_coordinates, gear_coordinates


def solve_day(data):
    # Get halo information around each number
    number_list, coordinate_list, coordinate_list_with_num = get_halos(data)
    # Get coordinates of all symbols and of gear symbols
    sym_coordinates, gear_coordinates = get_symbol_data(data)

    # Part 1
    # Check which parts are next to symbols
    # Loop over all halo coordinates and see in the list of symbol coordinates
    # If it is, add to list of part numbers
    part_numbers = []
    for part_num, halo in zip(number_list, coordinate_list):  # number_dict.items():
        for coordinate in halo:
            if coordinate in sym_coordinates:
                part_numbers.append(part_num)
                break

    # Part 2
    # Find which two parts are adjacent to gear
    # Loop over all gears and then all halo coordinates,
    # If within halo, add part number to gear part tracking
    # Then count the number of part numbers, if only 2 of them, add to list of
    # Gear ratio parts list
    gear_ratio_parts = []
    for gear_coor in gear_coordinates:
        part_nums = []
        for part_num, halo in zip(number_list, coordinate_list):
            for coordinate in halo:
                if coordinate == gear_coor:
                    part_nums.append(part_num)
        if len(part_nums) == 2:
            gear_ratio_parts.append(part_nums.copy())
        # else:
        #     print(gear_coor, part_nums)

    # Find total gear ratio
    # Loop over each pair of gear parts and sum up their products
    gear_ratio = 0
    for part_nums in gear_ratio_parts:
        gear_ratio += part_nums[0] * part_nums[1]

    # num_strings = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # part_numbers_2 = []
    # is_not_partnum = []
    # wtf = []
    # for part_num, subdata in zip(number_list, coordinate_list_with_num):  # number_dict.items():
    #     temp = []
    #     temp_2 = []
    #     for row in subdata:
    #         temp.extend([i in num_strings or i == '.' for i in row])
    #         if str(part_num) not in row:
    #             temp_2.extend([i in num_strings for i in row])
    #     is_not_partnum.append(all(temp))
    #     if any(temp_2):
    #         wtf.append(part_num)
    #     if not all(temp):
    #         # if part_num not in part_numbers_2:
    #         part_numbers_2.append(part_num)


    print('Sum of part numbers, ', sum(part_numbers))
    print('Sum of gear ratios, ', gear_ratio)
    # print('Sum of part numbers, ', sum(part_numbers_2))

    return sum(part_numbers), gear_ratio


output_test, gear_ratio_test = solve_day(test)
print('Output equal to test output, ', output_test == test_answer)
output, gear_ratio = solve_day(lines)

