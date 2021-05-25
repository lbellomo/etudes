from functools import reduce
from typing import List, Tuple

RawData = List[str]
Chunk = Tuple[int, ...]
Data = List[Chunk]


def read_data(path: str) -> RawData:
    with open(path) as f:
        return [line.strip() for line in f.readlines()]


def process_data(raw_data: RawData) -> Data:
    data = [tuple(map(int, i.split("-"))) for i in raw_data]
    data.sort(key=lambda x: x[0])
    return data


def join_chunks(list_chunks: Data, new_chunk: Chunk) -> Data:
    # when we have a == "[]" add the first chunk
    if not list_chunks:
        return [new_chunk]

    last_low, last_top = list_chunks[-1]
    new_low, new_top = new_chunk

    # if the chunks overlap we join them
    if last_top + 1 == new_low or last_top > new_low:
        list_chunks.pop()
        list_chunks.append((last_low, max(new_top, last_top)))
        return list_chunks
    else:
        return list_chunks + [new_chunk]


def solve_a(data: Data) -> int:
    data_reduced: Data = reduce(join_chunks, data, [])
    return data_reduced[0][-1] + 1


if __name__ == "__main__":
    data = process_data(read_data("input.txt"))
    sol_a = solve_a(data)
    print(f"sol a: {sol_a}")


def test_sol_a():
    test_data = """5-8
0-2
4-7""".split(
        "\n"
    )
    data = process_data(test_data)
    assert solve_a(data) == 3
