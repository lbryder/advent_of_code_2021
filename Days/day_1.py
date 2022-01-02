def day_1(name):
    file = open('../Inputs/day1.txt')
    input = file.read().split('\n')
    # count = part_1(input)
    count = part_2_real(input)

    print(f'{count}')


def part_1(input):
    old = None
    count = 0
    for line in input:
        if old and int(line) > old:
            count += 1

        old = int(line)
    return count

def part_2_real(input):
    values = []
    for idx, val in enumerate(input):
        if idx < 1:
            pass
        elif idx == len(input)-1:
            pass
        else:
            value = int(input[idx-1]) + int(val) + int(input[idx+1])
            values.append(value)

    count = 0
    old = None
    for val in values:
        if old and val > old:
            count += 1
        old = val
    return count
