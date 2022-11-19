from typing import Optional, NamedTuple
import numpy as np
import numpy.typing as npt

with open("input.txt") as f:
    raw_data = [line.strip() for line in f]

Display = npt.NDArray[np.int_]


class Instruction(NamedTuple):
    operation: str
    axis_name: Optional[str]
    a: int
    b: int


def parse(line: str) -> Instruction:
    if "rect" in line:
        operation, line = line.split()
        axis_name = None
        a, b = line.split("x")
    elif "rotate" in line:
        operation, axis_name, a, _, b = line.split()
        a = a.split("=")[-1]

    return Instruction(operation, axis_name, int(a), int(b))


def rect(display: Display, a: int, b: int) -> Display:
    display[:b, :a] = 1
    return display


def rotate(display: Display, axis_name: Optional[str], a: int, b: int) -> Display:
    if axis_name == "column":
        display[:, a] = np.roll(display[:, a], b, axis=0)
    elif axis_name == "row":
        display[a, :] = np.roll(display[a, :], b)

    return display


def parse_operation(display: Display, seq: Instruction) -> Display:
    if seq.operation == "rect":
        display = rect(display, seq.a, seq.b)
    elif seq.operation == "rotate":
        display = rotate(display, seq.axis_name, seq.a, seq.b)
    return display


display = np.zeros([6, 50], dtype=int)
sequence = [parse(line) for line in raw_data]

for seq in sequence:
    display = parse_operation(display, seq)

sol_a = display.sum()
print(f"{sol_a = }")

sol_b = ["".join(str(i) for i in column).replace("0", " ") for column in display]
print("sol_b =")
for line in sol_b:
    print(line)
