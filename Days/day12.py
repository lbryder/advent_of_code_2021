def run():
    file = open('Inputs/day12.txt')
    input = file.read().splitlines()
    count = part_1(input)
    # count = part_2(input)

    print(f'{count}')


def part_1(lines):
    roads = {}
    paths = []
    for line in lines:
        s, e = line.split("-")
        end_points = roads.get(s, set())
        end_points.add(e)
        start_points = roads.get(e, set())
        start_points.add(s)
        roads.update({s: end_points})
        roads.update({e: start_points})

    start_point = "start"
    path = [start_point]
    paths = all_next_steps(paths, path, roads)
    paths.sort()

    # [print(path) for path in paths]
    return len(paths)


def all_next_steps(paths, path, roads):
    new_paths = []
    next_roads = roads.get(path[-1], [])
    max_lower_paths = max([path.count(p) for p in path if p.islower()])
    for r in next_roads:
        if (r == 'end'):
            new_paths.append(path+[r])
        elif (r == 'start'):
            pass
        elif (r.islower() and path.count(r)+max_lower_paths > 2):
            # If a lower path is already taken twice, and this is taken at least once (i.e. 1+2 > 2)
            pass
        else:
            new_paths.extend(all_next_steps(paths, path+[r], roads))

    return new_paths

