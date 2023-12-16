import numpy as np

test = [[7, 15, 30], [9, 40, 200]]
test_answer = 288

data_input = [[53, 83, 72, 88], [333, 1635, 1289, 1532]]

test_2 = [[71530], [940200]]
test_answer_2 = 71503

data_input_2 = [[53837288], [333163512891532]]


def solve_day(data):
    num_wins = []
    # Loop over each rach and total amount of time for the race
    for race, total_time in enumerate(data[0]):
        num_wins.append(0)
        # Loop over each number of time I could hold the button for
        for button_hold_time in range(total_time):
            # Check if result beats best time, if so, count it
            if button_hold_time * (total_time - button_hold_time) > data[1][race]:
                num_wins[race] += 1
    # Calculate product of number of possible ways to win each race
    prod_num_wins = np.array(num_wins).prod()
    print('Product of number of different ways to win, ', prod_num_wins)

    return num_wins, prod_num_wins


num_wins_test, output_test = solve_day(test)
print('Output equal to test output for part 1, ', output_test == test_answer)
num_wins, output = solve_day(data_input)
num_wins_test_2, output_test_2 = solve_day(test_2)
print('Output equal to test output for part 1, ', output_test_2 == test_answer_2)
num_wins_2, output_2 = solve_day(data_input_2)

