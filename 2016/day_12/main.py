from typing import List, Tuple, Dict, Union, Any
from dataclasses import dataclass, field

Register = str
Data = List[str]


@dataclass
class State:
    registers: Dict[Register, int] = field(default_factory=dict)
    index: int = 0


def read_data(path: str) -> Data:
    with open(path) as f:
        return [line.strip() for line in f.readlines()]


def parse_data(data: Data) -> List[Tuple[Any, List[Union[str, int]]]]:
    funcs = dict(cpy=cpy, inc=inc, dec=dec, jnz=jnz)

    instructions = []
    for raw_line in data:
        line = raw_line.split()
        func = funcs[line[0]]
        args = []
        for i in line[1:]:
            try:
                arg: Union[int, str] = int(i)
            except ValueError:
                arg = i
            args.append(arg)
        instructions.append((func, args))

    return instructions


def cpy(x: Union[Register, int], y: Register, state: State) -> State:
    if isinstance(x, str):
        targer = state.registers[x]
    else:
        targer = x

    state.registers[y] = targer
    return state


def inc(x: Register, state: State) -> State:
    state.registers[x] += 1
    return state


def dec(x: Register, state: State) -> State:
    state.registers[x] -= 1
    return state


def jnz(x: Union[Register, int], y: int, state: State) -> State:
    if isinstance(x, str):
        cond = state.registers[x]
    else:
        cond = x

    if cond != 0:
        state.index += y
    return state


def solve(data, c=0):
    instructions = parse_data(data)
    state = State()

    for i in list("abcd"):
        state.registers[i] = 0

    state.registers["c"] = c

    while True:
        next_instruction = state.index
        if next_instruction >= len(instructions):
            break
        func, args = instructions[next_instruction]
        state = func(*args, state=state)

        if next_instruction == state.index:
            state.index += 1

    return state.registers["a"]


if __name__ == "__main__":
    data = read_data("input.txt")
    sol_a = solve(data)
    print(f"sol a: {sol_a}")

    sol_b = solve(data, c=1)
    print(f"sol b: {sol_b}")


def test_solve():
    data = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a""".split(
        "\n"
    )
    assert solve(data) == 42
