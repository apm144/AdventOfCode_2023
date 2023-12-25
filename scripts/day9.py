import numpy as np

# Read in data, new item for each line
f = open(r'..\inputs\input_day9.txt')
lines = f.readlines()
f.close()
lines = [i.strip() for i in lines]

test_1 = [
    '0 3 6 9 12 15',
    '1 3 6 10 15 21',
    '10 13 16 21 30 45',
]
test_answer = 114
test_answer_2 = 2


def solve_day(data):
    # Loop over input row, conver to list of integers
    number_lists = []
    for row in data:
        number_lists.append([int(i) for i in row.split()])

    results_part_1 = []
    results_part_2 = []
    # Loop over each number list (row in input file)
    for number_list in number_lists:
        # Initialize list of list.  This will build up as we go down each level
        all_lists = [np.array(number_list)]
        # While loop as we descend the differences.  Will stop when all are 0.
        # Initially had sum() != 0 but that did not work with +/- integers
        while not all([i == 0 for i in all_lists[-1]]):
        # while sum(all_lists[-1]) != 0:
            # Used np.diff() to get differences between values
            all_lists.append(np.diff(all_lists[-1]))
        val = 0
        val_2 = 0
        # For part 1, sum up the last values of the lists
        # For part 2, subtract off the value below it, starting from the bottom
        for sub_list in all_lists[::-1]:
            val += sub_list[-1]
            val_2 = sub_list[0] - val_2
        results_part_1.append(val)
        results_part_2.append(val_2)

    # The answer to the puzzle is the sum of these results lists
    print('Sum of next values, ', sum(results_part_1))
    print('Sum of previous values, ', sum(results_part_2))
    return sum(results_part_1), sum(results_part_2)


output_test, output_test_2 = solve_day(test_1)
print('Output equal to test_1 output for part 1, ', output_test == test_answer)
print('Output equal to test_2 output for part 2, ', output_test_2 == test_answer_2)
output, output_2 = solve_day(lines)

