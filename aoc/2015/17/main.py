from itertools import combinations

with open("input.txt") as f:
    containers = [int(i) for i in f]

sol_a = sum(
    sum(sum(choice) == 150 for choice in combinations(containers, n))
    for n in range(len(containers))
)
print(f"{sol_a = }")

for n in range(len(containers)):
    sum_n = sum(sum(choice) == 150 for choice in combinations(containers, 4))
    if sum_n:
        break

sol_b = sum_n
print(f"{sol_b = }")
