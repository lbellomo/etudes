from math import prod
from itertools import combinations


packages = """1
3
5
11
13
17
19
23
29
31
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113
"""
packages = set([int(i) for i in packages.split()])


def solve(count_groups: int) -> int:
    # each group with the same weight
    target_weight = sum(packages) / count_groups

    # find the minimum element for a group
    for group_size in range(1, len(packages)):
        group = [
            set(case)
            for case in combinations(packages, group_size)
            if sum(case) == target_weight
        ]
        if group:
            break

    # caculate quantum entanglement
    return min(prod(i) for i in group)


sol_a = solve(3)
print(f"{sol_a = }")


sol_b = solve(4)
print(f"{sol_b = }")
