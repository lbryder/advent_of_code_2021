from timeit import default_timer as timer
import helper as helper


def run():
    inputs_path = 'Input/'
    file = open('%sday6.txt' % inputs_path)

    input_lines = file.read().split('\n')

    result = part_1(input_lines)
    result_2 = part_2(input_lines)

    print(f'part1: {result}')
    print(f'part2: {result_2}')


def parse_line(line):
    # s = line
    # int(s)
    return line


def part_1(input):
    load_sum = 0
    res_list = []
    chars = set()
    idx = 0

    iterable = input[0]
    for i, l in enumerate(iterable):
        chars = set(iterable[i:i + 4])
        if len(chars) == 4:
            return i+4

    return 0


def part_2(input):
    iterable = input[0]
    for i, l in enumerate(iterable):
        chars = set(iterable[i:i + 14])
        if len(chars) == 14:
            return i+14
    return 0


if __name__ == '__main__':
    start = timer()
    run()
    end = timer()
    print(f'Time spent: {end - start}')
