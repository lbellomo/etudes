import numpy as np

with open("input.txt") as f:
    raw_data = [line.strip() for line in f]


def find_next(circuits, state):
    for circuit in circuits:
        c_type = circuit["type"]
        if c_type == "SET" and (
            circuit["from_0"].isnumeric() or circuit["from_0"] in state
        ):
            return circuit
        elif c_type == "NOT" and circuit["from_0"] in state:
            return circuit
        elif c_type in ["RSHIFT", "LSHIFT"] and circuit["from_0"] in state:
            return circuit
        elif (
            c_type in ["OR", "AND"]
            and (circuit["from_0"].isnumeric() or circuit["from_0"] in state)
            and (circuit["from_1"].isnumeric() or circuit["from_1"] in state)
        ):
            return circuit


state = {}
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


while circuits:
    circuit = find_next(circuits, state)
    circuits.remove(circuit)

    from_0 = circuit["from_0"]
    if from_0.isnumeric():
        from_0 = int(from_0)

    from_1 = circuit.get("from_1", "")
    if from_1.isnumeric():
        from_1 = int(from_1)

    if circuit["type"] == "SET":
        from_0 = state.get(circuit["from_0"])
        if not from_0:
            from_0 = np.array(int(circuit["from_0"]), dtype=np.uint16)

        result = from_0
    elif circuit["type"] == "NOT":
        result = ~state[circuit["from_0"]]
    elif circuit["type"] == "RSHIFT":
        result = state[circuit["from_0"]] >> int(circuit["shift"])
    elif circuit["type"] == "LSHIFT":
        result = state[circuit["from_0"]] << int(circuit["shift"])
    elif circuit["type"] == "OR":
        result = state[circuit["from_0"]] | state[circuit["from_1"]]
    elif circuit["type"] == "AND":
        from_0 = state.get(circuit["from_0"])
        if not from_0:
            from_0 = np.array(int(circuit["from_0"]), dtype=np.uint16)

        result = from_0 & state[circuit["from_1"]]

    state[circuit["to"]] = np.array(result, dtype=np.uint16)

sol_a = state["a"]
print("sol_a =", int(sol_a))


raw_data_2 = [i if "44430 -> b" not in i else f"{sol_a} -> b" for i in raw_data]

state = {}
circuits = []

for line in raw_data_2:
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


while circuits:
    circuit = find_next(circuits, state)
    circuits.remove(circuit)

    from_0 = circuit["from_0"]
    if from_0.isnumeric():
        from_0 = int(from_0)

    from_1 = circuit.get("from_1", "")
    if from_1.isnumeric():
        from_1 = int(from_1)

    if circuit["type"] == "SET":
        from_0 = state.get(circuit["from_0"])
        if not from_0:
            from_0 = np.array(int(circuit["from_0"]), dtype=np.uint16)

        result = from_0
    elif circuit["type"] == "NOT":
        result = ~state[circuit["from_0"]]
    elif circuit["type"] == "RSHIFT":
        result = state[circuit["from_0"]] >> int(circuit["shift"])
    elif circuit["type"] == "LSHIFT":
        result = state[circuit["from_0"]] << int(circuit["shift"])
    elif circuit["type"] == "OR":
        result = state[circuit["from_0"]] | state[circuit["from_1"]]
    elif circuit["type"] == "AND":
        from_0 = state.get(circuit["from_0"])
        if not from_0:
            from_0 = np.array(int(circuit["from_0"]), dtype=np.uint16)

        result = from_0 & state[circuit["from_1"]]

    state[circuit["to"]] = np.array(result, dtype=np.uint16)

sol_b = state["a"]
print("sol_b =", int(sol_b))
