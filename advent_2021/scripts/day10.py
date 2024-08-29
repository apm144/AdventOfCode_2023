import numpy as np

# Read in data, new item for each line
f = open(r'..\inputs\input_day10.txt')
lines = f.readlines()
f.close()

test = [
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '{([(<{}[<>[]}>{[]{[(<()>',
    '(((({<>}<{<{<>}{[]{[]{}',
    '[[<[([]))<([[{}[[()]]]',
    '[{[{({}]{}}([{[{{{}}([]',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '[<(<(<(<{}))><([]([]()',
    '<{([([[(<>()){}]>(<<{{',
    '<{([{{}}[<[[[<>{}]]]>[]]',
]

test_answer = 26397
test_2_answer = 288957


def solve_part_1(data):
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
