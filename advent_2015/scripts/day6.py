import numpy as np

# Read in data, new item for each line
f = open(r'..\inputs\input_day6.txt')
lines = f.readlines()
f.close()

test = [
    'turn on 0,0 through 999,999',
]
test_answer = 1000000
test2 = [
    'toggle 0,0 through 999,0',
]
test_2_answer = 1000
test3 = [
    'turn on 0,0 through 999,999',
    'turn off 499,499 through 500,500',
]
test_3_answer = 999996
test4 = [
    'turn on 0,0 through 0,0',
]
test_4_answer = 1
test5 = [
    'toggle 0,0 through 999,999',
]
test_5_answer = 2000000


# Function to parse input data into useful information
# Input file is list of commands with 'toggle', 'on', or 'off' and starting and ending coordinates
# Function will identify command and list the start/end coordinates as [command, [start, coor], [end, coor]]
def parse_input_data(data):
    commands = []
    # Loop over every line in input data
    for row in data:
        # Split by whitespace
        parsed_row = row.split()
        # If the number of elements in row is 4, it is a toggle command
        # Create command ['toggle', ['x0', 'y0'], ['x1', 'y1']]
        if len(parsed_row) == 4:
            commands.append(['toggle', parsed_row[1].split(','), parsed_row[3].split(',')])
        # If the 2nd element is 'on', it is an on command
        # Create command ['on', ['x0', 'y0'], ['x1', 'y1']]
        elif parsed_row[1] == 'on':
            commands.append(['on', parsed_row[2].split(','), parsed_row[4].split(',')])
        # If the 2nd element is 'off', it is an off command
        # Create command ['off', ['x0', 'y0'], ['x1', 'y1']]
        else:
            commands.append(['off', parsed_row[2].split(','), parsed_row[4].split(',')])
    # The coordinates are strings, need to convert on integers
    for i, command in enumerate(commands):
        commands[i][1] = [int(command[1][0]), int(command[1][1])]
        commands[i][2] = [int(command[2][0]), int(command[2][1])]
    # Return list of commands
    return commands


# Function that creates grid, follows input commands, and returns total number of on lights.
def solve_part_1(data):
    # Parse input file
    commands = parse_input_data(data)
    # Create grid.  Assign them all off (-1) initially.  On is 1.
    grid = np.ones((1000, 1000)) * -1
    # Loop through commands
    for command in commands:
        # If on command, set all between coordinates to on (1)
        if command[0] == 'on':
            grid[command[1][0]:command[2][0] + 1, command[1][1]:command[2][1] + 1] = 1
        # If off command, set all between coordinates to off (-1)
        elif command[0] == 'off':
            grid[command[1][0]:command[2][0] + 1, command[1][1]:command[2][1] + 1] = -1
        # If toggle command, switch between on (1) and off (-1) by multiplying all coordinates by -1.
        else:  # command[0] == 'toggle:
            grid[command[1][0]:command[2][0] + 1, command[1][1]:command[2][1] + 1] *= -1
    # Setting off (-1) numbers in grid to 0 for summation.
    grid[grid == -1] = 0
    # Return number of lights that are on (1) by summing entire grid
    return np.sum(grid)


# Function that creates grid, follows input commands, and returns total brightness of the lights.
def solve_part_2(data):
    # Parse input file
    commands = parse_input_data(data)
    # Create grid.  Assign starting brightness of all lights to 0.
    grid = np.zeros((1000, 1000))
    # Loop through commands
    for command in commands:
        # If on command, increase brightness between coordinates by 1.
        if command[0] == 'on':
            grid[command[1][0]:command[2][0] + 1, command[1][1]:command[2][1] + 1] += 1
        # If off command, decrease brightness between coordinates by 1.
        # If brightness goes negative, set to 0.
        elif command[0] == 'off':
            grid[command[1][0]:command[2][0] + 1, command[1][1]:command[2][1] + 1] -= 1
            grid[grid < 0] = 0
        # If toggle command, increase brightness between coordinates by 2.
        else:  # command[0] == 'toggle:
            grid[command[1][0]:command[2][0] + 1, command[1][1]:command[2][1] + 1] += 2
    # Return total brightness of the grid by summing entire grid
    return np.sum(grid)


output_test = solve_part_1(test)
print('Output equal to test output, ', output_test == test_answer, output_test)
output_test_2 = solve_part_1(test2)
print('Output equal to test output, ', output_test_2 == test_2_answer, output_test_2)
output_test_3 = solve_part_1(test3)
print('Output equal to test output, ', output_test_3 == test_3_answer, output_test_3)
output = solve_part_1(lines)
print('Number of lights on', output)

output_test_4 = solve_part_2(test4)
print('Output equal to test output, ', output_test_4 == test_4_answer, output_test_4)
output_test_5 = solve_part_2(test5)
print('Output equal to test output, ', output_test_5 == test_5_answer, output_test_5)
output_2 = solve_part_2(lines)
print('Total brightness', output_2)
