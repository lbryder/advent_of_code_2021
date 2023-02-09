from timeit import default_timer as timer
import helper as helper
from collections import defaultdict


def run():
    inputs_path = 'Input/'
    file = open('%sday7.txt' % inputs_path)
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
    parents = []
    subfolders = defaultdict(list)
    sizes = dict()
    for inp in input:
        if inp[0] == "$":
            comm = inp[2:4]
            if comm == "cd":
                comm, direct = inp[2:].split(" ")
                if direct == "..":
                    parents.pop()
                elif direct == '/':
                    parents.append(".")
                else:
                    parents.append(direct)
        else:
            x, y = inp.split(" ")
            path = get_path(parents)
            if x == "dir":
                subfolders[path].append(y)
            else:
                sizes[path] = sizes.get(path, 0) + int(x)

    total_size = dict()
    for folder in subfolders.keys():
        calc_size(folder, subfolders, sizes, total_size)

    max_size = max(total_size.values())
    need_limit = 30000000 - (70000000 - max_size)
    # print(total_size)
    return min([x[1] for x in total_size.items() if x[1] >= need_limit])


def calc_size(folder, subfolders, sizes, total_sizes):
    total = total_sizes.get(folder, 0)
    if total != 0:
        return total
    size = sizes.get(folder, 0)
    for f in subfolders.get(folder, []):
        size += calc_size(folder + "/" + f, subfolders, sizes, total_sizes)
    total_sizes.update({folder: size})
    return size


def get_path(parents):
    return "/".join(parents)


def part_2(input):
    lines = [parse_line(li) for li in input]

    return 0


if __name__ == '__main__':
    start = timer()
    run()
    end = timer()
    print(f'Time spent: {end - start}')
