from collections import deque


def read_data(path):
    with open(path) as f:
        return f.read()


def parse_data(raw_data):
    for i in raw_data.split(","):
        i = i.strip()
        turn_direction, magnitude = i[0], int(i[1:])
        yield turn_direction, magnitude


def solve_a(data):
    directions = deque(["N", "E", "S", "W"], maxlen=4)
    directions_values = {"N": [0, 1], "E": [1, 0], "S": [0, -1], "W": [-1, 0]}
    pos = [0, 0]

    for turn_direction, magnitude in data:
        # clockwise
        if turn_direction == "R":
            directions.rotate(-1)
        # counter clockwise
        elif turn_direction == "L":
            directions.rotate(1)
        else:
            raise ValueError("Something wrong with the data")

        diff_value = directions_values[directions[0]]
        for j in range(2):
            pos[j] += diff_value[j] * magnitude

    return sum(abs(i) for i in pos)


def solve_b(data):
    directions = deque(["N", "E", "S", "W"], maxlen=4)
    directions_values = {"N": [0, 1], "E": [1, 0], "S": [0, -1], "W": [-1, 0]}
    pos = [0, 0]
    know_pos = set()

    for turn_direction, magnitude in data:
        # clockwise
        if turn_direction == "R":
            directions.rotate(-1)
        # counter clockwise
        elif turn_direction == "L":
            directions.rotate(1)
        else:
            raise ValueError("Something wrong with the data")

        diff_value = directions_values[directions[0]]
        for _ in range(magnitude):
            for j in range(2):
                pos[j] += diff_value[j]

            pos_str = "|".join([str(i) for i in pos])
            if pos_str in know_pos:
                return sum(abs(i) for i in pos)
            else:
                know_pos.update([pos_str])


if __name__ == "__main__":
    sol_a = solve_a(parse_data(read_data("input.txt")))
    print(f"sol part a: {sol_a}")

    sol_b = solve_b(parse_data(read_data("input.txt")))
    print(f"sol part a: {sol_b}")


def test_solve_a():
    test_data = ["R2, L3", "R2, R2, R2", "R5, L5, R5, R3"]
    results = [5, 2, 12]

    for data, result in zip(test_data, results):
        assert solve_a(parse_data(data)) == result


def test_solve_b():
    assert solve_b(parse_data("R8, R4, R4, R8")) == 4
