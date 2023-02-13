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

    file = open('%sday15.txt' % inputs_path)
    input_lines = file.read().split('\n')
    result = part_1(input_lines)
    print(f'part1: {result}')

    result_2 = part_2(input_lines)
    print(f'part2: {result_2}')


def parse_line(line):
    sens, beac = line.split(":")
    sens_x, sens_y = [int(x.split("=")[1]) for x in sens.split(",")]
    beac_x, beac_y = [int(x.split("=")[1]) for x in beac.split(",")]

    return [(sens_x, sens_y), (beac_x, beac_y)]


def part_1(input):
    lines = [parse_line(li) for li in input]
    sensor_distances = []
    for sensor, beacon in lines:
        dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        sensor_distances.append([sensor, dist])

    check_row = 2000000

    return count_covered(check_row, sensor_distances)[0]


def count_covered(check_row, sensor_distances):
    y = check_row
    covers = []
    for s in sensor_distances:
        dist_to_add = max(s[1] - abs(y - s[0][1]), 0)
        if dist_to_add > 0:
            min_cover = s[0][0] - dist_to_add
            max_cover = s[0][0] + dist_to_add
            covers.append((min_cover, max_cover))
    covers.sort()

    last_max = None
    no_of_covered = 0
    not_covered = []
    for cover in covers:
        x_min = cover[0]
        x_max = cover[1]

        if last_max is None:
            last_max = x_min

        new_min = max(x_min, last_max)
        if last_max < x_min and x_min < 4_000_000 and x_max > 0:
            not_covered.append((last_max + 1, y))
        if x_max > new_min:
            no_of_covered += x_max - new_min
            last_max = x_max

    return no_of_covered, not_covered


def part_2(input):
    lines = [parse_line(li) for li in input]
    sensor_distances = []
    for sensor, beacon in lines:
        dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        sensor_distances.append([sensor, dist])

    # How to optimize: Only search sensor edges + 1.
    for y in range(4000000):
        result = count_covered(y, sensor_distances)
        not_covered = result[1]
        if len(not_covered) > 0:
            p = not_covered[0]
            return p[0]*4000000+p[1]

    return 0


if __name__ == '__main__':
    start = timer()
    run()
    end = timer()
    print(f'Time spent: {end - start}')
