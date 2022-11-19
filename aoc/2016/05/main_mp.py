import multiprocessing as mp
from hashlib import md5
from typing import Optional

door_id = "cxdnnyjw"

zeros_count = 5
target = "0" * zeros_count

step_size = 500_000
q: mp.Queue[str] = mp.Queue()


def check_door(password: str) -> Optional[str]:
    h = md5(password.encode())

    if h.hexdigest()[:zeros_count] == target:
        q.put(h.hexdigest())

    return None


def solve_a() -> str:
    result = ""
    step = 0

    while len(result) < 8:
        start = step * step_size
        end = (step + 1) * step_size

        with mp.Pool() as p:
            p.map(check_door, (door_id + str(i) for i in range(start, end)))

        step += 1

        while not q.empty():
            r = q.get()
            result += r[zeros_count]

    return result


def solve_b() -> str:
    target_keys = "01234567"

    result: dict[str, str] = {}
    step = 0

    while len(result) != 8:
        start = step * step_size
        end = (step + 1) * step_size

        with mp.Pool() as p:
            p.map(check_door, (door_id + str(i) for i in range(start, end)))

        step += 1

        while not q.empty():
            r = q.get()
            if r[zeros_count] not in result and r[zeros_count] in target_keys:
                result[r[zeros_count]] = r[zeros_count + 1]

    return "".join(result[i] for i in target_keys)


if __name__ == "__main__":
    sol_a = solve_a()
    print(f"{sol_a = }")

    sol_b = solve_b()
    print(f"{sol_b = }")
