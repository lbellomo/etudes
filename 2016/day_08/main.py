from typing import List, Tuple

import numpy as np

Screen = np.ndarray


def read_data(path: str) -> List[str]:
    with open(path) as f:
        return [line.strip() for line in f.readlines()]


def init_screen(x_size: int, y_size: int) -> Screen:
    return np.zeros((x_size, y_size), dtype=np.int0)


def rect(x: int, y: int, screen: Screen) -> Screen:
    screen[:y, :x] = 1
    return screen


def rotate_column(x: int, shift: int, screen: Screen) -> Screen:
    screen[:, x] = np.roll(screen[:, x], shift)
    return screen


def rotate_row(y: int, shift: int, screen: Screen) -> Screen:
    screen[y, :] = np.roll(screen[y, :], shift)
    return screen


def solve(data: List[str], size: Tuple[int, int]) -> Screen:
    screen = init_screen(*size)
    instructions = []

    for line in data:
        func_type, rest = line.split(" ", maxsplit=1)
        if func_type == "rect":
            x, y = [int(i) for i in rest.split("x")]
            instructions.append([rect, (x, y, screen)])
        elif func_type == "rotate":
            rest_split = rest.split()

            if rest_split[0] == "column":
                func = rotate_column  # type: ignore
            elif rest_split[0] == "row":
                func = rotate_row  # type: ignore
            else:
                raise ValueError("invalid func type")

            value = int(rest_split[-3].split("=")[-1])
            shift = int(rest_split[-1])
            instructions.append([func, (value, shift, screen)])

    for func, args in instructions:  # type: ignore
        screen = func(*args)  # type: ignore

    return screen


def solve_a(data: List[str], size: Tuple[int, int]) -> np.number:
    screen = solve(data, size)
    return screen.sum()


if __name__ == "__main__":
    data = read_data("input.txt")
    size = (6, 50)
    sol_a = solve_a(data, size)
    print(f"sol a: {sol_a}")

    sol = solve(data, size)
    print("sol b:")
    for row in sol:
        print(" ".join([str(i) for i in row.tolist()]).replace("0", " "))


def test_solve_a():
    test_size = (3, 7)
    test_data = """rect 3x2
    rotate column x=1 by 1
    rotate row y=0 by 4
    rotate column x=1 by 1""".split(
        "\n"
    )

    assert solve_a(test_data, test_size) == 6
