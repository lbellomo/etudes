tramp = "^"
safe = "."

rules = {"^^.", ".^^", "^..", "..^"}


def apply_rules(chunk: str) -> str:
    if chunk in rules:
        return tramp
    else:
        return safe


def get_next_row(row: str) -> str:
    first_chunk = apply_rules("." + row[:2])
    last_chunk = apply_rules(row[-2:] + ".")
    center_chunks = [apply_rules(row[i : i + 3]) for i in range(len(row) - 2)]
    return "".join([first_chunk] + center_chunks + [last_chunk])


def solve(row: str, n_rows: int) -> int:
    count_safe = row.count(".")
    for _ in range(n_rows - 1):
        row = get_next_row(row)
        count_safe += row.count(".")

    return count_safe


if __name__ == "__main__":
    data = "^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^."  # noqa: E501
    n_rows = 40
    sol_a = solve(data, n_rows)
    print(f"sol a: {sol_a}")

    n_rows = 400000
    sol_b = solve(data, n_rows)
    print(f"sol b: {sol_b}")


def test_solve_a():
    row = ".^^.^.^^^^"
    n_rows = 10
    assert solve(row, n_rows) == 38
