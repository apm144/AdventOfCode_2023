import copy

import numpy as np
import itertools

# Read in data, new item for each line
f = open(r'..\inputs\input_day14.txt')
lines = f.readlines()
f.close()
lines = [i.strip() for i in lines]

test_1 = [
    'O....#....',
    'O.OO#....#',
    '.....##...',
    'OO.#O....O',
    '.O.....O#.',
    'O.#..O.#.#',
    '..O..#O..O',
    '.......O..',
    '#....###..',
    '#OO..#....',
]
test_answer_1 = 136
test_answer_2 = 64


# Function used to find new locations of round rocks after tilting north.
# Input is current round rock coordinates, and grid of cube rocks with 1 at location of cube rocks.
def get_new_coordinates(rock_coordinates, cube_rock_grid):
    # Initialize grid for location of round rocks after tilting north
    new_round_grid = np.zeros(cube_rock_grid.shape).astype(int)
    new_coordinates = []

    # Loop over all rock coordinates
    # NOTE: important that coordinates are sorted by row_id
    for row_id, col_id in rock_coordinates:
        # If no cube rock between round rock and north edge
        # Will have sum of cube_rock_grid between current location and edge = 0
        if sum(cube_rock_grid[0:row_id, col_id]) == 0:
            # Find location of new_row_id, which is simply the sum of the rocks
            # that are already in place on the new grid
            new_row_id = sum(new_round_grid[0:row_id, col_id])
        # If there is a cube rock between round rock and north edge
        else:
            # Figure out the closest cube rock
            # Get all the cube rocks from current row_id to north edge in current column
            # Then select the last one.
            cube_row = [i for i in range(len(cube_rock_grid[0:row_id, col_id]))
                        if cube_rock_grid[i, col_id] == 1][-1]
            # New_row_id is sum (number of round rocks) of rocks that are already in
            # place on the new grid AFTER the cube_row
            new_row_id = sum(new_round_grid[cube_row:row_id, col_id]) + cube_row + 1
        # Setting new_round_grid = 1 for the new coordinate
        # Because it is subsequently used for future round rocks
        new_round_grid[new_row_id, col_id] = 1
        # Setting new_coordinates
        new_coordinates.append([new_row_id, col_id])

    # Return new_coordinates of round rocks
    return new_coordinates


# Function that will return new coordinates after rotating 90 clockwise
# Input is list of current coordinates, and length of the grid (must be square).
def rotate_clockwise(coordinates, len_grid):
    new_coor = []
    for row_id_orig, col_id_orig in coordinates:
        new_coor.append([col_id_orig, len_grid - 1 - row_id_orig])
    return new_coor


# Function that will return coordinates after a full cycle (north tilt, west tilt,
# south tilt, and east tilt).  Output coordinates will be in the original orientation.
# Input is list of coordinates, and list of grids of cube rocks used for each tilt.
def get_cycle_coordinates(coordinates, grids):
    # Loop over each grid - north, west, south, east
    for grid in grids:
        # Get new coordinates after tilt
        output_coor = get_new_coordinates(coordinates, grid)
        # Rotate the new coordinates 90 degree clockwise (i.e. to go from north tilt
        # to west tilt, the coordinates must rotate clockwise)
        output_coor = rotate_clockwise(output_coor, len(grid))
        # Sort the new, rotated coordinates by new row_id
        output_coor = sorted(output_coor)
        coordinates = copy.deepcopy(output_coor)
    return coordinates


def solve_day_part_1(data):

    # Loop over the input rows
    grid_north = []
    rock_coordinates = []
    for row_id, row in enumerate(data):
        cube_rock_row = []
        for col_id, char in enumerate(row):
            # If character is a 'O' (rolling rock), save the coordinates
            if char == 'O':
                cube_rock_row.append(0)
                rock_coordinates.append([row_id, col_id])
            # If character is '#' (cube rock), set grid as 1
            elif char == '#':
                cube_rock_row.append(1)
            else:
                cube_rock_row.append(0)
        grid_north.append(cube_rock_row)

    # Make grid of cube rocks a numpy array
    grid_north = np.array(grid_north)

    # Set up load-from-north mapping.
    # Invert the rows from 1-size of grid (load count)
    # Then set up map for the amount of load (value) given the row_id (key)
    loads = list(range(1, len(grid_north) + 1))[::-1]
    load_map = {i: j for i, j in enumerate(loads)}

    # Get the new coordinates after tilting north
    # Input is current rock coordinates and grid (location) of cube rocks
    new_coordinates = get_new_coordinates(rock_coordinates, grid_north)

    # Calculate the total load, which is sum of loads (based on row_id of new coordinates).
    total_load = sum([load_map[i[0]] for i in new_coordinates])

    print('Total load, ', total_load)
    return total_load


def solve_day_part_2(data):

    # Loop over the input rows
    grid_north = []
    rock_coordinates = []
    for row_id, row in enumerate(data):
        cube_rock_row = []
        for col_id, char in enumerate(row):
            # If character is a 'O' (rolling rock), save the coordinates
            if char == 'O':
                cube_rock_row.append(0)
                rock_coordinates.append([row_id, col_id])
            # If character is '#' (cube rock), set grid as 1
            elif char == '#':
                cube_rock_row.append(1)
            else:
                cube_rock_row.append(0)
        grid_north.append(cube_rock_row)

    # Make grid of cube rocks a numpy array
    grid_north = np.array(grid_north)
    # Make other grids needed for the full cycle
    grid_west = np.rot90(grid_north, -1)
    grid_south = np.rot90(grid_west, -1)
    grid_east = np.rot90(grid_south, -1)

    # Set up load-from-north mapping.
    # Invert the rows from 1-size of grid (load count)
    # Then set up map for the amount of load (value) given the row_id (key)
    loads = list(range(1, len(grid_north) + 1))[::-1]
    load_map = {i: j for i, j in enumerate(loads)}

    orig_coor = copy.deepcopy(rock_coordinates)
    coor = copy.deepcopy(orig_coor)

    # Initialize load_tracker - list of total load on north beam AFTER each cycle.
    # The cycle is the index of the list
    load_tracker = [0]
    spacer = 1

    # Loop over up to 1000 cycles.  The idea here is to loop over many cycles and find
    # a pattern that can be extrapolated to 1e9 cycles.
    for cycle in range(1, 1000):
        # Get new coordinates after each cycle
        coor = get_cycle_coordinates(coor, [grid_north, grid_west, grid_south, grid_east])
        # print(cycle, sum([load_map[i[0]] for i in coor]))
        # Add the total_load to the tracker list
        load_tracker.append(sum([load_map[i[0]] for i in coor]))

        # After a minimum number of cycles (here 50), look to see if there is a pattern.
        if cycle > 50:
            # Look at the last 50 total_loads
            sub_tracker = load_tracker[-50:]
            # Identify the potential spacing of the pattern - take the first entry and
            # see if it is elsewhere in the tracker
            spacer = [i for i, j in enumerate(sub_tracker) if j == sub_tracker[0]]
            # If it is not (length = 1) then continue looking
            if len(spacer) <= 1:
                continue
            spacer = spacer[1]
            # Will not see if ALL the values in the sub_tracker have the same spacing
            # If they do, then we have a consistent pattern
            flag = True
            # Loop over all values from 0 up to spacer value
            for init_idx in range(spacer):
                # Create a range object with the same spacer starting at init_idx
                # Will check to see if the running difference is 0 for all (pattern)
                # If it is not, set flag to False and break out
                if not all(np.diff(np.array(sub_tracker)[np.arange(init_idx, len(sub_tracker), spacer)]) == 0):
                    flag = False
                    break
            if flag:
                break

    # Assuming there is a pattern, need to extrapolate to 1e9 cycles
    total_load = 0
    # Taking just the tail of the tracker with indices (up to spacer)
    sub_tracker = [[i, j] for i, j in enumerate(load_tracker)][-spacer:]
    # Look for where the  1e9 less index modulus spacer is 0, that is the extrapolated total_load.
    for idx, load_val in sub_tracker:
        if (1000000000 - idx) % spacer == 0:
            total_load = load_val

    print('Total load after 1 billion cycles, ', total_load)
    return total_load


output_test_1 = solve_day_part_1(test_1)
print('Output equal to test_1 output for part 1, ', output_test_1 == test_answer_1)
output = solve_day_part_1(lines)
output_test_2 = solve_day_part_2(test_1)
print('Output equal to test_1 output for part 2, ', output_test_2 == test_answer_2)
output_2 = solve_day_part_2(lines)
