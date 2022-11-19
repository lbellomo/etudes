from itertools import groupby


seed = "1113122113"


def iterate(seed, n):
    value = seed
    for _ in range(n):
        value = "".join(f"{len(list(g))}{k}" for k, g in groupby(value))
    return len(value)


sol_a = iterate(seed, 40)
print(f"{sol_a = }")

sol_b = iterate(seed, 50)
print(f"{sol_b = }")
