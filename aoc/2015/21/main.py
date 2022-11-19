from itertools import combinations
from dataclasses import dataclass

player_hp = 100
boss_hp = 104
boss_damage = 8
boss_armor = 1


@dataclass
class Item:
    name: str
    cost: int
    damage: int
    armor: int
    i_type: str

    def __post_init__(self):
        self.cost = int(self.cost)
        self.damage = int(self.damage)
        self.armor = int(self.armor)


@dataclass
class Character:
    hp: int
    damage: int
    armor: int

    def hit(self, other):
        other.hp -= max(1, self.damage - other.armor)

    def is_dead(self):
        if self.hp <= 0:
            return True
        return False


def fight(player, boss):
    while True:
        player.hit(boss)
        if boss.is_dead():
            return True
        boss.hit(player)
        if player.is_dead():
            return False


def get_cost(w, a, r0, r1, normal=True):
    choice = [w, a, r0, r1]
    cost = sum(item_choice.cost for item_choice in choice)
    damage = sum(item_choice.damage for item_choice in choice)
    armor = sum(item_choice.armor for item_choice in choice)

    player = Character(player_hp, damage, armor)
    boss = Character(boss_hp, boss_damage, boss_armor)

    player_win = fight(player, boss)

    if normal:
        if player_win:
            return cost
        else:
            return 100_000

    else:
        if not player_win:
            return cost
        else:
            return -1


raw_weapons = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0"""

raw_armors = """Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5"""

raw_rings = """Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""


def parse_items(raw_items):
    item_type = raw_items.split(":", maxsplit=1)[0]
    return [
        Item(*item.rsplit(maxsplit=3), item_type) for item in raw_items.split("\n")[1:]
    ]


weapons = parse_items(raw_weapons)
armors = parse_items(raw_armors)
rings = parse_items(raw_rings)

none_item = ("None", "0", "0", "0")

armors += [Item(*none_item, "Armor")]
rings += [Item(*none_item, "Ring")] * 2


costs = []

for w in weapons:
    for a in armors:
        for r0, r1 in combinations(rings, 2):
            costs.append(get_cost(w, a, r0, r1))

sol_a = min(costs)
print(f"{sol_a = }")

costs = []

for w in weapons:
    for a in armors:
        for r0, r1 in combinations(rings, 2):
            costs.append(get_cost(w, a, r0, r1, normal=False))

sol_b = max(costs)
print(f"{sol_b = }")
