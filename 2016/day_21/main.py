from typing import List, Tuple
from collections import deque

RawData = List[str]
Args = List[str]
Operation = Tuple[str, Args]
Data = List[Operation]


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


def swap(txt: str, args: Args) -> str:
    if args[0].isnumeric():
        i, j = tuple(int(i) for i in args)
    else:
        i, j = tuple(txt.index(i) for i in args)

    txt_list = list(txt)
    txt_list[i], txt_list[j] = txt_list[j], txt_list[i]
    return "".join(txt_list)


def rotate(txt: str, args: Args) -> str:
    if len(args) == 2:
        steps = int(args[1])
        # rotate: right == positive, left == negative
        if args[0] == "left":
            steps *= -1

    else:
        index = txt.index(args[0])
        steps = index + 1
        if index >= 4:
            steps += 1

    txt_deque = deque(txt)
    txt_deque.rotate(steps)
    return "".join(txt_deque)


def reverse(txt: str, args: Args) -> str:
    i, j = tuple(int(i) for i in args)
    txt_list = list(txt)
    txt_list[i : j + 1] = txt_list[i : j + 1][::-1]
    return "".join(txt_list)


def move(txt: str, args: Args) -> str:
    i, j = tuple(int(i) for i in args)
    txt_list = list(txt)
    letter = txt_list.pop(i)
    txt_list.insert(j, letter)
    return "".join(txt_list)


def solve_a(txt: str, data: Data) -> str:
    for chunk in data:
        operation = operations[chunk[0]]
        args = chunk[1]
        txt = operation(txt, args)

    return txt


operations = {"swap": swap, "rotate": rotate, "reverse": reverse, "move": move}


if __name__ == "__main__":

    txt = "abcdefgh"
    data = parse_data(read_data("input.txt"))
    sol_a = solve_a(txt, data)
    print(f"sol a: {sol_a}")


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

    assert solve_a(txt, data) == "decab"
