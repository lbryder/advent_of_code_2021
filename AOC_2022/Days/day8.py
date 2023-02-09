from timeit import default_timer as timer
import helper as helper


def run():
    inputs_path = 'Input/'
    file = open('%sday8.txt' % inputs_path)
    input_lines = file.read().split('\n')
    result = part_1(input_lines)
    result_2 = part_2(input_lines)

    print(f'part1: {result}')
    print(f'part2: {result_2}')


def parse_line(line):
    # s = line
    # int(s)
    return line


def is_visible(grid, i, j):
    tree = grid[i][j]
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for x, y in dirs:
        no_of_rows = len(grid)
        no_of_cols = len(grid[0])

        r_i = i + x
        c_i = j + y
        trees = []
        while (0 <= r_i < no_of_rows) and (0 <= c_i < no_of_cols):
            trees.append(grid[r_i][c_i])
            r_i += x
            c_i += y

        exists_higher = [x for x in trees if x >= tree]
        if len(exists_higher) == 0:
            return True

    return False


def score(grid, i, j):
    tree = grid[i][j]
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    scores = []
    for x, y in dirs:
        no_of_rows = len(grid)
        no_of_cols = len(grid[0])

        r_i = i + x
        c_i = j + y
        trees = []
        while (0 <= r_i < no_of_rows) and (0 <= c_i < no_of_cols):
            t = grid[r_i][c_i]
            trees.append(t)
            r_i += x
            c_i += y
            if t >= tree:
                break

        scores.append(len(trees))

    score = 1
    for q in scores:
        score = score * q

    return score


def part_1(input):
    tree_sum = 0
    vis_trees = []

    grid = []
    for r in input:
        row = [int(c) for c in r]
        grid.append(row)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            visible = is_visible(grid, i, j)
            if visible:
                vis_trees.append(grid[i][j])

    # return vis_trees
    return len(vis_trees)


def part_2(input):
    tree_sum = 0
    vis_trees = []
    scores = []

    grid = []
    for r in input:
        row = [int(c) for c in r]
        grid.append(row)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            scores.append(score(grid, i, j))

    # return vis_trees
    return max(scores)


if __name__ == '__main__':
    start = timer()
    run()
    end = timer()
    print(f'Time spent: {end - start}')
