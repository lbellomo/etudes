from itertools import product

import numpy as np


with open("input.txt") as f:
    raw_data = [line.strip() for line in f]

data = np.array(
    [[int(i) for i in line.replace(",", "").split()[2::2]] for line in raw_data]
)
data_light = data[:, :-1]
cals = data[:, -1]


def score(choice, cals=False):
    cookie = (data_light * np.array(choice).reshape(-1, 1)).sum(axis=0)
    return cookie[cookie > 0].prod()


def total_cals(choice):
    return sum(choice[i] * cals[i] for i in range(4))


sol_a = max(
    score(choice) for choice in product(range(100), repeat=4) if sum(choice) == 100
)
print(f"{sol_a = }")


choices = (
    choice
    for choice in product(range(100), repeat=4)
    if sum(choice) == 100 and total_cals(choice) == 500
)

sol_b = max(score(choice) for choice in choices)
print(f"{sol_b = }")
