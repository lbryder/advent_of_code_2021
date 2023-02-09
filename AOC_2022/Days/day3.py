from timeit import default_timer as timer


def run():
    inputs_path = 'Input/'
    file = open('%sday3.txt' % inputs_path)
    input_lines = file.read().split('\n')
    result = part_1(input_lines)
    # result = part_2(input_lines)

    print(f'{result}')


def part_1(input):
    common_letters = []
    for x in input:
        size = int(len(x) / 2)
        ruc_1 = x[:size]
        ruc_2 = x[size:]
        for letter in set(ruc_1):
            if letter in ruc_2:
                common_letters.append(letter)

    prios = [get_prio(x) for x in common_letters]

    return sum(prios)


def get_prio(x: str) -> int:
    if x.islower():
        return ord(x) - ord('a') + 1
    else:
        return ord(x) - ord('A') + 27


def part_2(input):
    common_letters = []
    for i in range(int(len(input) / 3)):
        ruc_1 = input[i * 3 + 0]
        ruc_2 = input[i * 3 + 1]
        ruc_3 = input[i * 3 + 2]
        for letter in set(ruc_1):
            if letter in ruc_2 and letter in ruc_3:
                common_letters.append(letter)

    prios = [get_prio(x) for x in common_letters]
    return sum(prios)


if __name__ == '__main__':
    start = timer()
    run()
    end = timer()
    print(f'Time spent: {end - start}')
