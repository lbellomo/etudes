from collections import namedtuple

with open("input.txt") as f:
    raw_instructions = [line.strip() for line in f]


def parse_instruction(i):
    i_register = None
    i_offset = None

    i_split = i.replace(",", "").split()
    i_type = i_split[0]

    if i_type in ["jio", "jie"]:
        i_register = i_split[1]
        i_offset = int(i_split[2])
    elif i_type == "jmp":
        i_offset = int(i_split[1])
    else:
        i_register = i_split[1]
    return Instruction(i_type, i_register, i_offset)


Instruction = namedtuple("Instruction", ("type", "register", "offset"))
instructions = [parse_instruction(i) for i in raw_instructions]


def solve():
    index = 0

    while True:
        try:
            i = instructions[index]
        except IndexError:
            return registers["b"]
        jump = False

        if i.type == "inc":
            registers[i.register] += 1
        elif i.type == "tpl":
            registers[i.register] *= 3
        elif i.type == "hlf":
            registers[i.register] //= 2
        elif i.type == "jmp":
            index += i.offset
            jump = True
        elif i.type == "jie":
            if registers[i.register] % 2 == 0:
                index += i.offset
                jump = True
        elif i.type == "jio":
            if registers[i.register] == 1:
                index += i.offset
                jump = True

        if not jump:
            index += 1


registers = {"a": 0, "b": 0}
sol_a = solve()
print(f"{sol_a = }")

registers = {"a": 1, "b": 0}
sol_b = solve()
print(f"{sol_b = }")
