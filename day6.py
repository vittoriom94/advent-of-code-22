import collections

import advent


def get_start_packet(data: str):
    d = collections.defaultdict(int)
    count = 0

    LEN = 4

    for i in range(len(data)):
        if d[data[i]] == 0:
            count += 1
        d[data[i]] += 1

        if i >= LEN:
            d[data[i-LEN]] -= 1
            if d[data[i-LEN]] == 0:
                count -= 1

        if count == LEN:
            return i+1
    raise Exception()


def get_start_message(data: str):
    d = collections.defaultdict(int)
    count = 0

    LEN = 14

    for i in range(len(data)):
        if d[data[i]] == 0:
            count += 1
        d[data[i]] += 1

        if i >= LEN:
            d[data[i - LEN]] -= 1
            if d[data[i - LEN]] == 0:
                count -= 1

        if count == LEN:
            return i + 1
    raise Exception()


advent.run(get_start_packet)
advent.run(get_start_message)
