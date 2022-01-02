from collections import Counter


def day_6():
    file = open('../Inputs/day6.txt')
    input = file.read().split('\n')
    # count = part_1(input[0])
    count = part_2(input[0])
    # Lanternfish()

    print(f'{count}')


def count_pop(population):
    return len(population)

def part_2(input):
    population_dict = dict(Counter(list(map(int, input.split(',')))))

    # day_tick
    for day in range(256):
        new_population = {}
        for age,count in population_dict.items():
            new_age = age - 1
            if (new_age < 0):
                new_age = 6
                new_population.update({8: count})

            new_count = new_population.get(new_age,0) + count
            new_population.update({new_age: new_count})

        population_dict = new_population

    return sum(population_dict.values())


def part_1(input):
    population = list(map(int, input.split(',')))

    # Day tick
    for day in range(80):
        population = day_tick(population)

    return count_pop(population)


def day_tick(population):
    next_day_population = []
    for fish in population:
        fish_after_step = fish - 1
        if (fish_after_step < 0):
            fish_after_step = 6
            baby_fish = 8
            next_day_population.append(baby_fish)

        next_day_population.append(fish_after_step)

    return next_day_population


class LanternFish():
    pass