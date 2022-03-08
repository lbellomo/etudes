from typing import Generator
from itertools import permutations

Triangle = list[int]
Data = list[Triangle]


def read_data(path_data: str) -> Data:
    with open(path_data) as f:
        return [[int(i) for i in line.split()] for line in f.readlines()]


def transpose(data: Data) -> Generator[Triangle, None, None]:
    for i in range(0, len(data), 3):
        for j in range(3):
            yield [data[i : i + 3][k][j] for k in range(3)]


def is_valid(triangle: Triangle) -> bool:
    for sides in permutations(triangle, 3):
        if sum(sides[:2]) <= sides[-1]:
            return False
    return True


if __name__ == "__main__":
    data = read_data("input.txt")

    sol_a = sum(is_valid(triangle) for triangle in data)
    sol_b = sum(is_valid(triangle) for triangle in transpose(data))

    print(f"sol_a: {sol_a}")
    print(f"sol_b: {sol_b}")


def test_is_valid():
    assert is_valid([5, 10, 25]) is False


def test_transpose():
    test_data = """101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603""".splitlines()
    test_data = [[int(i) for i in line.split()] for line in test_data]
    for triangle in transpose(test_data):
        # look that all the triangles have the same hundreds digit
        assert len(set(i // 100 for i in triangle)) == 1
