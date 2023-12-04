from math import prod
from typing import NamedTuple

with open("input.txt") as f:
    data = [line.strip() for line in f]


class Record(NamedTuple):
    red: int
    green: int
    blue: int


class Game(NamedTuple):
    id: int
    records: list[Record]


def parse_record(raw_record: str) -> Record:
    record_dict = {"red": 0, "blue": 0, "green": 0}
    for value in raw_record.strip().split(", "):
        number, color = value.split()
        record_dict[color] = int(number)

    return Record(**record_dict)


def parse_game(raw_game: str) -> Game:
    game_id_raw, rest = raw_game.split(":")
    _, game_id_raw = game_id_raw.split()
    game_id = int(game_id_raw)

    records = [parse_record(record) for record in rest.split(";")]
    return Game(id=game_id, records=records)


def check_game(game: Game, limit: Record) -> bool:
    return any(
        (
            record.red > limit.red
            or record.green > limit.green
            or record.blue > limit.blue
        )
        for record in game.records
    )


def power_min_set(game: Game) -> int:
    return prod(max(record[i] for record in game.records) for i in range(3))


games = [parse_game(raw_game) for raw_game in data]
limit = Record(red=12, green=13, blue=14)

sol_a = sum(game.id for game in games if not check_game(game, limit))
print(f"{sol_a = }")

sol_b = sum(power_min_set(game) for game in games)
print(f"{sol_b = }")
