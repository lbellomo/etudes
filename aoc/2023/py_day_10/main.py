from itertools import product, pairwise


with open("input.txt") as f:
    data = f.read().splitlines()


def match_dir(dx, dy):
    match (dx, dy):
        case (1, 0):
            dir = "R"
        case (-1, 0):
            dir = "L"
        case (0, -1):
            dir = "U"
        case (0, 1):
            dir = "D"
        case _:
            raise ValueError
    return dir


def adjacent(p):
    x, y = p

    for dx, dy in product([-1, 0, 1], repeat=2):
        if abs(dx) == abs(dy):
            continue

        new_x = x + dx
        new_y = y + dy

        if new_x < 0 or new_y < 0 or new_x >= shape[0] or new_y >= shape[1]:
            continue

        dir = match_dir(dx, dy)

        p = (new_x, new_y)
        ch = data[new_y][new_x]
        yield ch, p, dir


def is_valid(ch, next_ch, dir):
    match (ch, dir):
        case ("|" | "L" | "J", "U") if next_ch in "|7F":
            return True
        case ("|" | "7" | "F", "D") if next_ch in "|LJ":
            return True
        case ("-" | "L" | "F", "R") if next_ch in "-7J":
            return True
        case ("-" | "J" | "7", "L") if next_ch in "-LF":
            return True
        case _:
            return False


def find_distances(start, p):
    ch = data[p[1]][p[0]]
    next_value = (ch, p)
    distances = {start: 0}
    i = 0

    while next_value:
        ch, p = next_value

        i += 1
        distances[p] = i

        next_value = next(
            (
                (new_ch, new_p)
                for new_ch, new_p, dir in adjacent(p)
                if is_valid(ch, new_ch, dir) and new_p not in distances
            ),
            None,
        )
    return distances


start = next(
    (i, j) for j, line in enumerate(data) for i, ch in enumerate(line) if ch == "S"
)
shape = len(data[0]), len(data)
paths = [
    new_p
    for new_ch, new_p, dir in adjacent(start)
    if any(is_valid(ch, new_ch, dir) for ch in "|LJ7F")
]
distances_a, distances_b = [find_distances(start, p) for p in paths]
sol_a = next(v for k, v in distances_a.items() if distances_b[k] == v and k != start)

print(f"{sol_a = }")

clean_map = [
    "".join([ch if (i, j) in distances_a else "." for i, ch in enumerate(line)])
    for j, line in enumerate(data)
]

R = (1, 0)
RD = (1, 1)
D = (0, 1)
DL = (-1, 1)
L = (-1, 0)
LU = (-1, -1)
U = (0, -1)
UR = (1, -1)

# navigate the main pipe counting all inner points that are not the main pipe

know_dots = set()

for (x0, y0), (x1, y1) in pairwise(distances_a.keys()):
    dx, dy = (x1 - x0, y1 - y0)
    dir = match_dir(dx, dy)

    ch = clean_map[y1][x1]
    # print(ch, dir)
    match (ch, dir):
        case ("F", "L"):
            side = [RD]
        case ("F", "U"):
            side = [L, LU, U]
        case ("7", "R"):
            side = [U, UR, R]
        case ("7", "U"):
            side = [DL]
        case ("J", "R"):
            side = [LU]
        case ("J", "D"):
            side = [R, RD, D]
        case ("L", "L"):
            side = [D, DL, L]
        case ("L", "D"):
            side = [UR]
        case ("-", "L"):
            side = [D]
        case ("-", "R"):
            side = [U]
        case ("|", "U"):
            side = [L]
        case ("|", "D"):
            side = [R]
        case _:
            raise ValueError

    side_p = [(x1 + x, y1 + y) for (x, y) in side]
    side_ch = [clean_map[y][x] for x, y in side_p]

    if "." in side_ch:
        know_dots.update(set(p for ch, p in zip(side_ch, side_p) if ch == "."))

    # print(side_ch)

# count the island in the center, far from the pipes

while True:
    new_dots = set()

    for p in know_dots:
        for new_ch, new_p, _ in adjacent(p):
            if new_p not in distances_a and new_p not in know_dots:
                new_dots.add(new_p)

    if new_dots:
        know_dots.update(new_dots)
    else:
        break

sol_b = len(know_dots)
print(f"{sol_b = }")
