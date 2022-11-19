from dataclasses import dataclass
from typing import NamedTuple
from collections import defaultdict

with open("input.txt") as f:
    raw_data = [line.strip() for line in f]


class Init(NamedTuple):
    value: int
    bot: int


class Target(NamedTuple):
    type: str
    value: int


@dataclass
class Move:
    bot: int
    target_low: Target
    target_high: Target
    done: bool = False


def parse_data(raw_data: list[str]) -> tuple[list[Init], list[Move]]:
    inits = []
    moves = []

    for line in raw_data:
        if "value" in line:
            split = line.split()
            inits.append(Init(int(split[1]), int(split[-1])))
        else:
            split = line.split()
            target_low = Target(split[5], int(split[6]))
            target_high = Target(split[-2], int(split[-1]))
            moves.append(Move(int(split[1]), target_low, target_high))
    return inits, moves


def solve(
    inits: list[Init], moves: list[Move]
) -> tuple[dict[int, list[int]], dict[int, int]]:
    bots = defaultdict(list)
    bins = {}

    for i in inits:
        bots[i.bot].append(i.value)

    while not all(m.done for m in moves):
        for m in moves:
            bot = bots[m.bot]
            if not m.done and len(bot) == 2:
                target_low = m.target_low.value
                value_min = min(bot)

                target_high = m.target_high.value
                value_max = max(bot)

                if m.target_low.type == "bot":
                    bots[target_low].append(value_min)
                else:
                    bins[target_low] = value_min

                if m.target_high.type == "bot":
                    bots[target_high].append(value_max)
                else:
                    bins[target_high] = value_max
                m.done = True

    return bots, bins


bots, bins = solve(*parse_data(raw_data))
sol_a = [k for k, v in bots.items() if sorted(v) == [17, 61]][0]
print(f"{sol_a = }")
sol_b = bins[0] * bins[1] * bins[2]
print(f"{sol_b = }")
