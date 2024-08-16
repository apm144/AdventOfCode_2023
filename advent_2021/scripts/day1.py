import numpy as np

# Read in data, new item for each line
f = open(r'..\inputs\input_day1.txt')
lines = f.readlines()
f.close()

test = [
    '199',
    '200',
    '208',
    '210',
    '200',
    '207',
    '240',
    '269',
    '260',
    '263',
]
test_answer = 7
test_2_answer = 5


# Function to determine how many increases given input Numpy Array
def get_count(values):
    # Create difference array
    dif_values = np.diff(values)
    # Determine if difference results in an increase
    count = [1 for i in dif_values if i > 0]
    # Return sum of increases
    return sum(count)


def solve_day_1_part_1(data):
    # Create list of integers (input are list of strings of numbers)
    values = np.array([int(i) for i in data])
    # Get number of increases from get_count function
    result = get_count(values)
    print('Number of increases is ', result)
    # Return result
    return result


def solve_day_1_part_2(data):
    # Create list of integers (input are list of strings of numbers)
    values = np.array([int(i) for i in data])
    # Create list of sums of three adjacent values
    grouped_values_sum = []
    for i in range(len(values) - 2):
        grouped_values_sum.append(values[i] + values[i + 1] + values[i + 2])
    # Get number of increases from get_count function
    result = get_count(grouped_values_sum)
    print('Number of increases within group of three is ', result)
    # Return result
    return result


output_test = solve_day_1_part_1(test)
print('Output equal to test output, ', output_test == test_answer)
output = solve_day_1_part_1(lines)

output_test_2 = solve_day_1_part_2(test)
print('Output equal to test_2 output, ', output_test_2 == test_2_answer)
output_2 = solve_day_1_part_2(lines)
