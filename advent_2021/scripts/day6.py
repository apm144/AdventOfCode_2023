import numpy as np

# Read in data, new item for each line
f = open(r'..\inputs\input_day6.txt')
lines = f.readlines()
f.close()

test = [
    '3,4,3,1,2',
]

test_answer = 5934
test_2_answer = 26984457539


def solve_day(data, num_days):

    # Get the list of initial values from input file
    inital_values = [int(i) for i in data[0].split(',')]

    # Create two tracking lists - one for number of lanternfish that have 6 day cycle,
    # and one for number with 8 day cycle
    six_day_inter_timer = [0] * 7
    eight_day_inter_timer = [0] * 9

    # From initial values, populate the six-day list by counting how many have how many days (index) left in cycle
    for val in inital_values:
        six_day_inter_timer[val] += 1

    # Loop over each day
    for day in range(1, num_days + 1):
        # Initialize how many new fish are created from each day cycle
        new_fish_eight_day = 0
        new_fish_six_day = 0
        # Loop over each interval time for the six-day cycle fish
        for inter_time in range(len(six_day_inter_timer)):
            # If the index is 0, these fish will do two things
            # 1. They will get their cycle reset for the six-day cycle (move to index 6)
            # 2. They will spawn new lanternfish in the eight-day cycle (move to index 8 of eight-day cycle)
            # This will be done after we cycle through each list, so right now the number of fish will be tracked
            if inter_time == 0:
                new_fish_six_day = six_day_inter_timer[inter_time]
            # If the index is not 0, the number in the current index will be moved down one index
            else:
                six_day_inter_timer[inter_time - 1] = six_day_inter_timer[inter_time]
        # Loop over each interval time for the six-day cycle fish
        for inter_time in range(len(eight_day_inter_timer)):
            # If the index is 0, these fish will do two things
            # 1. They will get their cycle reset but to the six-day cycle (move to index 6 of six-day cycle)
            # 2. They will spawn new lanternfish in the eight-day cycle (move to index 8 of eight-day cycle)
            # This will be done after we cycle through each list, so right now the number of fish will be tracked
            if inter_time == 0:
                new_fish_eight_day = eight_day_inter_timer[inter_time]
            # If the index is not 0, the number in the current index will be moved down one index
            else:
                eight_day_inter_timer[inter_time - 1] = eight_day_inter_timer[inter_time]
        # For the new lanternfish, each of the tracked values above will be added together to the end of each cycle
        six_day_inter_timer[6] = new_fish_six_day + new_fish_eight_day
        eight_day_inter_timer[8] = new_fish_six_day + new_fish_eight_day


    print('Number of fish after 80days is {}.'.format(sum(six_day_inter_timer) + sum(eight_day_inter_timer)))
    # Return the total number of lanternfish after the input number of days
    return sum(six_day_inter_timer) + sum(eight_day_inter_timer)


output_test = solve_day(test, 80)
print('Output equal to test output, ', output_test == test_answer)
output = solve_day(lines, 80)

output_test_2 = solve_day(test, 256)
print('Output equal to test_2 output, ', output_test_2 == test_2_answer)
output_2 = solve_day(lines, 256)
