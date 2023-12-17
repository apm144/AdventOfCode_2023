import numpy as np
from collections import Counter
import os
import re

# Read in data, new item for each line
f = open(r'..\inputs\input_day7.txt')
lines = f.readlines()
f.close()
lines = [i.strip() for i in lines]

test = [
    '32T3K 765',
    'T55J5 684',
    'KK677 28',
    'KTJJT 220',
    'QQQJA 483',
]
test_answer = 6440
test_answer_2 = 5905


# Function that will rank each group of cards
def rank_cards(grouped_hands, alphabet_order):
    rank_start = 1
    sorted_hands = {}
    total_sum = 0
    # Loop over each type and List of [hand, bid]
    for type, hands_and_bids in grouped_hands.items():
        hands = [i[0] for i in hands_and_bids]
        # This return a sorted tuple of (hand, sort_index).
        # The sort index will be used to then sort the bids.
        sorted_index_hands = [i for i in
                              sorted(enumerate(hands), key=lambda word: [alphabet_order.index(c) for c in word[1]])]
        # For each type, create list of list of [hand, bid] that is sorted
        sorted_hands[type] = [[i[1], hands_and_bids[i[0]][1]] for i in sorted_index_hands]
        # Create rank of the hands, goes from rank_start to len(# of hands in type)
        # Reverses order because we want the lower rank to be the worse hand
        ranks = [i + rank_start for i in range(len(sorted_hands[type]))][::-1]
        # Sorted dictionary now also contains rank information
        sorted_hands[type] = [[sorted_hands[type][i][0], sorted_hands[type][i][1], ranks[i]] for i in range(len(ranks))]
        # Summing up rank*bid for this type
        type_sum = sum([ranks[i] * sorted_hands[type][i][1] for i in range(len(ranks))])
        # Increasing rank start for next type
        rank_start += len(ranks)
        total_sum += type_sum
    return total_sum, sorted_hands


# Function that identifies hand type based on number of unique cards in each hand
def get_hand_type(hand):
    dict_hand = dict(Counter(hand))
    if len(dict_hand) == 5:
        return 'high_card'
    if len(dict_hand) == 4:
        return 'one_pair'
    if len(dict_hand) == 3:  # two pair, three of kind
        # If one of them has 3 card count
        if 3 in dict_hand.values():
            return 'three_of_a_kind'
        return 'two_pair'
    if len(dict_hand) == 2:  # full house, four of kind
        # If one of them has a 4 card count
        if 4 in dict_hand.values():
            return 'four_of_a_kind'
        return 'full_house'
    return 'five_of_a_kind'


def solve_day_part_1(data):
    # split, identify, and group into hand type
    grouped_hands = {
        'high_card': [],
        'one_pair': [],
        'two_pair': [],
        'three_of_a_kind': [],
        'full_house': [],
        'four_of_a_kind': [],
        'five_of_a_kind': []
    }
    # Loop over each row (hand)
    for row in data:
        hand = row.split()[0]
        bid = int(row.split()[1])
        # Get hand type from function
        # Add hand and bid to dictionary that groups hands based on type
        hand_type = get_hand_type(hand)
        grouped_hands[hand_type].append([hand, bid])

    # Set sort order and create sorted dictionary
    # Function also tallies the total sum of the rank*bid
    alphabet_order = 'AKQJT98765432'
    total_sum, sorted_hands = rank_cards(grouped_hands, alphabet_order)

    print('Sum of winnings, ', total_sum)

    return total_sum, sorted_hands


def solve_day_part_2(data):
    # split, identify, and group into hand type
    grouped_hands = {
        'high_card': [],
        'one_pair': [],
        'two_pair': [],
        'three_of_a_kind': [],
        'full_house': [],
        'four_of_a_kind': [],
        'five_of_a_kind': [],
    }
    hand_ranking = {
        'high_card': 0,
        'one_pair': 1,
        'two_pair': 2,
        'three_of_a_kind': 3,
        'full_house': 4,
        'four_of_a_kind': 5,
        'five_of_a_kind': 6,
    }
    # Loop over each row (hand)
    for row in data:
        hand = row.split()[0]
        bid = int(row.split()[1])
        best_hand = 'high_card'
        orig_hand = hand
        # Check if J is in the hand
        # If so, do a loop to replace J with any other card in the hand to find the
        # best hand
        # If not, will just find the hand type from the current cards
        if 'J' in hand:
            # Looping over every letter in the hand and replacing J with that
            # letter to see if that change will make a better hand than current
            # best hand.  Even if letter is J, algorithm will still work, it will
            # just identify the original hand type
            for letter in set(hand):
                temp_hand = orig_hand.replace('J', letter)
                temp_type = get_hand_type(temp_hand)
                # Check to see if this new hand is better than the current best hand
                # If so, update to the new best hand type
                if hand_ranking[temp_type] > hand_ranking[best_hand]:
                    best_hand = temp_type
        else:
            best_hand = get_hand_type(hand)
        # Add hand and bid to dictionary that groups hands based on type
        grouped_hands[best_hand].append([hand, bid])

    # Set sort order and create sorted dictionary
    # Function also tallies the total sum of the rank*bid
    alphabet_order = 'AKQT98765432J'
    total_sum, sorted_hands = rank_cards(grouped_hands, alphabet_order)

    print('Sum of winnings, ', total_sum)

    return total_sum, sorted_hands


output_test, sorted_hands_test = solve_day_part_1(test)
print('Output equal to test output for part 1, ', output_test == test_answer)
output, sorted_hands = solve_day_part_1(lines)
output_test_2, sorted_hands_test_2 = solve_day_part_2(test)
print('Output equal to test output for part 2, ', output_test_2 == test_answer_2)
output_2, sorted_hands_2 = solve_day_part_2(lines)

