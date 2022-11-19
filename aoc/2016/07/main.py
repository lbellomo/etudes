import re
from itertools import tee
from typing import NamedTuple, Iterator


class Ip(NamedTuple):
    outside: list[str]
    inside: list[str]


def parse(line: str) -> Ip:
    split = re.split(r"\[|\]", line)
    return Ip(split[::2], split[1::2])


def multiwise(iterable: str, n: int) -> Iterator[tuple[str, ...]]:
    iterables = tee(iterable, n)
    for i, iterable_copy in enumerate(iterables):
        for _ in range(i):
            next(iterable_copy, None)

    return zip(*iterables)


def check_abba(chunk: str) -> bool:
    for i, j, k, l in multiwise(chunk, 4):
        if i == j or k == l:
            continue
        if i == l and j == k:
            return True
    return False


with open("input.txt") as f:
    data = [parse(line.strip()) for line in f]

sol_a = sum(
    any(check_abba(chunk) for chunk in ip.outside)
    and not any(check_abba(chunk) for chunk in ip.inside)
    for ip in data
)
print(f"{sol_a = }")


def is_aba(ip: Ip) -> bool:
    abas = [
        i + j + k
        for chunk in ip.inside
        for i, j, k in multiwise(chunk, 3)
        if i == k and i != j
    ]
    babs = [
        j + i + j
        for chunk in ip.outside
        for i, j, k in multiwise(chunk, 3)
        if i == k and i != j
    ]

    return any(aba in babs for aba in abas)


sol_b = sum(is_aba(ip) for ip in data)
print(f"{sol_b = }")
