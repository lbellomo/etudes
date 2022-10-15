from typing import cast
from string import ascii_lowercase
from collections import namedtuple, Counter, deque

with open("input.txt") as f:
    raw_data = [line.strip() for line in f]

Room = namedtuple("Room", ["name", "id", "checksum"])


def parse_room(line: str) -> Room:
    split = line.split("-")
    return Room(split[:-1], *split[-1][:-1].split("["))


rooms = [parse_room(line) for line in raw_data]

# sum(
#     int(r.id)
#     for r in rooms
#     if "".join(
#         map(
#             lambda x: x[0],
#             sorted(
#                 sorted(Counter("".join(r.name)).most_common(), key=lambda x: x[0]),
#                 key=lambda x: x[1],
#                 reverse=True,
#             ),
#         )
#     )[:5]
#     == r.checksum
# )


def is_valid_checksum(r: Room) -> bool:
    most_common = Counter("".join(r.name)).most_common()
    most_common = sorted(
        sorted(most_common, key=lambda x: x[0]), key=lambda x: x[1], reverse=True
    )
    checksum = "".join(i[0] for i in most_common)[:5]
    return cast(bool, r.checksum == checksum)


sol_a = sum(map(lambda x: int(x.id), filter(is_valid_checksum, rooms)))
print(f"{sol_a = }")

d = deque(ascii_lowercase)


def decrypt_letter(char: str, sector_id: int) -> str:
    if char == " ":
        return "-"
    elif char == "-":
        return " "
    else:
        dist_to_char = -d.index(char)
        d.rotate(dist_to_char - sector_id)
        return d[0]


def decrypt(r: Room) -> str:
    return "".join(decrypt_letter(char, int(r.id)) for char in "-".join(r.name))


sol_b = int([r for r in rooms if "northpole" in decrypt(r)][0].id)
print(f"{sol_b = }")
