import advent


def calculate_score_guide(input: str):
    scores = {
        ('A', 'X'): 4,
        ('A', 'Y'): 8,
        ('A', 'Z'): 3,
        ('B', 'X'): 1,
        ('B', 'Y'): 5,
        ('B', 'Z'): 9,
        ('C', 'X'): 7,
        ('C', 'Y'): 2,
        ('C', 'Z'): 6,
    }

    data = input.splitlines()
    rounds = []

    for d in data:
        play = d.split()
        rounds.append((play[0], play[1]))

    return sum(map(lambda x: scores[x], rounds))


def calculate_optimal_score(input: str):
    scores = {
        ('A', 'X'): 3,
        ('A', 'Y'): 4,
        ('A', 'Z'): 8,
        ('B', 'X'): 1,
        ('B', 'Y'): 5,
        ('B', 'Z'): 9,
        ('C', 'X'): 2,
        ('C', 'Y'): 6,
        ('C', 'Z'): 7,
    }

    data = input.splitlines()
    rounds = []

    for d in data:
        play = d.split()
        rounds.append((play[0], play[1]))
    return sum(map(lambda x: scores[x], rounds))


advent.run(calculate_score_guide)
advent.run(calculate_optimal_score)
