import numpy as np
import numpy.typing as npt


def parse(line: str) -> slice:
    split = line.split("-")
    start = int(split[0])
    end = int(split[1]) + 1
    return np.s_[start:end]


with open("input.txt") as f:
    data = [parse(line.strip()) for line in f]


def solve() -> npt.NDArray[np.bool_]:
    ips = np.ones([np.iinfo(np.uint32).max], dtype=bool)

    for ban_range in data:
        ips[ban_range] = False
    return ips


ips = solve()

sol_a = ips.argmax()
print(f"{sol_a = }")

sol_b = ips.sum()
print(f"{sol_b = }")
