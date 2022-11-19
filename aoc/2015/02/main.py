import pandas as pd

df = pd.read_csv("input.txt", sep="x", names=["length", "width", "height"])

# 2*l*w + 2*w*h + 2*h*l
df["lw"] = df.length * df.width
df["wh"] = df.width * df.height
df["hl"] = df.height * df.length
sol_a = (
    2 * df["lw"] + 2 * df["wh"] + 2 * df["hl"] + df[["lw", "wh", "hl"]].min(axis=1)
).sum()

print(f"{sol_a = }")

df = pd.read_csv("input.txt", sep="x", names=["length", "width", "height"])

sol_b = ((df.sum(axis=1) - df.max(axis=1)) * 2 + df.prod(axis=1)).sum()
print(f"{sol_b = }")
