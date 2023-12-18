import numpy as np
import os
import re

# Read in data, new item for each line
f = open(r'..\inputs\input_day5.txt')
lines = f.readlines()
f.close()
lines = [i.strip() for i in lines]

f = open(r'..\inputs\input_day5_test.txt')
test = f.readlines()
f.close()
test = [i.strip() for i in test]

test_answer = 35
test_answer_2 = 46


def get_mapping(data):
    identifier = ''
    seeds_location = []
    mapping = {}

    for i, row in enumerate(data):
        if 'seeds:' in row:
            seeds_location = data[0].split(':')[1].split()
            seeds_location = [int(i) for i in seeds_location]
        elif row.strip() == '':
            continue
        elif 'map:' in row:
            identifier = row
            mapping[identifier] = []
        else:
            numbers = row.split()
            numbers = [int(i) for i in numbers]
            mapping[identifier].append(numbers)
    return seeds_location, mapping

def solve_day_part_1(data):
    seeds_location, mapping = get_mapping(data)

    seeds_location_1 = list(range(seeds_location[0], seeds_location[0] + seeds_location[1]))
    seeds_location_2 = list(range(seeds_location[2], seeds_location[2] + seeds_location[3]))
    seeds_location = seeds_location_1 + seeds_location_2

    id_order = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:',
                'water-to-light map:', 'light-to-temperature map:', 'temperature-to-humidity map:',
                'humidity-to-location map:']
    final_location = []
    for val in seeds_location:
        # print(val)
        for identifier in id_order:
            for numbers in mapping[identifier]:
                if numbers[1] <= val and val <= numbers[1] + numbers[2] - 1:
                    val = numbers[0] + (val - numbers[1])
                    break
            # print(identifier, val)
            if identifier == id_order[-1]:
                final_location.append(val)

    print('Lowest location number, ', min(final_location))

    return min(final_location), final_location


def solve_day_part_2(data):
    seeds_location, mapping = get_mapping(data)

    seeds_location = [[i, j] for i, j in zip(seeds_location[::2], seeds_location[1::2])]

    for identifier in mapping.keys():
        mapping[identifier] = sorted(mapping[identifier], key=lambda x: x[1])

    id_order = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:',
                'water-to-light map:', 'light-to-temperature map:', 'temperature-to-humidity map:',
                'humidity-to-location map:']

    range_list = seeds_location[0]
    min_val = range_list[0]
    max_val = range_list[0] + range_list[1] - 1
    identifier = id_order[0]
    start_i = 0
    end_i = 0
    new_ranges = []
    for i, numbers in enumerate(mapping[identifier]):

        if numbers[1] <= min_val and min_val <= numbers[1] + numbers[2] - 1:
            new_ranges.append([min_val, min(max_val, numbers[1] + numbers[2] - 1), numbers[0]])
            print('ere')  #
        if numbers[1] <= max_val and max_val <= numbers[1] + numbers[2] - 1:
            new_ranges.append([max(min_val, numbers[1]), max_val, numbers[0]])
            print('here')

    final_location = []
    for val in seeds_location:
        # print(val)
        for identifier in id_order:
            for numbers in mapping[identifier]:
                if numbers[1] <= val and val <= numbers[1] + numbers[2] - 1:
                    val = numbers[0] + (val - numbers[1])
                    break
            # print(identifier, val)
            if identifier == id_order[-1]:
                final_location.append(val)

    print('Lowest location number, ', min(final_location))

    return min(final_location)




output_test, final_location = solve_day_part_1(test)
# print('Output equal to test output for part 1, ', output_test == test_answer)
# output = solve_day_part_1(lines)
output_test_2 = solve_day_part_2(test)
print('Output equal to test output for part 2, ', output_test_2 == test_answer_2)
# output_2 = solve_day_part_2(lines)

