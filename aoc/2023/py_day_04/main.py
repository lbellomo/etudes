with open("input.txt") as f:
    data = f.read().splitlines()

import re
from typing import NamedTuple


class Card(NamedTuple):
    id: int
    win_numbers: list[int]
    numbers: list[int]


def parse_card(line: str) -> Card:
    card_id, win_numbers, numbers = re.split(r":|\|", line)
    card_id = int(card_id.strip("Card").strip())
    win_numbers = [int(i) for i in win_numbers.split()]
    numbers = [int(i) for i in numbers.split()]
    return Card(card_id, win_numbers, numbers)


def count_matches(c: Card) -> int:
    return sum(True for i in c.numbers if i in c.win_numbers)


def calc_points(c: Card) -> int:
    matches = count_matches(c)

    if not matches:
        return 0
    else:
        return 2 ** (matches - 1)


cards = [parse_card(line) for line in data]

sol_a = sum(calc_points(c) for c in cards)
print(f"{sol_a = }")

counter = {c.id: 1 for c in cards}

for c in cards:
    matches = count_matches(c)
    for i in range(1, matches + 1):
        counter[c.id + i] += counter[c.id]

sol_b = sum(counter.values())
print(f"{sol_b = }")
