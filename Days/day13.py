def run():
    file = open('Inputs/day13.txt')
    input = file.read().splitlines()
    count = part_1(input)

    print(f'{count}')


def fold_points_2(point_2, fold):
    axis = fold[0]
    num = fold[1]
    new_points = set()
    for p in point_2:
        x, y = p
        if axis == 'x':
            # p_x = p[0]
            # p_y = p[1]
            if x > num:
                x = 2 * num - x
            # else:
            #     x = p_x
            #
            # y = p_y
        else:
            # p_x = p[0]
            # p_y = p[1]
            if y > num:
                y = 2 * num - y
            # else:
            #     y = p_y

            # x = p_x

        new_points.add((x, y))
    return new_points


def part_1(lines):
    folds = []
    points = {}
    instruction = False
    point_2 = set()
    for i, line in enumerate(lines):
        if (line == ""):
            instruction = True
        elif not instruction:
            x, y = line.split(",")
            row = int(y)
            column = int(x)
            points_in_row = points.get(row, set())
            points_in_row.add(column)
            points.update({row: points_in_row})
            point_2.add((column, row))
        else:
            fold_sub_string = line.replace("fold along ", "")
            (coord, num) = fold_sub_string.split("=")
            folds.append((coord, int(num)))

    # printPoints(points)
    for fold in folds:
        print(fold)

    for fold in folds:
        point_2 = fold_points_2(point_2, fold)

    # part 1
    #     fold = folds[0]
    #     new_points = fold_points_2(point_2, fold)
    #     no_of_points = len(new_points)

    print(" ")
    printPoints(point_2)
    no_of_points = len(point_2)

    return no_of_points


def printPoints(points):
    for row in range(max([p[1] for p in points]) + 1):
        row_line = ""
        for column in range(max([p[0] for p in points]) + 1):
            if (column, row) in points:
                point_str = "#"
            else:
                point_str = "."
            row_line += point_str
            if (column+1) % 5 == 0:
                row_line += " "
        print(row_line)


def getNumberOfColumns(sets):
    max_row = 0
    for s in sets.values():
        max_row = max(max(s), max_row)

    return max_row


