import numpy as np

# Read in data, new item for each line
f = open(r'..\inputs\input_day9.txt')
lines = f.readlines()
f.close()

test = [
    '2199943210',
    '3987894921',
    '9856789892',
    '8767896789',
    '9899965678',
]

test_answer = 15
test_2_answer = 1134


# Function to locate the minimum points of the grid
def get_min_points(grid):
    index = []
    height = []
    # Loop over each row then column
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            # If not along an edge, subtract or add 1 and check if the point is lower than current location (i, j)
            # If the neighboring point is lower or the same height as the current location
            # then continue to the next point
            # If it is not, move to the next if statement
            if i != 0 and grid[i - 1, j] <= grid[i, j]:
                continue
            if j != 0 and grid[i, j - 1] <= grid[i, j]:
                continue
            if i != grid.shape[0] - 1 and grid[i + 1, j] <= grid[i, j]:
                continue
            if j != grid.shape[1] - 1 and grid[i, j + 1] <= grid[i, j]:
                continue
            # If current point gets through all if statements then it is a minimum and it is added to tracking lists
            index.append([i, j])
            height.append(grid[i, j])
    return index, height


def solve_part_1(data):
    # Parse input file and make into grid
    grid = []
    # Loop over each row and make each character into an integer (not line break)
    for row in data:
        grid.append([int(i) for i in row if i != '\n'])
    # Make numpy array for easier indexing
    grid = np.array(grid)

    # Get the index (list of (x, y) coordinates) and height of the minimum points of the grid
    index, height = get_min_points(grid)

    # Risk level is height plus 1
    height = np.array(height) + 1

    print('Sum of risk levels {}.'.format(sum(height)))
    # Return the sum of the risk levels
    return sum(height)


# Recursive function to find indices of points in a basin (given one point in basin, find all points surrounded by 9s.
def get_basin_points(pts_to_check, pts_in_basin, grid):
    new_pts = []
    # Loop over input list of pts_to_check (list of (x, y)) in a grid
    for point in pts_to_check:
        # If the current point is not already in the pts_in_basin tracking list then add it
        if point not in pts_in_basin:
            pts_in_basin.append(point)
        # Each if statement checks three things and if all are True then the neighboring point is added to the basin
        # 1. if point is not on edge such that neighbor in direction checked exists
        # 2. if neighbor is not 9
        # 3. if neighbor is not already in basin
        if point[0] != 0 and grid[point[0] - 1, point[1]] != 9 and [point[0] - 1, point[1]] not in pts_in_basin:
            new_pts.append([point[0] - 1, point[1]])
            pts_in_basin.append([point[0] - 1, point[1]])
        if point[1] != 0 and grid[point[0], point[1] - 1] != 9 and [point[0], point[1] - 1] not in pts_in_basin:
            new_pts.append([point[0], point[1] - 1])
            pts_in_basin.append([point[0], point[1] - 1])
        if (point[0] != grid.shape[0] - 1 and grid[point[0] + 1, point[1]] != 9 and
                [point[0] + 1, point[1]] not in pts_in_basin):
            new_pts.append([point[0] + 1, point[1]])
            pts_in_basin.append([point[0] + 1, point[1]])
        if (point[1] != grid.shape[1] - 1 and grid[point[0], point[1] + 1] != 9 and
                [point[0], point[1] + 1] not in pts_in_basin):
            new_pts.append([point[0], point[1] + 1])
            pts_in_basin.append([point[0], point[1] + 1])
    # After all the if statements, check if there are any new points to send back into the function
    if len(new_pts) > 0:
        pts_in_basin = get_basin_points(new_pts, pts_in_basin, grid)
    # If no new points, return the points found in the basin
    return pts_in_basin


def solve_part_2(data):
    # Parse input file and make into grid
    grid = []
    # Loop over each row and make each character into an integer (not line break)
    for row in data:
        grid.append([int(i) for i in row if i != '\n'])
    # Make numpy array for easier indexing
    grid = np.array(grid)

    # Get the index (list of (x, y) coordinates) and height of the minimum points of the grid
    index, height = get_min_points(grid)

    # Each index (list of (x, y) coordinates of minimum points) is in its own basin, so loop over each
    # to find size of the basin
    basin_sizes = []
    for idx in index:
        pts_in_basin = []
        # Get indices of points in a given basin
        get_basin_points([idx], pts_in_basin, grid)
        # Track number of points in a basin
        basin_sizes.append(len(pts_in_basin))

    # Reverse sort the basin sizes - want the largest three
    basin_sizes = sorted(basin_sizes, reverse=True)

    print('Product of three largest basins is {}.'.format(basin_sizes[0] * basin_sizes[1] * basin_sizes[2]))
    # Return the product of largest three basins
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


output_test = solve_part_1(test)
print('Output equal to test output, ', output_test == test_answer)
output = solve_part_1(lines)

output_test_2 = solve_part_2(test)
print('Output equal to test_2 output, ', output_test_2 == test_2_answer)
output_2 = solve_part_2(lines)
