from collections import Counter

with open("input.txt") as f:
    data = [line.strip() for line in f]

len_data = len(data[0])


def solve(filter_max: bool) -> str:
    result = ""
    for i in range(len_data):
        c = Counter(row[i] for row in data)
        if filter_max:
            result += c.most_common()[0][0]
        else:
            result += c.most_common()[-1][0]

    return result


sol_a = solve(filter_max=True)
print(f"{sol_a = }")

sol_b = solve(filter_max=False)
print(f"{sol_b = }")
