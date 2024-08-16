import numpy as np
import os
import re
import copy

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


# Parse input file to separate out initial seed locations and how the numbers
# map through the process
def get_mapping(data):
    identifier = ''
    seeds_location = []
    mapping = {}

    # Loop over each row of input file
    for i, row in enumerate(data):
        # If seed row, split by ':' then space and turn into integers
        if 'seeds:' in row:
            seeds_location = data[0].split(':')[1].split()
            seeds_location = [int(i) for i in seeds_location]
        # Skip blank lines
        elif row.strip() == '':
            continue
        # Using 'map' to identify label - set label as key for dictionary
        # Initialize empty list to populate with mapping data
        elif 'map:' in row:
            identifier = row
            mapping[identifier] = []
        # Fill dictionary with mapping data, separated integers by spaces
        else:
            numbers = row.split()
            numbers = [int(i) for i in numbers]
            mapping[identifier].append(numbers)
    # Return list of ints for initial seed locations and
    # dictionary of list of list of ints for mapping information
    return seeds_location, mapping


def solve_day_part_1(data):
    # The idea is to map each seed through the mapping process and identify the final
    # location of the seeds.  Will determine if seed is inside the range of mapping
    # and implement if it is.

    # Get mapping and seed information
    seeds_location, mapping = get_mapping(data)

    id_order = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:',
                'water-to-light map:', 'light-to-temperature map:', 'temperature-to-humidity map:',
                'humidity-to-location map:']
    final_location = []
    # Loop over each seed location
    for val in seeds_location:
        # Loop over each mapping step
        for identifier in id_order:
            # Loop over each line of mapping
            for numbers in mapping[identifier]:
                # If seed location is in the mapping range, implement the mapping
                # Then break out of the current loop because this step in the mapping is complete
                if numbers[1] <= val and val <= numbers[1] + numbers[2] - 1:
                    val = numbers[0] + (val - numbers[1])
                    break
        # Final value when all mapping steps are completed
        final_location.append(val)

    print('Lowest location number, ', min(final_location))
    # Return both the minimum of the final location and the list of seed locations
    return min(final_location), final_location


# For a given input range and step in the mapping, determine output range(s)
def get_new_ranges(init_range, mappings):
    # Minimum and maximum values of the input range (start and length)
    min_val = init_range[0]
    max_val = init_range[0] + init_range[1] - 1
    new_ranges = []
    # Loop through numbers of the mapping.  There are four possibilities.
    # If identified, portion that is inside the range is identified, and the
    # new mapped start will be identified (shift based on location relative to
    # start of mapping.
    for numbers in mappings:
        # Whole min/max range in number range
        if numbers[1] <= min_val and max_val <= numbers[1] + numbers[2] - 1:
            dif = min_val - numbers[1]
            new_ranges.append([min_val, max_val, numbers[0] + dif])
        # Whole number range in min/max range
        elif numbers[1] > min_val and max_val > numbers[1] + numbers[2] - 1:
            new_ranges.append([numbers[1], numbers[1] + numbers[2] - 1, numbers[0]])
        # Min_val inside number range, but max_val outside
        elif numbers[1] <= min_val <= numbers[1] + numbers[2] - 1:
            dif = min_val - numbers[1]
            new_ranges.append([min_val, numbers[1] + numbers[2] - 1, numbers[0] + dif])
        # Max_val inside number range, but min_val outside
        elif numbers[1] <= max_val <= numbers[1] + numbers[2] - 1:
            new_ranges.append([numbers[1], max_val, numbers[0]])

    # Filling in blank ranges - where there are gaps in ranges identified above
    # If input range not in any of the number ranges
    if len(new_ranges) == 0:
        new_ranges.append([min_val, max_val, min_val])
    # If beginning of input range is missing
    if min_val != new_ranges[0][0]:
        new_ranges = [[min_val, new_ranges[0][0] - 1, min_val]] + new_ranges
    # If ending of input range is missing
    if max_val != new_ranges[-1][1]:
        new_ranges.append([new_ranges[-1][1] + 1, max_val, new_ranges[-1][1] + 1])
    # Loop over all identified ranges and fill in any that are missing
    missing_ranges = []
    for i in range(len(new_ranges) - 1):
        if new_ranges[i][1] + 1 != new_ranges[i + 1][0]:
            missing_ranges.append([new_ranges[i][1] + 1, new_ranges[i + 1][0] - 1, new_ranges[i][1] + 1])
    # If any missing are identified, add them then sort
    if len(missing_ranges) > 0:
        new_ranges.extend(missing_ranges)
    new_ranges = sorted(new_ranges, key=lambda x: x[0])

    # The current list [min, max, start of new] is not in the proper format [start, length]
    # so changing format
    base_format = []
    for num_range in new_ranges:
        base_format.append([num_range[2], num_range[1] - num_range[0] + 1])
    return base_format


def solve_day_part_2(data):
    # The idea is to map each seed RANGE through the mapping process and identify the final
    # RANGES of the seeds.  As a range goes through the mapping, it may need to be
    # split into more than one range.  Those subsequent ranges may be split further
    # as we move through the mapping, so bookkeeping will be a challenge.  After mapping
    # select the minimum range start as the minimum location.

    # Get mapping and seed information
    # Reusing get_mapping() returns list of integers for seed locations
    # Need to turn into a list of list of start and length ranges
    seeds_location, mapping = get_mapping(data)
    seeds_location = [[i, j] for i, j in zip(seeds_location[::2], seeds_location[1::2])]

    # Sort the mapping by the 'from' starting point - make it easier to
    # identify gaps in the ranges
    for identifier in mapping.keys():
        mapping[identifier] = sorted(mapping[identifier], key=lambda x: x[1])

    id_order = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:',
                'water-to-light map:', 'light-to-temperature map:', 'temperature-to-humidity map:',
                'humidity-to-location map:']

    min_values = []
    # Loop over each range list for seed locations
    for range_list in seeds_location:
        # Initializing variable that will get updated
        # This variable is a list ranges (list of start and length)
        base_format = [range_list]
        # Loop over each step in mapping
        for identifier in id_order:
            next_ranges = []
            # Loop over each range list in base_format (again this gets updated)
            for init_range in base_format:
                # Get new range list for current range list and current step in mapping
                # next_ranges gets extended by new range list(s)
                next_ranges.extend(get_new_ranges(init_range, mapping[identifier]))
            # Update variable to carry current list of ranges
            base_format = copy.deepcopy(next_ranges)
        # After last step in mapping, get the minimum range location
        min_values.append(min([i[0] for i in base_format]))

    print('Lowest location number, ', min(min_values))

    return min(min_values)


output_test, final_location = solve_day_part_1(test)
print('Output equal to test output for part 1, ', output_test == test_answer)
output = solve_day_part_1(lines)
output_test_2 = solve_day_part_2(test)
print('Output equal to test output for part 2, ', output_test_2 == test_answer_2)
output_2 = solve_day_part_2(lines)

