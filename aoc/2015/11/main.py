from itertools import groupby


seed = "cqjxjnds"


def find_next(value):
    value_ord = [ord(i) for i in value[::-1]]

    for i, v in enumerate(value_ord):
        new_v = v + 1
        if new_v == 123:
            new_v = ord("a")
            value_ord[i] = new_v
        else:
            value_ord[i] = new_v
            break

    return "".join(chr(i) for i in value_ord[::-1])


def rule_1(value):
    for i, j, k in zip(value[0:], value[1:], value[2:]):
        if ord(i) == ord(j) - 1 == ord(k) - 2:
            return True

    return False


def rule_2(value):
    for char in "iol":
        if char in value:
            return False

    return True


def rule_3(value):
    sum_pairs = sum(len(list(g)) >= 2 for k, g in groupby(value))
    return sum_pairs >= 2


def solve(value):
    while not (rule_1(value) & rule_2(value) & rule_3(value)):
        value = find_next(value)

    return value


sol_a = solve(seed)
print(f"{sol_a = }")
sol_b = solve(find_next(sol_a))
print(f"{sol_b = }")
