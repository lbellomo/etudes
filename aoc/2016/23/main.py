#!/usr/bin/env python3
import math
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


def solve(s):
    while True:
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


def initial_state(a):
    pos = 0
    registers = {i: 0 for i in "abcd"}
    registers["a"] = a
    data = read_data()

    s = State(pos, registers, data)
    return s


s = initial_state(a=7)
sol_a = solve(s)
print(f"{sol_a = }")

# i=6 sol=6120 math.factorial(i)=720 diff: 5400
# i=7 sol=10440 math.factorial(i)=5040 diff: 5400
# i=8 sol=45720 math.factorial(i)=40320 diff: 5400
# i=9 sol=368280 math.factorial(i)=362880 diff: 5400
# i=10 sol=3634200 math.factorial(i)=3628800 diff: 5400

# sol = i! + 5400

sol_b = math.factorial(12) + 5400
print(f"{sol_b = }")
