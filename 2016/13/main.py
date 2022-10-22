import numpy as np
import numpy.typing as npt


def is_wall(i: int, j: int) -> bool:
    n = (i * i + 3 * i + 2 * i * j + j + j * j) + fav_number
    return bin(n)[2:].count("1") % 2 != 0


def build_maze(fav_number: int) -> npt.ArrayLike:
    size = 1_000
    maze = np.zeros([size, size], dtype=int)
    for i, j in [(i, j) for i in range(size) for j in range(size)]:
        if is_wall(i, j):
            target = 0
        else:
            target = 1

        maze[i, j] = target
    return maze


def get_new_pos(current_pos, distance: int, know_pos):
    distance += 1
    new_pos = []
    for pos in current_pos:
        for p in [pos + np.array(d) for d in directions]:
            x, y = p[0], p[1]
            if not (x >= 0 and y >= 0):
                continue
            if maze[x, y] and not tuple(p) in know_pos:  # type: ignore
                new_pos.append(p)
                know_pos.add(tuple(p))

    return new_pos, distance, know_pos


fav_number = 1358
target = np.array([31, 39])
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

maze = build_maze(fav_number)


def solve_a() -> int:
    distance = 0
    init_pos = np.array([1, 1])
    pos = init_pos

    current_pos = [pos]
    know_pos = set([tuple(pos)])

    while tuple(target) not in know_pos:
        current_pos, distance, know_pos = get_new_pos(current_pos, distance, know_pos)

    return distance


sol_a = solve_a()
print(f"{sol_a = }")


def solve_b() -> int:
    distance = 0
    init_pos = np.array([1, 1])
    pos = init_pos

    current_pos = [pos]
    know_pos = set([tuple(pos)])

    for _ in range(50):
        current_pos, distance, know_pos = get_new_pos(current_pos, distance, know_pos)

    return len(know_pos)


sol_b = solve_b()
print(f"{sol_b = }")
