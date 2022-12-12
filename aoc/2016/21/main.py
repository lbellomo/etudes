#!/usr/bin/env python3

from collections import deque

with open("input.txt") as f:
    raw_data = [line.strip() for line in f]


def parse_data():
    filter_words = [
        "based",
        "on",
        "position",
        "of",
        "letter",
        "with",
        "to",
        "positions",
        "through",
        "steps",
        "step",
    ]

    data = []
    for line in raw_data:
        row = [i for i in line.split() if i not in filter_words]
        data.append([int(i) if i.isdigit() else i for i in row])

    return data


def swap_pos(s: str, i: int, j: int) -> str:
    s_list = list(s)
    s_list[i], s_list[j] = s_list[j], s_list[i]
    return "".join(s_list)


def swap_letter(s: str, x: str, y: str) -> str:
    s_list = list(s)
    i = s_list.index(x)
    j = s_list.index(y)
    s_list[i], s_list[j] = s_list[j], s_list[i]
    return "".join(s_list)


def rotate(s: str, direction: str, steps: int) -> str:
    s_deque = deque(s)

    if direction == "left":
        steps *= -1

    s_deque.rotate(steps)
    return "".join(s_deque)


def rotate_pos(s: str, x: str) -> str:
    s_deque = deque(s)

    steps = s_deque.index(x)

    if steps >= 4:
        steps += 1

    steps += 1

    s_deque.rotate(steps)
    return "".join(s_deque)


def reverse(s: str, i: int, j: int) -> str:
    s_list = list(s)

    s_list[i : j + 1] = reversed(s_list[i : j + 1])
    return "".join(s_list)


def move(s: str, i: int, j: int) -> str:
    s_list = list(s)
    s_list.insert(j, s_list.pop(i))
    return "".join(s_list)


def rotate_rev(s: str, direction: str, steps: int) -> str:
    steps *= -1
    return rotate(s, direction, steps)


def rotate_pos_rev(s: str, x: str) -> str:
    for i in range(len(s)):
        s_deque = deque(s)
        s_deque.rotate(i)

        s_tmp = "".join(s_deque)

        if rotate_pos(s_tmp, x) == s:
            break

    return s_tmp


def move_rev(s: str, i: int, j: int) -> str:
    return move(s, j, i)


def solve(s: str, is_reverse: bool = False) -> str:
    data = parse_data()

    if is_reverse:
        data = reversed(data)

    for operation in data:
        function = operation.pop(0)
        match function:
            case "swap":
                try:
                    s = swap_pos(s, *operation)
                except TypeError:
                    s = swap_letter(s, *operation)
            case "rotate":
                if len(operation) == 2:
                    if is_reverse:
                        s = rotate_rev(s, *operation)
                    else:
                        s = rotate(s, *operation)
                else:
                    if is_reverse:
                        s = rotate_pos_rev(s, *operation)
                    else:
                        s = rotate_pos(s, *operation)
            case "reverse":
                s = reverse(s, *operation)
            case "move":
                if is_reverse:
                    s = move_rev(s, *operation)
                else:
                    s = move(s, *operation)

    return s


sol_a = solve("abcdefgh")
print(f"{sol_a = }")

sol_b = solve("fbgdceah", is_reverse=True)
print(f"{sol_b = }")


def test_swap_pos():
    s = "abcde"
    assert swap_pos(s, 4, 0) == "ebcda"


def test_swap_letter():
    s = "ebcda"
    assert swap_letter(s, "d", "b") == "edcba"


def test_rotate():
    s = "abcde"
    assert rotate(s, "left", 1) == "bcdea"


def test_rotate_pos():
    s = "abdec"
    assert rotate_pos(s, "b") == "ecabd"
    s = "ecabd"
    assert rotate_pos(s, "d") == "decab"


def test_reverse():
    s = "edcba"
    assert reverse(s, 0, 4) == "abcde"


def test_move():
    s = "bcdea"
    assert move(s, 1, 4) == "bdeac"
    s = "bdeac"
    assert move(s, 3, 0) == "abdec"
