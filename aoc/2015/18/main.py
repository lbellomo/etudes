import numpy as np
from scipy import signal

with open("input.txt") as f:
    raw_data = [
        [int(i) for i in line.replace("#", "1").replace(".", "0").strip()] for line in f
    ]

kernel = np.ones([3, 3])
kernel[1, 1] = 0

grid = np.array(raw_data)

for _ in range(100):
    neighbors = signal.convolve2d(grid, kernel, mode="same")
    on_to_on = np.where((grid == 1) & ((neighbors == 2) | (neighbors == 3)), grid, 0)
    off_to_on = np.where((grid == 0) & (neighbors == 3), 1, 0)
    grid = np.zeros_like(grid) + on_to_on + off_to_on

sol_a = grid.sum()
print(f"{sol_a = }")

grid = np.array(raw_data)
grid[0, 0], grid[0, -1], grid[-1, 0], grid[-1, -1] = (1, 1, 1, 1)

for _ in range(100):
    neighbors = signal.convolve2d(grid, kernel, mode="same")
    on_to_on = np.where((grid == 1) & ((neighbors == 2) | (neighbors == 3)), grid, 0)
    off_to_on = np.where((grid == 0) & (neighbors == 3), 1, 0)
    grid = np.zeros_like(grid) + on_to_on + off_to_on
    grid[0, 0], grid[0, -1], grid[-1, 0], grid[-1, -1] = (1, 1, 1, 1)

sol_b = grid.sum()
print(f"{sol_b = }")
