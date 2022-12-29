import functools
import itertools
from typing import Callable

import advent


class Monkey:
    def __init__(self, items: list, operation: Callable[[int], int], test_value: int, true_monkey_id: int,
                 false_monkey_id: int):
        self.items = items
        self.operation = operation
        self.test_value = test_value
        self.true_monkey_id = true_monkey_id
        self.false_monkey_id = false_monkey_id

    def check_worry(self, item_id: int) -> bool:
        return self.items[item_id] % self.test_value == 0

    def relief(self, item_id: int) -> None:
        self.items[item_id] = self.items[item_id] // 3

    def worry(self, item_id: int) -> None:
        self.items[item_id] = self.operation(self.items[item_id])

    def run_round(self, monkeys: list['Monkey']) -> None:
        while self.items:
            self.worry(0)
            self.relief(0)
            new_monkey_id = self.true_monkey_id if self.check_worry(0) else self.false_monkey_id
            monkeys[new_monkey_id].items.append(self.items.pop(0))

    def run_round_no_relief(self, monkeys: list['Monkey'], mod: int) -> None:
        while self.items:
            self.worry(0)
            self.items[0] = self.items[0] % mod
            new_monkey_id = self.true_monkey_id if self.check_worry(0) else self.false_monkey_id
            monkeys[new_monkey_id].items.append(self.items.pop(0))


def parse_operation(op, val):
    def op_call(x, y):
        return x * y if op == "*" else x + y

    def f(x):
        return op_call(x, x) if val == "old" else op_call(x, int(val))

    return f


def parse_input(data: str):
    monkeys = []
    lines = data.splitlines()
    for i in range(0, len(lines), 7):
        items = [int(item.strip()) for item in lines[i+1][17:].split(',')]
        operation = parse_operation(lines[i + 2].split()[-2], lines[i + 2].split()[-1])
        monkey = Monkey(items, operation, int(lines[i + 3].split()[-1]), int(lines[i + 4].split()[-1]),
                        int(lines[i + 5].split()[-1]))
        monkeys.append(monkey)
    return monkeys


def get_monkey_business(data: str):
    monkeys = parse_input(data)
    inspect = [0]*len(monkeys)
    for _ in range(20):

        for i, monkey in enumerate(monkeys):
            to_inspect = len(monkey.items)
            inspect[i] += to_inspect
            monkey.run_round(monkeys)
    inspect.sort(reverse=True)
    return inspect[0]*inspect[1]


def get_monkey_business_no_relief(data: str):
    monkeys = parse_input(data)
    mod = functools.reduce(lambda x,y: x*y, (m.test_value for m in monkeys), 1)
    inspect = [0]*len(monkeys)
    for _ in range(10000):
        for i, monkey in enumerate(monkeys):
            to_inspect = len(monkey.items)
            inspect[i] += to_inspect
            monkey.run_round_no_relief(monkeys, mod)
    inspect.sort(reverse=True)
    return inspect[0]*inspect[1]


advent.run(get_monkey_business)
advent.run(get_monkey_business_no_relief)
