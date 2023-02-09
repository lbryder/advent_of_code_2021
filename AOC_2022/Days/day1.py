from timeit import default_timer as timer


def run():
    inputs_path = 'Input/'
    file = open('%sday1.txt' % inputs_path)
    input_lines = file.read().split('\n')
    count = solve_2(input_lines)

    print(f'{count}')


def solve(input):
    load_sum = 0
    elves = []
    for i in range(len(input)):
        if input[i] == "":
            elves.append(load_sum)
            load_sum = 0
        else:
            load_sum += int(input[i])

    # return max(elves)
    elves.sort()
    elves.reverse()
    return elves[0] + elves[1] + elves[2]

def solve_2(input):
    longline = " ".join(input)
    split_ = [y.split(" ") for y in longline.split("  ")]
    sums = [sum([int(x) for x in y]) for y in split_]
    return max(sums)

if __name__ == '__main__':
    start = timer()
    run()
    end = timer()
    print(f'Time spent: {end - start}')

