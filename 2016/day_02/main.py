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


def parse_line(line: str, pos_to_num: MappingPos) -> str:
    pos = (0, 0)
    for char in line:
        vec = char_to_vec[char]
        # new_pos = (pos[0] + vec[0], pos[1] + vec[1])
        new_pos = tuple(pos_elem + vec_elem for pos_elem, vec_elem in zip(pos, vec))
        new_pos = cast(tuple[int, int], new_pos)

        if pos_to_num.get(new_pos):
            pos = new_pos

    return pos_to_num[pos]


def solve(data: list[str], pos_to_num: MappingPos) -> str:
    return "".join([parse_line(line, pos_to_num) for line in data])


if __name__ == "__main__":
    data = read_data("input.txt")
    sol_a = solve(data, pos_to_num_simple)
    sol_b = solve(data, pos_to_num_complex)
    print(f"sol_a: {sol_a}")
    print(f"sol_b: {sol_b}")
