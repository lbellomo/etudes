from enum import Enum
from typing import Iterable, cast
from dataclasses import dataclass
from collections import namedtuple, deque


raw_data = "L4, R2, R4, L5, L3, L1, R4, R5, R1, R3, L3, L2, L2, R5, R1, L1, L2, R2, R2, L5, R5, R5, L2, R1, R2, L2, L4, L1, R5, R2, R1, R1, L2, L3, R2, L5, L186, L5, L3, R3, L5, R4, R2, L5, R1, R4, L1, L3, R3, R1, L1, R4, R2, L1, L4, R5, L1, R50, L4, R3, R78, R4, R2, L4, R3, L4, R4, L1, R5, L4, R1, L2, R3, L2, R5, R5, L4, L1, L2, R185, L5, R2, R1, L3, R4, L5, R2, R4, L3, R4, L2, L5, R1, R2, L2, L1, L2, R2, L2, R1, L5, L3, L4, L3, L4, L2, L5, L5, R2, L3, L4, R4, R4, R5, L4, L2, R4, L5, R3, R1, L1, R3, L2, R2, R1, R5, L4, R5, L3, R2, R3, R1, R4, L4, R1, R3, L5, L1, L3, R2, R1, R4, L4, R3, L3, R3, R2, L3, L3, R4, L2, R4, L3, L4, R5, R1, L1, R5, R3, R1, R3, R4, L1, R4, R3, R1, L5, L5, L4, R4, R3, L2, R1, R5, L3, R4, R5, L4, L5, R2"  # noqa: E501

Point = tuple[int, int]
Turn = Enum("Turn", ["R", "L"])


class Direction(Enum):
    N = (1, 0)
    E = (0, 1)
    S = (-1, 0)
    W = (0, -1)


Instruction = namedtuple("Instruction", ["turn", "steps"])


def parse_instructions(raw_data: str) -> Iterable[Instruction]:
    return map(lambda x: Instruction(Turn[x[0]], int(x[1:])), raw_data.split(", "))


def distance(point: Point) -> int:
    return sum(abs(i) for i in point)


@dataclass
class Pos:
    point: Point = (0, 0)
    direction: deque[Direction] = deque(i for i in Direction)
    know_points = set([(0, 0)])
    twice_point: list[Point] = []

    def update(self, instruction: Instruction) -> None:
        match instruction.turn:
            case Turn.R:
                self.direction.rotate(-1)
            case Turn.L:
                self.direction.rotate(1)

        for _ in range(instruction.steps):
            self.point = cast(
                Point, tuple(i + j for i, j in zip(self.point, self.direction[0].value))
            )
            if self.point in self.know_points:
                self.twice_point.append(self.point)
            self.know_points.update([self.point])


pos = Pos()
for instruction in parse_instructions(raw_data):
    pos.update(instruction)

sol_a = distance(pos.point)
print(f"{sol_a = }")

sol_b = distance(pos.twice_point[0])
print(f"{sol_b = }")
