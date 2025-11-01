import numpy as np

# Read in data, new item for each line
f = open(r'..\inputs\input_day11.txt')
lines = f.readlines()
f.close()

test = [
    '5483143223',
    '2745854711',
    '5264556173',
    '6141336146',
    '6357385478',
    '4167524645',
    '2176841721',
    '6882881134',
    '4846848554',
    '5283751526',
]

test_answer = 1656
test_2_answer = 288957


def solve_part_1(data):
    grid = []
    for i, row in enumerate(data):
        grid.append([int(j) for j in row.strip()])
    grid = np.array(grid)

    flashes = np.zeros(grid.shape, dtype=int)
    counts = 0

    for step in range(1, 101):
        flashes = np.zeros(grid.shape, dtype=int)
        new_grid = grid + 1
        flashes[new_grid > 9] = 1
        new_grid[new_grid > 9] = 0
        counts += np.sum(flashes)

        while np.sum(flashes) > 0:

            new_flashes = np.zeros(grid.shape, dtype=int)
            for i in range(grid.shape[0]):
                for j in range(grid.shape[1]):
                    if flashes[i, j] == 0:
                        continue
                    if flashes[i, j] == 1 and i != 0 and new_grid[i - 1, j] != 0:
                        new_grid[i - 1, j] += 1
                    if flashes[i, j] == 1 and i != 0 and j != 0 and new_grid[i - 1, j - 1] != 0:
                        new_grid[i - 1, j - 1] += 1
                    if flashes[i, j] == 1 and i != 0 and j != new_grid.shape[1] - 1 and new_grid[i - 1, j + 1] != 0:
                        new_grid[i - 1, j + 1] += 1
                    if flashes[i, j] == 1 and i != new_grid.shape[0] - 1 and new_grid[i + 1, j] != 0:
                        new_grid[i + 1, j] += 1
                    if flashes[i, j] == 1 and i != new_grid.shape[0] - 1 and j != 0 and new_grid[i + 1, j - 1] != 0:
                        new_grid[i + 1, j - 1] += 1
                    if flashes[i, j] == 1 and i != new_grid.shape[0] - 1 and j != new_grid.shape[1] - 1 and new_grid[i + 1, j + 1] != 0:
                        new_grid[i + 1, j + 1] += 1
                    if flashes[i, j] == 1 and j != 0 and new_grid[i, j - 1] != 0:
                        new_grid[i, j - 1] += 1
                    if flashes[i, j] == 1 and j != new_grid.shape[1] - 1 and new_grid[i, j + 1] != 0:
                        new_grid[i, j + 1] += 1

            new_flashes[new_grid > 9] = 1
            new_grid[new_grid > 9] = 0
            flashes = new_flashes
            counts += np.sum(flashes)

        grid = new_grid
        print('here')


    corrupt_data = []
    # Loop over each row of input data
    for row in data:
        # Remove white space
        row = row.strip()
        group_list = []
        # Loop over each character in the row
        for char in row:
            # If opening character, add to tracking list
            if char in '([{<':
                group_list.append(char)
            # If it is not, it is either a closing character or an error
            else:
                # If closing character, remove the last character from the tracking list and move to next character
                if group_list[-1] == '(' and char == ')':
                    group_list = group_list[0:-1]
                    continue
                elif group_list[-1] == '[' and char == ']':
                    group_list = group_list[0:-1]
                    continue
                elif group_list[-1] == '{' and char == '}':
                    group_list = group_list[0:-1]
                    continue
                elif group_list[-1] == '<' and char == '>':
                    group_list = group_list[0:-1]
                    continue
                # If it is error, add the erroneous character to the corrupt_data list and break out of current loop
                else:
                    corrupt_data.append(char)
                    break

    score_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}

    # Convert the character to its score using scoring dictionary
    scores = [score_dict[i] for i in corrupt_data]

    print('Sum of corrupted data scores {}.'.format(sum(scores)))
    # Return the sum of corrupted data scores
    return sum(scores)


def solve_part_2(data):
    incomplete_data = []
    # Loop over each row of input data
    for row in data:
        # Remove white space
        row = row.strip()
        group_list = []
        corrupt = False
        for char in row:
            # If opening character, add to tracking list
            if char in '([{<':
                group_list.append(char)
            # If it is not, it is either a closing character or an error
            else:
                # If closing character, remove the last character from the tracking list and move to next character
                if group_list[-1] == '(' and char == ')':
                    group_list = group_list[0:-1]
                    continue
                elif group_list[-1] == '[' and char == ']':
                    group_list = group_list[0:-1]
                    continue
                elif group_list[-1] == '{' and char == '}':
                    group_list = group_list[0:-1]
                    continue
                elif group_list[-1] == '<' and char == '>':
                    group_list = group_list[0:-1]
                    continue
                # If it is error then break out of current loop and set corrupt flag to True
                else:
                    corrupt = True
                    break
        # If not corrupted data then add to incomplete list
        if not corrupt:
            incomplete_data.append(group_list)

    closing_dict = {'(': ')', '[': ']', '{': '}', '<': '>'}
    closing_data = []
    # Loop over incomplete data list and determine the characters needed to close using the closing char dictionary
    # When closing, loop over the incomplete data in reverse order
    for data in incomplete_data:
        closing_data.append([closing_dict[i] for i in data[::-1]])

    score_dict = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    # For each closing string, loop over each character and multiply by 5 then add score from scoring dictionary
    for data in closing_data:
        score = 0
        for char in data:
            score *= 5
            score += score_dict[char]
        scores.append(score)

    # Sort scores
    scores = sorted(scores)

    print('Middle autocomplete score {}.'.format(scores[int((len(scores) - 1) / 2)]))
    # Return the middle autocomplete score
    return scores[int((len(scores) - 1) / 2)]


output_test = solve_part_1(test)
print('Output equal to test output, ', output_test == test_answer)
output = solve_part_1(lines)

output_test_2 = solve_part_2(test)
print('Output equal to test_2 output, ', output_test_2 == test_2_answer)
output_2 = solve_part_2(lines)
