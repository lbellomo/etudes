target = 33_100_000

num_houses = 1_000_000

house_presents = [0 for _ in range(num_houses)]

for i in range(1, num_houses):
    for j in range(i, num_houses, i):
        house_presents[j] += i * 10

sol_a = next(i for i, presents in enumerate(house_presents) if presents >= target)
print(f"{sol_a = }")

house_presents = [0 for _ in range(num_houses)]

for i in range(1, num_houses):
    for j, _ in zip(range(i, num_houses, i), range(50)):
        house_presents[j] += i * 11

sol_b = next(i for i, presents in enumerate(house_presents) if presents >= target)
print(f"{sol_b = }")
