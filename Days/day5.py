from collections import Counter


def part_1(input):
    line_points = []
    lines = []
    for inp_line in input:
        p_0, p_1 = inp_line.split(" -> ")
        x_0, y_0 = map(int, p_0.split(","))
        x_1, y_1 = map(int, p_1.split(","))
        lines.append([x_0,y_0,x_1,y_1])

        if (x_0 == x_1 or y_0 == y_1):
            for x in range(min(x_0,x_1), max(x_0, x_1)+1):
                for y in range(min(y_0, y_1), max(y_0, y_1)+1):
                    line_points.append((x,y))
        else:
            # Diagonal.
            direction = ((x_1 - x_0) / abs(x_1 - x_0), (y_1 - y_0) / abs(y_1 - y_0))
            for i in range(abs(x_1 - x_0)+1):
                line_points.append((int(x_0 + direction[0]*i),int(y_0 + direction[1]*i)))

    occurences = Counter(line_points)
    overlap_points = [x for x in occurences if occurences.get(x) > 1]
    numver = len(overlap_points)

    return numver



def run():
    file = open('Inputs/day5.txt')
    input = file.read().split('\n')
    count = part_1(input)
    # count = part_2(input)

    print(f'{count}')


