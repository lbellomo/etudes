#!/usr/bin/env python3

from itertools import permutations
from collections import namedtuple

import numpy as np


def parse_line(line):

    line_split = line.split()
    x, y = line_split[0].replace("x", "").replace("y", "").split("-")[1:]

    line_info = [int(i.replace("T", "").replace("%", "")) for i in line_split[1:]]

    return Row(int(x), int(y), *line_info)


with open("input.txt") as f:
    _ = next(f)
    header = next(f).lower().replace("%", "").split()
    Row = namedtuple("Row", ["x", "y"] + header[1:])
    data = [parse_line(line) for line in f]


def solve_a():
    count = 0

    for a, b in permutations(data, 2):
        if a.used == 0:
            continue

        if b.avail >= a.used:
            count += 1

    return count


def print_grid():
    nodes = np.zeros([30, 36], dtype=str)

    for row in data:
        if row.used == 0:
            value = "_"
        elif row.used > 100:
            value = "#"
        else:
            value = "."

        nodes[row.y, row.x] = value

    nodes[0, 0] = "@"
    nodes[0, -1] = "G"

    for line in nodes.tolist():
        print("".join(line))


# all the grid - big nodes (#) - the empty one (_)
sol_a = 30 * 36 - 34 - 1
print(f"{sol_a = }")

print_grid()

# go to left to y == 1
# go to up to x == 0
# go to G
# go to @, need 5 moves for each y-step

sol_b = 34 + 27 + 34 + 5 * 34
print(f"{sol_b = }")
