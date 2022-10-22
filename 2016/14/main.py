from hashlib import md5
from functools import lru_cache
from typing import Optional


@lru_cache(maxsize=2000)
def get_hexdigest(i: int) -> str:
    return md5((salt + str(i)).encode()).hexdigest()


@lru_cache(maxsize=2000)
def get_secure_hexdigest(i: int) -> str:
    hexdigest = md5((salt + str(i)).encode()).hexdigest()
    for _ in range(2016):
        hexdigest = md5(hexdigest.encode()).hexdigest()
    return hexdigest


def find_triple(hexdigest: str) -> Optional[str]:
    for i, j, k in zip(hexdigest, hexdigest[1:], hexdigest[2:]):
        if i == j == k:
            return i
    return None


def check_fives(char: str, i: int, secure: bool) -> bool:
    if not secure:
        hash_fun = get_hexdigest
    else:
        hash_fun = get_secure_hexdigest
    for j in range(1, 1001):
        if char * 5 in hash_fun(i + j):
            return True
    return False


def solve(secure: bool) -> int:
    i = 0
    pad_key: list[int] = []
    while len(pad_key) != 64:
        if not secure:
            hexdigest = get_hexdigest(i)
        else:
            hexdigest = get_secure_hexdigest(i)
        triple = find_triple(hexdigest)
        if triple and check_fives(triple, i, secure):
            pad_key.append(i)

        i += 1
    return pad_key[-1]


salt = "abc"
assert solve(secure=False) == 22728
assert solve(secure=True) == 22551

salt = "zpqevtbw"

sol_a = solve(secure=False)
print(f"{sol_a = }")

sol_b = solve(secure=True)
print(f"{sol_b = }")
