from typing import NamedTuple
from itertools import cycle

with open("input.txt") as f:
    raw_data = f.read().split("\n\n")


class Node(NamedTuple):
    left: str
    right: str


def parse_line(line):
    key, values = line.split(" = ")
    left, right = values.strip("(").strip(")").split(", ")
    return key, Node(left, right)


instructions, maps = raw_data
network = {k: v for k, v in (parse_line(line) for line in maps.splitlines())}

pos = "AAA"
count = 0
loop_op = cycle(instructions)


while pos != "ZZZ":
    match next(loop_op):
        case "L":
            pos = network[pos].left
        case "R":
            pos = network[pos].right
    count += 1

sol_a = count
print(f"{sol_a = }")
