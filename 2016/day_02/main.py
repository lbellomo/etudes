from typing import cast

MappingPos = dict[tuple[int, int], str]

pos_to_num_simple = {
    pos: str(num)
    for num, pos in enumerate(
        ((i, j) for j in range(1, -2, -1) for i in range(-1, 2)), start=1
    )
}
pos_to_num_complex = {
    pos: char
    for char, pos in zip(
        "123456789ABCD",
        [(i, j) for j in range(2, -3, -1) for i in range(-2, 3) if abs(i) + abs(j) < 3],
    )
}
char_to_vec = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}


def read_data(path_data: str) -> list[str]:
    with open(path_data) as f:
        return [line.strip() for line in f.readlines()]


def parse_line(
    pos: tuple[int, int], line: str, pos_to_num: MappingPos
) -> tuple[int, int]:
    for char in line:
        vec = char_to_vec[char]
        new_pos = cast(
            tuple[int, int],
            tuple(pos_elem + vec_elem for pos_elem, vec_elem in zip(pos, vec)),
        )

        if pos_to_num.get(new_pos):
            pos = new_pos

    return pos


def solve(data: list[str], pos_to_num: MappingPos, init_pos: tuple[int, int]) -> str:
    pos = init_pos
    result = []
    for line in data:
        pos = parse_line(pos, line, pos_to_num)
        result.append(pos)

    return "".join(pos_to_num[pos] for pos in result)


if __name__ == "__main__":
    data = read_data("input.txt")
    sol_a = solve(data, pos_to_num_simple, (0, 0))
    sol_b = solve(data, pos_to_num_complex, (-2, 0))
    print(f"sol_a: {sol_a}")
    print(f"sol_b: {sol_b}")


test_data = """
ULL
RRDDD
LURDL
UUUUD""".split()


def test_solve_simple():
    assert solve(test_data, pos_to_num_simple, (0, 0)) == "1985"


def test_solve_complex():
    assert solve(test_data, pos_to_num_complex, (-2, 0)) == "5DB3"
