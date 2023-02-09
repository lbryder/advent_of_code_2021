from timeit import default_timer as timer
import helper as helper


def run():
    inputs_path = 'Input/'
    file = open('%sday11.txt' % inputs_path)
    input_lines = file.read().split('\n\n')
    result = part_1(input_lines)
    result_2 = part_2(input_lines)

    print(f'part1: {result}')
    print(f'part2: {result_2}')


def parse_group(group_lines):
    group = group_lines.split("\n")
    monkey = int(group[0].split(" ")[1][:-1])
    items = [int(x) for x in group[1].split(":")[1].split(",")]
    operation = lambda old: eval(group[2].split(" = ")[1])
    test = int(group[3].split(" by ")[1])
    true_monkey = int(group[4].split("monkey ")[1])
    false_monkey = int(group[5].split("monkey ")[1])

    return (monkey, items, operation, test, true_monkey, false_monkey)


def part_1(input):
    lines = [parse_group(li) for li in input]
    throws = [0] * len(lines)
    rounds = 20
    monkey_items = dict()
    strategies = dict()

    for m, i, o, t, t_m, f_m in lines:
        monkey_items.update({m: i})
        strategies.update({m: (o, t, t_m, f_m)})

    for r in range(rounds):
        for i, x in enumerate(lines):
            items = monkey_items[i]
            operation = strategies[i][0]
            test = strategies[i][1]
            true_m = strategies[i][2]
            false_m = strategies[i][3]
            for it in items:
                new_level = operation(it) // 3
                new_monkey = true_m if (new_level % test) == 0 else false_m
                monkey_items[new_monkey].append(new_level)
                throws[i] = throws[i] + 1
            monkey_items.update({i: []})

    throws.sort()
    return throws[-1]*throws[-2]


def use_operation(operation, it, divisors):
    for i, x in enumerate(it):
        it[i] = operation(x) % divisors[i]
    # return [operation(it[i]) % d for i, d in enumerate(divisors)]
    return it


def part_2(input):
    lines = [parse_group(li) for li in input]
    divisors = []
    throws = [0] * len(lines)
    rounds = 10000
    monkey_items = dict()
    strategies = dict()

    for m, i, o, t, t_m, f_m in lines:
        items = [[x] * len(lines) for x in i]
        monkey_items.update({m: items})
        strategies.update({m: (o, t, t_m, f_m)})
        divisors.append(t)

    for r in range(rounds):
        # if r % 1000 == 0:
        #     print("round: " + str(r))
        for i, _ in enumerate(lines):
            items = monkey_items[i]
            operation = strategies[i][0]
            # test = strategies[i][1]
            true_m = strategies[i][2]
            false_m = strategies[i][3]
            for it in items:
                new_level = use_operation(operation, it, divisors)
                new_monkey = true_m if new_level[i] == 0 else false_m
                monkey_items[new_monkey].append(new_level)
                throws[i] = throws[i] + 1
            monkey_items.update({i: []})

    # return throws
    throws.sort()
    return throws[-1] * throws[-2]


if __name__ == '__main__':
    start = timer()
    run()
    end = timer()
    print(f'Time spent: {end - start}')
