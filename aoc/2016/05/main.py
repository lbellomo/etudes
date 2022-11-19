from hashlib import md5
from typing import Optional

door_id = "cxdnnyjw"

zeros_count = 5
target = "0" * zeros_count


def check_door(password: str) -> Optional[str]:
    h = md5(password.encode())

    if h.hexdigest()[:zeros_count] == target:
        return h.hexdigest()

    return None


def solve_a() -> str:
    result: list[str] = []
    i = 0
    while len(result) != 8:
        r = check_door(door_id + str(i))
        if r:
            result.append(r[zeros_count])
        i += 1

    return "".join(filter(None, result))


sol_a = solve_a()
print(f"{sol_a = }")


def solve_b() -> str:
    result: dict[str, str] = {}
    target_keys = "01234567"
    i = 0
    while not len(result) == 8:
        r = check_door(door_id + str(i))
        if r and r[zeros_count] not in result and r[zeros_count] in target_keys:
            result[r[zeros_count]] = r[zeros_count + 1]

        i += 1

    return "".join(result[i] for i in target_keys)


sol_b = solve_b()
print(f"{sol_b = }")
