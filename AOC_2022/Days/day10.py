from timeit import default_timer as timer
import helper as helper

def run():
    inputs_path = 'Input/'
    file = open('%sday10.txt' % inputs_path)
    input_lines = file.read().split('\n')
    result = part_1(input_lines)
    result_2 = part_2(input_lines)

    print(f'part1: {result}')
    print(f'part2: {result_2}')

def parse_line(line):
    # s = line
    # int(s)
    return line


def add_cycle(cycles, x, res_list):
    print("Cycles " + str(cycles) + " , X: " + str(x))
    cycle_row = (cycles-1) % 40
    pixel = '#' if x-1 <= cycle_row <= x+1 else "."
    if cycle_row == 39:
        res_list.append(cycles * x)
        return pixel + "\n"
    return pixel


def part_1(input):
    x = 1
    cycles = 0
    res_list = []
    s = "\n"

    lines = [parse_line(li) for li in input]
    overlaps = [x for x in lines]

    for line in input:
        if line == "noop":
            cycles +=1
            s += add_cycle(cycles, x, res_list)
        else:
            v = int(line.split(" ")[1])
            cycles +=1
            s += add_cycle(cycles, x, res_list)
            cycles +=1
            s += add_cycle(cycles, x, res_list)
            x +=v

    return s
    # return sum(res_list)
    # return (res_list)

def part_2(input):
    lines = [parse_line(li) for li in input]

    return 0

if __name__ == '__main__':
    start = timer()
    run()
    end = timer()
    print(f'Time spent: {end - start}')

