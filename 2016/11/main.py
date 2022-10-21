from itertools import combinations
from copy import deepcopy
from dataclasses import dataclass
from typing import Iterable, Optional

Floor = list[str]


@dataclass
class State:
    floors: list[Floor]
    elevator: int


def get_hash(state: State) -> str:
    inverse = {"G": "M", "M": "G"}
    return str(state.elevator) + "|".join(
        [
            "".join(
                sorted(
                    [
                        elem if not (elem[0] + inverse[elem[1]]) in floor else elem[1]
                        for elem in floor
                    ]
                )
            )
            for floor in state.floors
        ]
    )


def is_target(state: State) -> bool:
    # return len(state.floors[3]) == 10
    return not any(any(state.floors[i]) for i in range(3))


def is_valid_floor(floor: Floor) -> bool:
    gen_in_floor = any(elem[1] == "G" for elem in floor)

    for elem in floor:
        if elem[1] == "M":
            component = elem[0]
            if component + "G" not in floor and gen_in_floor:
                return False
    return True


def is_valid(state: State) -> bool:
    return all(is_valid_floor(floor) for floor in state.floors)


def find_next_states(state: State) -> Iterable[State]:
    elevator = state.elevator
    for next_elevator in [elevator + 1, elevator - 1]:
        if not (3 >= next_elevator >= 0):
            continue

        for moved_elem in [(elem,) for elem in state.floors[elevator]] + list(
            combinations(state.floors[elevator], 2)
        ):
            new_state = deepcopy(state)
            new_state.elevator = next_elevator

            # si todos los pisos de abajo estan vacios, no bajo nada
            if elevator > next_elevator and not any(
                any(state.floors[i]) for i in range(elevator)
            ):
                continue

            new_state.floors[elevator] = [
                elem for elem in new_state.floors[elevator] if elem not in moved_elem
            ]
            new_state.floors[next_elevator] = new_state.floors[next_elevator] + [
                elem for elem in moved_elem
            ]
            yield new_state


def solve(initial_state: State) -> Optional[int]:
    count = 0
    state = initial_state
    states = [state]
    know_states = set([get_hash(state)])

    while states:
        next_states = []
        count += 1
        for state in states:
            for s in find_next_states(state):
                if is_target(s):
                    return count
                if is_valid(s) and get_hash(s) not in know_states:
                    next_states.append(s)
                    know_states.add(get_hash(s))

        states = next_states
    return None


initial_floors: list[Floor] = [
    ["TG", "TM", "PG", "SG"],
    ["PM", "SM"],
    ["pG", "pM", "RG", "RM"],
    [],
]

initial_state = State(initial_floors, elevator=0)
sol_a = solve(initial_state)
print(f"{sol_a = }")

initial_floors_b: list[Floor] = [
    ["TG", "TM", "PG", "SG", "EG", "EM", "DG", "DM"],
    ["PM", "SM"],
    ["pG", "pM", "RG", "RM"],
    [],
]

initial_state = State(initial_floors_b, elevator=0)
sol_b = solve(initial_state)
print(f"{sol_b = }")
