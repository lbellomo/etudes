from itertools import permutations

import pandas as pd

df = pd.read_csv("input.txt", delimiter=r"\s+", names=list("abc"))


def check_valid(row: pd.Series) -> bool:
    return all(
        map(lambda x: True if x[0] + x[1] > x[2] else False, permutations(row, r=3))
    )


sol_a = df.apply(check_valid, axis=1).sum()
print(f"{sol_a = }")

df_flat = pd.concat([df.a, df.b, df.c])

new_df = pd.DataFrame(
    {
        "a": df_flat[::3].reset_index(drop=True),
        "b": df_flat[1::3].reset_index(drop=True),
        "c": df_flat[2::3].reset_index(drop=True),
    }
)

sol_b = new_df.apply(check_valid, axis=1).sum()
print(f"{sol_b = }")
