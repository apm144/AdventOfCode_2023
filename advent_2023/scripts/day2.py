import numpy as np
import os

# Read in data, new item for each line
f = open(r'..\inputs\input_day2.txt')
lines = f.readlines()
f.close()

test = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
]
test_answer = 8
test_answer_2 = 2286


def solve_day(data):
    # Dictionary of maximum cubes in game for first puzzle
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    draw_outcomes = {}
    possible_outcomes = {}
    minimum_outcomes = {}
    # Loop through each input row - games played
    for row in data:
        # Start with a possible game - Boolean to indicate whether game is possible or not
        possible = True
        subsets = []
        # Initializing dictionary for current minimum cubes; will get updated during the games/rounds
        minimum_cubes = {'red': 0, 'green': 0, 'blue': 0}
        # Game number is split from rounds by ':'
        game_round_split = row.split(':')
        # Getting game number - second element after space of first element of game_round_split
        game_number = int(game_round_split[0].split()[1])
        # Each round is separated by ';'
        rounds = game_round_split[1].split(';')
        # Looping over each round
        for round in rounds:
            # Each cube is separated by ','
            cubes_split = round.split(',')
            # Making dictionary of this round's draw - color : count (converted to integer)
            draws = {i.split()[1]: int(i.split()[0]) for i in cubes_split}
            subsets.append(draws)
            # Looping through each color for two reasons
            for color, number in draws.items():
                # First puzzle - see if game is possible - if any of the counts of the colors
                # is greater than the maximum, then the game is not possible - possible flag changed to False
                if number > max_cubes[color]:
                    possible = False
                # Second puzzle - increase minimum count if current count is greater
                # than current minimum count
                if number > minimum_cubes[color]:
                    minimum_cubes[color] = number
        # For each game updating dictionaries tracking information - key is game number
        # Outcome of each draw - list of length of number of draws which contain
        # dictionaries of the draws
        draw_outcomes[game_number] = subsets.copy()
        # Outcome of the game if possible or not - Boolean
        possible_outcomes[game_number] = possible
        # Minimum necessary cube count of each color - dictionary of color: minimum count
        minimum_outcomes[game_number] = minimum_cubes.copy()

    # List of game numbers that are possible - include only if Boolean value of dictionary is True
    possible_games = [i for i, j in possible_outcomes.items() if j]
    # List of power of sets for each game - product of minimum counts for each color
    power_of_sets = [np.prod(list(i.values())) for i in minimum_outcomes.values()]
    # Puzzle outputs are the individual sums of these two lists
    print('Sum of game IDs for possible games,', sum(possible_games))
    print('Sum of minimum of power sets of cubes,', sum(power_of_sets))

    return sum(possible_games), sum(power_of_sets)


output_test, output_test_2 = solve_day(test)
print('Output equal to test output, ', output_test == test_answer)
print('Output equal to test_2 output, ', output_test_2 == test_answer_2)
output, output_2 = solve_day(lines)

