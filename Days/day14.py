from collections import Counter, defaultdict


def run():
    file = open('../Inputs/day14.txt')
    input = file.read().splitlines()
    count = part_1(input)

    print(f'{count}')


def do_inserts_2(occ_dict, rules_2):
    new_dict = {}
    for k in occ_dict.keys():
        # new_dict.update({k: occ_dict.get(k)})
        for r in rules_2.get(k):
            new_dict.update({r: new_dict.get(r, 0) + occ_dict.get(k)})
    return new_dict


def count_letters(occ_dict, elements):
    count_dict = {}
    for pair in occ_dict:
        occurences = occ_dict.get(pair)
        c = pair[0]
        count_dict.update({c: count_dict.get(c, 0) + occurences})

    # for k in count_dict.keys():
    #     count_dict.update({k: count_dict.get(k)/2})

    start = elements[0]
    end = elements[-1]
    for c in [start, end]:
        count_dict.update({c: count_dict.get(c, 0) + 1})

    return count_dict


def part_1(input):
    is_rules = False
    rules = {}
    rules_2 = {}
    elements = ""
    for line in input:
        if line == "":
            is_rules = True
        elif is_rules:
            match, sub = line.split(" -> ")
            rules.update({match: sub})
            rules_2.update({match: [match[0:1] + sub, sub + match[1]]})
        else:
            elements = line

    occ_dict = {}
    for i in range(len(elements) - 1):
        sub = elements[i: i + 2]
        occ_dict.update({sub: occ_dict.get(sub, 0) + 1})

    for step in range(40):
        occ_dict = do_inserts_2(occ_dict, rules_2)

    letters = count_letters(occ_dict, elements)
    min_occ = min(letters.values())
    max_occ = max(letters.values())
    diff = max_occ - min_occ

    return diff


def do_insert_2(elements, rules):
    new_elements = elements[0:1]
    for i in range(len(elements) - 1):
        sub = elements[i: i + 2]
        insert_str = rules.get(sub)
        new_elements += insert_str
        new_elements += sub[1]

    return new_elements
