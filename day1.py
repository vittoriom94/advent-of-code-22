import advent


def most_calories(input: str):
    elves_calories = sorted([sum(map(int, elf.splitlines())) for elf in input.split('\n\n')], reverse=True)
    return elves_calories[0]


def top_three(input: str):
    elves_calories = sorted([sum(map(int, elf.splitlines())) for elf in input.split('\n\n')], reverse=True)
    return sum(elves_calories[0:3])


advent.run(most_calories)
advent.run(top_three)