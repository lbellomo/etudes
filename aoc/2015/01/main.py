from collections import Counter

with open("input.txt") as f:
    raw_data = f.read()

count = Counter(raw_data)
print(f'result a: {count["("] - count[")"]}')

level = 0
for i, ch in enumerate(raw_data):
    if ch == "(":
        level += 1
    elif ch == ")":
        level -= 1
    else:
        raise ValueError(f"Invalid char {ch}")

    if level < 0:
        break

    # print(i, level, ch)
print(f"result a: {i+1}")
