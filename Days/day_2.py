def part_2(input):
    hori = 0
    depth = 0
    aim = 0

    for line in input:
        split = line.split(' ')
        command = split[0]
        val = int(split[1])

        if command == 'forward':
            hori += val
            depth += (aim*val)
        elif command == 'down':
            aim += val
        elif command == 'up':
            aim -= val
        else:
            pass

    return hori * depth

def day_2():
    file = open('../Inputs/day2.txt')
    input = file.read().split('\n')
    # count = part_1(input)
    count = part_2(input)

    print(f'{count}')

def part_1(input):
    hori = 0
    depth = 0

    for line in input:
        split = line.split(' ')
        command = split[0]
        val = int(split[1])

        if command == 'forward':
            hori += val
        elif command == 'down':
            depth +=val
        elif command == 'up':
            depth -= val
        else:
            pass

    return hori * depth
