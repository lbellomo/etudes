from typing import List, Callable
from math import trunc

import pytest  # type: ignore


def read_input(path_input: str) -> List[int]:
    with open(path_input) as f_in:
        return [int(line) for line in f_in.readlines()]


def find_fuel(mass: int) -> int:
    return trunc(mass / 3) - 2


def find_fuel_recursive(mass: int) -> int:
    total = 0
    while True:
        fuel = find_fuel(mass)
        if fuel > 0:
            total += fuel
            mass = fuel
        else:
            return total


def solve(data: List[int], fuel_function: Callable[[int], int]) -> int:
    return sum(fuel_function(i) for i in data)


if __name__ == "__main__":
    data = read_input("input.txt")
    sol_a = solve(data, find_fuel)
    print("Sol a: ", sol_a)
    sol_b = solve(data, find_fuel_recursive)
    print("Sol b: ", sol_b)


@pytest.mark.parametrize(
    "test_input,expected", [(12, 2), (14, 2), (1969, 654), (100756, 33583)]
)
def test_find_fuel(test_input, expected):
    assert find_fuel(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [(14, 2), (1969, 966), (100756, 50346)])
def test_find_fuel_recursive(test_input, expected):
    assert find_fuel_recursive(test_input) == expected
