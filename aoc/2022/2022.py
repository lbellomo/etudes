# +
from string import ascii_letters
from itertools import islice
from functools import partial
from queue import LifoQueue


def batched(iterable, n):
    "Batch data into tuples of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch



# -

def solve_01():
    def parse_group(group):
        return [int(i) for i in group]

    with open("inputs/day_01.txt") as f:
        groups = [parse_group(group.split()) for group in f.read().split("\n\n")]
        
    sol_a = max(sum(group) for group in groups)
    sol_b = sum(sorted((sum(group) for group in groups), reverse=True)[:3])

    return sol_a, sol_b


def solve_02():
    with open("inputs/day_02.txt") as f:
        games = [line.strip() for line in f]

    def points_outcome(game):
        match game.split():
            # win
            case ("A", "Y") | ("B", "Z") | ("C", "X") : return 6
            # draw
            case ("A", "X") | ("B", "Y") | ("C", "Z") : return 3
            # lose
            case (_, _): return 0

    def points_shape(game):
        match game.split():
            case (_, "X"): return 1
            case (_, "Y"): return 2  
            case (_, "Z"): return 3

    def points(game):
        return points_outcome(game) + points_shape(game)

    def predict_shape(game):
        # X -> lose
        # Y -> draw
        # Z -> win
        match game.split():
            case ("A", "X"): return "A Z"
            case ("A", "Y"): return "A X"
            case ("A", "Z"): return "A Y"
            case ("B", "X"): return "B X"
            case ("B", "Y"): return "B Y"
            case ("B", "Z"): return "B Z"
            case ("C", "X"): return "C Y"
            case ("C", "Y"): return "C Z"
            case ("C", "Z"): return "C X"

    sol_a = sum(points(game) for game in games)
    sol_b = sum(points(predict_shape(game)) for game in games)

    return sol_a, sol_b


def solve_03():

    priority = {j: i for i, j in enumerate(ascii_letters, start=1)}

    def split_compartments(bag):
        mid_point = len(bag) // 2
        return (bag[:mid_point], bag[mid_point:])


    with open("inputs/day_03.txt") as f:
        rucksacks = [line.strip() for line in f]
        
    def score(group):
        ch = next(filter(lambda ch: all(ch in chunk for chunk in group[1:]), group[0]))
        return priority[ch]

    split_rucksacks = (split_compartments(bag) for bag in rucksacks)

    sol_a = sum((score(bag) for bag in split_rucksacks))
    sol_b = sum((score(group) for group in batched(rucksacks, 3)))

    return sol_a, sol_b   


def solve_04():

    with open("inputs/day_04.txt") as f:
        raw_data = [line.strip() for line in f]

    def duple_to_list(duple):
        x, y = duple.split("-")
        return list(range(int(x), int(y)+1))

    def is_overlap(pair, fun):
        a, b = tuple(map(duple_to_list, pair.split(",")))
        return fun(i in b for i in a) or fun(i in a for i in b)

    is_overlap_all = partial(is_overlap, fun=all)
    is_overlap_any = partial(is_overlap, fun=any)

    sol_a = sum(map(is_overlap_all, raw_data))
    sol_b = sum(map(is_overlap_any, raw_data))

    return sol_a, sol_b



def solve_05():
    with open("inputs/day_05.txt") as f:
        raw_crates, raw_procedures = f.read().split("\n\n")

    def parse_crates(raw_crates):    
        raw_crates = raw_crates.splitlines()
        raw_crates = filter(lambda col: col[-1] != " ", [[row[i] for row in raw_crates] for i in range(len(raw_crates[0]))])

        crates = dict()

        for col in  raw_crates:
            queue = LifoQueue()
            col_id = col[-1]
            col = filter(lambda ch: ch.isalpha(), reversed(col))
            for elem in col:
                queue.put(elem)

            crates[col_id] = queue

        return crates

    def parse_procedure(raw_procedure):
        _, n, _, id_from, _, id_to = raw_procedure.split()
        return int(n), id_from, id_to

    def move_crates_9000(crates, n, id_from, id_to):
        for _ in range(n):
            elem = crates[id_from].get()
            crates[id_to].put(elem)
            
    def move_crates_9001(crates, n, id_from, id_to):
        elems = [crates[id_from].get() for _ in range(n)]
        for elem in reversed(elems):
            crates[id_to].put(elem)

    def solve(move_crates):
        crates = parse_crates(raw_crates)

        for (n, id_from, id_to) in procedures:
            move_crates(crates, n, id_from, id_to)

        return  "".join([q.get() for q in crates.values()])

    procedures = [parse_procedure(i) for i in raw_procedures.splitlines()]

    sol_a = solve(move_crates_9000)
    sol_b = solve(move_crates_9001)

    return sol_a, sol_b



# %%time
if __name__ == "__main__":
    solve_01()
    solve_02()
    solve_03()
    solve_04()
    solve_05()


