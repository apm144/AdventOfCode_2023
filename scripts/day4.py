import numpy as np
import os
import re

# Read in data, new item for each line
f = open(r'..\inputs\input_day4.txt')
lines = f.readlines()
f.close()
lines = [i.strip() for i in lines]

test = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
]
test_answer = 13
test_answer_2 = 30


def solve_day_part_1(data):
    card_winning_nums = {}
    # Loop over each row
    for row in data:
        # Get card ID (integer) from splitting with ':' and card ID will be 2nd element on the first part of split
        card_nums = row.split(':')
        card_id = int(card_nums[0].split()[1])
        # Getting winning numbers and game numbers; put them in np.arrays
        winning_nums = np.array([int(i) for i in card_nums[1].split('|')[0].split()])
        game_nums = np.array([int(i) for i in card_nums[1].split('|')[1].split()])
        # Identifying winning numbers, adding to tracking dictionary
        card_winning_nums[card_id] = game_nums[np.isin(game_nums, winning_nums)]

    # Get sum of winning numbers
    running_sum = 0
    winning_vals = {}
    # Loop over each game
    for card_id, winning_nums in card_winning_nums.items():
        sum_val = 0
        # Count winning numbers and increase by factor of two each subsequent win
        # beyond the first
        for num in winning_nums:
            if sum_val == 0:
                sum_val = 1
            else:
                sum_val *= 2
        running_sum += sum_val
        winning_vals[card_id] = sum_val

    print('Sum of winning points, ', running_sum)

    return running_sum


def solve_day_part_2(data):
    number_of_cards = {}
    # Loop over each row
    for row in data:
        # Identify winning numbers from each game, same as part 1
        card_nums = row.split(':')
        card_id = int(card_nums[0].split()[1])
        winning_nums = np.array([int(i) for i in card_nums[1].split('|')[0].split()])
        game_nums = np.array([int(i) for i in card_nums[1].split('|')[1].split()])
        winning_numbers = game_nums[np.isin(game_nums, winning_nums)]

        # Tracking number of original scratch cards and copies
        # Every scratch card has only one original but any number of copies
        if card_id not in number_of_cards.keys():
            number_of_cards[card_id] = {'orig': 1, 'copies': 0}
        else:
            number_of_cards[card_id]['orig'] = 1

        # Current number of copies of a scratch card are the number of originals
        # plus number of copies
        current_copies = number_of_cards[card_id]['copies'] + number_of_cards[card_id]['orig']
        # Loop over each winning number, that will be the number of subsequent
        # scratch cards that also need to be increased by the number of current_copies
        for i in range(1, len(winning_numbers) + 1):
            # If new scratch card, the number of copies will be the number of current_copies
            # If new scratch card, orig will be set to 0 because it will be increased when the
            # scratch card is reviewed above
            if i + card_id not in number_of_cards.keys():
                number_of_cards[i + card_id] = {'orig': 0, 'copies': current_copies}
            # If not new scratch card, the number of copies is increased by current_copies
            else:
                number_of_cards[i + card_id]['copies'] += current_copies

    # The total number of scratch cards is then the number of copies and originals of all cards
    print('Sum of number of cards, ', sum([i['copies'] + i['orig'] for i in number_of_cards.values()]))
    return sum([i['copies'] + i['orig'] for i in number_of_cards.values()])


output_test = solve_day_part_1(test)
print('Output equal to test output for part 1, ', output_test == test_answer)
output = solve_day_part_1(lines)
output_test_2 = solve_day_part_2(test)
print('Output equal to test output for part 2, ', output_test_2 == test_answer_2)
output_2 = solve_day_part_2(lines)

