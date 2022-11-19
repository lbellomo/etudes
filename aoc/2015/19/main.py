from random import shuffle
from collections import Counter

with open("input.txt") as f:
    raw_data = [line.strip() for line in f]


medicine_molecule = raw_data[-1]
raw_replacements = raw_data[:-2]

replacements = [tuple(line.split(" => ")) for line in raw_replacements]


def combinations_molecule(k, v, count):
    index = 0

    while True:
        next_index = medicine_molecule.find(k, index)

        if next_index == -1:
            break

        new_molecule = medicine_molecule[:next_index] + medicine_molecule[
            next_index:
        ].replace(k, v, 1)
        count.update([new_molecule])
        index = next_index + 1


def solve_a():
    count = Counter()

    for replacement in replacements:
        combinations_molecule(*replacement, count)

    return len(count)


def solve_b():

    molecule = medicine_molecule
    count_steps = 0

    while molecule != "e":
        tmp_molecule = molecule
        for i, j in replacements:
            if j not in molecule:
                continue

            molecule = molecule.replace(j, i, 1)
            count_steps += 1

        # no changes
        if tmp_molecule == molecule:
            count_steps = 0
            molecule = medicine_molecule
            shuffle(replacements)

    return count_steps


sol_a = solve_a()
print(f"{sol_a = }")

sol_b = solve_b()
print(f"{sol_b = }")
