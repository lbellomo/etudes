#!/usr/bin/env python3

from dataclasses import dataclass


def intify(obj):
    try:
        return int(obj)
    except ValueError:
        return obj


def read_data():
    with open("input.txt") as f:
        raw_data = [line.strip().split() for line in f]

    return [[intify(i) for i in row] for row in raw_data]


@dataclass
class State:
    pos: int
    registers: dict[str, int]
    data: list
    clock: list


def get_value(x):
    match x:
        case str():
            value = s.registers[x]
        case int():
            value = x

    return value


def copy(x, y):
    s.registers[y] = get_value(x)
    s.pos += 1


def inc(x):
    s.registers[x] += 1
    s.pos += 1


def dec(x):
    s.registers[x] -= 1
    s.pos += 1


def jnz(x, y):
    if get_value(x) != 0:
        s.pos += get_value(y)
    else:
        s.pos += 1


def tgl(x):
    index = s.pos + get_value(x)
    s.pos += 1

    if index >= len(s.data):
        return

    instruction = s.data[index]

    match instruction:
        case "inc", i:
            new_instruction = ["dec", i]
        case _, i:
            new_instruction = ["inc", i]
        case "jnz", i, j:
            new_instruction = ["cpy", i, j]
        case _, i, j:
            new_instruction = ["jnz", i, j]

    s.data[index] = new_instruction


def out(x):
    s.pos += 1
    value = get_value(x)
    if value not in [0, 1]:
        raise ValueError

    if len(s.clock) == 0:
        s.clock.append(value)
    else:
        last_value = s.clock[-1]
        match (value, last_value):
            case (0, 1) | (1, 0):
                s.clock.append(value)
            case (_, _):
                raise ValueError


def solve(s):
    while len(s.clock) < 100:
        try:
            instruction = s.data[s.pos]
        except IndexError:
            return s.registers["a"]

        match instruction:
            case "cpy", x, y:
                copy(x, y)
            case "inc", x:
                inc(x)
            case "dec", x:
                dec(x)
            case "jnz", x, y:
                jnz(x, y)
            case "tgl", x:
                tgl(x)
            case "out", x:
                out(x)

    return


def initial_state(a):
    pos = 0
    registers = {i: 0 for i in "abcd"}
    registers["a"] = a
    data = read_data()
    clock = []

    s = State(pos, registers, data, clock)
    return s


i = 1
while True:
    s = initial_state(a=i)
    try:
        _ = solve(s)
        break
    except ValueError:
        i += 1
        continue

sol_a = i
print(f"{sol_a = }")
