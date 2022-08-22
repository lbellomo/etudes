import numpy as np
from collections import Counter

with open("input.txt") as f:
    raw_data = f.read()

helper = {
    "^": np.array([0, 1]),
    ">": np.array([1, 0]),
    "<": np.array([-1, 0]),
    "v": np.array([0, -1]),
}

pos = np.zeros(2, dtype=int)
counter = Counter([str(pos)])

for ch in raw_data:
    pos += helper[ch]
    counter.update([str(pos)])

print(f"sol a: {len(counter)}")

pos_santa = np.zeros(2, dtype=int)
pos_robot = np.zeros(2, dtype=int)
counter = Counter([str(pos_santa), str(pos_robot)])

for i, ch in enumerate(raw_data):
    if i % 2 == 0:
        pos_santa += helper[ch]
        counter.update([str(pos_santa)])
    else:
        pos_robot += helper[ch]
        counter.update([str(pos_robot)])

print(f"sol b: {len(counter)}")
