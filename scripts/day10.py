import numpy as np

# Read in data, new item for each line
f = open(r'..\inputs\input_day10.txt')
lines = f.readlines()
f.close()
lines = [i.strip() for i in lines]

test_1 = [
    '-L|F7',
    '7S-7|',
    'L|7||',
    '-L-J|',
    'L|-JF',
]
test_2 = [
    '7-F7-',
    '.FJ|7',
    'SJLL7',
    '|F--J',
    'LJ.LJ',
]
test_answer_1 = 4
test_answer_2 = 8

test_3 = [
    '...........',
    '.S-------7.',
    '.|F-----7|.',
    '.||.....||.',
    '.||.....||.',
    '.|L-7.F-J|.',
    '.|..|.|..|.',
    '.L--J.L--J.',
    '...........',
]
test_4 = [
    '..........',
    '.S------7.',
    '.|F----7|.',
    '.||....||.',
    '.||....||.',
    '.|L-7F-J|.',
    '.|..||..|.',
    '.L--JL--J.',
    '..........',
]
test_answer_3 = 4
test_answer_4 = 4
test_5 = [
    '.F----7F7F7F7F-7....',
    '.|F--7||||||||FJ....',
    '.||.FJ||||||||L7....',
    'FJL7L7LJLJ||LJ.L-7..',
    'L--J.L7...LJS7F-7L7.',
    '....F-J..F7FJ|L7L7L7',
    '....L7.F7||L7|.L7L7|',
    '.....|FJLJ|FJ|F7|.LJ',
    '....FJL-7.||.||||...',
    '....L---J.LJ.LJLJ...',
]
test_6 = [
    'FF7FSF7F7F7F7F7F---7',
    'L|LJ||||||||||||F--J',
    'FL-7LJLJ||||||LJL-77',
    'F--JF--7||LJLJ7F7FJ-',
    'L---JF-JLJ.||-FJLJJ7',
    '|F|F-JF---7F7-L7L|7|',
    '|FFJF7L7F-JF7|JL---7',
    '7-L-JL7||F7|L7F-7F7|',
    'L.L7LFJ|||||FJL7||LJ',
    'L7JLJL-JLJLJL--JLJ.L',
]
test_answer_5 = 8
test_answer_6 = 10



def get_next_corr(pre_corr, curr_corr, pipe_type):
    next_corr = []
    if pipe_type == '-':
        # From left
        if pre_corr[1] == curr_corr[1] - 1:
            # Going right
            next_corr = [curr_corr[0], curr_corr[1] + 1]
        else:
            # Going left
            next_corr = [curr_corr[0], curr_corr[1] - 1]
    if pipe_type == '|':
        # From above
        if pre_corr[0] == curr_corr[0] - 1:
            # Going down
            next_corr = [curr_corr[0] + 1, curr_corr[1]]
        else:
            # Going up
            next_corr = [curr_corr[0] - 1, curr_corr[1]]
    if pipe_type == 'L':
        # From above
        if pre_corr[0] == curr_corr[0] - 1:
            # Going right
            next_corr = [curr_corr[0], curr_corr[1] + 1]
        else:
            # Going up
            next_corr = [curr_corr[0] - 1, curr_corr[1]]
    if pipe_type == 'J':
        # From above
        if pre_corr[0] == curr_corr[0] - 1:
            # Going left
            next_corr = [curr_corr[0], curr_corr[1] - 1]
        else:
            # Going up
            next_corr = [curr_corr[0] - 1, curr_corr[1]]
    if pipe_type == '7':
        # From left
        if pre_corr[1] == curr_corr[1] - 1:
            # Going down
            next_corr = [curr_corr[0] + 1, curr_corr[1]]
        else:
            # Going left
            next_corr = [curr_corr[0], curr_corr[1] - 1]
    if pipe_type == 'F':
        # From right
        if pre_corr[1] == curr_corr[1] + 1:
            # Going down
            next_corr = [curr_corr[0] + 1, curr_corr[1]]
        else:
            # Going right
            next_corr = [curr_corr[0], curr_corr[1] + 1]
    return next_corr


def solve_day_part_1(data):

    grid = []
    start = []
    for i, row in enumerate(data):
        grid.append([j for j in row])
        if 'S' in row:
            start = [i, [j for j, k in enumerate(row) if k == 'S'][0]]

    next_corr = []
    pipe_type = ''
    # Checking up
    if start[0] != 0:
        if grid[start[0] - 1][start[1]] in ['F', '|', '7']:
            next_corr = [start[0] - 1, start[1]]
            pipe_type = grid[start[0] - 1][start[1]]
    # Checking left
    if start[1] != 0:
        if grid[start[0]][start[1] - 1] in ['-', 'F', 'L']:
            next_corr = [start[0], start[1] - 1]
            pipe_type = grid[start[0]][start[1] - 1]
    # Checking down
    if start[0] != len(grid) - 1:
        if grid[start[0] + 1][start[1]] in ['|', 'L', 'J']:
            next_corr = [start[0] + 1, start[1]]
            pipe_type = grid[start[0] + 1][start[1]]
    # Checking right
    if start[1] != len(grid[0]) - 1:
        if grid[start[0]][start[1] + 1] in ['-', '7', 'J']:
            next_corr = [start[0], start[1] + 1]
            pipe_type = grid[start[0]][start[1] + 1]

    counter = 1
    curr_corr = next_corr.copy()
    pre_corr = start.copy()

    moves = [start.copy(), next_corr.copy()]
    while pipe_type != 'S':
        next_corr = get_next_corr(pre_corr, curr_corr, pipe_type)
        moves.append(next_corr.copy())
        counter += 1
        pipe_type = grid[next_corr[0]][next_corr[1]]
        pre_corr = curr_corr.copy()
        curr_corr = next_corr.copy()

    print('Farthest point is , ', int(counter / 2))
    return int(counter / 2)



output_test = solve_day_part_1(test_1)
print('Output equal to test_1 output for part 1, ', output_test == test_answer_1)
output_test_2 = solve_day_part_1(test_2)
print('Output equal to test_2 output for part 1, ', output_test_2 == test_answer_2)
output = solve_day_part_1(lines)
# output_test_3 = solve_day_part_2(test_3)
# print('Output equal to test_2 output for part 2, ', output_test_3 == test_answer_3)
# output_2 = solve_day_part_2(lines)

