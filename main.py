from timeit import default_timer as timer

#from AOC_2022.Days import day1
from Days import day13

if __name__ == '__main__':
    start = timer()
    day13.run()
    end = timer()
    print(f'Time spent: {end - start}')
