# +
import collections
from string import ascii_letters
from itertools import islice, groupby, pairwise
from functools import partial
from dataclasses import dataclass
from math import prod

# recipes from itertools docs
def batched(iterable, n):
    "Batch data into tuples of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


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
        """Points based on the result of the game"""
        match game.split():
            # win
            case ("A", "Y") | ("B", "Z") | ("C", "X"):
                return 6
            # draw
            case ("A", "X") | ("B", "Y") | ("C", "Z"):
                return 3
            # lose
            case (_, _):
                return 0

    def points_shape(game):
        """Points based on the played shape"""
        match game.split():
            # rock
            case (_, "X"):
                return 1
            # paper
            case (_, "Y"):
                return 2
            # scissors
            case (_, "Z"):
                return 3

    def points(game):
        """Total points for a game"""
        return points_outcome(game) + points_shape(game)

    def predict_shape(game):
        """Predcit which shape we need to play to archive the
        expected result

        Meanings:
         X -> lose
         Y -> draw
         Z -> win
        """
        match game.split():
            case ("A", "X"):
                return "A Z"
            case ("A", "Y"):
                return "A X"
            case ("A", "Z"):
                return "A Y"
            case ("B", "X"):
                return "B X"
            case ("B", "Y"):
                return "B Y"
            case ("B", "Z"):
                return "B Z"
            case ("C", "X"):
                return "C Y"
            case ("C", "Y"):
                return "C Z"
            case ("C", "Z"):
                return "C X"

    sol_a = sum(points(game) for game in games)
    sol_b = sum(points(predict_shape(game)) for game in games)

    return sol_a, sol_b


def solve_03():

    priority = {j: i for i, j in enumerate(ascii_letters, start=1)}

    def split_compartments(bag):
        """Split bag in half in two compartments"""
        mid_point = len(bag) // 2
        return (bag[:mid_point], bag[mid_point:])

    with open("inputs/day_03.txt") as f:
        rucksacks = [line.strip() for line in f]

    def score(group):
        """Find the score (priority) for the only shared chard in group"""
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
        return list(range(int(x), int(y) + 1))

    def is_overlap(pair, fun):
        """Check if pair overlap depending on fun"""
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
        raw_crates = filter(
            lambda col: col[-1] != " ",
            [[row[i] for row in raw_crates] for i in range(len(raw_crates[0]))],
        )

        crates = dict()

        for col in raw_crates:
            queue = list()
            col_id = col[-1]
            col = filter(lambda ch: ch.isalpha(), reversed(col))
            for elem in col:
                queue.append(elem)

            crates[col_id] = queue

        return crates

    def parse_procedure(raw_procedure):
        _, n, _, id_from, _, id_to = raw_procedure.split()
        return int(n), id_from, id_to

    def move_crates_9000(crates, n, id_from, id_to):
        """Move crates in a LIFO way"""
        for _ in range(n):
            elem = crates[id_from].pop()
            crates[id_to].append(elem)

    def move_crates_9001(crates, n, id_from, id_to):
        """Move crates in chunks (preserving order in the chunk"""
        elems = [crates[id_from].pop() for _ in range(n)]
        for elem in reversed(elems):
            crates[id_to].append(elem)

    def solve(move_crates):
        crates = parse_crates(raw_crates)

        for (n, id_from, id_to) in procedures:
            move_crates(crates, n, id_from, id_to)

        return "".join([q.pop() for q in crates.values()])

    procedures = [parse_procedure(i) for i in raw_procedures.splitlines()]

    sol_a = solve(move_crates_9000)
    sol_b = solve(move_crates_9001)

    return sol_a, sol_b


def solve_06():
    with open("inputs/day_06.txt") as f:
        buffer = f.read().strip()

    def solve(buffer, n):
        return next(
            i
            for i, chunk in enumerate(sliding_window(buffer, n), start=n)
            if len(chunk) == len(set(chunk))
        )

    sol_a = solve(buffer, 4)
    sol_b = solve(buffer, 14)

    return sol_a, sol_b


def solve_07():
    with open("inputs/day_07.txt") as f:
        raw_data = [line.strip() for line in f]

    def join_dir(current_dir, path):
        """Poor man's 'os.path.join'"""
        if current_dir == "/":
            return f"/{path}"
        else:
            return f"{current_dir}/{path}"    

    def change_dir(current_dir, cd):
        """Update current_dir"""
        match cd.split()[-1]:
            case "/":
                return "/"
            case "..":
                return current_dir.rsplit("/", maxsplit=1)[0]
            case path:
                return join_dir(current_dir, path)

    def create_item(current_dir, ls):
        """Create an dict with the 'ls' info"""
        other_dirs = [join_dir(current_dir, d.split()[-1]) for d in ls if d.startswith("dir")]
        files = [file for file in ls if not file.startswith(("$", "dir"))]

        return  {
            "dir": current_dir,
            "other_dirs": other_dirs,
            "files": files
        }    

    def get_size_dir(item):
        """Recursively navigate the tree calculating the item size"""
        size_files = sum(int(file.split()[0]) for file in item["files"])
        return size_files + sum(get_size_dir(tree[d]) for d in item["other_dirs"]) 

    def make_tree(raw_data):
        """Parse the input to a dict where each item is a dir"""
        commands = batched((list(g) for k, g in groupby(raw_data, lambda x: x.startswith("$ ls") or not x.startswith("$"))), 2)
        current_dir = None
        tree = dict()       

        for cd_list, ls in commands:
            for cd in cd_list:
                current_dir = change_dir(current_dir, cd)
            tree[current_dir] = create_item(current_dir, ls)

        return tree

    tree = make_tree(raw_data)
    total_size = 70000000
    used_size = get_size_dir(tree["/"])
    free_size = total_size - used_size

    sol_a = sum(filter(lambda size: size < 100000, (get_size_dir(item) for item in tree.values())))
    sol_b = sorted(filter(lambda size: size + free_size > 30000000, (get_size_dir(item) for item in tree.values())))[0]

    return sol_a, sol_b


def solve_08():
    with open("inputs/day_08.txt") as f:
        raw_data = [line.strip() for line in f]

    tree_map = {(i, j): int(ch) for i, row in enumerate(raw_data) for j, ch in enumerate(row)}

    def is_visible_direction(current_tree, i, j, shift_x, shift_y):
        i, j = i+shift_x, j+shift_y
        other_tree = tree_map.get((i, j))
        if other_tree is None:
            return True
        elif other_tree >= current_tree:
            return False
        else:
            return is_visible_direction(current_tree, i, j, shift_x, shift_y)


    def is_visible(i, j):
        current_tree = tree_map[(i, j)]
        return any([
            is_visible_direction(current_tree, i, j, 1, 0),
            is_visible_direction(current_tree, i, j, -1, 0),
            is_visible_direction(current_tree, i, j, 0, 1),
            is_visible_direction(current_tree, i, j, 0, -1)
        ])

    def count_tree_direction(current_tree, i, j, shift_x, shift_y):
        i, j = i+shift_x, j+shift_y
        other_tree = tree_map.get((i, j))
        if other_tree is None:
            return 0
        elif other_tree >= current_tree:
            return 1
        else:
            return 1 + count_tree_direction(current_tree, i, j, shift_x, shift_y)


    def count_tree(i, j):
        current_tree = tree_map[(i, j)]
        return (count_tree_direction(current_tree, i, j, 1, 0) * 
            count_tree_direction(current_tree, i, j, -1, 0) * 
            count_tree_direction(current_tree, i, j, 0, 1)*
            count_tree_direction(current_tree, i, j, 0, -1))

    sol_a = sum(is_visible(i, j) for i in range(len(raw_data)) for j in range(len(raw_data[0])))
    sol_b = max(count_tree(i, j) for i in range(len(raw_data)) for j in range(len(raw_data[0])))
    
    return sol_a, sol_b


def solve_09():
    with open("inputs/day_09.txt") as f:
        raw_data = (line.strip() for line in f)
        motions = list(map(lambda x: (x[0], int(x[1])), (map(str.split, raw_data))))
    
    def update_head(head, direction):
        xh, yh = head

        # update head
        match direction:
            case "U":
                yh += 1
            case "D":
                yh -= 1
            case "R":
                xh += 1
            case "L":
                xh -= 1

        return (xh, yh) 

    def update_knot(new_head, tail):
        # i use help from fasterthatlime
        # https://fasterthanli.me/series/advent-of-code-2022/part-9#part-2
        xh, yh = new_head
        xt, yt = tail

        match (xh - xt, yh - yt):
            case (0, 0) | (0,1) | (1,0) | (0, -1) | (-1, 0):
                dx, dy = (0, 0)
            case (1, 1) | (1, -1) | (-1, 1) | (-1, -1):
                dx, dy = (0, 0)
            case (0, 2):
                dx, dy = (0, 1)
            case (0, -2):
                dx, dy = (0, -1)
            case (2, 0):
                dx, dy = (1, 0)
            case (-2, 0):
                dx, dy = (-1, 0)
            case (2, 1) | (1, 2) | (2, 2):
                dx, dy = (1, 1)
            case (2, -1) | (1, -2) | (2, -2):
                dx, dy = (1, -1)
            case (-2, 1) | (-1, 2) | (-2, 2):
                dx, dy = (-1, 1)
            case (-2, -1) | (-1, -2) | (-2, -2):
                dx, dy = (-1, -1)

        return xt + dx, yt + dy

    def step_simple(head, tail, direction):        
        new_head = update_head(head, direction)
        new_tail = update_knot(new_head, tail)

        return new_head, new_tail

    def move_simple(head, tail, motion, know_pos):
        direction, n = motion
        for _ in range(n):
            head, tail = step_simple(head, tail, direction)
            know_pos.add(tail)

        return head, tail


    def solve_a(motions):
        head = (0, 0)
        tail = (0, 0)

        know_pos = set()
        know_pos.add(tail)

        for motion in motions:
            head, tail = move_simple(head, tail, motion, know_pos)

        return len(know_pos)

    def step_long(rope, direction):
        new_rope = [update_head(rope[0], direction)]

        for (head, tail) in pairwise(rope):
            new_rope.append(update_knot(new_rope[-1], tail))

        return new_rope

    def move_long(rope, motion, know_pos):
        direction, n = motion
        for _ in range(n):
            rope = step_long(rope, direction)
            know_pos.add(rope[-1])

        return rope

    def solve_b(motions):
        rope = [(0, 0) for _ in range(10)]

        know_pos = set()
        know_pos.add(rope[-1])

        for motion in motions:
            rope = move_long(rope, motion, know_pos)
        return len(know_pos)

    sol_a = solve_a(motions)
    sol_b = solve_b(motions)

    return sol_a, sol_b


def solve_10():
    with open("inputs/day_10.txt") as f:
        raw_data = [line.strip() for line in f]

    program = list(reversed(list(map(lambda x: x if x.isalpha() else int(x), (i.split()[-1] for i in raw_data)))))

    signal_strength = 1
    sum_signals_strength = 0
    instruction = None

    display = list()

    for i in range(1, 241):

        if not instruction:
            instruction = program.pop()
            is_new = True

        # in 20, 60, 100, 140, 180, 220
        if (i - 20) % 40 == 0:  
            sum_signals_strength += i * signal_strength

        if abs(signal_strength + 1 - (i % 40)) <= 1:
            ch = "#"
        else:
            ch = "."

        display.append(ch)

        match (instruction, is_new):
            case ("noop", _):
                instruction = None
            case (_i, True):
                is_new = False
            case (i, False):
                signal_strength += i
                instruction = None
                
    sol_a = sum_signals_strength 
    sol_b = ["".join(line) for line in (batched(display, 40))]
    
    return sol_a, sol_b


def solve_11():

    with open("inputs/day_11.txt") as f:
        raw_monkeys = f.read().split("\n\n")

    def make_operation(operation, item):
        match operation.split():
            case ["old", "*", "old"]:
                return item*item
            case ["old", "*", i]:
                return item * int(i)
            case ["old", "+", i]:
                return item + int(i)    

    @dataclass
    class Monkey:
        items: list
        operation: str
        test_divisible: int
        monkey_true: int
        monkey_false: int
        inspected_items: int = 0

    def get_last_elem_line(line):
        return int(line.split()[-1])

    def create_monkey(lines):
        items = [int(i) for i in lines[1].replace(",", "").split() if i.isnumeric()]
        operation = lines[2].split("=")[-1].strip()
        test_divisible = get_last_elem_line(lines[3])
        monkey_true = get_last_elem_line(lines[4])
        monkey_false = get_last_elem_line(lines[5])

        return Monkey(items, operation, test_divisible, monkey_true, monkey_false)

    def thrown(monkey, monkeys, divide_worry, prod_divisibles=None):
        for item in monkey.items:
            item = make_operation(monkey.operation, item)
            if divide_worry:
                item = item // 3
            else:
                item = item % prod_divisibles

            if item % monkey.test_divisible == 0:
                monkeys[monkey.monkey_true].items.append(item)
            else:
                monkeys[monkey.monkey_false].items.append(item)

            monkey.inspected_items += 1

        monkey.items = []

    def solve(divide_worry, rounds):
        monkeys = [create_monkey(monkey.splitlines()) for monkey in raw_monkeys]
        prod_divisibles = prod(m.test_divisible for m in monkeys)

        for _ in range(rounds):
            for monkey in monkeys:
                thrown(monkey, monkeys, divide_worry, prod_divisibles)

        return prod(sorted([m.inspected_items for m in monkeys], reverse=True)[:2])

    sol_a = solve(divide_worry=True, rounds=20)
    sol_b = solve(divide_worry=False, rounds=10_000)

    return sol_a, sol_b



# %%time
if __name__ == "__main__":
    solve_01()
    solve_02()
    solve_03()
    solve_04()
    solve_05()
    solve_06()
    solve_07()
    solve_08()
    solve_09()   
    solve_10()
    solve_11()




