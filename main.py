from timeit import default_timer as timer

from Days import day15

if __name__ == '__main__':
    start = timer()
    day15.run()
    end = timer()
    print(f'Time spent: {end - start}')
