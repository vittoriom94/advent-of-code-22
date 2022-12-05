import advent


def get_top_row(input: str):
    stacks = [[] for _ in range(9)]

    def move(amount, src, dest):
        for i in range(amount):
            stacks[dest-1].append(stacks[src-1].pop())

    data = input.splitlines()
    for i in range(9):
        for j in range(8):
            if data[7-j][1+i*4] != " ":
                stacks[i].append(data[7-j][1+i*4])

    for mov in data[10:]:
        instr = mov.split()
        move(int(instr[1]), int(instr[3]), int(instr[5]))
    toprow = [stack[-1] for stack in stacks]
    return "".join(toprow)


def get_top_row_move_bulk(input: str):
    stacks = [[] for _ in range(9)]

    def move(amount, src, dest):
        tomove = []
        for i in range(amount):
            tomove.append(stacks[src-1].pop())
        for i in range(amount):
            stacks[dest-1].append(tomove.pop())

    data = input.splitlines()
    for i in range(9):
        for j in range(8):
            if data[7-j][1+i*4] != " ":
                stacks[i].append(data[7-j][1+i*4])

    for mov in data[10:]:
        instr = mov.split()
        move(int(instr[1]), int(instr[3]), int(instr[5]))
    toprow = [stack[-1] for stack in stacks]
    return "".join(toprow)


advent.run(get_top_row)
advent.run(get_top_row_move_bulk)
