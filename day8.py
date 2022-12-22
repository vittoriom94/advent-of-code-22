import advent


def count_visible(data: str):
    lines = data.splitlines()

    trees = []
    for i in range(len(lines)):
        cur_line = []
        for j in range(len(lines[i])):
            cur_line.append(int(lines[i][j]))
        trees.append(cur_line)

    def in_range(i, j):
        return 0 <= i < len(trees) and 0 <= j < len(trees[0])

    def is_visible(tree: tuple[int, int]):
        r, c = tree
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        from_h = trees[r][c]
        for i, j in dirs:
            cnt = 1
            while in_range(r + i * cnt, c + j * cnt):
                if from_h <= trees[r + i * cnt][c + j * cnt]:
                    break
                cnt += 1
            if not in_range(r + i * cnt, c + j * cnt):
                return True

        return False

    tot = 0
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            if is_visible((i, j)):
                tot += 1

    return tot


def get_score(data: str):
    lines = data.splitlines()

    trees = []
    for i in range(len(lines)):
        cur_line = []
        for j in range(len(lines[i])):
            cur_line.append(int(lines[i][j]))
        trees.append(cur_line)

    def in_range(i, j):
        return 0 <= i < len(trees) and 0 <= j < len(trees[0])

    def score(tree: tuple[int, int]):
        r, c = tree
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        from_h = trees[r][c]
        cur_score = 1
        for i, j in dirs:
            cnt = 1
            while in_range(r + i * cnt, c + j * cnt):
                if from_h <= trees[r + i * cnt][c + j * cnt]:
                    break
                cnt += 1
            if not in_range(r + i * cnt, c + j * cnt):
                cnt -= 1
            cur_score = cur_score*cnt

        return cur_score

    max_score = 0
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            max_score = max(max_score, score((i, j)))

    return max_score


advent.run(count_visible)
advent.run(get_score)
