from typing import List, Tuple
from collections import defaultdict

Data = List[str]


def read_data(path: str) -> Data:
    with open(path) as f:
        return [line.strip() for line in f.readlines()]


def init(data: Data) -> Tuple[defaultdict, defaultdict, List[List[str]]]:
    bots = defaultdict(list)
    bins: defaultdict = defaultdict(list)

    # init state of the robots in "bots"
    init_values = [line for line in data if line.startswith("value")]

    for init_value in init_values:
        init_value = init_value.split()  # type: ignore
        value = int(init_value[1])
        bot = init_value[-1]
        bots[bot].append(value)

    # parse all move
    all_move = [line.split() for line in data if line.startswith("bot")]
    all_move = {
        move[1]: dict(
            low_type=move[5],
            low_target=move[6],
            high_type=move[-2],
            high_target=move[-1],
        )
        for move in all_move
    }  # type: ignore

    return bots, bins, all_move


def step(
    bots: defaultdict, bins: defaultdict, all_move: List[List[str]]
) -> Tuple[defaultdict, defaultdict]:
    for bot, v in bots.items():
        if len(v) == 2:
            break
    else:
        raise ValueError("not bot with 2 chuips!")

    bots.pop(bot)
    low = min(v)
    high = max(v)

    next_move = all_move[bot]
    for target_type, target_id, value in zip(
        ["low_type", "high_type"], ["low_target", "high_target"], [low, high]
    ):
        if next_move[target_type] == "bot":  # type: ignore
            bots[next_move[target_id]].append(value)  # type: ignore
        elif next_move[target_type] == "output":  # type: ignore
            bins[next_move[target_id]].append(value)  # type: ignore

    return bots, bins


def solve_a(data: Data, target_chips: set) -> int:
    bots, bins, all_move = init(data)

    while True:
        bots, bins = step(bots, bins, all_move)

        find_target = [(k, v) for k, v in bots.items() if set(v) == target_chips]
        if find_target:
            return find_target[0][0]


def solve_b(data: Data, target_chips: set) -> int:
    bots, bins, all_move = init(data)

    while True:
        try:
            bots, bins = step(bots, bins, all_move)
        except ValueError:
            break

    return bins["0"][0] * bins["1"][0] * bins["2"][0]


if __name__ == "__main__":
    data = read_data("input.txt")
    target_chips = set([61, 17])

    sol_a = solve_a(data, target_chips)
    print(f"sol a: {sol_a}")
    sol_b = solve_b(data, target_chips)
    print(f"sol b: {sol_b}")


def test_solve_a():
    test_data = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2""".split(
        "\n"
    )
    test_target_chip = set([3, 5])
    assert solve_a(test_data, test_target_chip) == "0"
