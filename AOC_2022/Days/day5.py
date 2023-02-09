from timeit import default_timer as timer
import helper as helper

def run():
    inputs_path = 'Input/'
    file = open('%sday5.txt' % inputs_path)
    #input_lines = file.read().split('\n')
    stack_lines, inst_lines = file.read().split('\n\n')
    result_new = part_1_new(stack_lines.split("\n"), inst_lines.split("\n"), False)
    #result = part_1(input_lines, True)
    #result_2 = part_1(input_lines, False)

    print(f'part1: {result_new}')
#    print(f'part1: {result}')
#    print(f'part2: {result_2}')


def part_1(input, is_part_1=False):
    instructions = False
    rows = []
    inst_list = []
    for line in input:
        if line == "":
            instructions = True
        elif instructions:
            move_s, to_s = line.split(" from ")
            movve = int(move_s.split(" ")[1])
            from_stack, to_stack = map(int, to_s.split(" to "))
            inst_list.append((movve, from_stack, to_stack))
        else:
            row_i = []
            for i, val in enumerate(line):
                if (i - 1) % 4 == 0:
                    row_i.append(val)
            rows.append(row_i)

    rows.reverse()

    stacks = [[] for _ in range(len(rows))]
    for row_i in rows:
        for j, val in enumerate(row_i):
            if val != " ":
                stacks[j].append(val)

    for n, a, b in inst_list:
        move_crates = stacks[a - 1][-n:]
        stacks[a - 1] = stacks[a - 1][:-n]
        if is_part_1:
            move_crates.reverse()
        stacks[b - 1].extend(move_crates)
        # print(stacks)

    top_crates = "".join([x[-1] for x in stacks])
    return top_crates

def part_1_new(stack_lines, inst_lines, is_part_1):

    stacks = parse_stacks(stack_lines)
    inst_list = parse_instructions(inst_lines)

    for n, a, b in inst_list:
        move_crates = stacks[a - 1][-n:]
        stacks[a - 1] = stacks[a - 1][:-n]
        if is_part_1:
            move_crates.reverse()
        stacks[b - 1].extend(move_crates)

    top_crates = "".join([x[-1] for x in stacks])
    return top_crates


def parse_instructions(inst_lines):
    inst_list = []
    for inst_line in inst_lines:
        move_string, to_string = inst_line.split(" from ")
        move_int = int(move_string.split(" ")[1])
        from_stack, to_stack = map(int, to_string.split(" to "))
        inst_list.append((move_int, from_stack, to_stack))
    return inst_list


def parse_stacks(stack_lines):
    rows = []
    for s_line in stack_lines:
        row_i = [x for i, x in enumerate(s_line) if i % 4 == 1]
        rows.append(row_i)
    rows.reverse()
    stacks = [[] for _ in range(len(rows))]
    for row_i in rows:
        for j, val in enumerate(row_i):
            if val != " ":
                stacks[j].append(val)
    return stacks


if __name__ == '__main__':
    start = timer()
    run()
    end = timer()
    print(f'Time spent: {end - start}')
