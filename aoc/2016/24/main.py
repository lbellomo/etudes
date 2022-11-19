from collections import namedtuple
from itertools import permutations, pairwise

import numpy as np
import numpy.typing as npt

with open("input.txt") as f:
    m = np.array([[i for i in line.strip()] for line in f])

Point = namedtuple("Point", ["x", "y"])

numbers = "01234567"
numbers_plus_zero = numbers + "0"


def get_neighbors(p: npt.ArrayLike) -> list[Point]:
    return [
        Point(*(p + np.array(direction)))
        for direction in [(-1, 0), (0, -1), (0, 1), (1, 0)]
    ]


def calculate_distances() -> dict[str, dict[str, int]]:
    distances = {}

    for char in numbers:

        current_distance = {}
        count = 1
        p_start = np.argwhere(m == char).reshape(-1)
        know_p = set()

        states = [Point(*p_start)]
        new_states = []

        while states:

            for p_current in states:
                if tuple(p_current) in know_p:
                    continue
                else:
                    know_p.add(tuple(p_current))

                p_neighbors = get_neighbors(p_current)

                for p_n in p_neighbors:
                    if tuple(p_n) in know_p:
                        continue

                    value = m[p_n[0], p_n[1]]
                    if value == "#":
                        continue
                    elif value not in current_distance and value != ".":
                        current_distance[value] = count

                    # for "." and "char"
                    new_states.append(p_n)

            count += 1
            states = new_states
            new_states = []

        distances[char] = current_distance
    return distances


distances = calculate_distances()


def score(case: tuple[str, ...]) -> int:
    return sum(distances[i][j] for i, j in pairwise("".join(case)))


def solve_a() -> int:
    all_cases = (case for case in permutations(numbers, len(numbers)) if case[0] == "0")
    return min(score(case) for case in all_cases)


sol_a = solve_a()
print(f"{sol_a = }")


def solve_b() -> int:
    all_cases = (
        case
        for case in permutations(numbers_plus_zero, len(numbers_plus_zero))
        if case[0] == "0" and case[-1] == "0"
    )
    return min(score(case) for case in all_cases)


sol_b = solve_b()
print(f"{sol_b = }")
