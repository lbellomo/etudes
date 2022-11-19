import hashlib

secret_key = b"iwrupvqb"


def solve(secret_key: bytes, zeros: int) -> int:
    i = 0
    target_zeros = "0" * zeros

    md5_base = hashlib.md5()
    md5_base.update(secret_key)

    while True:
        md5 = md5_base.copy()
        md5.update(str(i).encode())
        hexdigest = md5.hexdigest()

        if hexdigest[:zeros] == target_zeros:
            return i

        i += 1


sol_a = solve(secret_key, 5)
print(f"{sol_a = }")
sol_b = solve(secret_key, 6)
print(f"{sol_b = }")
