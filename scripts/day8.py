from math import lcm

# Read in data, new item for each line
f = open(r'..\inputs\input_day8.txt')
lines = f.readlines()
f.close()
lines = [i.strip() for i in lines]

test_1 = [
    'RL',
    '',
    'AAA = (BBB, CCC)',
    'BBB = (DDD, EEE)',
    'CCC = (ZZZ, GGG)',
    'DDD = (DDD, DDD)',
    'EEE = (EEE, EEE)',
    'GGG = (GGG, GGG)',
    'ZZZ = (ZZZ, ZZZ)',
]
test_2 = [
    'LLR',
    '',
    'AAA = (BBB, BBB)',
    'BBB = (AAA, ZZZ)',
    'ZZZ = (ZZZ, ZZZ)',
]
test_3 = [
    'LR',
    '',
    '11A = (11B, XXX)',
    '11B = (XXX, 11Z)',
    '11Z = (11B, XXX)',
    '22A = (22B, XXX)',
    '22B = (22C, 22C)',
    '22C = (22Z, 22Z)',
    '22Z = (22B, 22B)',
    'XXX = (XXX, XXX)',
]
test_answer_1 = 2
test_answer_2 = 6
test_answer_3 = 6


# Function to read in the input and return list of instructions (converted to
# integers for indices of the tuples) and mapping for instructions - turn into
# dictionary to look up L/R list given key.
def parse_input(data):
    moves = []
    # Mapping L and R to which element in tuple to use
    moves_mapping = {'L': 0, 'R': 1}
    mapping = {}
    # Loop over each row of input
    for i, row in enumerate(data):
        # If first row, read in directions (L/R)
        if i == 0:
            # Convert L/R to integers for index of tuples
            moves = [moves_mapping[move] for move in row]
        # Skip blank row
        elif row == '':
            continue
        # Read in mapping information
        else:
            # Find identifier (key) for dictionary
            identifier = row.split(' = ')[0]
            # Split tuple into list of strings
            mapping[identifier] = row.split(' = ')[1].strip('()').split(', ')
    return moves, mapping

def solve_day_part_1(data, start='AAA'):
    # Get input data
    moves, mapping = parse_input(data)

    counter = 0
    curr_element = start
    # While loop to control number of times to loop over directions
    # Exit when result is 'ZZZ'
    while curr_element != 'ZZZ':
        # Loop over list of moves
        for move in moves:
            # Update current_element and increase counter
            curr_element = mapping[curr_element][move]
            counter += 1
            # Break out of loop if element is 'ZZZ'
            if curr_element == 'ZZZ':
                break

    print('Number of steps, ', counter)
    # Return counter (how many steps)
    return counter


def solve_day_part_2(data):
    # Get input data
    moves, mapping = parse_input(data)

    # The idea is to identify how many times each of the starting elements take
    # to end (find an element that ends with 'Z').  This is done for each.
    # The end result when ALL end with 'Z' will be the least common multiple of
    # all of these.
    # NOTE: I was surprised that this worked.  The counter at which the first and
    # subsequent times a ends-with-z occurs for any given are spaced the same.
    # I expected the first to be shifted by some amount, but it was not so simply
    # finding the LCM of the list of numbers works.

    # Get the list of starting elements - any that end in 'A'
    start_elements = [i for i in mapping.keys() if i.endswith('A')]
    multiples = []
    # Loop over each starting element
    for start_element in start_elements:
        counter = 0
        curr_element = start_element
        # While loop to control number of times to loop over directions
        # Exit when result ends with 'Z'
        while not curr_element.endswith('Z'):
            # Loop over list of moves
            for move in moves:
                # Update current_element and increase counter
                curr_element = mapping[curr_element][move]
                counter += 1
                # Break out of loop if element ends with 'Z'
                if curr_element.endswith('Z'):
                    break
        # For each starting element, add its multiple to list
        multiples.append(counter)
    # Answer when ALL end in 'Z' is the least common multiple of all the numbers
    puzzle_answer = lcm(*multiples)

    # # Brute force method, answer on order of 10 trillion - did not complete
    # counter = 0
    # curr_elements = [i for i in mapping.keys() if i.endswith('A')]
    # while not all([i.endswith('Z') for i in curr_elements]):
    #     for move in moves:
    #         curr_elements = [mapping[i][move] for i in curr_elements]
    #         counter += 1
    #         if any([i.endswith('Z') for i in curr_elements]):
    #             print(curr_elements, counter)
    #         if all([i.endswith('Z') for i in curr_elements]):
    #             break
    # print('Number of steps, ', counter)
    # return counter
    print('Number of steps, ', puzzle_answer)
    return puzzle_answer


output_test = solve_day_part_1(test_1)
print('Output equal to test_1 output for part 1, ', output_test == test_answer_1)
output_test_2 = solve_day_part_1(test_2)
print('Output equal to test_2 output for part 1, ', output_test_2 == test_answer_2)
output = solve_day_part_1(lines)
output_test_3 = solve_day_part_2(test_3)
print('Output equal to test_2 output for part 2, ', output_test_3 == test_answer_3)
output_2 = solve_day_part_2(lines)

