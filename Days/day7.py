def dist(x, i):
    x_i = abs(x - i)*(abs(x - i) + 1)
    abs1 = abs(int(x_i / 2))
    return abs1


def part_1(input):
    crabs = list(map(int, input[0].split(",")))
    costs = []
    for i in range(max(crabs)):
        crabs_part_1 = [abs(x - i) for x in crabs]
        crabs_ = [dist(x, i) for x in crabs]
        cost = sum(crabs_)
        costs.append(cost)

    return min(costs)



def run():
    file = open('Inputs/day7.txt')
    input = file.read().split('\n')
    count = part_1(input)
    # count = part_2(input)

    print(f'{count}')


