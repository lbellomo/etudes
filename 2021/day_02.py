import pandas as pd


df = pd.read_csv("inputs/day_02.txt", sep=" ", names=["direction", "value"])

sum_dir = df.groupby("direction").sum()
sol_a = ((sum_dir.loc["down"] - sum_dir.loc["up"])*sum_dir.loc["forward"])
print("sol a: ", sol_a.value)

aim = 0
pos = 0
deep = 0

for row in df.itertuples():
    if row.direction == "down":
        aim += row.value
    elif row.direction == "up":
        aim -= row.value
    elif row.direction == "forward":
        pos += row.value
        deep += aim*row.value
    else:
        raise ValueError("invalid direction!")

sol_b = pos*deep
print("sol b: ", sol_b)
