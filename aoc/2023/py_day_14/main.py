with open("input.txt") as f:
    raw_data = f.read().splitlines()


def transpose(pattern):
    return ["".join(row[i] for row in pattern) for i in range(size)]


size = len(raw_data[0])
data = transpose(raw_data)


def advance(row):
    while ".O" in row:
        row = row.replace(".O", "O.", 1)
    return row


data = [advance(row) for row in data]

sol_a = sum(
    [sum(i for i, elem in enumerate(row[::-1], start=1) if elem == "O") for row in data]
)
print(f"{sol_a = }")


def rev(data):
    return [row[::-1] for row in data]


def cycle(data):
    data = [advance(row) for row in transpose(data)]
    data = [advance(row) for row in transpose(data)]
    data = [advance(row) for row in rev(transpose(data))]
    data = [advance(row) for row in rev(transpose(rev(data)))]

    return rev(data)


data = raw_data[::]

know_states = set()
state = "".join(data)
used_cycles = 0

while state not in know_states:
    know_states.update((state,))
    data = cycle(data)
    state = "".join(data)
    used_cycles += 1

state = "".join(data)
data = cycle(data)
loop_len = 1

while "".join(data) != state:
    data = cycle(data)
    loop_len += 1

left_cycles = (1000000000 - used_cycles) % loop_len

for _ in range(left_cycles):
    data = cycle(data)

data = transpose(data)
sol_b = sum(
    [sum(i for i, elem in enumerate(row[::-1], start=1) if elem == "O") for row in data]
)
print(f"{sol_b = }")
