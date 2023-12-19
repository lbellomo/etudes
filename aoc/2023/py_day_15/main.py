from typing import NamedTuple


with open("input.txt") as f:
    raw_data = f.read()


def hash_(string):
    value = 0
    for ch in string:
        value += ord(ch)
        value = (value * 17) % 256
    return value


class Step(NamedTuple):
    label: str
    operation: str
    focal_length: int | None


data = raw_data.strip().split(",")

sol_a = sum(hash_(s) for s in data)
print(f"{sol_a = }")


def parse(s):
    if "-" in s:
        label, _ = s.split("-")
        return Step(label, "-", None)
    elif "=" in s:
        label, focal_length = s.split("=")
        return Step(label, "=", int(focal_length))


steps = [parse(s) for s in data]

boxes = [dict() for _ in range(256)]

for s in steps:
    box = boxes[hash_(s.label)]
    if s.operation == "=":
        box[s.label] = s.focal_length
    elif s.operation == "-" and s.label in box:
        box.pop(s.label)

sol_b = sum(
    i * j * v
    for i, box in enumerate(boxes, start=1)
    for j, v in enumerate(box.values(), start=1)
)
print(f"{sol_b = }")
