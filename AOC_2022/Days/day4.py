from timeit import default_timer as timer


def run():
    inputs_path = 'Input/'
    file = open('%sday4.txt' % inputs_path)
    input_lines = file.read().split('\n')
    result = part_1(input_lines)
    result_2 = part_2(input_lines)

    print(f'part1: {result}')
    print(f'part2: {result_2}')


def part_1(input):
    ints = [parse_line(li) for li in input]
    overlaps = [1 if x_1 <= y_1 and x_2 >= y_2 or (y_1 <= x_1 and y_2 >= x_2)
                else 0
                for x_1, x_2, y_1, y_2 in ints]
    print(sum(overlaps))

    contained = []
    for a, b, x, y in ints:
        if a <= x and b >= y:
            contained.append(a)
        elif x <= a and y >= b:
            contained.append(a)

    return len(contained)


def parse_line(line):
    split = line.split(",")
    seg_1 = split[0]
    seg_2 = split[1]
    seg_1_min, seg_1_max = [int(x) for x in seg_1.split("-")]
    seg_2_min, seg_2_max = [int(x) for x in seg_2.split("-")]
    return seg_1_min, seg_1_max, seg_2_min, seg_2_max


def part_2(input):
    contained = []
    ints = [parse_line(li) for li in input]
    overlaps = [1 if x_1 <= y_2 and x_2 >= y_1 or (y_1 <= x_2 and y_2 >= x_1)
                else 0
                for x_1, x_2, y_1, y_2 in ints]
    print(sum(overlaps))



    for line in input:
        seg_1, seg_2 = line.split(",")
        seg_1_min, seg_1_max = [int(x) for x in seg_1.split("-")]
        seg_2_min, seg_2_max = [int(x) for x in seg_2.split("-")]
        if seg_1_min <= seg_2_max and seg_1_max >= seg_2_min:
            contained.append(line)
        elif seg_2_min <= seg_1_max and seg_2_max >= seg_1_min:
            contained.append(line)
    return len(contained)


if __name__ == '__main__':
    start = timer()
    run()
    end = timer()
    print(f'Time spent: {end - start}')
