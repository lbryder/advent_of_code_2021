from timeit import default_timer as timer
import helper as helper
from functools import cmp_to_key


def run():
    inputs_path = 'Input/'
    file = open('%sday13.txt' % inputs_path)
    test_file = open('%stest-input.txt' % inputs_path)
    input_lines = file.read().split('\n\n')
    test_lines = test_file.read().split('\n\n')

    test_result = part_1(test_lines)
    print(f'Test-part1: {test_result}')
    test_result_2 = part_2(test_lines)
    print(f'Test-part2: {test_result_2}')

    result = part_1(input_lines)
    print(f'part1: {result}')

    result_2 = part_2(input_lines)
    print(f'part2: {result_2}')


def parse_line(line):
    # s = line
    # int(s)
    return line


def compare_pair(left, right):
    if isinstance(left, int):
        if isinstance(right, int):
            if left < right:
                # print(left, right, "true")
                return -1
            elif right < left:
                # print(left, right, "false")
                return 1
            else:
                return 0
        else:
            return compare_pair([left], right)
    elif isinstance(right, int):
        return compare_pair(left, [right])
    else:
        for i, x_i in enumerate(left):
            if len(right) <= i:
                return 1
            else:
                r_i = right[i]
                sub_compare = compare_pair(x_i, r_i)
                if sub_compare != 0:
                    return sub_compare

    return -1 if len(right) > len(left) else 0


def part_1(input):
    load_sum = 0
    res_list = []
    order_index = []
    parsed_signals = parse_signals(input, order_index)

    return sum(order_index)


def parse_signals(input, order_index):
    parsed_signals = []
    for p_i, pair in enumerate(input):
        res_pair = []
        for line in pair.split("\n"):
            res_line = parse_nested_lists(line)
            res_pair.append(res_line[0])

        left, right = res_pair
        in_order = compare_pair(left, right) < 0
        if in_order:
            order_index.append(p_i + 1)
        parsed_signals.append(left)
        parsed_signals.append(right)
    return parsed_signals


def parse_nested_lists(line):
    res_line = []
    get_next_list(line, res_line)
    return res_line


def get_next_list(line, cur_result):
    line_list = []
    s = ''
    i = 1
    while line is not None and i < len(line):
        x = line[i]
        if x == '[':
            line = get_next_list(line[i:], line_list)
            i = 0
        elif x == ']':
            if len(s) > 0:
                line_list.append(int(s))
            cur_result.append(line_list)
            return line[i:]
        elif x == ',':
            if len(s) > 0:
                line_list.append(int(s))
            s = ""
        elif x.isdigit():
            s += x
        i += 1


def part_2(input):
    parsed_signals = parse_signals(input, [])

    sig_1 = [[2]]
    parsed_signals.append(sig_1)
    sig_2 = [[6]]
    parsed_signals.append(sig_2)
    parsed_signals.sort(key=cmp_to_key(compare_pair))
    v_sig1 = parsed_signals.index(sig_1) + 1
    v_sig2 = parsed_signals.index(sig_2) + 1
    return v_sig1 * v_sig2


if __name__ == '__main__':
    start = timer()
    run()
    end = timer()
    print(f'Time spent: {end - start}')
