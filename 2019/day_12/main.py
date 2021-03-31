from math import prod
from collections import Counter
from typing import Iterable

import pytest  # type: ignore


def read_data(path_data: str) -> list[str]:
    with open(path_data) as f_in:
        data = [line.strip() for line in f_in]
    return data


def process_data(data: list[str]) -> tuple[list[list[int]], list[list[int]]]:
    moons_pos = []
    moons_vel = []
    for line in data:
        moon = [
            int(i.split("=")[1])
            for i in line.replace("<", "").replace(">", "").split(", ")
        ]
        moons_pos.append(moon)
        moons_vel.append([0, 0, 0])
    return moons_pos, moons_vel


def update_vel(moons_pos: list[list[int]], moons_vel: list[list[int]]):
    """One step updating the velocity moons"""
    len_moons = len(moons_pos)

    for i in range(len_moons):
        for j in range(i + 1, len_moons):

            # iter over x, y, z
            for coor in range(3):
                if moons_pos[i][coor] < moons_pos[j][coor]:
                    moons_vel[i][coor] += 1
                    moons_vel[j][coor] -= 1
                elif moons_pos[i][coor] > moons_pos[j][coor]:
                    moons_vel[i][coor] -= 1
                    moons_vel[j][coor] += 1
                else:
                    continue


def update_pos(moons_pos: list[list[int]], moons_vel: list[list[int]]):
    """One step updating the position of all moons"""
    len_moons = len(moons_pos)

    for i in range(len_moons):
        for coor in range(3):
            moons_pos[i][coor] += moons_vel[i][coor]


def solve_a(moons_pos: list[list[int]], moons_vel: list[list[int]], steps: int) -> int:
    for _ in range(steps):
        update_vel(moons_pos, moons_vel)
        update_pos(moons_pos, moons_vel)

    total_energy = sum(
        sum(abs(i) for i in pos) * sum(abs(i) for i in vel)
        for pos, vel in zip(moons_pos, moons_vel)
    )
    return total_energy


def find_prime_factors(n: int) -> list[int]:
    factors = []
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = n // i
                factors.append(i)
                break
    return factors


def find_least_common_multiple(numbers: list[int]) -> int:
    all_prime_factors = [find_prime_factors(numbers[i]) for i in range(len(numbers))]

    primes: dict[int, int] = {}
    for prime_factors in all_prime_factors:
        for prime, count in Counter(prime_factors).items():
            if primes.get(prime, 0) < count:
                primes[prime] = count

    return prod(prime ** count for prime, count in primes.items())


def solve_b(moons_pos: list[list[int]], moons_vel: list[list[int]]) -> int:

    step = 0
    find = [0, 0, 0]

    know_states: list[set[Iterable[int]]] = [set(), set(), set()]

    while not all(find):

        for i in range(3):
            if not find[i]:
                state = tuple(
                    [pos[i] for pos in moons_pos] + [vel[i] for vel in moons_vel]
                )
                if state in know_states[i]:
                    find[i] = step
                else:
                    know_states[i].update([state])

        update_vel(moons_pos, moons_vel)
        update_pos(moons_pos, moons_vel)

        step += 1

    return find_least_common_multiple(find)


if __name__ == "__main__":
    data = read_data("input.txt")
    # data = example_2
    moons_pos, moons_vel = process_data(data)
    sol_a = solve_a(moons_pos, moons_vel, 1000)
    print(f"sol_a: {sol_a}")
    moons_pos, moons_vel = process_data(data)
    sol_b = solve_b(moons_pos, moons_vel)
    print(f"sol_b: {sol_b}")


example_1 = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""".split(
    "\n"
)

example_2 = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>""".split(
    "\n"
)


@pytest.mark.parametrize(
    "test_input,steps,expected", ([example_1, 10, 179], [example_2, 100, 1940])
)
def test_solve_a(test_input, steps, expected):
    moons_pos, moons_vel = process_data(test_input)
    sol = solve_a(moons_pos, moons_vel, steps)
    assert sol == expected


@pytest.mark.parametrize(
    "test_input,expected", ([example_1, 2772], [example_2, 4686774924])
)
def test_solve_b(test_input, expected):
    moons_pos, moons_vel = process_data(test_input)
    sol = solve_b(moons_pos, moons_vel)
    assert sol == expected
