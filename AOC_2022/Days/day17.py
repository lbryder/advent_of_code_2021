from timeit import default_timer as timer
import helper as helper

def run():
    inputs_path = 'Input/'
    test_file = open('%stest-input.txt' % inputs_path)
    test_input = test_file.read().split('\n')

    test_result = part_1(test_input)
    print(f'Test-part1: {test_result}')
    test_result_2 = part_2(test_input)
    print(f'Test-part2: {test_result_2}')

    file = open('%sday16.txt' % inputs_path)
    input_lines = file.read().split('\n')
    result = part_1(input_lines)
    print(f'part1: {result}')

    result_2 = part_2(input_lines)
    print(f'part2: {result_2}')


def parse_line(line):
    # s = line
    # int(s)
    return line

def part_1(input):
    load_sum = 0
    res_list = []

    lines = [parse_line(li) for li in input]
    overlaps = [x for x in lines]

    for x in lines:
        res_list.append(x)

    return len(res_list)

def part_2(input):
    lines = [parse_line(li) for li in input]

    return 0

if __name__ == '__main__':
    start = timer()
    run()
    end = timer()
    print(f'Time spent: {end - start}')

