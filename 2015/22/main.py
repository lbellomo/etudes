from __future__ import annotations

from enum import Enum
from copy import copy
from dataclasses import dataclass

spell_cost = {
    "magic missile": 53,
    "drain": 73,
    "shield": 113,
    "poison": 173,
    "recharge": 229,
}


class Spells(Enum):
    MAGIC_MISSILE = "magic_missile"
    DRAIN = "drain"
    SHIELD = "shield"
    POISON = "poison"
    RECHARGE = "recharge"


mage_hp = 50
mage_mana = 500

# input
boss_hp = 71
boss_damage = 10


@dataclass
class Boss:
    hp: int = boss_hp
    damage: int = boss_damage

    timer_poison: int = 0

    def hit(self, other: Mage) -> None:
        other.hp -= max(1, self.damage - other.armor)

    def tick(self) -> None:
        if self.timer_poison > 0:
            self.timer_poison -= 1

            self.hp -= 3


@dataclass
class Mage:
    hp: int = mage_hp
    mana: int = mage_mana
    armor: int = 0
    mana_spent: int = 0
    is_hardmode: bool = False

    timer_shield: int = 0
    timer_recharge: int = 0

    def spend_mana(self, spell: str) -> None:
        cost = spell_cost[spell]

        self.mana -= cost
        if self.mana < 0:
            raise ValueError("Not enoght mana for magic missile")

        self.mana_spent += cost

    def cast_magic_missile(self, other: Boss) -> None:
        self.spend_mana("magic missile")

        other.hp -= 4

    def cast_drain(self, other: Boss) -> None:
        self.spend_mana("drain")

        other.hp -= 2
        self.hp += 2

    def cast_shield(self) -> None:
        self.spend_mana("shield")

        if self.timer_shield != 0:
            raise ValueError("Can't cast shield now")

        self.timer_shield = 6
        self.armor = 7

    def cast_poison(self, other: Boss) -> None:
        self.spend_mana("poison")

        if other.timer_poison != 0:
            raise ValueError("Can't cast poison now")

        other.timer_poison = 6

    def cast_recharge(self) -> None:
        self.spend_mana("recharge")

        if self.timer_recharge != 0:
            raise ValueError("Can't cast recharge now")

        self.timer_recharge = 5

    def tick(self) -> None:
        if self.timer_shield > 0:
            self.timer_shield -= 1
            if self.timer_shield == 0:
                self.armor = 0

        if self.timer_recharge > 0:
            self.timer_recharge -= 1
            self.mana += 101


def turn(mage: Mage, boss: Boss, spell: Spells) -> tuple[Mage, Boss]:
    if mage.is_hardmode:
        mage.hp -= 1
        if mage.hp <= 0:
            raise ValueError("rip mage")

    mage.tick()
    boss.tick()
    if boss.hp <= 0:
        return mage, boss

    mage_spell = mage.__getattribute__(f"cast_{spell.value}")

    try:
        mage_spell(boss)
    except TypeError:
        mage_spell()

    if boss.hp <= 0:
        return mage, boss
    mage.tick()
    boss.tick()
    if boss.hp <= 0:
        return mage, boss
    boss.hit(mage)
    if mage.hp <= 0:
        raise ValueError("rip mage")

    return mage, boss


def solve(hardmode: bool) -> int:
    possible_mana_cost: list[int] = []

    states = [(Mage(is_hardmode=hardmode), Boss())]

    while states and len(possible_mana_cost) < 10:

        next_states = []
        for mage, boss in states:
            for spell in Spells:
                try:
                    next_states.append(turn(copy(mage), copy(boss), spell))
                except ValueError:
                    pass

        # collect mage.mana_spent for each dead boss
        possible_mana_cost += [m.mana_spent for m, b in next_states if b.hp <= 0]
        states = [(m, b) for m, b in next_states if b.hp > 0]

    return min(possible_mana_cost)


sol_a = solve(hardmode=False)
print(f"{sol_a = }")

sol_b = solve(hardmode=True)
print(f"{sol_b = }")
