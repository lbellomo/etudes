from collections import Counter
from typing import Dict

with open("inputs/day_06.txt") as f:
    init_state = [int(i) for i in f.read().strip().split(",")]

State = Dict[int, int]


def update(state: State) -> State:
    new_state = {i: 0 for i in range(9)}
    for k, v in state.items():
        if k == 0:
            new_state[6] += v
            new_state[8] += v
        else:
            new_state[k-1] += v

    return new_state


def update_n_days(n: int) -> int:
    state = dict(Counter(init_state))

    for _ in range(n):
        state = update(state)
    return sum(state.values())


print("sol_a =", update_n_days(80))
print("sol_b =", update_n_days(256))
