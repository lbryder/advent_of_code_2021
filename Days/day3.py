def part_1(input):


    length = len(input[0])
    zero_bit_rates = [0]*length
    one_bit_rates = [0]*length
    for line in input:
        for index in range(len(line)):
            bit = int(line[index])
            if bit == 1:
                one_bit_rates[index] = one_bit_rates[index] + 1
            else:
                zero_bit_rates[index] = zero_bit_rates[index] + 1

    gamma_rate = ''
    epsilon_rate = ''

    for i in range(length):
        if one_bit_rates[i] > zero_bit_rates[i]:
            gammabit = '1'
            epsilonbit = '0'
        else:
            gammabit = '0'
            epsilonbit = '1'

        gamma_rate += gammabit
        epsilon_rate += epsilonbit

    gamma_int = int(gamma_rate, 2)
    epsilon_int = int(epsilon_rate, 2)

    return gamma_int * epsilon_int


def get_CO2(input):
    valid_lines = input
    for i in range(len(input)):
        one_lines = []
        zero_lines = []
        for line in valid_lines:
            if int(line[i]) == 1:
                one_lines.append(line)
            else:
                zero_lines.append(line)

        len_ones = len(one_lines)
        len_zeros = len(zero_lines)
        if len_ones < len_zeros:
            valid_lines = one_lines
        else:
            valid_lines = zero_lines

        if len(valid_lines) == 1:
            return valid_lines[0]

    return valid_lines[0]


def part_2(input):

    oxy_line = get_Oxy(input)
    co_line = get_CO2(input)

    product = int(oxy_line, 2) * int(co_line, 2)
    return product


def get_Oxy(input):
    valid_lines = input
    for i in range(len(input)):
        one_lines = []
        zero_lines = []
        for line in valid_lines:
            if int(line[i]) == 1:
                one_lines.append(line)
            else:
                zero_lines.append(line)

        len_ones = len(one_lines)
        len_zeros = len(zero_lines)
        if len_ones >= len_zeros:
            valid_lines = one_lines
        else:
            valid_lines = zero_lines

        if len(valid_lines) == 1:
            return valid_lines[0]

    return valid_lines[0]


def run():
    file = open('Inputs/day3.txt')
    input = file.read().split('\n')
    # count = part_1(input)
    count = part_2(input)

    print(f'{count}')