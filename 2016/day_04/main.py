from typing import List, Iterator, Tuple, Optional
from itertools import cycle
from functools import partial
from collections import Counter
from string import ascii_lowercase

RawData = List[str]


def read_data(path: str) -> RawData:
    with open(path) as f:
        return [line.strip() for line in f.readlines()]


def process_data(
    raw_data: RawData, remove_dash: bool = True
) -> Iterator[Tuple[str, int, str]]:
    for line in raw_data:
        letters, other = line.rsplit("-", maxsplit=1)

        if remove_dash:
            letters = letters.replace("-", "")

        ids, checksum = other[:-1].split("[")
        yield letters, int(ids), checksum


def check_checksum(letters: str, checksum: str) -> bool:
    counter = Counter(letters)
    # sort alfabetical first, and then by count
    sorted_counter = sorted(
        sorted(counter.items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True
    )
    # keep only the fisrt 5 (the checksum len)
    most_common = "".join(i[0] for i in sorted_counter[:5])

    if most_common == checksum:
        return True
    return False


def solve_a(raw_data: RawData) -> int:
    sum_ids = 0

    for letters, ids, checksum in process_data(raw_data):
        if check_checksum(letters, checksum):
            sum_ids += ids

    return sum_ids


def decode_ch(ch_input: str, ids: int) -> str:
    ch = ""
    if ch_input == "-":
        cycle_letters = cycle("- ")
    else:
        cycle_letters = cycle(ascii_lowercase)

    while ch != ch_input:
        ch = next(cycle_letters)

    for _ in range(ids):
        ch = next(cycle_letters)

    return ch


def decode_letters(letters: str, ids: int) -> str:
    partial_decode_ch = partial(decode_ch, ids=ids)
    return "".join(map(partial_decode_ch, letters))


def solve_b(raw_data: RawData) -> Optional[int]:
    for letters, ids, _ in process_data(raw_data, remove_dash=False):
        real_name = decode_letters(letters, ids)
        if real_name == "northpole-object-storage":
            return ids
    return None


if __name__ == "__main__":
    raw_data = read_data("input.txt")
    sol_a = solve_a(raw_data)
    print(f"sol a: {sol_a}")

    sol_b = solve_b(raw_data)
    print(f"sol b: {sol_b}")


def test_check_checksum():
    test_raw_data = [
        "aaaaa-bbb-z-y-x-123[abxyz]",
        "a-b-c-d-e-f-g-h-987[abcde]",
        "not-a-real-room-404[oarel]",
        "totally-real-room-200[decoy]",
    ]
    test_result = [True, True, True, False]

    for raw_data, result in zip(test_raw_data, test_result):
        letters, _, checksum = next(process_data([raw_data]))
        assert check_checksum(letters, checksum) == result


def test_decode_letters():
    letters = "qzmt-zixmtkozy-ivhz"
    ids = 343

    assert decode_letters(letters, ids) == "very encrypted name"
