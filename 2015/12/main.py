import json

with open("input.txt") as f:
    data = json.loads(f.read().strip())


def search_inside(item, check_red=False):
    if isinstance(item, dict):
        # don't count if any value in dict is red for part b
        if check_red:
            if any(i == "red" for i in item.values()):
                return 0
        return sum(search_inside(i, check_red=check_red) for i in item.values())
    elif isinstance(item, list):
        return sum(search_inside(i, check_red=check_red) for i in item)
    elif isinstance(item, str):
        return 0
    elif isinstance(item, int):
        return item


sol_a = search_inside(data)
print(f"{sol_a = }")

sol_b = search_inside(data, check_red=True)
print(f"{sol_b = }")
