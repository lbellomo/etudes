from collections import Counter
from typing import List


def read_input(path: str) -> List[str]:
    with open(path) as f:
        return [line.strip() for line in f.readlines()]


def get_message(data: List[str], filter_max: bool) -> str:
    counters: List[Counter] = [Counter() for _ in range(len(data[0]))]

    for line in data:
        for ch, counter in zip(line, counters):
            counter.update(ch)

    message = []
    for counter in counters:
        if filter_max:
            elem = 0
        else:
            elem = -1
        message.append(counter.most_common()[elem][0])

    return "".join(message)


def solve_a(data: List[str]) -> str:
    return get_message(data, filter_max=True)


def solve_b(data: List[str]) -> str:
    return get_message(data, filter_max=False)


if __name__ == "__main__":
    data = read_input("input.txt")
    sol_a = solve_a(data)
    print(f"sol a: {sol_a}")

    sol_b = solve_b(data)
    print(f"sol b: {sol_b}")

test_data = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar""".split()


def test_solve_a():
    result = "easter"
    assert solve_a(test_data) == result


def test_solve_b():
    result = "advent"
    assert solve_b(test_data) == result
