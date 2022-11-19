import numpy as np
import numpy.typing as npt
from dataclasses import dataclass
from hashlib import md5

passcode = "bwnlcvfs"
open_door_chars = "bcdef"
target = np.array([3, 3])
char_directions = list("UDLR")
directions = [np.array(i) for i in [[-1, 0], [1, 0], [0, -1], [0, 1]]]


@dataclass
class State:
    pos: npt.ArrayLike
    path: str = ""


def find_next_states(state: State) -> list[State]:
    next_state = []
    hexdigest = md5((passcode + state.path).encode()).hexdigest()[:4]
    open_doors = [True if i in open_door_chars else False for i in hexdigest]

    for is_open, direction, char in zip(open_doors, directions, char_directions):
        if is_open:
            new_pos = state.pos + direction
            if not (0 <= new_pos[0] <= 3 and 0 <= new_pos[1] <= 3):
                continue

            new_state = State(new_pos, state.path + char)
            next_state.append(new_state)

    return next_state


def solve_a() -> str:
    steps = 0
    initial_state = State(np.array([0, 0], dtype=int))
    state = initial_state
    all_states = [state]

    while not any(np.all(state.pos == target) for state in all_states):
        next_states = []
        for state in all_states:
            next_states += find_next_states(state)

        steps += 1
        all_states = next_states

    return [state.path for state in all_states if np.all(state.pos == target)][0]


def solve_b() -> int:
    steps = 0
    initial_state = State(np.array([0, 0], dtype=int))
    state = initial_state
    all_states = [state]
    solutions_paths = []

    while all_states:
        next_states = []
        for state in all_states:
            next_states += find_next_states(state)

        steps += 1
        solutions_paths += [
            state.path for state in next_states if np.all(state.pos == target)
        ]

        all_states = [state for state in next_states if np.any(state.pos != target)]

    return len(max(solutions_paths, key=lambda x: len(x)))


sol_a = solve_a()
print(f"{sol_a = }")

sol_b = solve_b()
print(f"{sol_b = }")
