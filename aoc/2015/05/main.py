import pandas as pd

df = pd.read_csv("input.txt", names=["data"])

sol_a = df[
    (df.data.str.count(r"[aeiou]") >= 3)
    & (df.data.str.count(r"(.)\1{1,}") > 0)
    & (~df.data.str.contains(r"ab|cd|pq|xy"))
].shape[0]
print(f"{sol_a = }")

sol_b = df[
    (df.data.str.contains(r"(..).*\1")) & (df.data.str.contains(r"([a-z])[a-z]\1"))
].shape[0]
print(f"{sol_b = }")
