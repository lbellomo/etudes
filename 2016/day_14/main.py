import hashlib
from typing import Optional, List


def get_md5_hex(salt: str, key_stretching=0) -> str:
    item_hash = hashlib.md5(salt.encode()).hexdigest()
    if key_stretching:
        for _ in range(key_stretching):
            item_hash = hashlib.md5(item_hash.encode()).hexdigest()

    return item_hash


def find_char_three_times(item_hash: str) -> Optional[str]:
    # results = set()  # use set to remove posibles duplicates
    # check if any chunk have the same elem
    for chunk in [item_hash[j: j + 3] for j in range(30)]:
        elem = chunk[0]
        if all(elem == char for char in chunk):
            return elem
    return None


def find_char_five_times(item_hash: str, char: str):
    return char * 5 in item_hash


def is_key(candidates: List[str]) -> bool:
    char = find_char_three_times(candidates[0])
    if not char:
        return False

    for candidate_hash in candidates[1:]:
        if find_char_five_times(candidate_hash, char):
            return True

    return False


def solve(salt: str, key_stretching: int = 0) -> int:
    index = 0
    count = 0
    candidates = []
    # Number of elem to keep in the list
    # we only need to compare to the next one thousand
    max_size = 1001

    for i in range(max_size):
        candidates.append(get_md5_hex(f"{salt}{i}", key_stretching))

    while count != 64:
        if is_key(candidates):
            count += 1

        index += 1
        candidates.pop(0)
        candidates.append(get_md5_hex(f"{salt}{max_size+index}", key_stretching))

    return index


if __name__ == "__main__":
    data = "zpqevtbw"
    key_stretching = 2016

    sol_a = solve(data)
    print(f"sol a: {sol_a}")

    sol_b = solve(data, key_stretching)
    print(f"sol b: {sol_b}")


def test_sol_a():
    salt = "abc"
    assert solve(salt) == 22728


def test_sol_b():
    salt = "abc"
    key_stretching = 2016
    assert solve(salt, key_stretching) == 22551
