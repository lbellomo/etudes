from collections import namedtuple
from operator import lt, gt

with open("input.txt") as f:
    raw_data = f.read().split("\n\n")


Rule = namedtuple("Rule", ["part", "op", "value", "target"])


def parse_rule(i):
    if ":" in i:
        rest, target = i.split(":")
    else:
        target = i
        return Rule(None, None, None, target)

    if "<" in rest:
        op = lt
        part, value = rest.split("<")
    elif ">" in rest:
        op = gt
        part, value = rest.split(">")

    return Rule(part, op, int(value), target)


def parse_workflow(w):
    k, rest = w.split("{")
    v = rest.strip("}").split(",")
    rules = [parse_rule(i) for i in v]
    return k, rules


def parse_rating(r):
    r = r[1:-1]
    r = dict([i.split("=") for i in r.split(",")])
    return {k: int(v) for k, v in r.items()}


def parse(raw_data):
    workflows, ratings = raw_data

    workflows = dict([parse_workflow(w) for w in workflows.splitlines()])
    ratings = [parse_rating(r) for r in ratings.splitlines()]
    return workflows, ratings


def check_workflow(workflow, item):
    for rule in workflow:
        if not rule.op:
            return rule.target
        elif rule.op(item[rule.part], rule.value):
            return rule.target


def pipeline(item):
    w_name = "in"

    while w_name not in "RA":
        w = workflows[w_name]
        w_name = check_workflow(w, item)

    return w_name == "A"


workflows, ratings = parse(raw_data)

sol_a = sum([sum(item.values()) for item in ratings if pipeline(item)])
print(f"{sol_a = }")
