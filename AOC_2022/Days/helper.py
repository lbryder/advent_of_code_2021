def test(input):
    return 1


def parse_grid(input):
    grid = []
    for r in input:
        row = [c for c in r.split(",")]
        grid.append(row)

    return grid


def get_neighbours(grid, x, y, diag=False):
    no_of_rows = len(grid)
    no_of_cols = len(grid[0])
    neigbs = set()

    for r_i in range(x - 1, x + 2):
        for c_i in range(y - 1, y + 2):
            if (-1 < r_i < no_of_rows) and (-1 < c_i < no_of_cols) and (diag or x == r_i or y == c_i):
                neigbs.add((r_i, c_i))
    return neigbs
