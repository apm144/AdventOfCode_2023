import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

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


# Function to get the next coordinate of the animal from the previous coordinate,
# current coordinate, and current coordinate pipe type.
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


def solve_day(data):

    grid = []
    start = []
    # Looping over each row to create the grid
    # Grid will have [row number, col number] coordinates
    for i, row in enumerate(data):
        grid.append([j for j in row])
        # Identifying start coordinate
        if 'S' in row:
            start = [i, [j for j, k in enumerate(row) if k == 'S'][0]]

    # Determine the next coordinate the animal is moving in from the start
    # Because start will have two possible directions, the next_corr variable
    # will be updated twice.  It does not matter which direction it goes.
    # Will check in each of the four directions and select it for a coordinate
    # if it has a valid pipe type.
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

    # Initializing variables for the while loop
    counter = 1
    # Current coordinate where animal is
    curr_corr = next_corr.copy()
    # Previous coordinate where animal was
    pre_corr = start.copy()
    # Setting numpy Boolean grid for path of the animal
    # 1 being a coordinate where the path is.
    bool_grid = np.zeros((len(grid), len(grid[0]))).astype(int)
    bool_grid[start[0], start[1]] = 1
    bool_grid[curr_corr[0], curr_corr[1]] = 1

    # Tracking list of coordinates of the path.  Will be used to make a polygon
    moves = [start.copy(), next_corr.copy()]
    # Loop through until we encounter the start again.
    while pipe_type != 'S':
        # Get the next coordinate using previous coordinate, current coordinate,
        # and pipe type
        next_corr = get_next_corr(pre_corr, curr_corr, pipe_type)
        # Add next coordinate to polygon list
        moves.append(next_corr.copy())
        # Update Boolean grid with path coordinate
        bool_grid[next_corr[0], next_corr[1]] = 1
        # Increase counter
        counter += 1
        # Update pipe type, previous coordinate, current coordinate
        pipe_type = grid[next_corr[0]][next_corr[1]]
        pre_corr = curr_corr.copy()
        curr_corr = next_corr.copy()

    # Make polygon
    polygon = Polygon(moves)
    inside_counter = 0
    # Loop over every coordinate in the grid to identify if a coordinate is inside
    # the path
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If a path coordinate, skip it
            if bool_grid[i, j] == 1:
                continue
            # If the sum of the Boolean grid from edge to the current coordinate
            # is 0, that means it is outside of the path, so it is skipped.
            # Check for each direction.
            if sum(bool_grid[i, 0:j + 1]) == 0:
                continue
            if sum(bool_grid[0:i + 1, j]) == 0:
                continue
            if sum(bool_grid[i, j:]) == 0:
                continue
            if sum(bool_grid[i:, j]) == 0:
                continue
            # Check if coordinate is inside the path.  If it is, increase counter.
            point = Point(i, j)
            if polygon.contains(point):
                inside_counter += 1

    print('Farthest point is , ', int(counter / 2))
    print('Number of points inside loop, ', inside_counter)
    return int(counter / 2), inside_counter


output_test = solve_day(test_1)
print('Output equal to test_1 output for part 1, ', output_test[0] == test_answer_1)
output_test_2 = solve_day(test_2)
print('Output equal to test_2 output for part 1, ', output_test_2[0] == test_answer_2)
output_test_3 = solve_day(test_3)
print('Output equal to test_3 output for part 2, ', output_test_3[1] == test_answer_3)
output_test_4 = solve_day(test_4)
print('Output equal to test_4 output for part 2, ', output_test_4[1] == test_answer_4)
output_test_5 = solve_day(test_5)
print('Output equal to test_5 output for part 2, ', output_test_5[1] == test_answer_5)
output_test_6 = solve_day(test_6)
print('Output equal to test_6 output for part 2, ', output_test_6[1] == test_answer_6)
output = solve_day(lines)

