#!/usr/bin/env python3
"""Emit data/packs/core/career_tables.json from explicit WFRP 4e-style ranges (core book aligned where fixed)."""
from __future__ import annotations

import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT_DIR = os.path.join(ROOT, "data", "packs", "core")

TRAPS = {
    "Academics": "Clothing, Dagger, Pouch, Sling Bag containing Writing Kit and 1d10 sheets of Parchment",
    "Burghers": "Cloak, Clothing, Dagger, Hat, Pouch, Sling Bag containing Lunch",
    "Courtiers": "Courtly Garb, Dagger, Pouch containing Tweezers, Ear Pick and a Comb",
    "Peasants": "Cloak, Clothing, Dagger, Pouch, Sling Bag containing Rations (1 day)",
    "Rangers": "Cloak, Clothing, Dagger, Pouch, Backpack containing Tinderbox, Blanket, Rations (1 day)",
    "Riverfolk": "Cloak, Clothing, Dagger, Pouch, Sling Bag containing a Flask of Spirits",
    "Rogues": "Clothing, Dagger, Pouch, Sling Bag containing 2 Candles, 1d10 Matches, a Hood or Mask",
    "Warriors": "Clothing, Hand Weapon, Dagger, Pouch",
}


def expand(spec: list[tuple[int, int, str, str]]) -> list[dict]:
    rows: list[dict] = []
    for lo, hi, career, cls in spec:
        rows.append(
            {
                "d100_from": lo,
                "d100_to": hi,
                "career": career,
                "career_class": cls,
                "base_trappings": TRAPS[cls],
            }
        )
    return rows


# Human (Reiklander) — Warriors block fixed vs legacy script (no unreachable Slayer).
HUMAN = expand(
    [
        (1, 1, "Apothecary", "Academics"),
        (2, 2, "Engineer", "Academics"),
        (3, 3, "Lawyer", "Academics"),
        (4, 5, "Nun", "Academics"),
        (6, 6, "Physician", "Academics"),
        (7, 11, "Priest", "Academics"),
        (12, 13, "Scholar", "Academics"),
        (14, 14, "Wizard", "Academics"),
        (15, 15, "Agitator", "Burghers"),
        (16, 17, "Artisan", "Burghers"),
        (18, 19, "Beggar", "Burghers"),
        (20, 20, "Investigator", "Burghers"),
        (21, 21, "Merchant", "Burghers"),
        (22, 23, "Rat Catcher", "Burghers"),
        (24, 26, "Townsman", "Burghers"),
        (27, 27, "Watchman", "Burghers"),
        (28, 28, "Advisor", "Courtiers"),
        (29, 29, "Artist", "Courtiers"),
        (30, 30, "Duellist", "Courtiers"),
        (31, 31, "Envoy", "Courtiers"),
        (32, 32, "Noble", "Courtiers"),
        (33, 35, "Servant", "Courtiers"),
        (36, 36, "Spy", "Courtiers"),
        (37, 37, "Warden", "Courtiers"),
        (38, 38, "Bailiff", "Peasants"),
        (39, 39, "Hedge Witch", "Peasants"),
        (40, 40, "Herbalist", "Peasants"),
        (41, 42, "Hunter", "Peasants"),
        (43, 43, "Miner", "Peasants"),
        (44, 44, "Mystic", "Peasants"),
        (45, 45, "Scout", "Peasants"),
        (46, 50, "Villager", "Peasants"),
        (51, 51, "Bounty Hunter", "Rangers"),
        (52, 52, "Coachman", "Rangers"),
        (53, 54, "Entertainer", "Rangers"),
        (55, 56, "Flagellant", "Rangers"),
        (57, 57, "Messenger", "Rangers"),
        (58, 58, "Pedlar", "Rangers"),
        (59, 59, "Road Warden", "Rangers"),
        (60, 60, "Witch Hunter", "Rangers"),
        (61, 62, "Boatman", "Riverfolk"),
        (63, 63, "Huffer", "Riverfolk"),
        (64, 65, "Riverwarden", "Riverfolk"),
        (66, 68, "Riverwoman", "Riverfolk"),
        (69, 70, "Seaman", "Riverfolk"),
        (71, 71, "Smuggler", "Riverfolk"),
        (72, 73, "Stevedore", "Riverfolk"),
        (74, 74, "Wrecker", "Riverfolk"),
        (75, 75, "Bawd", "Rogues"),
        (76, 76, "Charlatan", "Rogues"),
        (77, 77, "Fence", "Rogues"),
        (78, 78, "Grave Robber", "Rogues"),
        (79, 83, "Outlaw", "Rogues"),
        (84, 84, "Racketeer", "Rogues"),
        (85, 87, "Thief", "Rogues"),
        (88, 88, "Witch", "Rogues"),
        (89, 90, "Cavalryman", "Warriors"),
        (91, 92, "Guard", "Warriors"),
        (93, 93, "Knight", "Warriors"),
        (94, 94, "Pit Fighter", "Warriors"),
        (95, 95, "Protagonist", "Warriors"),
        (96, 99, "Soldier", "Warriors"),
        (100, 100, "Warrior Priest", "Warriors"),
    ]
)

# Dwarf — Warriors: Slayer occupies top band per core; Warrior Priest not on dwarf table in legacy script.
DWARF = expand(
    [
        (1, 1, "Apothecary", "Academics"),
        (2, 4, "Engineer", "Academics"),
        (5, 6, "Lawyer", "Academics"),
        (7, 7, "Physician", "Academics"),
        (8, 9, "Scholar", "Academics"),
        (10, 11, "Agitator", "Burghers"),
        (12, 17, "Artisan", "Burghers"),
        (18, 18, "Beggar", "Burghers"),
        (19, 20, "Investigator", "Burghers"),
        (21, 24, "Merchant", "Burghers"),
        (25, 25, "Rat Catcher", "Burghers"),
        (26, 31, "Townsman", "Burghers"),
        (32, 34, "Watchman", "Burghers"),
        (35, 36, "Advisor", "Courtiers"),
        (37, 37, "Artist", "Courtiers"),
        (38, 38, "Duellist", "Courtiers"),
        (39, 40, "Envoy", "Courtiers"),
        (41, 41, "Noble", "Courtiers"),
        (42, 42, "Servant", "Courtiers"),
        (43, 43, "Spy", "Courtiers"),
        (44, 45, "Warden", "Courtiers"),
        (46, 47, "Bailiff", "Peasants"),
        (48, 49, "Hunter", "Peasants"),
        (50, 54, "Miner", "Peasants"),
        (55, 55, "Scout", "Peasants"),
        (56, 56, "Villager", "Peasants"),
        (57, 60, "Bounty Hunter", "Rangers"),
        (61, 61, "Coachman", "Rangers"),
        (62, 63, "Entertainer", "Rangers"),
        (64, 65, "Messenger", "Rangers"),
        (66, 67, "Pedlar", "Rangers"),
        (68, 69, "Boatman", "Riverfolk"),
        (70, 70, "Huffer", "Riverfolk"),
        (71, 72, "Riverwoman", "Riverfolk"),
        (73, 73, "Seaman", "Riverfolk"),
        (74, 75, "Smuggler", "Riverfolk"),
        (76, 77, "Stevedore", "Riverfolk"),
        (78, 78, "Wrecker", "Riverfolk"),
        (79, 79, "Fence", "Rogues"),
        (80, 82, "Outlaw", "Rogues"),
        (83, 83, "Racketeer", "Rogues"),
        (84, 84, "Thief", "Rogues"),
        (85, 87, "Guard", "Warriors"),
        (88, 90, "Pit Fighter", "Warriors"),
        (91, 93, "Protagonist", "Warriors"),
        (94, 96, "Soldier", "Warriors"),
        (97, 100, "Slayer", "Warriors"),
    ]
)

# Halfling — fix empty Warrior tail from legacy script using human-like spread.
HALFLING = expand(
    [
        (1, 1, "Apothecary", "Academics"),
        (2, 2, "Engineer", "Academics"),
        (3, 4, "Lawyer", "Academics"),
        (5, 6, "Physician", "Academics"),
        (7, 8, "Scholar", "Academics"),
        (9, 10, "Agitator", "Burghers"),
        (11, 15, "Artisan", "Burghers"),
        (16, 19, "Beggar", "Burghers"),
        (20, 21, "Investigator", "Burghers"),
        (22, 25, "Merchant", "Burghers"),
        (26, 28, "Rat Catcher", "Burghers"),
        (29, 31, "Townsman", "Burghers"),
        (32, 33, "Watchman", "Burghers"),
        (34, 34, "Advisor", "Courtiers"),
        (35, 36, "Artist", "Courtiers"),
        (37, 37, "Envoy", "Courtiers"),
        (38, 43, "Servant", "Courtiers"),
        (44, 44, "Spy", "Courtiers"),
        (45, 46, "Warden", "Courtiers"),
        (47, 47, "Bailiff", "Peasants"),
        (48, 50, "Herbalist", "Peasants"),
        (51, 52, "Hunter", "Peasants"),
        (53, 53, "Miner", "Peasants"),
        (54, 54, "Scout", "Peasants"),
        (55, 57, "Villager", "Peasants"),
        (58, 58, "Bounty Hunter", "Rangers"),
        (59, 60, "Coachman", "Rangers"),
        (61, 63, "Entertainer", "Rangers"),
        (64, 65, "Messenger", "Rangers"),
        (66, 67, "Pedlar", "Rangers"),
        (68, 68, "Road Warden", "Rangers"),
        (69, 69, "Boatman", "Riverfolk"),
        (70, 70, "Huffer", "Riverfolk"),
        (71, 71, "Riverwarden", "Riverfolk"),
        (72, 74, "Riverwoman", "Riverfolk"),
        (75, 75, "Seaman", "Riverfolk"),
        (76, 79, "Smuggler", "Riverfolk"),
        (80, 82, "Stevedore", "Riverfolk"),
        (83, 85, "Bawd", "Rogues"),
        (86, 86, "Charlatan", "Rogues"),
        (87, 87, "Fence", "Rogues"),
        (88, 88, "Grave Robber", "Rogues"),
        (89, 89, "Outlaw", "Rogues"),
        (90, 90, "Racketeer", "Rogues"),
        (91, 94, "Thief", "Rogues"),
        (95, 96, "Cavalryman", "Warriors"),
        (97, 98, "Guard", "Warriors"),
        (99, 99, "Knight", "Warriors"),
        (100, 100, "Warrior Priest", "Warriors"),
    ]
)

# High Elf — rebuilt from legacy non-dead branches; Warriors include Warrior Priest on 100.
HIGH_ELF = expand(
    [
        (1, 2, "Apothecary", "Academics"),
        (3, 6, "Lawyer", "Academics"),
        (7, 8, "Physician", "Academics"),
        (9, 12, "Scholar", "Academics"),
        (13, 16, "Wizard", "Academics"),
        (17, 19, "Artisan", "Burghers"),
        (20, 21, "Investigator", "Burghers"),
        (22, 26, "Merchant", "Burghers"),
        (27, 28, "Townsman", "Burghers"),
        (29, 29, "Watchman", "Burghers"),
        (30, 31, "Advisor", "Courtiers"),
        (32, 32, "Artist", "Courtiers"),
        (33, 34, "Duellist", "Courtiers"),
        (35, 37, "Envoy", "Courtiers"),
        (38, 40, "Noble", "Courtiers"),
        (41, 43, "Spy", "Courtiers"),
        (44, 45, "Warden", "Courtiers"),
        (46, 47, "Herbalist", "Peasants"),
        (48, 50, "Hunter", "Peasants"),
        (51, 56, "Scout", "Peasants"),
        (57, 59, "Bounty Hunter", "Rangers"),
        (60, 62, "Entertainer", "Rangers"),
        (63, 63, "Messenger", "Rangers"),
        (64, 64, "Boatman", "Riverfolk"),
        (65, 79, "Seaman", "Riverfolk"),
        (80, 80, "Smuggler", "Riverfolk"),
        (81, 82, "Bawd", "Rogues"),
        (83, 85, "Charlatan", "Rogues"),
        (86, 88, "Outlaw", "Rogues"),
        (89, 92, "Cavalryman", "Warriors"),
        (93, 94, "Guard", "Warriors"),
        (95, 95, "Knight", "Warriors"),
        (96, 97, "Pit Fighter", "Warriors"),
        (98, 98, "Protagonist", "Warriors"),
        (99, 99, "Soldier", "Warriors"),
        (100, 100, "Warrior Priest", "Warriors"),
    ]
)

# Wood Elf — fill gaps from legacy (River 79 only, Rogues 80-85, Warriors complete).
WOOD_ELF = expand(
    [
        (1, 1, "Scholar", "Academics"),
        (2, 5, "Wizard", "Academics"),
        (6, 10, "Artisan", "Burghers"),
        (11, 14, "Advisor", "Courtiers"),
        (15, 18, "Artist", "Courtiers"),
        (19, 25, "Envoy", "Courtiers"),
        (26, 31, "Noble", "Courtiers"),
        (32, 35, "Spy", "Courtiers"),
        (36, 42, "Herbalist", "Peasants"),
        (43, 52, "Hunter", "Peasants"),
        (53, 57, "Mystic", "Peasants"),
        (58, 68, "Scout", "Peasants"),
        (69, 70, "Bounty Hunter", "Rangers"),
        (71, 75, "Entertainer", "Rangers"),
        (76, 78, "Messenger", "Rangers"),
        (79, 79, "Wrecker", "Riverfolk"),
        (80, 85, "Outlaw", "Rogues"),
        (86, 90, "Cavalryman", "Warriors"),
        (91, 92, "Guard", "Warriors"),
        (93, 94, "Knight", "Warriors"),
        (95, 96, "Pit Fighter", "Warriors"),
        (97, 97, "Protagonist", "Warriors"),
        (98, 99, "Soldier", "Warriors"),
        (100, 100, "Warrior Priest", "Warriors"),
    ]
)


def validate(rows: list[dict], name: str) -> None:
    covered = set()
    for r in rows:
        for x in range(r["d100_from"], r["d100_to"] + 1):
            if x in covered:
                raise SystemExit(f"Overlap {name} on {x}")
            covered.add(x)
    missing = [x for x in range(1, 101) if x not in covered]
    if missing:
        raise SystemExit(f"{name} missing rolls: {missing[:20]}...")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    tables = {
        "Human (Reiklander)": HUMAN,
        "Dwarf": DWARF,
        "Halfling": HALFLING,
        "High Elf": HIGH_ELF,
        "Wood Elf": WOOD_ELF,
    }
    for k, v in tables.items():
        validate(v, k)
    path = os.path.join(OUT_DIR, "career_tables.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"species": tables, "source": "core", "merge_policy": "replace_species_tables"}, f, indent=2)
    print("Wrote", path)


if __name__ == "__main__":
    main()
