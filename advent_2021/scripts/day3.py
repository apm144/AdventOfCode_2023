import numpy as np

# Read in data, new item for each line
f = open(r'..\inputs\input_day3.txt')
lines = f.readlines()
f.close()

test = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]
test_answer = 198
test_2_answer = 230


def solve_part_1(data):
    # Determine number of bits to check
    num_bits = len(data[0].strip())
    # Initialize final value with all zeros
    gamma_rate = ['0'] * num_bits
    epsilon_rate = ['0'] * num_bits
    # Loop over each bit
    for i in range(num_bits):
        zero_count = 0
        one_count = 0
        # Loop over each row to determine counts of zeros and ones for current bit
        for row in data:
            if row[i] == '0':
                zero_count += 1
            else:
                one_count += 1
        # Determine which bit to set for each rate:
        # if more ones, set gamma rate to 1;
        # if more zeros set epsilon rate to 1
        if one_count > zero_count:
            gamma_rate[i] = '1'
        else:
            epsilon_rate[i] = '1'
    # Convert gamma_rate and epsilon_rate to decimal
    gamma_rate_dec = int(''.join(gamma_rate), 2)
    epsilon_rate_dec = int(''.join(epsilon_rate), 2)
    print('Gamma rate is {}, epsilon rate is {}, product of both is {}.'.format(gamma_rate_dec, epsilon_rate_dec,
                                                                                gamma_rate_dec * epsilon_rate_dec))
    # Return product of gamma_rate and epsilon_rate
    return gamma_rate_dec * epsilon_rate_dec


def solve_part_2(data):
    # Determine number of bits to check
    num_bits = len(data[0].strip())
    data = np.array(data)
    # Initializing indices to for tracking oxygen generation and CO2 scrubber
    # While following criteria, will retain acceptable binary codes using these indices
    keep_ids_ox_gen = np.array(list(range(len(data))))
    keep_ids_co2_scrub = np.array(list(range(len(data))))
    # Loop over each bit to identify counts and compare them to determine which is larger
    # Will track indices of ones and zeros for current bit
    for i in range(num_bits):
        zero_ids = []
        one_ids = []
        # Loop over each row and keep indice in zero_ids list or one_ids list depending if it is zero or one, respectively
        for j, row in enumerate(data[keep_ids_ox_gen]):
            if row[i] == '0':
                zero_ids.append(j)
            else:
                one_ids.append(j)
        # Update indices based on criteria
        # for Oxygen Gen, keep larger number of indices with tie going to ones
        # Update keep_ids based on criteria
        if len(one_ids) >= len(zero_ids):
            keep_ids_ox_gen = keep_ids_ox_gen[one_ids]
        else:
            keep_ids_ox_gen = keep_ids_ox_gen[zero_ids]
        # If down to one entry, stop
        if len(keep_ids_ox_gen) == 1:
            break

    # Same algorithm for CO2 scrubber except for criteria
    for i in range(num_bits):
        zero_ids = []
        one_ids = []
        for j, row in enumerate(data[keep_ids_co2_scrub]):
            if row[i] == '0':
                zero_ids.append(j)
            else:
                one_ids.append(j)
        # Update indices based on criteria
        # for CO2 scrubber, keep smaller number of indices with tie going to zeros
        # Update keep_ids based on criteria
        if len(one_ids) >= len(zero_ids):
            keep_ids_co2_scrub = keep_ids_co2_scrub[zero_ids]
        else:
            keep_ids_co2_scrub = keep_ids_co2_scrub[one_ids]
        if len(keep_ids_co2_scrub) == 1:
            break

    # Convert ox_gen and co2_scrub to decimal
    ox_gen_dec = int(''.join(data[keep_ids_ox_gen][0]), 2)
    co2_scrub_dec = int(''.join(data[keep_ids_co2_scrub][0]), 2)

    print('Oxygen gen rate is {}, CO2 scrub rate is {}, product of both is {}.'.format(ox_gen_dec, co2_scrub_dec,
                                                                                       ox_gen_dec * co2_scrub_dec))
    # Return product of ox_gen and co2_scrub
    return ox_gen_dec * co2_scrub_dec


output_test = solve_part_1(test)
print('Output equal to test output, ', output_test == test_answer)
output = solve_part_1(lines)

output_test_2 = solve_part_2(test)
print('Output equal to test_2 output, ', output_test_2 == test_2_answer)
output_2 = solve_part_2(lines)
