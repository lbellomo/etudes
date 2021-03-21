from typing import List

import pytest  # type: ignore


def parse_input(input_str: str) -> List[int]:
    return [int(i) for i in input_str.split(",")]


def read_input(path_input: str) -> List[int]:
    with open(path_input) as f_in:
        return parse_input(f_in.read())


def solve(data: List[int]) -> List[int]:
    for i in range(0, len(data), 4):
        opcode = data[i]
        if opcode == 99:
            break
        else:
            a = data[data[i + 1]]
            b = data[data[i + 2]]
            c = data[i + 3]

            if opcode == 1:
                data[c] = a + b
            elif opcode == 2:
                data[c] = a * b
            else:
                raise ValueError(f"Invalid value at position {i}")
    return data


def set_noun_verb(data: List[int], noun: int, verb: int):
    data[1] = noun
    data[2] = verb


def solve_part_b(start_data: List[int], output: int):
    for noun in range(100):
        for verb in range(100):
            data = start_data.copy()
            set_noun_verb(data, noun, verb)
            data = solve(data)
            if data[0] == output:
                return 100 * noun + verb


if __name__ == "__main__":
    # part a
    data = read_input("input.txt")
    set_noun_verb(data, 12, 2)
    data = solve(data)
    print(f"Sol part a: {data[0]}")
    # part b
    start_data = read_input("input.txt")
    sol_b = solve_part_b(start_data, 19690720)
    print(f"Sol part b: {sol_b}")


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("1,0,0,0,99", "2,0,0,0,99"),
        ("2,3,0,3,99", "2,3,0,6,99"),
        ("2,4,4,5,99,0", "2,4,4,5,99,9801"),
        ("1,1,1,4,99,5,6,0,99", "30,1,1,4,2,5,6,0,99"),
    ],
)
def test_solve(test_input, expected):
    data = parse_input(test_input)
    answer = parse_input(expected)
    sol = solve(data)
    assert sol == answer
