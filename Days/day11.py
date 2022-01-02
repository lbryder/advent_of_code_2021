def run():
    file = open('Inputs/day11.txt')
    input = file.read().split('\n')
    count = part_1(input)
    # count = part_2(input)

    print(f'{count}')


def step(octos):
    flash_points = []
    for i, row in enumerate(octos):
        for j, octo in enumerate(row):
            new_octo = octo + 1
            if new_octo > 9:
                flash_points.append([i, j])
            octos[i][j] = new_octo
    flashes = 0

    while not len(flash_points) < 1:
        flash = flash_points.pop(0)
        x = flash[0]
        y = flash[1]
        octos[x][y] = 0
        flashes +=1
        for i in range(max(x - 1, 0), min(len(octos), x + 2)):
            for j in range(max(y - 1, 0), min(len(octos[0]), y + 2)):
                octo = octos[i][j]
                if (0 < octo):
                    octo += 1
                if octo == 10:
                    flash_points.append([i,j])
                octos[i][j] = octo

    return flashes


def part_1(lines):
    octos = []
    for line in lines:
        octo_row = []
        for num in line:
            octo_row.append(int(num))
        octos.append(octo_row)

    flashed = 0
    for row in octos:
        print(row)

    i = 0
    no_of_octos = len(octos) * len(octos[0])
    while (True):
        i += 1
        new_flash = step(octos)
        flashed += new_flash
        if (new_flash == no_of_octos):
            return i

        # if (i+1) % 10 == 0:
        #     print(f" - Step {i} ---")
        #     for row in octos:
        #         print(row)

    return flashed
