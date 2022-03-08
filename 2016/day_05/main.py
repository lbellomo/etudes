from typing import Optional
from hashlib import md5


def find_valid_hash(secret: bytes) -> Optional[str]:
    secret_hash = md5(secret).hexdigest()
    if secret_hash[:5] == "0" * 5:
        return secret_hash
    return None


def solve_a(door_id: bytes) -> str:
    i = 0
    result: list[str] = []
    while len(result) != 8:
        secret = door_id + str(i).encode()
        secret_hash = find_valid_hash(secret)
        if secret_hash:
            result.append(secret_hash[5])
        i += 1

    return "".join(result)


def solve_b(door_id: bytes) -> str:
    i = 0
    result = ["_" for _ in range(8)]
    while "_" in result:
        secret = door_id + str(i).encode()
        secret_hash = find_valid_hash(secret)
        if secret_hash:
            try:
                pos = int(secret_hash[5])
                if result[pos] == "_":
                    result[pos] = secret_hash[6]
            except (ValueError, IndexError):
                pass
        i += 1

    return "".join(result)


if __name__ == "__main__":
    data = b"cxdnnyjw"

    sol_a = solve_a(data)
    print(f"sol_a: {sol_a}")

    sol_b = solve_b(data)
    print(f"sol_b: {sol_b}")


def test_find_valid_hash():
    assert find_valid_hash(b"abc5017308").startswith("000008f82")


def test_solve_a():
    assert solve_a(b"abc") == "18f47a30"


def test_solve_b():
    assert solve_b(b"abc") == "05ace8e3"
