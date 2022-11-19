from collections import deque

raw_data = """Disc #1 has 13 positions; at time=0, it is at position 11.
Disc #2 has 5 positions; at time=0, it is at position 0.
Disc #3 has 17 positions; at time=0, it is at position 11.
Disc #4 has 3 positions; at time=0, it is at position 0.
Disc #5 has 7 positions; at time=0, it is at position 2.
Disc #6 has 19 positions; at time=0, it is at position 17.
"""

Discs = list[deque[int]]


def parse_data(raw_data: str) -> Discs:
    discs = []
    for line in raw_data.splitlines():
        split = line[:-1].split()
        len_pos, pos = int(split[3]), int(split[-1])
        d = deque(range(len_pos))
        d.rotate(-d.index(pos))
        discs.append(d)
    return discs


def solve(discs: Discs) -> int:

    for i, d in enumerate(discs, start=1):
        d.rotate(-i)

    count = 0
    while not all(d[0] == 0 for d in discs):
        for d in discs:
            d.rotate(-1)
        count += 1

    return count


discs = parse_data(raw_data)
sol_a = solve(discs)
print(f"{sol_a = }")

discs = parse_data(raw_data)
discs.append(deque(range(11)))
sol_b = solve(discs)
print(f"{sol_b = }")
