from timeit import default_timer as timer
import helper as helper


def run():
    inputs_path = 'Input/'
    test_file = open('%stest-input.txt' % inputs_path)
    test_lines = test_file.read().split('\n')

    test_result = part_1(test_lines)
    print(f'Test-part1: {test_result}')
    test_result_2 = part_2(test_lines)
    print(f'Test-part2: {test_result_2}')

    file = open('%sday14.txt' % inputs_path)
    input_lines = file.read().split('\n')

    result = part_1(input_lines)
    print(f'part1: {result}')
    result_2 = part_2(input_lines)
    print(f'part2: {result_2}')


def parse_line(line):
    # s = line
    # int(s)
    return line


def get_next_pos(x, y, map):
    if map.get((x, y + 1)) is None:
        return x, y + 1
    elif map.get((x - 1, y + 1)) is None:
        return x - 1, y + 1
    elif map.get((x + 1, y + 1)) is None:
        return x + 1, y + 1
    else:
        map.update({(x, y): "O"})
        return x, y


def part_1(input):
    start_x, start_y = 500, 0

    map = get_map(input)
    max_depth = max([p[1] for p in map.keys()])
    unit_of_sands = 0
    while True:
        x, y = start_x, start_y
        sand_moving = True
        while sand_moving:
            n_x, n_y = get_next_pos(x, y, map)
            if (n_x, n_y) == (x, y):
                sand_moving = False
                unit_of_sands += 1
            elif n_y > max_depth:
                return unit_of_sands
            else:
                x, y = n_x, n_y

    pass


def get_map(input_lines):
    map = dict()
    for line in input_lines:
        points = [(int(a), int(b)) for a, b in [y.split(",") for y in line.split(" -> ")]]
        start_p = points[0]
        x, y = start_p
        map.update({(x, y): "#"})
        for p in points[1:]:
            x_diff = p[0] - x
            y_diff = p[1] - y
            x_dir = int(x_diff / max(abs(x_diff), 1))
            y_dir = int(y_diff / max(abs(y_diff), 1))
            for i in range(max(abs(x_diff), abs(y_diff))):
                x = x + x_dir
                y = y + y_dir
                map.update({(x, y): "#"})
    return map


def part_2(input):
    start_x, start_y = 500, 0

    map = get_map(input)
    max_depth = max([p[1] for p in map.keys()])
    unit_of_sands = 0
    while True:
        x, y = start_x, start_y
        sand_moving = True
        while sand_moving:
            n_x, n_y = get_next_pos(x, y, map)
            if (n_x, n_y) == (x, y):
                sand_moving = False
                unit_of_sands += 1
                if n_y == start_y:
                    return unit_of_sands
            elif n_y > max_depth+1:
                map.update({(n_x, n_y): "#"})
            else:
                x, y = n_x, n_y

    return 0


if __name__ == '__main__':
    start = timer()
    run()
    end = timer()
    print(f'Time spent: {end - start}')
