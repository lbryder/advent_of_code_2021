from collections import Counter, defaultdict


def run():
    input_name = 'day16.txt'
    file = open('Inputs/%s' % input_name)
    input = file.read().splitlines()
    count = part_1(input[0])

    print(f'{count}')


def part_1(input):
    number_of_bits = len(input) * 4
    binary = bin(int(input, 16))[2:]
    bits = binary.zfill(number_of_bits)

    digits_bin = parse_packet(bits)

    return digits_bin


def parse_packet(bin_string):
    vers = int(bin_string[:3], 2)
    type_int = int(bin_string[3:6], 2)
    rest_string = bin_string[6:]
    val = 1 if type_int == 1 else 0
    if type_int == 4:
        value = parseValue(rest_string)
        val = value[0]
        rest_string = value[1]
    else:
        len_type = int(rest_string[0])
        if len_type == 0:
            pack_len = 15
            len_end = 1 + pack_len
            total_len = int(rest_string[1:len_end], 2)
            rest_string = rest_string[len_end:]
            stop_length = len(rest_string) - total_len
            while len(rest_string) > stop_length:
                res = parse_packet(rest_string)
                vers += res[0]
                val = calc_val(val, type_int, res[2])
                rest_string = res[3]


        else:
            pack_len = 11
            len_bit_start = 1
            len_end = len_bit_start + pack_len
            num_of_sub = int(rest_string[len_bit_start:len_end], 2)
            rest_string = rest_string[len_end:]
            for i in range(num_of_sub):
                res = parse_packet(rest_string)
                rest_string = res[3]
                val = calc_val(val, type_int, res[2])
                vers += res[0]

    return [vers, type_int, val, rest_string]


def parseValue(bin_string):
    digits = ""
    i = 0
    while i < len(bin_string):
        is_last_digit = bin_string[i] == "0"
        digit_string = bin_string[i + 1:i + 5]
        digits += digit_string
        if is_last_digit:
            value = int(digits, 2)
            return [value, bin_string[i+5:]]
        else:
            i += 5
    return [0, ""]

def calc_val(curr_val, type, new_val):
    if type == 0:
        result_val = curr_val + new_val
    elif type == 1:
        result_val = curr_val * new_val
    elif type == 2:
        if curr_val > 0:
            result_val = min(curr_val, new_val)
        else:
            result_val = new_val
    elif type == 3:
        result_val = max(curr_val, new_val)
    elif type == 5:
        if curr_val == 0:
            result_val = new_val
        elif curr_val > new_val:
            result_val = 1
        else:
            result_val = 0
    elif type == 6:
        if curr_val == 0:
            result_val = new_val
        elif curr_val < new_val:
            result_val = 1
        else:
            result_val = 0
    elif type == 7:
        if curr_val == 0:
            result_val = new_val
        elif curr_val == new_val:
            result_val = 1
        else:
            result_val = 0

    return result_val