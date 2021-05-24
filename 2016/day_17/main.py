import hashlib
from typing import List

import pytest

rooms = {}
for i in range(1, 4 * 4 + 1):
    options = {}
    if not i % 4 == 0:
        options["R"] = str(i + 1)
    if not i % 4 == 1:
        options["L"] = str(i - 1)
    if i > 4:
        options["U"] = str(i - 4)
    if i <= 12:
        options["D"] = str(i + 4)

    rooms[str(i)] = options


def get_choices(passcode: str, room: str) -> List[str]:
    valid_chars = "bcdef"

    md5 = hashlib.md5(passcode.encode()).hexdigest()[:4]

    valid_options = [True if ch in valid_chars else False for ch in md5]
    valid_choices = [
        choice for choice, is_valid in zip("UDLR", valid_options) if is_valid
    ]
    choices = [choice for choice in valid_choices if choice in rooms[room]]
    return choices


def solve_a(states):
    while True:
        new_states = []
        for state in states:
            room = state["room"]
            passcode = state["passcode"]

            choices = get_choices(passcode, room)

            if choices:
                for choice in choices:
                    new_room = rooms[room][choice]
                    new_passcode = passcode + choice

                    if new_room == "16":
                        return new_passcode[8:]

                    new_states.append({"room": new_room, "passcode": new_passcode})

        states = new_states


if __name__ == "__main__":
    room = "1"
    passcode = "bwnlcvfs"  # "ihgpwlah"
    state = {"room": "1", "passcode": passcode}
    states = [state]
    sol_a = solve_a(states)
    print(f"sol a: {sol_a}")


test_data_a = [
    ("ihgpwlah", "DDRRRD"),
    ("kglvqrro", "DDUDRLRRUDRD"),
    ("ulqzkmiv", "DRURDRUDDLLDLUURRDULRLDUUDDDRR"),
]


@pytest.mark.parametrize("passcode,expected", test_data_a)
def test_solve_a(passcode, expected):
    states = [{"room": "1", "passcode": passcode}]
    sol = solve_a(states)
    assert sol == expected
