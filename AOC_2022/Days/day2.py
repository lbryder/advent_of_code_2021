from timeit import default_timer as timer


def run():
    inputs_path = 'Input/'
    file = open('%sday2.txt' % inputs_path)
    input_lines = file.read().split('\n')
    # result = part_1(input_lines)
    result = part_2(input_lines)

    print(f'{result}')


def part_1(input):
    load_sum = 0
    res_list = []

    score = 0
    for line in input:
        split = line.split(' ')
        start = split[0]
        response = split[1]
        if (start == "A"):
            if response == "X":
                score +=1
                score +=3
            elif response == "Y":
                score +=2
                score +=6
            elif response == "Z":
                score +=3
                score +=0
        if (start == "B"):
            if response == "X":
                score +=1
                score +=0
            elif response == "Y":
                score +=2
                score +=3
            elif response == "Z":
                score +=3
                score +=6
        if (start == "C"):
            if response == "X":
                score +=1
                score +=6
            elif response == "Y":
                score +=2
                score +=0
            elif response == "Z":
                score +=3
                score +=3






    return score



def part_2(input):
    score = 0
    for line in input:
        split = line.split(' ')
        start = split[0]
        response = split[1]
        if (start == "A"):
            if response == "X":
                score += 3
                score += 0
            elif response == "Y":
                score += 1
                score += 3
            elif response == "Z":
                score += 2
                score += 6
        if (start == "B"):
            if response == "X":
                score += 1
                score += 0
            elif response == "Y":
                score += 2
                score += 3
            elif response == "Z":
                score += 3
                score += 6
        if (start == "C"):
            if response == "X":
                score += 2
                score += 0
            elif response == "Y":
                score += 3
                score += 3
            elif response == "Z":
                score += 1
                score += 6

    return score

if __name__ == '__main__':
    start = timer()
    run()
    end = timer()
    print(f'Time spent: {end - start}')

