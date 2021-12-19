import numpy as np

sonar = np.loadtxt("inputs/day_01.txt")

sol_a = (sonar[:-1] < sonar[1:]).sum()
# also from @asmeurer:
# (sonar[:-1] < sonar[1:]) == (np.diff(sonar) > 0)
print("sol a: ", sol_a)

window = np.convolve(sonar, np.ones(3), mode="valid")
# also from @asmeurer too:
# window = sonar[:-2] + sonar[1:-1] + sonar[2:]

sol_b = (np.diff(window) > 0).sum()
print("sol b: ", sol_b)
