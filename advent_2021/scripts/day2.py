import numpy as np

# Read in data, new item for each line
f = open(r'..\inputs\input_day2.txt')
lines = f.readlines()
f.close()

test = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2',
]
test_answer = 150
test_2_answer = 900


def solve_part_1(data):
    depth = 0
    hor_pos = 0
    # Loop over each direction and number of steps
    for row in data:
        # Parse by splitting into direction and steps; make steps into integer
        direction, steps = row.split()
        steps = int(steps)
        # Increase horizontal position if moving forward by number of steps
        if direction == 'forward':
            hor_pos += steps
        # Decrease depth by number of steps when moving up
        elif direction == 'up':
            depth -= steps
        # Increase depth by number of steps when moving down (if not forward or up)
        else:
            depth += steps
    print('Horizontal position is {}, depth is {}, product of both is {}.'.format(hor_pos, depth,
                                                                                  hor_pos * depth))
    # Return product of horizontal position and depth
    return depth * hor_pos


def solve_part_2(data):
    depth = 0
    hor_pos = 0
    aim = 0
    # Loop over each direction and number of steps
    for row in data:
        # Parse by splitting into direction and steps; make steps into integer
        direction, steps = row.split()
        steps = int(steps)
        # Increase horizontal position if moving forward by number of steps
        # Also increase depth by product of depth and aim
        if direction == 'forward':
            hor_pos += steps
            depth += aim * steps
        # Decrease aim by number of steps when moving up
        elif direction == 'up':
            aim -= steps
        # Increase aim by number of steps when moving down (not forward or up)
        else:
            aim += steps
    print('Horizontal position is {}, depth is {}, product of both is {}.'.format(hor_pos, depth,
                                                                                  hor_pos * depth))
    # Return product of depth and horizontal position
    return depth * hor_pos

output_test = solve_part_1(test)
print('Output equal to test output, ', output_test == test_answer)
output = solve_part_1(lines)

output_test_2 = solve_part_2(test)
print('Output equal to test_2 output, ', output_test_2 == test_2_answer)
output_2 = solve_part_2(lines)
