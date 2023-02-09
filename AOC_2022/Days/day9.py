from timeit import default_timer as timer
import helper as helper


def run():
    inputs_path = 'Input/'
    file = open('%sday9.txt' % inputs_path)
    input_lines = file.read().split('\n')
    result = part_1(input_lines)
    # result_2 = part_2(input_lines)

    print(f'part1: {result}')
    # print(f'part2: {result_2}')


def parse_line(line):
    direction, moves = line.split(" ")
    return direction, int(moves)


def part_1(input):
    is_part_1 = False
    knots = [(0, 0)] * 10

    lines = [parse_line(li) for li in input]

    visited = list()
    visited.append((0, 0))
    for d, moves in lines:
        vect = (0, 0)
        if d == "U":
            vect = (0, 1)
        elif d == "R":
            vect = (1, 0)
        elif d == "L":
            vect = (-1, 0)
        elif d == "D":
            vect = (0, -1)

        for _ in range(moves):
            for j in range(len(knots)):
                t_x, t_y = knots[j]
                if j == 0:
                    x, y = vect
                    t_x += x
                    t_y += y
                    t_p = (t_x, t_y)
                else:
                    h_x, h_y = knots[j - 1]
                    t_p = calc_tail(t_x, t_y, h_x, h_y)
                    if (not is_part_1 and j == 9) or (is_part_1 and j == 1):
                        visited.append(t_p)

                knots[j] = t_p

    no_of_visited = len(set(visited))
    return no_of_visited


def calc_tail(t_x, t_y, h_x, h_y):
    y_diff = h_y - t_y
    x_diff = h_x - t_x
    abs_y = abs(y_diff)
    abs_x = abs(x_diff)
    if abs_x < 2 and abs_y < 2:
        return t_x, t_y
    elif x_diff == 0:
        y_new = y_diff // abs_y
        t_y += y_new
    elif y_diff == 0:
        x_new = x_diff // abs_x
        t_x += x_new
    else:
        y_new = y_diff // abs_y
        x_new = x_diff // abs_x
        t_x += x_new
        t_y += y_new

    return t_x, t_y


if __name__ == '__main__':
    start = timer()
    run()
    end = timer()
    print(f'Time spent: {end - start}')
