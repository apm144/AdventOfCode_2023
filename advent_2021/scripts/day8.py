import numpy as np

# Read in data, new item for each line
f = open(r'..\inputs\input_day8.txt')
lines = f.readlines()
f.close()

test = [
    'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
    'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
    'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
    'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
    'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
    'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
    'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
    'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
    'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
    'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce',
]

test_example = [
    'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf',
]

test_answer = 26
test_example_answer = 5353
test_2_answer = 61229


def solve_part_1(data):
    # Parse input file - create two lists: one being the unique patters for 0-9 and one being the output pattern
    unique_patterns = []
    output_values = []
    # Loop over each line in input file
    for row in data:
        # Unique patterns for 0-9 and output patterns are separated by |
        before, after = row.split(' | ')
        # Each 0-9 pattern separated by space - add to unique patterns list
        unique_patterns.append(before.split())
        # Each output pattern separated by space - add to output patterns list
        output_values.append(after.split())

    # Only looking for the unique patterns in the output (from output_values list) that are unique length
    # This would be length 2 for the 1 value, length 3 for the 7 value, length 4 for the 4 value, and length 7 for the 8
    # Simply count all these up
    counts = []
    # Loop over each set of four output_values
    for four_output_values in output_values:
        count = 0
        # Loop over each output_value
        for output_value in four_output_values:
            # If length is one of 2, 3, 4, 7 then count it
            if len(output_value) in (2, 3, 4, 7):
                count += 1
        counts.append(count)

    print('Number of unique output values {}.'.format(sum(counts)))
    # Return the sum of the counts
    return sum(counts)


def solve_part_2(data):
    # Parse input file - create two lists: one being the unique patters for 0-9 and one being the output pattern
    # Each pattern will be sorted alphabetically because they will be used as keys in a dictionary and they could
    # be rearranged between their unique pattern and their output pattern
    all_unique_patterns = []
    all_output_patterns = []
    # Loop over each line in input file
    for row in data:
        # Unique patterns for 0-9 and output patterns are separated by |
        before, after = row.split(' | ')
        # Each 0-9 pattern separated by space - sort each pattern alphabetically then add to unique patterns list
        unique_patterns = before.split()
        unique_patterns = [''.join(sorted(i)) for i in unique_patterns]
        all_unique_patterns.append(unique_patterns)
        # Each output pattern separated by space - sort each pattern alphabetically then add to output patterns list
        output_patterns = after.split()
        output_patterns = [''.join(sorted(i)) for i in output_patterns]
        all_output_patterns.append(output_patterns)

    # Loop through each unique pattern and execute an algorithm to identify each pattern with its 0-9 value
    # Once identified, the pattern and value will be placed in a dictionary to be used for the output pattern
    output_values = []
    for unique_patterns, output_patterns in zip(all_unique_patterns, all_output_patterns):
        seven_pattern = ''
        three_pattern = ''
        six_pattern = ''
        mapping_key = {}
        # Loop over each pattern in unique pattern and identify the easy values based on length:
        # Length 2 for the 1 value, length 3 for the 7 value, length 4 for the 4 value, and length 7 for the 8
        for pattern in unique_patterns:
            if len(pattern) == 2:
                mapping_key[pattern] = 1
            if len(pattern) == 3:
                mapping_key[pattern] = 7
                seven_pattern = pattern
            if len(pattern) == 4:
                mapping_key[pattern] = 4
            if len(pattern) == 7:
                mapping_key[pattern] = 8
        # Loop over each pattern that is length 5 (could be 2, 3, or 5 value)
        # Identify the 3 because the 7 pattern is fully inside of it - use set difference between each pattern
        # and the seven pattern - the 3 value would have a set difference of 2 but the others would have a
        # set difference of 3
        for pattern in unique_patterns:
            if len(pattern) == 5:
                if len(set(pattern) - set(seven_pattern)) == 2:
                    mapping_key[pattern] = 3
                    three_pattern = pattern
                    break
        # Loop over each pattern that is length 6 (could be 0, 6, or 9 value)
        # Identify the 9 because the 3 pattern is fully inside of it - use set difference between each pattern
        # and the three pattern - the 9 value would have a set difference of 1 but the others would have a
        # set difference of 2
        for pattern in unique_patterns:
            if len(pattern) == 6:
                if len(set(pattern) - set(three_pattern)) == 1:
                    mapping_key[pattern] = 9
                    break
        # Loop over each pattern that is length 6 (could be 0, 6, or 9 value)
        # The 7 pattern would be completely inside the 0 value and the 9 value, but the 9 value is already identified
        # Use set difference between each pattern and seven pattern equal to 3 and not have the pattern in the
        # dictionary key
        for pattern in unique_patterns:
            if len(pattern) == 6:
                if len(set(pattern) - set(seven_pattern)) == 3 and pattern not in mapping_key.keys():
                    mapping_key[pattern] = 0
                    break
        # Loop over each pattern that is length 6 (could be 0, 6, or 9 value)
        # The 6 value is the pattern that is not already in the dictionary key
        for pattern in unique_patterns:
            if len(pattern) == 6 and pattern not in mapping_key.keys():
                mapping_key[pattern] = 6
                six_pattern = pattern
                break
        # Loop over each pattern that is length 5 (could be 2, 3, or 5 value)
        # Identify the 5 because it is fully inside the 6 pattern - use set difference between the three pattern
        # and all the other patterns - the 5 value would have a set difference of 1 but the others would have a
        # set difference of 2
        for pattern in unique_patterns:
            if len(pattern) == 5:
                if len(set(six_pattern) - set(pattern)) == 1:
                    mapping_key[pattern] = 5
                    break
        # Loop over each pattern that is length 5 (could be 2, 3, or 5 value)
        # The 2 value is the pattern that is not already in the dictionary key
        for pattern in unique_patterns:
            if len(pattern) == 5 and pattern not in mapping_key.keys():
                mapping_key[pattern] = 2
                break

        # Use the dictionary to identify the integer of the output pattern
        output_value = [mapping_key[i] for i in output_patterns]
        output_values.append(int(''.join(str(digit) for digit in output_value)))

    print('Number of unique output values {}.'.format(sum(output_values)))
    # Return the sum of the output values
    return sum(output_values)

output_test = solve_part_1(test)
print('Output equal to test output, ', output_test == test_answer)
output = solve_part_1(lines)

output_example = solve_part_2(test_example)
print('Output equal to test_example output, ', output_example == test_example_answer)
output_test_2 = solve_part_2(test)
print('Output equal to test_2 output, ', output_test_2 == test_2_answer)
output_2 = solve_part_2(lines)
