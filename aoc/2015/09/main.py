from itertools import pairwise, permutations

with open("input.txt") as f:
    raw_data = [line.strip() for line in f]

routes = {}
places = set()

for line in raw_data:
    place_a, _, place_b, _, dist = line.split()
    dist = int(dist)
    routes[f"{place_a}-{place_b}"] = dist
    routes[f"{place_b}-{place_a}"] = dist

    places.add(place_a)
    places.add(place_b)

sol_a = min(
    sum(routes["-".join(pairs)] for pairs in pairwise(choice))
    for choice in permutations(places, len(places))
)
print(f"{sol_a = }")

sol_b = max(
    sum(routes["-".join(pairs)] for pairs in pairwise(choice))
    for choice in permutations(places, len(places))
)
print(f"{sol_b = }")
