from collections import deque
from dataclasses import dataclass
from typing import Optional, cast

num_elves = 3_017_957


@dataclass
class Elf:
    number: int
    present: int


def find_left(elves: deque[Elf]) -> Optional[int]:

    for i, elf in enumerate(elves):
        if i == 0:
            continue
        elif elf.present != 0:
            return i

    return None


def solve_a(num_elves: int) -> int:
    elves = deque([Elf(i, 1) for i in range(1, num_elves + 1)])

    while True:
        if elves[0].present == 0:
            elves.rotate(-1)
            continue

        next_elf = find_left(elves)
        if next_elf:
            elves[0].present += elves[next_elf].present
            elves[next_elf].present = 0
        else:
            break

        elves.rotate(-1)

    return [elf for elf in elves if elf.present != 0][0].number


sol_a = solve_a(num_elves)
print(f"{sol_a = }")

# this implementation is too slow (because it is expensive to remove elements
# from the middle of the deque) but it is useful to be able to look at the
# first 100 cases and get clues
# also big clues from Numberphile video:
# https://www.youtube.com/watch?v=uCsD3ZGzMgE
def solve_b_slow(num_elves: int) -> int:
    elves = deque([Elf(i, 1) for i in range(1, num_elves + 1)])

    while len(elves) != 1:
        elf = elves[0]
        target_elf = elves[len(elves) // 2]

        elf.present += target_elf.present
        elves.remove(target_elf)

        elves.rotate(-1)

    return elves[0].number


# for i in range(3, 100):
#     print(f"{i} -> {solve_b_slow(i)}")

# elves: 3 -> last: 3
# elves: 4 -> last: 1
# elves: 5 -> last: 2
# elves: 6 -> last: 3
# elves: 7 -> last: 5
# elves: 8 -> last: 7
# elves: 9 -> last: 9
# elves: 10 -> last: 1
# elves: 11 -> last: 2
# [...]
# elves: 26 -> last: 25
# elves: 27 -> last: 27
# elves: 28 -> last: 1
# [...]
# elves: 80 -> last: 79
# elves: 81 -> last: 81
# elves: 82 -> last: 1
# elves: 83 -> last: 2
# elves: 84 -> last: 3
# [...]


def solve_b(num_elves: int) -> int:
    last_pow: int = (
        next(filter(lambda x: x[0], [(3**i > num_elves, i) for i in range(20)]))[1]
        - 1
    )
    return num_elves - cast(int, 3**last_pow)


sol_b = solve_b(num_elves)
print(f"{sol_b = }")
