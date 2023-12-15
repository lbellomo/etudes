from itertools import combinations

with open("input.txt") as f:
    raw_data = f.read().splitlines()

data = raw_data[:]

double_rows = [j for j, line in enumerate(data) if "#" not in line]
double_cols = [i for i in range(len(data[0])) if "#" not in [line[i] for line in data]]

# add rows
empty_row = "." * len(data[0])  # ["." for _ in range(len(data[0]))]

for j in reversed(double_rows):
    data.insert(j, empty_row)

# add cols
for i in reversed(double_cols):
    for j, row in enumerate(data):
        data[j] = row[:i] + "." + row[i:]


def distance(g0, g1):
    x0, y0 = g0
    x1, y1 = g1
    return abs(x1 - x0) + abs(y1 - y0)


galaxies = [
    (i, j) for j, line in enumerate(data) for i, ch in enumerate(line) if ch == "#"
]
sol_a = sum(distance(g0, g1) for g0, g1 in combinations(galaxies, 2))
print(f"{sol_a = }")


def distance_2(g0, g1, shift):
    shift -= 1

    x0, y0 = g0
    x1, y1 = g1

    shift_x = sum((x1 > i > x0 or x0 > i > x1 for i in double_cols)) * shift
    shift_y = sum((y1 > i > y0 or y0 > i > y1 for i in double_rows)) * shift

    return abs(x1 - x0) + abs(y1 - y0) + shift_x + shift_y


data = raw_data

galaxies = [
    (i, j) for j, line in enumerate(data) for i, ch in enumerate(line) if ch == "#"
]
shift = 1000000
sol_b = sum(distance_2(g0, g1, shift) for g0, g1 in combinations(galaxies, 2))
print(f"{sol_b = }")
