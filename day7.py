import typing

import advent


class Dir:
    def __init__(self, parent: typing.Union[None, 'Dir']):
        self.parent = parent
        self.dirs = dict()
        self.size = 0

    def __repr__(self):
        return f"Dir - Size: {self.size}, Subfolders: {len(self.dirs)}"


def get_sum_maxed(data: str):
    MAX = 100000
    cdl = data.splitlines()

    root = Dir(None)
    cur_dir = root

    tot = 0

    for line in cdl:
        match line.split():
            case ["$", "cd", "/"]:
                cur_dir = root
            case ["$", "cd", ".."]:
                size = cur_dir.size
                cur_dir = cur_dir.parent
                cur_dir.size += size
            case ["$", "cd", newdir]:
                if newdir not in cur_dir.dirs:
                    cur_dir.dirs[newdir] = Dir(cur_dir)
                cur_dir = cur_dir.dirs[newdir]
            case [("dir" | "$"), _]:
                pass
            case [size, _]:
                cur_dir.size += int(size)
    while cur_dir != root:
        size = cur_dir.size
        cur_dir = cur_dir.parent
        cur_dir.size += size

    def explore(node: Dir):
        if node.size < MAX:
            nonlocal tot
            tot += node.size
        for v in node.dirs.values():
            explore(v)
    explore(root)
    return tot


def free_small_dir(data: str):
    TOT_SIZE = 70000000
    MIN = 30000000

    cdl = data.splitlines()

    root = Dir(None)
    cur_dir = root

    for line in cdl:
        match line.split():
            case ["$", "cd", "/"]:
                cur_dir = root
            case ["$", "cd", ".."]:
                size = cur_dir.size
                cur_dir = cur_dir.parent
                cur_dir.size += size
            case ["$", "cd", newdir]:
                if newdir not in cur_dir.dirs:
                    cur_dir.dirs[newdir] = Dir(cur_dir)
                cur_dir = cur_dir.dirs[newdir]
            case [("dir" | "$"), _]:
                pass
            case [size, _]:
                cur_dir.size += int(size)
    while cur_dir != root:
        size = cur_dir.size
        cur_dir = cur_dir.parent
        cur_dir.size += size

    free_space = TOT_SIZE-root.size
    required = MIN-free_space

    def small_enough(node: Dir):
        if node.size < required:
            return float('inf')
        return min([node.size] + [small_enough(ch) for ch in node.dirs.values()])

    return small_enough(root)


advent.run(get_sum_maxed)
advent.run(free_small_dir)
