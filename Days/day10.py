def run():
    file = open('Inputs/day10.txt')
    input = file.read().split('\n')
    count = part_1(input)
    # count = part_2(input)

    print(f'{count}')


def isValid_1(subList, expected_end):
    i = 0
    ends = []
    while i < len(subList):
        char = subList[i]
        if char == '(':
            match = ')'
        elif char == '[':
            match = ']'
        elif char == '{':
            match = '}'
        elif char == '<':
            match = '>'
        else:
            if expected_end == char:
                # valid
                return (i, None, [])
            else:
                # Error - Wrong char
                return (i, char, [])

        new_idx, err_char, missing_ends = isValid_1(subList[i + 1::], match)
        i += new_idx + 1
        if (err_char is not None):
            # Err char in sub blcok
            return (i, err_char, [])

        ends.extend(missing_ends)
        i += 1

    if expected_end is not None:
        ends.append(expected_end)
    # Might be missing end.
    return (len(subList) - 1, None, ends)


def calculate_end_score(end):
    end_scoring = {')': 1, ']': 2, '}': 3, '>': 4}
    total = 0
    for end_char in end:
        total *= 5
        total += end_scoring.get(end_char)
    return total


def part_1(lines):
    err_chars = []
    char_score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    ends = []
    for line in lines:
        idx, err_char, missing_ends = isValid_1(line, None)
        if err_char is not None:
            err_chars.append(char_score.get(err_char))
        if missing_ends is not None:
            ends.append(missing_ends)

    # return sum(err_chars)
    end_scores = [calculate_end_score(x) for x in ends if len(x) > 0]
    end_scores.sort()
    return end_scores[int(len(end_scores) / 2)]
