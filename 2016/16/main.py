def next_state(state: str) -> str:
    return state + "0" + "".join("1" if i == "0" else "0" for i in reversed(state))


assert next_state("1") == "100"
assert next_state("0") == "001"
assert next_state("11111") == "11111000000"
assert next_state("111100001010") == "1111000010100101011110000"


def checksum(data: str) -> str:
    while len(data) % 2 == 0:
        data = "".join(["1" if i == j else "0" for i, j in zip(data[::2], data[1::2])])
    return data


assert checksum("110010110100") == "100"


def solve(initial_state: str, disk_size: int) -> str:
    state = initial_state
    while len(state) < disk_size:
        state = next_state(state)

    return checksum(state[:disk_size])


assert solve("10000", 20) == "01100"

initial_state = "10111100110001111"

disk_size = 272
sol_a = solve(initial_state, disk_size)
print(f"{sol_a = }")

disk_size = 35651584
sol_b = solve(initial_state, disk_size)
print(f"{sol_b = }")
