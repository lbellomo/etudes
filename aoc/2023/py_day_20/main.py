from math import lcm
from dataclasses import dataclass


with open("input.txt") as f:
    raw_data = f.read().splitlines()


@dataclass
class Button:
    def process(self, **kwargs):
        return False


@dataclass
class Broadcaster:
    def process(self, input, **kwargs):
        return input


@dataclass
class FlipFlop:
    state: str = "off"

    def process(self, input, **kwargs):
        if input:
            return None
        elif self.state == "off":
            self.state = "on"
            return True
        elif self.state == "on":
            self.state = "off"
            return False


@dataclass
class Conjunction:
    state: dict

    def process(self, input, prev_node):
        self.state[prev_node] = input
        return not all(v for v in self.state.values())


@dataclass
class Output:
    def process(self, **kwargs):
        return None


def parse_line(line):
    src, target = line.split(" -> ")

    targets = target.split(", ")
    clean_src = src.strip("%").strip("&")
    return src, clean_src, targets


def parse_data(raw_data):
    links = {"button": ["broadcaster"]}
    for line in raw_data:
        src, clean_src, targets = parse_line(line)
        links[clean_src] = targets

    links["output"] = []

    nodes = {"button": Button()}
    for line in raw_data:
        src, clean_src, targets = parse_line(line)

        match src:
            case "button":
                nodes[clean_src] = Button()
            case "broadcaster":
                nodes[clean_src] = Broadcaster()
            case src if src.startswith("%"):
                nodes[clean_src] = FlipFlop()
            case src if src.startswith("&"):
                state = {k: False for k, v in links.items() if clean_src in v}
                nodes[clean_src] = Conjunction(state=state)
            case "output":
                nodes[clean_src] = Output()

    nodes["output"] = Output()
    return links, nodes


def solve_a():
    links, nodes = parse_data(raw_data)

    low_pulse_count = 0
    high_pulse_count = 0

    for _ in range(1000):
        prev_node = None
        start_pulse = None
        start_node = "button"
        current_state = [(prev_node, start_pulse, start_node)]

        while current_state:
            next_state = []

            for prev_node, pulse, key in current_state:
                node = nodes.get(key)
                if not node:
                    continue

                pulse = node.process(input=pulse, prev_node=prev_node)

                for node_link in links[key]:
                    if pulse is None:
                        continue
                    elif not pulse:
                        low_pulse_count += 1
                    elif pulse:
                        high_pulse_count += 1
                    next_state.append((key, pulse, node_link))

            current_state = next_state

    return low_pulse_count * high_pulse_count


sol_a = solve_a()
print(f"{sol_a = }")


def find_first_high(target_node):
    links, nodes = parse_data(raw_data)

    i = 0
    while True:
        i += 1
        prev_node = None
        start_pulse = None
        start_node = "button"
        current_state = [(prev_node, start_pulse, start_node)]

        while current_state:
            next_state = []

            for prev_node, pulse, key in current_state:
                if prev_node == target_node and pulse:
                    return i

                node = nodes.get(key)
                if not node:
                    continue

                pulse = node.process(input=pulse, prev_node=prev_node)

                for node_link in links[key]:
                    if pulse is None:
                        continue
                    next_state.append((key, pulse, node_link))

            current_state = next_state


# [k for k, v in links.items() if "rx" in v]
def solve_b():
    links, nodes = parse_data(raw_data)
    return lcm(*[find_first_high(k) for k, v in links.items() if "hp" in v])


sol_b = solve_b()
print(f"{sol_b = }")
