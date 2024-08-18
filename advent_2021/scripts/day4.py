import numpy as np

# Read in data, new item for each line
f = open(r'..\inputs\input_day4.txt')
lines = f.readlines()
f.close()

f = open(r'..\inputs\input_day4_test.txt')
test = f.readlines()
f.close()

test_answer = 4512
test_2_answer = 1924


# Parse input file to separate out initial draws of bingo and bingo grids
def get_grids(data):
    draws = []
    grid_id = -1
    grids = []

    # Loop over each row of input file
    for i, row in enumerate(data):
        # If first row, create list of numbers drawn
        if i == 0:
            draws = [int(j) for j in row.split(',')]
        # Skip blank lines, increase grid_id
        elif row.strip() == '':
            grid_id += 1
            grids.append([])
            continue
        # Creating bingo grids for each grid_id
        else:
            grids[grid_id].append([int(j) for j in row.split()])
    # Make grids numpy arrays
    for i in range(len(grids)):
        grids[i] = np.array(grids[i])
    return draws, grids


def solve_part_1(data):

    # Get draw values and list of grids
    draws, grids = get_grids(data)
    # Will be tracking selected values with Numpy Array of 1s (selected) and 0s (unselected) for each grid
    # Will do a Numpy sum across each axis to see if bingo has occurred (sum is 5)
    selected_grids = [np.zeros((5, 5), dtype=int) for i in grids]

    winner = False
    winner_grid_id = 0
    winner_draw_id = 0
    # Loop through each draw
    for draw_id, draw in enumerate(draws):
        # Loop through each grid
        for grid_id, grid in enumerate(grids):
            # Add together current drawn grid with new Boolean grid for the current draw
            selected_grids[grid_id] = (draw == grid) + selected_grids[grid_id]
            # Calculating sum in each axis (columns and rows)
            col_sums = np.sum(selected_grids[grid_id], axis=0)
            row_sums = np.sum(selected_grids[grid_id], axis=1)
            # If there is a 5 anywhere, this current grid and draw is a winner, set flags and break out of for loop
            if any(row_sums == 5) | any(col_sums == 5):
                winner = True
                winner_grid_id = grid_id
                winner_draw_id = draw_id
                break
        # If grid was a winner, break out of drawing loop
        if winner:
            break

    # Calculate the sum of the unmarked values of the winning grid (where they are 0 in the selected_grid)
    sum_unmarked = np.sum(grids[winner_grid_id][selected_grids[winner_grid_id] == 0])

    print('Winning draw is {}, winning grid is {}, sum of unmarked numbers on grid {}, '
          'product of winning draw and sum is {}.'.format(draws[winner_draw_id], winner_grid_id, sum_unmarked,
                                                          draws[winner_draw_id] * sum_unmarked))
    # Return product of winning draw number and sum of unmarked numbers of winning grid
    return draws[winner_draw_id] * sum_unmarked


def solve_part_2(data):

    # Get draw values and list of grids
    draws, grids = get_grids(data)
    # Will be tracking selected values with Numpy Array of 1s (selected) and 0s (unselected) for each grid
    # Will do a Numpy sum across each axis to see if bingo has occurred (sum is 5)
    selected_grids = [np.zeros((5, 5), dtype=int) for i in grids]
    # Tracking of winning grid_ids so will not continue to draw numbers from them
    winner_grid_ids = []
    # Tracking products of winning draw numbers and sum of unmarked numbers on winning grids
    product_values = []

    # Loop through each draw
    for draw_id, draw in enumerate(draws):
        # Loop through each grid
        for grid_id, grid in enumerate(grids):
            # Check to see if grid has already won; if so continue
            if grid_id in winner_grid_ids:
                continue
            # Add together current drawn grid with new Boolean grid for the current draw
            selected_grids[grid_id] = (draw == grid) + selected_grids[grid_id]
            # Calculating sum in each axis (columns and rows)
            col_sums = np.sum(selected_grids[grid_id], axis=0)
            row_sums = np.sum(selected_grids[grid_id], axis=1)
            # If there is a 5 anywhere, this current grid and draw is a winner
            if any(row_sums == 5) | any(col_sums == 5):
                # Calculate sum of unmarked numbers in current grid
                sum_unmarked = np.sum(grid[selected_grids[grid_id] == 0])
                # Add grid_id to winner_grid_ids so numbers will not continue to be drawn from it
                winner_grid_ids.append(grid_id)
                # Add product of draw number and sum of unmarked number to tracking list
                product_values.append(draw * sum_unmarked)
        # If all grids are winners, break out of the drawing loop
        if len(winner_grid_ids) == len(grids):
            break

    # The last product_values is the last winning grid, so that is the value that is to be returned
    print('Product of winning draw and sum is {}.'.format(product_values[-1]))
    return product_values[-1]


output_test = solve_part_1(test)
print('Output equal to test output, ', output_test == test_answer)
output = solve_part_1(lines)

output_test_2 = solve_part_2(test)
print('Output equal to test_2 output, ', output_test_2 == test_2_answer)
output_2 = solve_part_2(lines)
