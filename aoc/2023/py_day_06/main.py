from math import prod


with open("input.txt") as f:
    data = f.read().splitlines()


def parse_line(line: str) -> list[int]:
    _, *values = line.split()
    return [int(i) for i in values]


def parse_line_kerning(line: str) -> int:
    _, *values = line.split()
    return int("".join(values))


def calc_distance(hold: int, t: int) -> int:
    return hold * (t - hold)


times, target_distances = parse_line(data[0]), parse_line(data[1])
sol_a = prod(
    sum(True for d in (calc_distance(i, t) for i in range(t + 1)) if d > target_d)
    for t, target_d in zip(times, target_distances)
)
print(f"{sol_a = }")

t, target_d = parse_line_kerning(data[0]), parse_line_kerning(data[1])
sol_b = sum(True for d in (calc_distance(i, t) for i in range(t + 1)) if d > target_d)
print(f"{sol_b = }")
