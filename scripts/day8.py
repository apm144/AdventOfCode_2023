import numpy as np
from collections import Counter
import os
import re

# Read in data, new item for each line
f = open(r'..\inputs\input_day8.txt')
lines = f.readlines()
f.close()
lines = [i.strip() for i in lines]

test_1 = [
    'RL',
    '',
    'AAA = (BBB, CCC)',
    'BBB = (DDD, EEE)',
    'CCC = (ZZZ, GGG)',
    'DDD = (DDD, DDD)',
    'EEE = (EEE, EEE)',
    'GGG = (GGG, GGG)',
    'ZZZ = (ZZZ, ZZZ)',
]
test_2 = [
    'LLR',
    '',
    'AAA = (BBB, BBB)',
    'BBB = (AAA, ZZZ)',
    'ZZZ = (ZZZ, ZZZ)',
]
test_3 = [
    'LR',
    '',
    '11A = (11B, XXX)',
    '11B = (XXX, 11Z)',
    '11Z = (11B, XXX)',
    '22A = (22B, XXX)',
    '22B = (22C, 22C)',
    '22C = (22Z, 22Z)',
    '22Z = (22B, 22B)',
    'XXX = (XXX, XXX)',
]
test_answer_1 = 2
test_answer_2 = 6
test_answer_3 = 6


def solve_day_part_1(data):

    moves = []
    moves_mapping = {'L': 0, 'R': 1}
    mapping = {}
    for i, row in enumerate(data):
        if i == 0:
            moves = [moves_mapping[move] for move in row]
        elif row == '':
            continue
        else:
            identifier = row.split(' = ')[0]
            mapping[identifier] = row.split(' = ')[1].strip('()').split(', ')

    counter = 0
    curr_element = 'AAA'
    while curr_element != 'ZZZ':
        for move in moves:
            curr_element = mapping[curr_element][move]
            counter += 1
            if curr_element == 'ZZZ':
                break

    print('Number of steps, ', counter)

    return counter




output_test = solve_day_part_1(test_1)
print('Output equal to test_1 output for part 1, ', output_test == test_answer_1)
output_test_2 = solve_day_part_1(test_2)
print('Output equal to test_2 output for part 1, ', output_test_2 == test_answer_2)
output = solve_day_part_1(lines)
# output_test_2, sorted_hands_test_2 = solve_day_part_2(test)
# print('Output equal to test output for part 2, ', output_test_2 == test_answer_2)
# output_2, sorted_hands_2 = solve_day_part_2(lines)

