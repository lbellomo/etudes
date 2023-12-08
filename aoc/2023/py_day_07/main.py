from typing import NamedTuple, Callable
from collections import Counter

with open("input.txt") as f:
    raw_data = f.read().splitlines()


class Item(NamedTuple):
    hand: str
    bid: int


def parse_line(line: str) -> Item:
    hand, bid = line.split()
    return Item(hand, int(bid))


def get_count_values(item: Item) -> list[int]:
    counter = Counter(item.hand)
    return sorted(list(counter.values()), reverse=True)


def get_count_values_joker(item: Item) -> list[int]:
    # print(item)
    counter = Counter(item.hand)

    if counter == Counter({"J": 5}):
        return [5]

    if "J" in counter:
        v_j = counter.pop("J")
        k, _ = counter.most_common()[0]
        counter[k] += v_j

    return sorted(list(counter.values()), reverse=True)


def calc_strength(count: Counter) -> int:
    match count:
        case [5]:
            return 0
        case [4, 1]:
            return 1
        case [3, 2]:
            return 2
        case [3, 1, 1]:
            return 3
        case [2, 2, _]:
            return 4
        case [2, 1, 1, 1]:
            return 5
        case [1, 1, 1, 1, 1]:
            return 6
        case _:
            raise ValueError()


def solve(
    hands: list[Item], cards_values: dict[str, int], get_count_values: Callable
) -> int:
    # sort by value in inverse orden
    for i in range(4, -1, -1):
        hands = sorted(hands, key=lambda x: cards_values[x.hand[i]])
    # sort by strength
    hands = sorted(hands, key=lambda x: calc_strength(get_count_values(x)))

    return sum([h.bid * i for i, h in enumerate(reversed(hands), start=1)])


data = [parse_line(line) for line in raw_data]
hands = data

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
cards_values = {v: i for i, v in enumerate(cards)}


sol_a = solve(hands, cards_values, get_count_values)
print(f"{sol_a = }")

hands = data

cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
cards_values = {v: i for i, v in enumerate(cards)}

hands = data

sol_b = solve(hands, cards_values, get_count_values_joker)
print(f"{sol_b = }")
