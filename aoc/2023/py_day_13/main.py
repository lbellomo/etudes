from itertools import pairwise


with open("input.txt") as f:
    raw_data = f.read()

data = [item.splitlines() for item in raw_data.split("\n\n")]


def transpose(pattern):
    size = len(pattern[0])
    return ["".join(row[i] for row in pattern) for i in range(size)]


def find_reflection(pattern):
    for (i, row), (j, other_row) in pairwise(enumerate(pattern)):
        if row == other_row and all(
            pattern[i - index_shift] == pattern[j + index_shift]
            for index_shift in range(1, min(i + 1, len(pattern) - j))
        ):
            return j
    return None


def summarize(pattern, f):
    r = f(pattern)
    if not r:
        r = f(transpose(pattern))
    else:
        r *= 100

    return r


sol_a = sum(summarize(pattern, find_reflection) for pattern in data)
print(f"{sol_a = }")


def distance(row, other_row):
    return sum(i != j for i, j in zip(row, other_row))


def find_reflection_smudge(pattern):
    for (i, row), (j, other_row) in pairwise(enumerate(pattern)):
        d = distance(row, other_row)

        if d == 0 or d == 1:
            rows_distances = [
                distance(pattern[i - index_shift], pattern[j + index_shift])
                for index_shift in range(0, min(i + 1, len(pattern) - j))
            ]
            if sum(rows_distances) == 1:
                return j

    return None


sol_b = sum(summarize(pattern, find_reflection_smudge) for pattern in data)
print(f"{sol_b = }")
