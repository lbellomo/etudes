import pandas as pd

with open("input.txt") as f:
    raw_data = [line.strip() for line in f]

raw_target_sue = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

target_sue = {}

for compounds in raw_target_sue.split("\n"):
    k_v = compounds.split(": ")
    target_sue[k_v[0]] = int(k_v[1])

sues = []
for raw_sue in raw_data:
    number, raw_sue = raw_sue.split(":", maxsplit=1)
    number = int(number.split()[-1])

    sue = {}
    sue["number"] = number

    for compounds in raw_sue.split(","):
        k_v = compounds.strip().split(": ")
        sue[k_v[0]] = int(k_v[1])

    sues.append(sue)

df = pd.DataFrame(sues)

mask = (df.children.isna()) | True
for k, v in target_sue.items():
    mask = mask & ((df[k].isna()) | (df[k] == v))

sol_a = df[mask].number.iloc[0]
print(f"{sol_a = }")

mask = (df.children.isna()) | True
for k, v in target_sue.items():
    if k in ["cats", "trees"]:
        mask = mask & ((df[k].isna()) | (df[k] > v))
    elif k in ["pomeranians", "goldfish"]:
        mask = mask & ((df[k].isna()) | (df[k] < v))
    else:
        mask = mask & ((df[k].isna()) | (df[k] == v))


sol_b = df[mask].number.iloc[0]
print(f"{sol_b = }")
