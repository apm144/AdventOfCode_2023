import numpy as np
import os

# Read in data, new item for each line
f = open(r'..\inputs\input_day1.txt')
lines = f.readlines()
f.close()

test = [
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet',
]
test_answer = 142

test_2 = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
]
test_2_answer = 281


def solve_day_1_part_1(data):
    all_numbers = []
    result_numbers = []

    # The goal here is to find the index where number integers occur.
    # Then sort these indices and select the first and last to make a two digit number

    # Looping over each row of the input
    for row in data:
        id_dict = {}
        # Looping over each number string
        for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            index = 0
            # Use str.find() - will only find the first instance
            # Need to put in a while loop to find multiple instances
            # If str.find() does not find the string we are looking for,
            # it will return a -1, which will be the flag to break out of the while loop
            while index < len(row):
                index = row.find(num, index)
                if index == -1:
                    break
                id_dict[index] = num
                index += len(num)

        # Sorting dictionary by indices (keys)
        id_dict = dict(sorted(id_dict.items()))
        # Adding all the numbers found in the row of input to list
        all_numbers.append(list(id_dict.values()))
        # Selecting the first and last integers from values of sorted dictionary
        numbers = [list(id_dict.values())[0], list(id_dict.values())[-1]]
        # Creating 2 digit integer
        result_numbers.append(int(''.join(numbers)))

    print('Sum of all calibration values,', sum(result_numbers))
    return sum(result_numbers)


def solve_day_1_part_2(data):
    all_numbers = []
    result_numbers = []
    # Make dictionary of mapping for number word to number integer
    numbers_map = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                   'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    # The goal here is to find the index where number words AND number integers start.
    # Then sort these indices and select the first and last to make a two digit number

    # Looping over each row of the input
    for row in data:
        id_dict = {}
        # Looping over each key/value in numbers map dictionary
        for num_word, num in numbers_map.items():
            # Need to then loop over the word AND integer to find the index
            # The index (key) and the integer (value) will go in a dictionary (id_dict)
            for num_find, num_str in {num: num, num_word: num}.items():
                index = 0
                # Use str.find() - will only find the first instance
                # Need to put in a while loop to find multiple instances
                # If str.find() does not find the string we are looking for,
                # it will return a -1, which will be the flag to break out of the while loop
                while index < len(row):
                    index = row.find(num_find, index)
                    if index == -1:
                        break
                    id_dict[index] = num_str
                    index += len(num_find)

        # Sorting dictionary by indices (keys)
        id_dict = dict(sorted(id_dict.items()))
        # Adding all the numbers found in the row of input to list
        all_numbers.append(list(id_dict.values()))
        # Selecting the first and last integers from values of sorted dictionary
        numbers = [list(id_dict.values())[0], list(id_dict.values())[-1]]
        # Creating 2 digit integer
        result_numbers.append(int(''.join(numbers)))

    print('Sum of all calibration values,', sum(result_numbers))
    return sum(result_numbers)

output_test = solve_day_1_part_1(test)
print('Output equal to test output, ', output_test == test_answer)
output = solve_day_1_part_1(lines)
output_test_2 = solve_day_1_part_2(test_2)
print('Output equal to test_2 output, ', output_test_2 == test_2_answer)
output_2 = solve_day_1_part_2(lines)
