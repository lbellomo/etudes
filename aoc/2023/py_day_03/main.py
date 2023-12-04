import re
import math
from itertools import product
from typing import NamedTuple

with open("input.txt") as f:
    data = f.read().splitlines()

p = re.compile(r"\d+")
symbols = set([ch for ch in "".join(data).replace(".", "") if not ch.isdigit()])

size_x = len(data)
size_y = len(data[0])


def point_neighbors(i, j):
    neighbors = list()

    for d_x, d_y in product([-1, 0, 1], repeat=2):
        tmp_i = i + d_x
        tmp_j = j + d_y
        if tmp_i >= 0 and tmp_j >= 0 and size_x > tmp_i and size_y > tmp_j:
            neighbors.append(data[tmp_i][tmp_j])
    return neighbors


def check_number(m, i):
    for j in range(m.start(), m.end()):
        neighbors = point_neighbors(i, j)
        if any(ch for ch in neighbors if ch in symbols):
            return int(m.group())
    return 0


sol_a = sum(
    [sum([check_number(m, i) for m in p.finditer(line)]) for i, line in enumerate(data)]
)
print(f"{sol_a = }")


class Number(NamedTuple):
    id: int
    hitbox: list[tuple[int, int]]
    value: int


count_numbers = 0
numbers = []

for i, line in enumerate(data):
    for m in p.finditer(line):
        hitbox = [(i, j) for j in range(m.start(), m.end())]
        value = int(m.group())
        number = Number(count_numbers, hitbox, value)
        numbers.append(number)
        count_numbers += 1


p = re.compile(r"\*")


def find_hit(i, j):
    for n in numbers:
        if (i, j) in n.hitbox:
            return n


def numbers_neighbors(i, j):
    neighbors = list()

    for d_x, d_y in product([-1, 0, 1], repeat=2):
        if (d_x, d_y) == (0, 0):
            continue

        tmp_i = i + d_x
        tmp_j = j + d_y
        if tmp_i >= 0 and tmp_j >= 0 and size_x > tmp_i and size_y > tmp_j:
            hit = find_hit(tmp_i, tmp_j)
            if hit and hit not in neighbors:
                neighbors.append(hit)
    return neighbors


def calc_gear_ratio(neighbors):
    if len(neighbors) == 2:
        return math.prod(n.value for n in neighbors)
    else:
        return 0


sol_b = sum(
    sum(calc_gear_ratio(numbers_neighbors(i, m.start())) for m in p.finditer(line))
    for i, line in enumerate(data)
)
print(f"{sol_b = }")
