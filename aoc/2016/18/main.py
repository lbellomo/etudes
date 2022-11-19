raw_data = "^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^."  # noqa: E501


def is_safe(row: list[int], i: int) -> int:
    if i == 0:
        left = 1
        center = row[i]
        right = row[i + 1]
    elif i == len(row) - 1:
        left = row[i - 1]
        center = row[i]
        right = 1
    else:
        left = row[i - 1]
        center = row[i]
        right = row[i + 1]

    if (left, center, right) in [(0, 0, 1), (1, 0, 0), (0, 1, 1), (1, 1, 0)]:
        return 0
    else:
        return 1


def solve(raw_data: str, n: int) -> int:
    row = [0 if i == "^" else 1 for i in raw_data]
    count = sum(row)

    for _ in range(n - 1):
        row = [is_safe(row, i) for i in range(len(row))]
        count += sum(row)
    return count


sol_a = solve(raw_data, 40)
print(f"{sol_a = }")

sol_b = solve(raw_data, 400_000)
print(f"{sol_b = }")
