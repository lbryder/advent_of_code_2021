from timeit import default_timer as timer
import helper as helper
import heapq


def run():
    inputs_path = 'Input/'
    file = open('%sday12.txt' % inputs_path)
    input_lines = file.read().split('\n')
    result = part_1(input_lines)
    print(f'part1: {result}')

    result_2 = part_2(input_lines)
    print(f'part2: {result_2}')


def part_1(input):
    start_r, start_c = 0, 0
    end_r, end_c = 0, 0
    grid = [[c for c in r] for r in input]
    for r, a in enumerate(grid):
        for c, b in enumerate(a):
            if b[0] == 'S':
                start_r, start_c = r, c
            elif b[0] == 'E':
                end_r, end_c = r, c

    return calc_shortest(grid, start_r, start_c, end_r, end_c)


def calc_shortest(grid, start_r: int, start_c: int, end_r, end_c):
    return calc_shortest_2(grid, start_r, start_c, end_r, end_c)[0]


def calc_shortest_2(grid, start_r: int, start_c: int, end_r, end_c):
    dists = [[None for _ in r] for r in grid]
    paths = [[[] for _ in r] for r in grid]
    visited = set()
    queue = []

    x, y = start_r, start_c
    dists[x][y] = 0
    heapq.heappush(queue, (0, x, y))

    while len(queue) > 0:
        _, x, y = heapq.heappop(queue)
        cur_val = grid[x][y][0]
        cur_dist = dists[x][y]
        cur_path = []
        list(paths[x][y])
        cur_path.append((x, y))

        neighbours = helper.get_neighbours(grid, x, y)
        for r, c in neighbours:
            val = grid[r][c]
            dist = dists[r][c]
            new_dist = cur_dist + 1
            if (dist is None or new_dist < dist) and can_move(cur_val, val):
                dists[r][c] = new_dist
                paths[r][c] = cur_path
                if (r, c) not in visited:
                    heapq.heappush(queue, (new_dist, r, c))
            elif r == end_r and c == end_c and can_move(cur_val, val):
                return cur_dist, cur_path
        visited.add((x, y))
    return (None, [])


def can_move(cur_h, val):
    v = getHeight(val)
    h = getHeight(cur_h)
    return v - h < 2


def getHeight(letter):
    if letter == 'S':
        return ord('a')
    elif letter == 'E':
        return ord('z')
    else:
        return ord(letter)


def part_2(input):
    end_r, end_c = 0, 0
    grid = [[c for c in r] for r in input]
    starts = []
    for r, a in enumerate(grid):
        for c, b in enumerate(a):
            if b[0] == 'S':
                starts.append((r, c))
            elif b[0] == 'E':
                end_r, end_c = r, c
            elif b[0] == 'a':
                starts.append((r, c))
    paths = [calc_shortest(grid, x[0], x[1], end_r, end_c) for x in starts]
    completed_paths = [x for x in paths if x is not None]
    # print_pathgrid(completed_paths, grid)
    return min(completed_paths)


def print_pathgrid(completed_paths, grid):
    completed_paths.sort(key=lambda x: x[0])
    dist, path = completed_paths[0]
    s = ""
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if (i, j) not in path:
                s += "."
            else:
                s += c
        s += "\n"
    print(s)

if __name__ == '__main__':
    start = timer()
    run()
    end = timer()
    print(f'Time spent: {end - start}')
