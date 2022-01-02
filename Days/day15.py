from collections import Counter, defaultdict


def run():
    input_name = 'day15.txt'
    file = open('Inputs/%s' % input_name)
    input = file.read().splitlines()
    count = part_1(input)

    print(f'{count}')


def part_1(input):
    risks = []
    for line in input:
        risk_line = [int(v) for v in line]
        risks.append(risk_line)

    no_of_rows = len(risks)
    no_of_cols = len(risks[no_of_rows - 1])

    multi_factor = 5
    big_risks = [[] for i in range(no_of_rows*multi_factor)]
    for i in range(0, multi_factor):
        for j in range(0, multi_factor):
            for x in range(no_of_rows):
                add_line = [trans(v+i+j) for v in risks[x]]
                big_risks[x + i * no_of_rows].extend(add_line)

    sums = calc_risk_sums(big_risks)
    no_of_rows_big = len(sums)
    no_of_cols_big = len(sums[no_of_rows_big - 1])

    # NOTE _end ups taking 15 sec for a 100x100 input. To improve, ensure to go through points with lowest dist first. End when encountering target.
    return sums[no_of_rows_big - 1][no_of_cols_big - 1] - sums[0][0]


def calc_risk_sums(risks):
    new_points = [(0, 0)]
    sums = []
    for line in risks:
        sums.append([0 for v in line])

    no_of_rows = len(risks)
    while len(new_points) > 0:
        to_check = new_points.pop(0)
        x_0 = to_check[0]
        y_0 = to_check[1]
        adjacents = []
        for i in range(-1, 2):
            adjacents.append((x_0 + i, y_0))
            adjacents.append((x_0, y_0 + i))

        for x, y in adjacents:
            if -1 < x < no_of_rows and -1 < y < len(risks[x]):
                point = risks[x][y]
                curr_risk = sums[x_0][y_0]
                new_risk = curr_risk + point
                existing_risk = sums[x][y]
                if existing_risk == 0 or existing_risk > new_risk:
                    sums[x][y] = new_risk
                    new_points.append((x, y))

    return sums

def trans(v):
    if v > 9:
        return v % 9
    else:
        return v
