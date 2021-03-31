from typing import Iterator

import pytest  # type: ignore


def read_data(path_data: str) -> list[int]:
    with open(path_data) as f_in:
        data = f_in.read()
    return [int(i) for i in data.split("-")]


def check_len(n: str) -> bool:
    return len(n) == 6


def get_chunks(n: str) -> Iterator[str]:
    return (n[i : i + 2] for i in range(len(n) - 1))


def check_adjacent_digits(n: str) -> bool:
    chunks = get_chunks(n)
    return any(chunk[0] == chunk[1] for chunk in chunks)


def check_never_decrese(n: str) -> bool:
    chunks = get_chunks(n)
    return all(chunk[0] <= chunk[1] for chunk in chunks)


def check_part_a(n: str) -> bool:
    is_valid = all((check_len(n), check_adjacent_digits(n), check_never_decrese(n)))
    return is_valid


def solve(range_start, range_end, func_part):
    return sum(func_part(str(i)) for i in range(range_start, range_end))


def check_strict_adjacent_digits(n: str) -> bool:
    last_index = len(n) - 1
    posibles_index = (i for i in range(last_index) if n[i] == n[i + 1])
    for i in posibles_index:
        if (i == 0 or n[i - 1] != n[i]) and (
            i == last_index - 1 or n[i + 2] != n[i + 1]
        ):
            return True
    return False


def check_part_b(n: str) -> bool:
    is_valid = all(
        (check_len(n), check_strict_adjacent_digits(n), check_never_decrese(n))
    )
    return is_valid


if __name__ == "__main__":
    data = read_data("input.txt")
    sol_a = solve(data[0], data[1], check_part_a)
    print(f"sol_a: {sol_a}")
    sol_b = solve(data[0], data[1], check_part_b)
    print(f"sol_b: {sol_b}")


@pytest.mark.parametrize(
    "test_input,expected", [(111111, True), (223450, False), (123789, False)]
)
def test_check_part_a(test_input, expected):
    sol = check_part_a(str(test_input))
    assert sol == expected


@pytest.mark.parametrize(
    "test_input,expected", [(112233, True), (123444, False), (111122, True)]
)
def test_check_part_b(test_input, expected):
    sol = check_part_b(str(test_input))
    assert sol == expected
