import numpy as np

# Read in data, new item for each line
f = open(r'..\inputs\input_day5.txt')
lines = f.readlines()
f.close()

test = [
    '0,9 -> 5,9',
    '8,0 -> 0,8',
    '9,4 -> 3,4',
    '2,2 -> 2,1',
    '7,0 -> 7,4',
    '6,4 -> 2,0',
    '0,9 -> 2,9',
    '3,4 -> 1,4',
    '0,0 -> 8,8',
    '5,5 -> 8,2',
]

test_answer = 5
test_2_answer = 12


def solve_part_1(data):

    # Parse input file
    # Split start point and end point by ' -> '
    # For each point, split x and y by ','
    # Result is a list (line segments) of list (pairs of x,y points) of list of (x,y) coordinates
    line_segments = []
    for row in data:
        start_pt, end_pt = row.split(' -> ')
        start_pt = [int(i) for i in start_pt.split(',')]
        end_pt = [int(i) for i in end_pt.split(',')]
        line_segments.append([start_pt, end_pt])

    # Identify segments that we want to keep which are those with either the same x value or the same y value
    # Also need to identify the size of the grid we will need, so tracking largest x and y encountered
    keep_segments = []
    max_x = 0
    max_y = 0
    # Loop over each pair of x,y coordinates
    for line_seg in line_segments:
        # Check if current line segment coordinate is largest x or y encountered
        # If so, make the new x/y the max value
        if max(line_seg[0][0], line_seg[1][0]) > max_x:
            max_x = max(line_seg[0][0], line_seg[1][0])
        if max(line_seg[0][1], line_seg[1][1]) > max_y:
            max_y = max(line_seg[0][1], line_seg[1][1])
        # Check if x coordinates or y coordinates are the same.  If so, add to keep list
        if line_seg[0][0] == line_seg[1][0] or line_seg[0][1] == line_seg[1][1]:
            keep_segments.append(line_seg)

    # Initialize a blank grid the size of the max x/y encountered
    # Will increase coordinates by 1 for each line segment
    grid = np.zeros((max_x + 1, max_y + 1), dtype=int)

    # Loop over each line segment
    for line_seg in keep_segments:
        # Initialize a new blank grid
        new_grid = np.zeros((max_x + 1, max_y + 1), dtype=int)
        # Determine the starting and ending points of the x/y coordinates for the line segments
        start_x = min(line_seg[0][0], line_seg[1][0])
        end_x = max(line_seg[0][0], line_seg[1][0])
        start_y = min(line_seg[0][1], line_seg[1][1])
        end_y = max(line_seg[0][1], line_seg[1][1])
        # Set coordinates of line segment to 1 using slices
        new_grid[start_x:end_x + 1, start_y:end_y + 1] = 1
        # Add new grid to full grid
        grid = grid + new_grid

    # Number of line segments with multiple overlaps are those with the full grid > 1
    num_multiple_intersections = np.sum(grid > 1)

    print('Number of locations with multiple intersections {}.'.format(num_multiple_intersections))
    # Return number of multiple intersections in grid
    return num_multiple_intersections


def solve_part_2(data):

    # Parse input file
    # Split start point and end point by ' -> '
    # For each point, split x and y by ','
    # Result is a list (line segments) of list (pairs of x,y points) of list of (x,y) coordinates
    line_segments = []
    for row in data:
        start_pt, end_pt = row.split(' -> ')
        start_pt = [int(i) for i in start_pt.split(',')]
        end_pt = [int(i) for i in end_pt.split(',')]
        line_segments.append([start_pt, end_pt])

    # Identify segments that we want to keep which are those with either the same x value or the same y value
    # Will also keep the segments that are diagonal - those that have magnitude difference between start and end
    # the same for x and y.
    # Also need to identify the size of the grid we will need, so tracking largest x and y encountered
    keep_hor_ver = []
    max_x = 0
    max_y = 0
    keep_diag = []
    # Loop over each pair of x,y coordinates
    for line_seg in line_segments:
        # Check if current line segment coordinate is largest x or y encountered
        # If so, make the new x/y the max value
        if max(line_seg[0][0], line_seg[1][0]) > max_x:
            max_x = max(line_seg[0][0], line_seg[1][0])
        if max(line_seg[0][1], line_seg[1][1]) > max_y:
            max_y = max(line_seg[0][1], line_seg[1][1])
        # Check if x coordinates or y coordinates are the same.  If so, add to keep horizontal/vertical list
        if line_seg[0][0] == line_seg[1][0] or line_seg[0][1] == line_seg[1][1]:
            keep_hor_ver.append(line_seg)
        # Check if segment is diagonal - if absolute value of difference between start and end is same for x and y
        # If so, add to diagonal list
        if abs(line_seg[0][0] == line_seg[1][0]) == abs(line_seg[0][1] == line_seg[1][1]):
            keep_diag.append(line_seg)

    # Initialize a blank grid the size of the max x/y encountered
    # Will increase coordinates by 1 for each line segment
    grid = np.zeros((max_x + 1, max_y + 1), dtype=int)

    # Loop over each line segment in keep horizontal/vertical list
    for line_seg in keep_hor_ver:
        # Initialize a new blank grid
        new_grid = np.zeros((max_x + 1, max_y + 1), dtype=int)
        # Determine the starting and ending points of the x/y coordinates for the line segments
        start_x = min(line_seg[0][0], line_seg[1][0])
        end_x = max(line_seg[0][0], line_seg[1][0])
        start_y = min(line_seg[0][1], line_seg[1][1])
        end_y = max(line_seg[0][1], line_seg[1][1])
        # Set coordinates of line segment to 1 using slices
        new_grid[start_x:end_x + 1, start_y:end_y + 1] = 1
        # Add new grid to full grid
        grid = grid + new_grid

    # Loop over each line segment in the keep diagonal list
    for line_seg in keep_diag:
        # Initialize a new blank grid
        new_grid = np.zeros((max_x + 1, max_y + 1), dtype=int)
        # Building ranges need to loop through to set to 1
        # If end point is larger than start point, than a simple range works
        # If not, need to do a range backwards and them reverse it
        # Do for both x and y
        if line_seg[1][0] > line_seg[0][0]:
            x_range = list(range(line_seg[0][0], line_seg[1][0] + 1))
        else:
            x_range = list(range(line_seg[1][0], line_seg[0][0] + 1))[::-1]
        if line_seg[1][1] > line_seg[0][1]:
            y_range = list(range(line_seg[0][1], line_seg[1][1] + 1))
        else:
            y_range = list(range(line_seg[1][1], line_seg[0][1] + 1))[::-1]
        # Loop over the ranges established above and set to 1
        for x, y in zip(x_range, y_range):
            new_grid[x, y] = 1
        # Add new grid to full grid
        grid = grid + new_grid

    # Number of line segments with multiple overlaps are those with the full grid > 1
    num_multiple_intersections = np.sum(grid > 1)

    print('Number of locations with multiple intersections {}.'.format(num_multiple_intersections))
    # Return number of multiple intersections in grid
    return num_multiple_intersections


output_test = solve_part_1(test)
print('Output equal to test output, ', output_test == test_answer)
output = solve_part_1(lines)

output_test_2 = solve_part_2(test)
print('Output equal to test_2 output, ', output_test_2 == test_2_answer)
output_2 = solve_part_2(lines)
