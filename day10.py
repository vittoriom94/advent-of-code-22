import advent


def get_strength(data: str):
    cycles = [20, 60, 100, 140, 180, 220]
    cycle = 0
    X = 1
    ss = 0

    def add_cycle():
        nonlocal ss, cycle
        cycle += 1
        if cycle in cycles:
            ss += X * cycle

    for command in data.splitlines():
        match command.split():
            case ["noop"]:
                add_cycle()
            case ["addx", val]:
                add_cycle()
                add_cycle()
                X += int(val)
    return ss


def print_crt(data: str):
    cycle = 0
    offset = 0
    row = []

    def add_cycle():
        nonlocal cycle
        if offset <= cycle < offset + 3:
            row.append("#")
        else:
            row.append(".")
        cycle += 1
        if cycle == 40:
            print(''.join(row))
            row.clear()
            cycle = 0

    for command in data.splitlines():
        match command.split():
            case ["noop"]:
                add_cycle()
            case ["addx", val]:
                add_cycle()
                add_cycle()
                offset += int(val)
    return 0


advent.run(get_strength)
advent.run(print_crt)
