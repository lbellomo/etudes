with open("input.txt") as f:
    raw_data = [line.strip() for line in f]

Registers = dict[str, int]


def solve(registers: Registers) -> Registers:
    step = 0
    while True:
        step_plus_one = True

        try:
            instruction = raw_data[step]
        except IndexError:
            return registers

        split = instruction.split()
        if "cpy" in instruction:
            x = split[1]
            y = split[-1]
            if x not in registers:
                registers[y] = int(x)
            else:
                registers[y] = registers[x]

        elif "inc" in instruction:
            x = split[-1]
            registers[x] += 1

        elif "dec" in instruction:
            x = split[-1]
            registers[x] -= 1

        elif "jnz" in instruction:
            x = split[1]
            y = split[-1]
            if x in registers:
                if registers[x] != 0:
                    step += int(y)
                    step_plus_one = False
            elif int(x) != 0:
                step += int(y)
                step_plus_one = False

        if step_plus_one:
            step += 1


registers = {char: 0 for char in "abcd"}
sol_a = solve(registers)["a"]
print(f"{sol_a = }")


registers = {char: 0 for char in "abcd"}
registers["c"] = 1
sol_b = solve(registers)["a"]
print(f"{sol_b = }")
