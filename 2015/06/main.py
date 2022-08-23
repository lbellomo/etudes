from collections import namedtuple

import numpy as np


with open("input.txt") as f:
    raw_data = [line.strip() for line in f]

Instruction = namedtuple("instruction", ["i_type", "i_slice"])
grid = np.zeros([1_000, 1_000], dtype=bool)

data = []
for line in raw_data:
    i_type, start, _, end = line.rsplit(maxsplit=3)

    start = [int(i) for i in start.split(",")]
    # i+1 so we also include the last point
    end = [int(i) + 1 for i in end.split(",")]
    i_slice = np.s_[start[0] : end[0], start[1] : end[1]]

    data.append(Instruction(i_type, i_slice))

for instruction in data:
    i_type, i_slice = instruction
    if i_type == "turn on":
        grid[i_slice] = 1
    elif i_type == "turn off":
        grid[i_slice] = 0
    elif i_type == "toggle":
        grid[i_slice] = ~grid[i_slice]
    else:
        raise ValueError(f"Invalid instruction {i_type}")

sol_a = grid.sum()
print(f"{sol_a = }")

grid = np.zeros([1_000, 1_000], dtype=int)

for instruction in data:
    i_type, i_slice = instruction
    if i_type == "turn on":
        grid[i_slice] += 1
    elif i_type == "turn off":
        grid[i_slice] -= 1
        grid[grid < 0] = 0
    elif i_type == "toggle":
        grid[i_slice] += 2
    else:
        raise ValueError(f"Invalid instruction {i_type}")

sol_b = grid.sum()
print(f"{sol_b = }")
