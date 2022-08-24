from itertools import permutations, pairwise

with open("input.txt") as f:
    raw_data = [line.strip() for line in f]

persons = set()
table = {}

for line in raw_data:
    person, _, positive, value, *_, target = line.split()
    value = int(value)
    if positive == "lose":
        value *= -1

    target = target[:-1]
    table[f"{person}-{target}"] = value

    persons.add(person)


def score(choice):
    right_side = sum(table[f"{person}-{target}"] for person, target in pairwise(choice))
    left_side = sum(
        table[f"{person}-{target}"] for person, target in pairwise(choice[::-1])
    )
    right_head_tail = table[f"{choice[0]}-{choice[-1]}"]
    left_head_tail = table[f"{choice[-1]}-{choice[0]}"]
    return right_side + left_side + right_head_tail + left_head_tail


def solve(persons):
    return max(score(choice) for choice in permutations(persons, len(persons)))


sol_a = solve(persons)
print(f"{sol_a = }")

for person in persons:
    table[f"{person}-Me"] = 0
    table[f"Me-{person}"] = 0

persons.add("Me")

sol_b = solve(persons)
print(f"{sol_b = }")
