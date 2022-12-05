import advent


def priority(c: str):
    return ord(c)-ord('A')+27 if 'A' <= c <= 'Z' else ord(c) - ord('a') + 1


def get_sum_priority(input: str):
    packs = input.splitlines()
    compartments = [(set(p[:len(p)//2]), set(p[len(p)//2:])) for p in packs]
    common = [c[0].intersection(c[1]) for c in compartments]

    return sum((priority(el.pop()) for el in common))


def get_group_priority(input: str):
    packs = [set(p) for p in input.splitlines()]
    s = 0
    for i in range(0, len(packs),3):
        s += priority(packs[i].intersection(packs[i+1]).intersection(packs[i+2]).pop())
    return s


advent.run(get_sum_priority)
advent.run(get_group_priority)
