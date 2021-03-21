from typing import List, Tuple, Set

import pytest  # type: ignore


t_point = Tuple[int, int]


def parse_data(raw_data: str) -> List[List[str]]:
    return [wire.strip().split(",") for wire in raw_data.split("\n") if wire]


def read_data(path_input: str) -> List[List[str]]:
    with open(path_input) as f_in:
        return parse_data(f_in.read())


def build_wire(wire: List[str]) -> List[t_point]:
    all_pos = []
    x, y = 0, 0
    for step in wire:
        direction = step[0]
        size = int(step[1:])
        for i in range(size):
            if direction == "U":
                y += 1
            elif direction == "D":
                y -= 1
            elif direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            else:
                raise ValueError("Invalid direction!")

            all_pos.append((x, y))

    return all_pos


def build_wires(
    wires: List[List[str]],
) -> Tuple[List[t_point], List[t_point], Set[t_point]]:
    wire_a = wires[0]
    wire_b = wires[1]
    all_pos_wire_a = build_wire(wire_a)
    all_pos_wire_b = build_wire(wire_b)
    intersections = set(all_pos_wire_a).intersection(all_pos_wire_b)
    return all_pos_wire_a, all_pos_wire_b, intersections


def solve_a(intersections: Set[t_point]) -> int:
    return min(abs(point[0]) + abs(point[1]) for point in intersections)


def solve_b(
    all_pos_wire_a: List[t_point],
    all_pos_wire_b: List[t_point],
    intersections: Set[t_point],
) -> int:
    distances = []
    for intersection in intersections:
        total = 0
        for all_pos in [all_pos_wire_a, all_pos_wire_b]:
            for pos in all_pos:
                if pos != intersection:
                    total += 1
                else:
                    total += 1
                    break
        distances.append(total)
    return min(distances)


if __name__ == "__main__":
    all_pos_wire_a, all_pos_wire_b, intersections = build_wires(read_data("input.txt"))
    print("sol part a: ", solve_a(intersections))
    print("sol part b: ", solve_b(all_pos_wire_a, all_pos_wire_b, intersections))

test_input_1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"
test_input_2 = (
    "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
)


@pytest.mark.parametrize(
    "test_input,expected", [(test_input_1, 159), (test_input_2, 135)]
)
def test_solve_a(test_input, expected):
    _, _, intersections = build_wires(parse_data(test_input))
    assert solve_a(intersections) == expected


@pytest.mark.parametrize(
    "test_input,expected", [(test_input_1, 610), (test_input_2, 410)]
)
def test_solve_b(test_input, expected):
    assert solve_b(*build_wires(parse_data(test_input))) == expected
