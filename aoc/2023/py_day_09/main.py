from itertools import pairwise
from functools import reduce

with open("input.txt") as f:
    raw_data = f.read().splitlines()


Record = list[int]


def parse_line(line: str) -> Record:
    return [int(i) for i in line.split()]


data = [parse_line(line) for line in raw_data]


def build_secuences(record: Record) -> list[Record]:
    secuences = [record]

    while any(record):
        record = [j - i for i, j in pairwise(record)]
        secuences.append(record)
    return secuences


def predict(record: Record) -> int:
    secuences = build_secuences(record)

    return sum(record[-1] for record in secuences)


def predict_backwards(record: Record) -> int:
    secuences = build_secuences(record)
    return reduce(lambda x, y: y - x, [record[0] for record in secuences][::-1], 0)


sol_a = sum(predict(record) for record in data)
print(f"{sol_a = }")

sol_b = sum(predict_backwards(record) for record in data)
print(f"{sol_b = }")
