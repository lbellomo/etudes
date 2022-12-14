#!/usr/bin/env python3

from itertools import takewhile

import numpy as np

with open("input.txt") as f:
    data = f.read().strip()


def solve_a(data):
    length = 0
    iter_data = iter(data)

    while True:

        for _ in takewhile(lambda x: x != "(", iter_data):
            length += 1

        marker = "".join(list(takewhile(lambda x: x != ")", iter_data)))
        if not marker:
            break

        windows, count = [int(i) for i in marker.split("x")]

        for _ in range(windows):
            next(iter_data)
            length += count

    return length


def solve_b(data):
    weights = np.ones(len(data), dtype=int)
    iter_data = iter(data)

    length = 0
    pos = 0

    while True:
        for _ in takewhile(lambda x: x != "(", iter_data):
            length += weights[pos]
            pos += 1

        marker = "".join(list(takewhile(lambda x: x != ")", iter_data)))
        if not marker:
            break

        pos += 2 + len(marker)
        windows, count = [int(i) for i in marker.split("x")]
        weights[pos : pos + windows] *= count

    return length


sol_a = solve_a(data)
print(f"{sol_a = }")

sol_b = solve_b(data)
print(f"{sol_b = }")
