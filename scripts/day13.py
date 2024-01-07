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


# Function the looks for reflection and returns number of rows above reflection
# Optional Boolean argument 'mirror' used to control whether looking for true reflection (part 1)
# or a reflection that is off by one character (part 2).
def get_pattern_sum(pattern, mirror=True):
    # Loop over each row but the last one
    for row_id_above in range(len(pattern) - 1):
        # Create the pattern above in reverse from original orientation because it will be compared to pattern below
        pattern_above = pattern[0: row_id_above + 1][::-1]
        # Create the pattern below
        pattern_below = pattern[row_id_above + 1:]
        # Look for minimum length between the two - will truncate larger pattern.
        min_id = min(len(pattern_above), len(pattern_below))
        pattern_above = pattern_above[0: min_id]
        pattern_below = pattern_below[0: min_id]
        # If looking for true reflection (part 1)
        if mirror:
            # If two patterns match, return number of rows above
            if pattern_above == pattern_below:
                return row_id_above + 1
        # If looking for patterns that are one off (part 2)
        else:
            num_diff = 0
            # Loop over each row in pattern_above and pattern_below, and sum up how many times they are different
            for row_pattern_id in range(len(pattern_above)):
                num_diff += sum([pattern_above[row_pattern_id][i] != pattern_below[row_pattern_id][i] for i in
                                 range(len(pattern_above[row_pattern_id]))])
            # If they are different by only one value, return number of rows above
            if num_diff == 1:
                return row_id_above + 1
    return 0


# Method for solving by expanding the grid by 1
def solve_day(data, mirror=True):

    # Loop over the input rows
    # Pattern data will be list of grid_data since there will be multiple grids
    pattern_data = []
    # Grid data will be list of list of strings representing the individual patterns to analyze.
    grid_data = []
    for row in data:
        # Indicator that one pattern ends and another will begin on the next row
        if row == '':
            # Add grid to pattern_data
            pattern_data.append(grid_data)
            # Reset grid for next pattern
            grid_data = []
            continue
        # Add row to grid_data
        grid_data.append(row)
    # After finished reading file, last grid needs to be added to pattern_data
    pattern_data.append(grid_data)

    row_sum = 0
    col_sum = 0
    # Loop over each pattern
    for pattern in pattern_data:
        # If pattern has reflective row, add rows above data to running sum
        # mirror argument is for whether to look for true reflection (part 1) or one rock/mirror difference (part 2).
        row_sum += get_pattern_sum(pattern, mirror)

        # Will use same code to look for column reflection, but will transpose pattern first
        pattern_t = []
        # Loop over each row
        for i in range(len(pattern[0])):
            # Initialize what will be the new row after transpose
            row = []
            # Loop over each '.' or '#' and put into new row
            for sublist in pattern:
                row.append(sublist[i])
            # Add this new row to tranposed pattern.  Need to join the individual characters
            pattern_t.append(''.join(row))

        # If patterh has reflective column (using transposed pattern), add columns to left to running sum
        col_sum += get_pattern_sum(pattern_t, mirror)

    # Print and return answer
    print('Summarized notes, ', col_sum + (100 * row_sum))
    return col_sum + (100 * row_sum)


output_test = solve_day(test_1)
print('Output equal to test_1 output for part 1, ', output_test == test_answer_1)
output = solve_day(lines)
output_test_2 = solve_day(test_1, mirror=False)
print('Output equal to test_1 output for part 2, ', output_test_2 == test_answer_2)
output_2 = solve_day(lines, mirror=False)
