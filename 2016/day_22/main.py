from typing import List
from collections import namedtuple
from itertools import permutations


Node = namedtuple("Node", ["x", "y", "size", "used", "avail", "use"])

RawData = List[str]
Data = List[Node]


def read_data(path: str) -> RawData:
    with open(path) as f:
        f.readline()
        f.readline()
        return [line.strip() for line in f.readlines()]


def parse_row(row: str) -> Node:
    row_split = row.split()
    pos = row_split.pop(0)
    x, y = [int(coord[1:]) for coord in pos.split("-")[1:]]
    use_str = row_split.pop()
    values = []

    for i in row_split:
        if not i.endswith("T"):
            raise ValueError("Value in another unit (not T)")

        values.append(int(i[:-1]))

    use = int(use_str[:-1])
    return Node(x, y, *values, use)  # type: ignore


def parse_data(raw_data: RawData) -> Data:
    return [parse_row(row) for row in raw_data]


def solve_a(data: Data) -> int:
    count = 0
    for a, b in permutations(data, 2):
        if a.used == 0:
            continue
        if a.used <= b.avail:
            count += 1
    return count


if __name__ == "__main__":
    data = parse_data(read_data("input.txt"))
    sol_a = solve_a(data)
    print(f"sol a: {sol_a}")
