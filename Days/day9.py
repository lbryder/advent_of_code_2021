def run():
    file = open('../Inputs/day9.txt')
    input = file.read().split('\n')
    count = part_1(input)
    # count = part_2(input)

    print(f'{count}')


def part_1(lines):
    map = []
    for line in lines:
        map_line = []
        for x in line:
            map_line.append(int(x))
        map.append(map_line)

    no_rows = len(map)
    no_of_cols = len(map[0])
    low_points = []
    for x in range(no_rows):
        for y in range(no_of_cols):
            elem = map[x][y]
            above = x > 0 and elem >= map[x - 1][y]
            below = x < no_rows-1 and elem >= map[x + 1][y]
            left = y > 0 and elem >= map[x][y -1]
            right = y < no_of_cols -1 and elem >= map[x][y+1]
            if not (above or below or left or right):
                low_points.append(elem)

    return sum([x+1 for x in low_points])


def part_1(lines):
    map = []
    for line in lines:
        map_line = []
        for x in line:
            map_line.append(int(x))
        map.append(map_line)

    no_rows = len(map)
    no_of_cols = len(map[0])
    low_points = []
    for x in range(no_rows):
        for y in range(no_of_cols):
            elem = map[x][y]
            above = x > 0 and elem >= map[x - 1][y]
            below = x < no_rows-1 and elem >= map[x + 1][y]
            left = y > 0 and elem >= map[x][y -1]
            right = y < no_of_cols -1 and elem >= map[x][y+1]
            if not (above or below or left or right):
                low_points.append([x,y])

    basins = []
    for low in low_points:
        basin_size = calculate_basin(low, map)
        basins.append(basin_size)

    basins.sort(reverse=True)
    prod = 1
    for i in range(3):
        prod *= basins[i]

    return prod

def calculate_basin(low, map):
    x_max = len(map)
    y_max = len(map[0])

    basin_points = [low]
    points_to_check = [low]

    no_rows = len(map)
    no_of_cols = len(map[0])


    while not len(points_to_check) < 1:
        point = points_to_check.pop(0)
        x = point[0]
        y = point[1]
        elem = map[x][y]

        for i in range(-1,2,2):
            point_to_add = []
            if (0 <= x+i < no_rows):
                new_point = [x + i, y]
                if elem <= map[x+i][y] < 9 and new_point not in basin_points:
                    point_to_add.append(new_point)
            if (0 <= y+i < no_of_cols):
                new_point = [x, y + i]
                if elem <= map[x][y+i] < 9 and new_point not in basin_points:
                    point_to_add.append(new_point)

            basin_points.extend(point_to_add)
            points_to_check.extend(point_to_add)

    return len(basin_points)

