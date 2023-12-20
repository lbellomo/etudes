from typing import NamedTuple

with open("input.txt") as f:
    raw_data = f.read().splitlines()


class Step(NamedTuple):
    dir: str
    meters: int


def parse(line):
    dir, meters, _ = line.split()
    meters = int(meters)
    return Step(dir, meters)


def add(pos, shift):
    x, y = pos
    xs, ys = shift
    return (x + xs, y + ys)


def update(pos, step):
    match step.dir:
        case "U":
            shift = (0, 1)
        case "D":
            shift = (0, -1)
        case "R":
            shift = (1, 0)
        case "L":
            shift = (-1, 0)

    for _ in range(step.meters):
        pos = add(pos, shift)
        know_pos.add(pos)
    return pos


def walk(pos):
    new_pos = list()

    for shift in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        tmp_pos = add(pos, shift)

        if tmp_pos[0] not in know_x or tmp_pos[1] not in know_y:
            raise ValueError("Invalid start point")

        if tmp_pos in know_pos:
            continue

        new_pos.append(tmp_pos)
    return new_pos


data = [parse(line) for line in raw_data]

pos = (0, 0)
know_pos = set((pos,))

for step in data:
    pos = update(pos, step)

know_x = set(p[0] for p in know_pos)
know_y = set(p[1] for p in know_pos)

# random start point inside
pos = (3, -1)
new_pos = [pos]

while new_pos:
    for pos in new_pos:
        know_pos.add(pos)
    tmp_new_pos = []
    for pos in new_pos:
        tmp_new_pos += walk(pos)

    new_pos = list(set(tmp_new_pos))

sol_a = len(know_pos)
print(f"{sol_a = }")
