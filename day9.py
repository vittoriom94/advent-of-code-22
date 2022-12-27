import collections
import dataclasses

import advent

Command = collections.namedtuple("Command", ["direction", "steps"])


@dataclasses.dataclass
class Coord:
    x: int
    y: int

    def move(self, direction: 'Coord'):
        self.x += direction.x
        self.y += direction.y

    def follow(self, head: 'Coord'):
        if abs(head.x - self.x) > 1:
            self.x += 1 if (head.x - self.x) > 0 else -1
            if head.y != self.y:
                self.y += 1 if (head.y - self.y) > 0 else -1
        elif abs(head.y - self.y) > 1:
            self.y += 1 if (head.y - self.y) > 0 else -1
            if head.x != self.x:
                self.x += 1 if (head.x - self.x) > 0 else -1


dirs = {
    "U": Coord(0, 1),
    "D": Coord(0, -1),
    "L": Coord(-1, 0),
    "R": Coord(1, 0)
}


def get_direction(d: str):
    return dirs[d]


def count_visited(data: str):
    commands = [Command(get_direction(line.split()[0]), int(line.split()[1])) for line in data.splitlines()]
    visited = set()

    tail = Coord(0, 0)
    head = Coord(0, 0)

    visited.add((tail.x, tail.y))

    for command in commands:
        for i in range(command.steps):
            head.move(command.direction)
            tail.follow(head)
            visited.add((tail.x, tail.y))

    return len(visited)


def count_multiple(data: str):
    commands = [Command(get_direction(line.split()[0]), int(line.split()[1])) for line in data.splitlines()]
    visited = set()

    pieces = [Coord(0, 0) for _ in range(10)]

    visited.add((0, 0))

    for command in commands:
        for _ in range(command.steps):
            pieces[0].move(command.direction)
            for i in range(1, 10):
                pieces[i].follow(pieces[i-1])
            visited.add((pieces[-1].x, pieces[-1].y))

    return len(visited)


advent.run(count_visited)
advent.run(count_multiple)
