with open("input.txt") as f:
    data = [line.strip() for line in f.readlines()]

sol_a = sum(len(line) for line in data) - sum(len(eval(line)) for line in data)
print(f"{sol_a = }")

# we only look for the new chars
# 2 from the first and last new '"'
# 1 for each '"' -> '\"'
# 1 for each '\' -> '\\'
sol_b = sum(2 + line.count('"') + line.count("\\") for line in data)
print(f"{sol_b = }")
