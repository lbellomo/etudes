import numpy as np


def get_next(last: int) -> int:
    return (last * 252533) % 33554393


size = 10_000
a = np.zeros([size, size], dtype=np.int64)

last = 20151125
a[0, 0] = last

for diagonal_size in range(1, size):
    for i, j in zip(range(0, diagonal_size + 1), range(diagonal_size, -1, -1)):
        last = get_next(last)
        a[i, j] = last

# check if make sense
# a[:6, :6].T

# row 3010, column 3019
sol = a[3018, 3009]
print(f"{sol = }")
