from collections import namedtuple

import advent


def count_completely_overlapping_pairs(input: str):
    Interval = namedtuple('Interval', ['start', 'end'])

    def get_interval(pair: str):
        s, e = pair.split('-')
        return Interval(start=int(s), end=int(e))
    lines = [line.split(',') for line in input.splitlines()]
    pairs = [(get_interval(first), get_interval(second)) for first, second in lines]
    count = 0
    for first, second in pairs:
        if (first.start <= second.start and first.end >= second.end) or (second.start <= first.start and second.end >= first.end):
            count += 1

    return count


def count_overlapping_pairs(input: str):
    Interval = namedtuple('Interval', ['start', 'end'])

    def get_interval(pair: str):
        s, e = pair.split('-')
        return Interval(start=int(s), end=int(e))

    lines = [line.split(',') for line in input.splitlines()]
    pairs = [(get_interval(first), get_interval(second)) for first, second in lines]
    count = 0
    for first, second in pairs:
        if (first.start <= second.start <= first.end) or (second.start <= first.start <= second.end):
            count += 1

    return count


advent.run(count_completely_overlapping_pairs)
advent.run(count_overlapping_pairs)
