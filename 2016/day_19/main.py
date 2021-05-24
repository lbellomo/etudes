from collections import deque


def solve_a(total_elfs: int) -> int:
    circle_elfs = deque([i for i in range(1, total_elfs + 1)])
    while circle_elfs:
        circle_elfs.rotate(-1)
        last = circle_elfs.popleft()

    return last


def solve_b(total_elfs: int) -> int:
    circle_elfs = deque([i for i in range(1, total_elfs + 1)])
    while circle_elfs:
        target_elf = circle_elfs[len(circle_elfs) // 2]
        # is not good idea remove some value in the middle (super slow)
        circle_elfs.remove(target_elf)
        circle_elfs.rotate(-1)

    return target_elf


if __name__ == "__main__":
    total_elfs = 3017957
    sol_a = solve_a(total_elfs)
    print(f"sol a: {sol_a}")

    # sol_b = solve_b(total_elfs)
    # print(f"sol b: {sol_b}")


def test_solve_a():
    total_elfs = 5
    assert solve_a(total_elfs) == 3


def test_solve_b():
    total_elfs = 5
    assert solve_b(total_elfs) == 2
