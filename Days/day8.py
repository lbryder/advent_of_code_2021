def day_8():
    file = open('../Inputs/day8.txt')
    input = file.read().split('\n')
    # count = part_1(input)
    count = part_2(input)

    print(f'{count}')


def part_1(lines):
    uniq_number_in_output = 0
    for line in lines:
        split = line.split("|")
        signals = split[0].split(" ")
        output = split[1].split(" ")
        for out in output:
            if (len(out) in (2,3,4,7)):
                uniq_number_in_output +=1

    return uniq_number_in_output


def getCorrespondingNumber(transformed_chars):
    number_mapping = [
        [set('abcefg'), 0],
        [set('cf'), 1],
        [set('acdeg'), 2],
        [set('acdfg'), 3],
        [set('bcdf'), 4],
        [set('abdfg'), 5],
        [set('abdefg'), 6],
        [set('acf'), 7],
        [set('abcdefg'), 8],
        [set('abcdfg'), 9]
    ]

    for number in number_mapping:
        if number[0] == set(transformed_chars):
            return number[1]
    pass


def part_2(lines):
    # uniq_number_in_output = 0
    total_of_out = 0

    for line in lines:
        split = line.split("|")
        signals = split[0].strip().split(" ")
        output = split[1].strip().split(" ")

        segments = {}
        for signal in signals:
            no_of_segments = len(signal)
            signal_chars = list(signal)
            all_signal_chars = segments.get(no_of_segments, list())
            all_signal_chars.extend(signal_chars)
            segments[no_of_segments] = all_signal_chars

        char_mapping = {'a':None,'b': None,'c': None,'d': None,'e': None,'f': None,'g': None}

        for key in char_mapping.keys():
            maps_to = None
            if (key in segments[3] and key not in segments[2]):
                maps_to = 'a'
            elif (key in segments[4] and segments[5].count(key) == 1 and key not in segments[2]):
                maps_to = 'b'
            elif (key in segments[2] and segments[6].count(key) == 2):
                maps_to = 'c'
            elif (key in segments[4] and segments[5].count(key) == 3):
                maps_to = 'd'
            elif (segments[6].count(key) == 2 and key not in segments[4]):
                maps_to = 'e'
            elif (segments[2].count(key) == 1 and segments[6].count(key) == 3):
                maps_to = 'f'
            elif (segments[6].count(key) == 3 and key not in segments[4] and key not in segments[3]):
                maps_to = 'g'

            char_mapping[key] = maps_to

        out_number = ''
        for out in output:
            transformed_chars = ''
            for out_char in out:
                transformed_chars += char_mapping.get(out_char)

            trans_out = getCorrespondingNumber(transformed_chars)
            out_number += str(trans_out)

        total_of_out += int(out_number)

    return total_of_out
