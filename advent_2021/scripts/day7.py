import numpy as np

# Read in data, new item for each line
f = open(r'..\inputs\input_day7.txt')
lines = f.readlines()
f.close()

test = [
    '16,1,2,0,4,2,7,1,2,14',
]

test_answer = 37
test_2_answer = 168


def solve_part_1(data):
    # Parse input file to get initial horizontal positions, make them integers
    horizontal_pos = np.array([int(i) for i in data[0].split(',')])

    # Loop over all possible positions (up to maximum), get the absolute distance between current position and
    # initial position, then sum up those differences.  Result will be list with index as the position the crabs are
    # moving to.  The best position will be the minimum.
    sums = [sum(abs(horizontal_pos - i)) for i in range(max(horizontal_pos))]

    print('Minimum position to move to is {}, minimum fuel usage is {}.'.format(np.argmin(sums), min(sums)))
    # Return the sum of the minimum position
    return min(sums)


def solve_part_2(data):
    # Parse input file to get initial horizontal positions, make them integers
    horizontal_pos = np.array([int(i) for i in data[0].split(',')])

    # Create cumulative sum array.  This will be the fuel that crabs use to move that distance away
    # from current position
    max_pos = max(horizontal_pos)
    cum_sum_array = np.cumsum(range(max_pos + 1))
    # Initializing final fuel usage list
    total_usage = []

    # Loop over all possible positions up to max
    for i in range(max_pos):
        # Determine the absolute distance between current point and initial position of all crabs
        diff = abs(horizontal_pos - i)
        # The fuel usage for each crab is the cumulative sum from their current position
        fuel_usage = cum_sum_array[diff]
        # The total usage for this position of all crabs is the sum of each individual fuel usage
        total_usage.append(sum(fuel_usage))

    print('Minimum position to move to is {}, minimum fuel usage is {}.'.format(np.argmin(total_usage),
                                                                                min(total_usage)))
    # Return the sum of the minimum fuel usage
    return min(total_usage)


output_test = solve_part_1(test)
print('Output equal to test output, ', output_test == test_answer)
output = solve_part_1(lines)

output_test_2 = solve_part_2(test)
print('Output equal to test_2 output, ', output_test_2 == test_2_answer)
output_2 = solve_part_2(lines)
