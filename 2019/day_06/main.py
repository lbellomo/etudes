from collections import defaultdict


def parse_data(path_data: str) -> list[str]:
    with open(path_data) as f:
        data = [i.strip() for i in f.readlines()]

    return data


def make_graph(data: list[str]) -> tuple[defaultdict[str, list[str]], set[str]]:

    g = defaultdict(list)  # graph
    uniques = set()

    for orbit in data:
        i, j = orbit.split(")")
        uniques.update([i, j])
        g[i].append(j)

    return g, uniques


def invert_graph(g: defaultdict[str, list[str]]) -> dict[str, str]:
    g_inverted = dict()

    for k, v in g.items():
        for sub_v in v:
            g_inverted[sub_v] = k

    return g_inverted


def calcule_distances(g_inverted: dict[str, str], uniques: set[str]):
    know_distances = {}

    for space_object in uniques:
        if space_object == "COM":
            continue
        object_distance = 0

        current_object = space_object
        while current_object != "COM":
            current_object = g_inverted[current_object]
            object_distance += 1

        know_distances[space_object] = object_distance

    return know_distances


def solve_a(data: list[str]) -> int:
    g, uniques = make_graph(data)
    g_inverted = invert_graph(g)
    know_distances = calcule_distances(g_inverted, uniques)
    return sum(know_distances.values())


def solve_b(data: list[str]) -> int:
    g_edges, uniques = make_graph(data)
    g_inverted = invert_graph(g_edges)

    for k, v in g_inverted.items():
        g_edges[k].append(v)

    start = "YOU"
    end = "SAN"

    distances_from_start_node = {start: 0}

    step = 0
    while len(uniques) != len(distances_from_start_node):
        for node, _ in [
            (node, distance)
            for node, distance in distances_from_start_node.items()
            if distance == step
        ]:
            for edge in g_edges[node]:
                if edge in distances_from_start_node:
                    continue
                distances_from_start_node[edge] = step + 1

        step += 1

    return (
        distances_from_start_node[end] - 2
    )  # we don't count the first and the last step


if __name__ == "__main__":
    data = parse_data("input.txt")
    sol_a = solve_a(data)

    print(f"Sol a: {sol_a}")

    sol_b = solve_b(data)

    print(f"Sol b: {sol_b}")


def test_solve_a():
    example_data_a = """COM)B
    B)C
    C)D
    D)E
    E)F
    B)G
    G)H
    D)I
    E)J
    J)K
    K)L""".split()

    assert solve_a(example_data_a) == 42


def test_solve_b():
    example_data_b = """COM)B
    B)C
    C)D
    D)E
    E)F
    B)G
    G)H
    D)I
    E)J
    J)K
    K)L
    K)YOU
    I)SAN""".split()

    assert solve_b(example_data_b) == 4
