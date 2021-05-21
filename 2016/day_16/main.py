import pytest


def dragon_curve_step(a: str) -> str:
    b = a[::-1]
    b = "".join("0" if i == "1" else "1" for i in b)
    return a + "0" + b


def checksum_step(data: str) -> str:
    chunks = (data[i: i + 2] for i in range(0, len(data), 2))
    return "".join("1" if chunk[0] == chunk[1] else "0" for chunk in chunks)


def solve(length: int, state: str) -> str:
    while len(state) < length:
        state = dragon_curve_step(state)

    state = state[:length]

    while len(state) % 2 == 0:
        state = checksum_step(state)

    return state


if __name__ == "__main__":
    length = 272
    state = "10111100110001111"

    sol_a = solve(length, state)
    print(f"sol a: {sol_a}")

    length = 35651584
    state = "10111100110001111"

    sol_b = solve(length, state)
    print(f"sol b: {sol_b}")


def test_sol():
    length = 20
    state = "10000"

    assert solve(length, state) == "01100"


test_a = [("1", "100"), ("0", "001"), ("11111", "11111000000"), ("111100001010", "1111000010100101011110000")]
test_data = [("110010110100", "110101"), ("110101", "100")]


@pytest.mark.parametrize("a,expected", test_a)
def test_dragon_curve_step(a, expected):
    assert dragon_curve_step(a) == expected


@pytest.mark.parametrize("data,expected", test_data)
def test_checksum_step(data, expected):
    assert checksum_step(data) == expected
