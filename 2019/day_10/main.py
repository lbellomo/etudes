from fractions import Fraction
from itertools import compress
from typing import Iterable

import pytest  # type: ignore


def read_data(path_data: str) -> list[str]:
    with open(path_data) as f_in:
        return [line.strip() for line in f_in.readlines()]


Point = tuple[int, int]


def read_asteroids(data: list[str]) -> list[tuple[int, int]]:
    asteroids = []
    for i, row in enumerate(data):
        for j, elem in enumerate(row):
            if elem == "#":
                asteroids.append((i, j))
    return asteroids


def diff_pos(a: Point, b: Point) -> Point:
    return (a[0] - b[0], a[1] - b[1])


def detect_asteroids(asteroid: Point, others: Iterable[Point]) -> int:
    # find the manhatan distance from center
    distances = [diff_pos(asteroid, other) for other in others]

    # filter elements in same row or column
    others_in_x = [i for i in distances if i[0] == 0]
    others_in_y = [i for i in distances if i[1] == 0]

    # count only the first element for both directions
    # (that element will block the rest, if there is more in that direction)
    any_up = any(i[1] > 0 for i in others_in_x)
    any_down = any(i[1] < 0 for i in others_in_x)
    any_left = any(i[0] > 0 for i in others_in_y)
    any_rigth = any(i[0] < 0 for i in others_in_y)
    any_to_filter = any_up + any_down + any_left + any_rigth

    # remove elemnt with distance zero in x or y
    distances = [i for i in distances if i not in others_in_x + others_in_y]

    # split in y > 0 and y < 0, because (1, 1) and (-1, -1) are reduced
    # to the same fraction but they are different elements (different direction)
    up_half = set(Fraction(i[0], i[1]) for i in distances if i[1] > 0)
    down_half = set(Fraction(i[0], i[1]) for i in distances if i[1] < 0)

    total = len(up_half) + len(down_half) + any_to_filter
    return total


def solve_a(data: list[str]) -> tuple[tuple[int, int], int]:
    asteroids = read_asteroids(data)

    shape = len(asteroids)

    detected = {}

    for i in range(shape):
        asteroid = asteroids[i]
        others = compress(asteroids, (i != j for j in range(shape)))
        total = detect_asteroids(asteroid, others)
        detected[asteroid] = total

    best = max(detected, key=lambda k: detected[k])
    return best, detected[best]


if __name__ == "__main__":
    data = read_data("input.txt")
    sol_a = solve_a(data)
    print(f"sol_a = {sol_a}")


example_0 = """.#..#
.....
#####
....#
...##""".split()

example_1 = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####""".split()

example_2 = """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.""".split()

example_3 = """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..""".split()

example_4 = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
""".split()


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (example_0, ((4, 3), 8)),
        (example_1, ((8, 5), 33)),
        (example_2, ((2, 1), 35)),
        (example_3, ((3, 6), 41)),
        (example_4, ((13, 11), 210))
    ],
)
def test_solve_a(test_input, expected):
    sol = solve_a(test_input)
    assert sol == expected
