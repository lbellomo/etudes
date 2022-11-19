import numpy as np

with open("input.txt") as f:
    raw_data = [line.strip() for line in f]


def parse_data(raw_data):
    circuits = []

    for line in raw_data:
        if "NOT" in line:
            c_type, c_from, _, c_to = line.split()
            circuits.append({"type": c_type, "from_0": c_from, "to": c_to})
        elif "OR" in line or "AND" in line:
            c_from_0, c_type, c_from_1, _, c_to = line.split()
            circuits.append(
                {"type": c_type, "from_0": c_from_0, "from_1": c_from_1, "to": c_to}
            )
        elif "RSHIFT" in line or "LSHIFT" in line:
            c_from, c_type, c_shift, _, c_to = line.split()
            circuits.append(
                {"type": c_type, "from_0": c_from, "shift": c_shift, "to": c_to}
            )
        else:
            c_from, _, c_to = line.split()
            c_type = "SET"
            circuits.append({"type": c_type, "from_0": c_from, "to": c_to})

    return circuits


def find_next(circuits, state):
    for circuit in circuits:
        c_type = circuit["type"]
        from_0 = circuit["from_0"]

        if c_type == "SET" and (from_0.isnumeric() or from_0 in state):
            return circuit
        elif c_type == "NOT" and from_0 in state:
            return circuit
        elif c_type in ["RSHIFT", "LSHIFT"] and from_0 in state:
            return circuit
        elif (
            c_type in ["OR", "AND"]
            and (from_0.isnumeric() or from_0 in state)
            and (circuit["from_1"].isnumeric() or circuit["from_1"] in state)
        ):
            return circuit


def solve(raw_data):
    state = {}
    circuits = parse_data(raw_data)

    while circuits:
        circuit = find_next(circuits, state)
        circuits.remove(circuit)

        c_type = circuit["type"]

        try:
            c_value = state[circuit["from_0"]]
        except KeyError:
            # this is a number and not a key, create a new array
            c_value = np.array(int(circuit["from_0"]), dtype=np.uint16)

        if c_type == "SET":
            result = c_value
        elif c_type == "NOT":
            result = ~c_value
        elif c_type == "RSHIFT":
            result = c_value >> int(circuit["shift"])
        elif c_type == "LSHIFT":
            result = c_value << int(circuit["shift"])
        elif c_type == "OR":
            result = c_value | state[circuit["from_1"]]
        elif c_type == "AND":
            result = c_value & state[circuit["from_1"]]

        state[circuit["to"]] = np.array(result, dtype=np.uint16)

    sol = state["a"]
    return int(sol)


sol_a = solve(raw_data)
print(f"{sol_a = }")

raw_data_2 = [i if "44430 -> b" not in i else f"{sol_a} -> b" for i in raw_data]
sol_b = solve(raw_data_2)
print(f"{sol_b = }")
