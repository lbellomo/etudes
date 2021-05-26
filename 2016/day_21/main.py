from typing import List, Tuple, Dict
from collections import deque

RawData = List[str]
Args = List[str]
Operation = Tuple[str, Args]
Data = List[Operation]


def make_table_reverse_rotate() -> Dict[int, int]:
    """A table for the inverse of the rotation. Only work for len % 2 == 0"""
    char = "a"
    table_reverse_rotate = dict()
    origin_txt = "abcdefgh"
    for i in range(len(origin_txt)):
        txt_deque = deque(origin_txt)
        txt_deque.rotate(i)
        txt = "".join(txt_deque)

        rotate_txt = rotate(txt, [char])
        new_index = rotate_txt.index(char)
        # measure the distance after the rotation
        table_reverse_rotate[new_index] = i - new_index

    return table_reverse_rotate


def read_data(path: str) -> RawData:
    with open(path) as f:
        return [line.strip() for line in f.readlines()]


def parse_line(line: str) -> Operation:
    line_split = line.split()
    args = []
    operation = line_split[0]

    if operation in ["swap", "reverse", "move"]:
        args.append(line_split[2])
        args.append(line_split[-1])
    elif operation == "rotate":
        if "left" in line or "right" in line:
            args.append(line_split[1])
            args.append(line_split[-2])
        elif "based on position" in line:
            args.append(line_split[-1])

    return operation, args


def parse_data(raw_data: RawData) -> Data:
    return [parse_line(line) for line in raw_data]


def swap(txt: str, args: Args, reverse: bool = False) -> str:
    if reverse:
        # this operation in reversible, no extra work needed
        pass

    if args[0].isnumeric():
        i, j = tuple(int(i) for i in args)
    else:
        i, j = tuple(txt.index(i) for i in args)

    txt_list = list(txt)
    txt_list[i], txt_list[j] = txt_list[j], txt_list[i]
    return "".join(txt_list)


def rotate(txt: str, args: Args, reverse: bool = False) -> str:
    if len(args) == 2:
        steps = int(args[1])
        # rotate: right == positive, left == negative
        if args[0] == "left":
            steps *= -1

        if reverse:
            steps *= -1

    else:
        char = args[0]
        if not reverse:
            index = txt.index(char)
            steps = index + 1
            if index >= 4:
                steps += 1
        else:
            steps = table_reverse_rotate[txt.index(char)]

    txt_deque = deque(txt)
    txt_deque.rotate(steps)
    return "".join(txt_deque)


def reverse(txt: str, args: Args, reverse: bool = False) -> str:
    if reverse:
        # this operation in reversible, no extra work needed
        pass

    i, j = tuple(int(i) for i in args)
    txt_list = list(txt)
    txt_list[i : j + 1] = txt_list[i : j + 1][::-1]
    return "".join(txt_list)


def move(txt: str, args: Args, reverse: bool = False) -> str:
    i, j = tuple(int(i) for i in args)
    if reverse:
        i, j = j, i

    txt_list = list(txt)
    letter = txt_list.pop(i)
    txt_list.insert(j, letter)
    return "".join(txt_list)


def solve(txt: str, data: Data, reverse=False) -> str:
    if reverse:
        data = data[::-1]

    for chunk in data:
        operation = operations[chunk[0]]
        args = chunk[1]
        txt = operation(txt, args, reverse)

    return txt


table_reverse_rotate = make_table_reverse_rotate()
# {1: -1, 3: -2, 5: -3, 7: -4, 2: 2, 4: 1, 6: 0, 0: 7}

operations = {"swap": swap, "rotate": rotate, "reverse": reverse, "move": move}

if __name__ == "__main__":

    txt = "abcdefgh"
    data = parse_data(read_data("input.txt"))
    sol_a = solve(txt, data)
    print(f"sol a: {sol_a}")

    scrambled_txt = "fbgdceah"
    sol_b = solve(scrambled_txt, data, reverse=True)
    print(f"sol b: {sol_b}")


def test_solve_a():
    raw_data = """swap position 4 with position 0
    swap letter d with letter b
    reverse positions 0 through 4
    rotate left 1 step
    move position 1 to position 4
    move position 3 to position 0
    rotate based on position of letter b
    rotate based on position of letter d""".split(
        "\n"
    )

    txt = "abcde"
    data = parse_data(raw_data)

    assert solve(txt, data) == "decab"


def test_solve_b():
    txt = "abcdefgh"
    data = parse_data(read_data("input.txt"))
    scrambled_txt = solve(txt, data)
    assert solve(scrambled_txt, data, reverse=True) == txt
