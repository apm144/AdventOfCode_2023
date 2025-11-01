import numpy as np

# Read in data, new item for each line
f = open(r'..\inputs\input_day1.txt')
lines = f.readlines()
f.close()

test = [
    '(())',
]
test_answer = 0
test2 = [
    '(((',
]
test_2_answer = 3


# function that counts ( and )
def solve_day_1_part_1(data):
    # Separate each character in string into individual items in list
    list_of_char = list(data[0])
    counter_left = 0
    counter_right = 0
    # Loop over each character and counts ( and ) into separate counters
    for paren in list_of_char:
        if paren == '(':
            counter_left = counter_left + 1
        else:
            counter_right = counter_right + 1
    # difference between floor counters is the floor Santa is on
    floor_number = counter_left - counter_right
    return floor_number


# Function to determine the step in instructions when Santa enters basement (floor -1)
def solve_day_1_part_2(data):
    # Separate each character in string into individual items in list
    list_of_char = list(data[0])
    counter_left = 0
    counter_right = 0
    step_counter = 1
    # Loop over each character and counts ( and ) into separate counters
    for paren in list_of_char:
        if paren == '(':
            counter_left = counter_left + 1
        else:
            counter_right = counter_right + 1
        # Check if Santa enters basement (floor -1)
        current_floor = counter_left - counter_right
        if current_floor == -1:
            # If he does, exit loop and return current step in instruction
            break
        # if not, increase step in instruction continue
        step_counter += 1
    return step_counter


output_test = solve_day_1_part_1(test)
print('Output equal to test output, ', output_test == test_answer, output_test)
output_test_2 = solve_day_1_part_1(test2)
print('Output equal to test output, ', output_test_2 == test_2_answer, output_test_2)
output = solve_day_1_part_1(lines)
print('Floor Santa goes to', output)


output_2 = solve_day_1_part_2(lines)
print('Position that Santa enters basement is', output_2)
