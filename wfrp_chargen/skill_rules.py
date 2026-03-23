from __future__ import annotations

import random
import re
from typing import Iterable

_TRADES = [
    "Smith",
    "Carpenter",
    "Tanner",
    "Cook",
    "Apothecary",
    "Charms",
    "Printing",
    "Engineer",
    "Herbalist",
    "Farrier",
]
_LANGUAGES = ["Classical", "Magick", "Khazalid", "Eltharin", "Mootish", "Bretonnian", "Wastelander"]
_MELEE = ["Basic", "Fencing", "Cavalry", "Two-handed", "Flail", "Polearm", "Fist"]
_ENTERTAIN = ["Storytelling", "Storyteller", "Sing", "Act", "Fortune Telling", "Taunt", "Any"]
_PERFORM = ["Drum or Fife", "Any"]
_PLAY = ["Dice", "Any"]
_CHANN = ["Light", "Amber", "Jade", "Gold", "Celestial", "Grey", "Amethyst", "Bright", "Any Colour"]


def resolve_skill_label(skill: str, rng: random.Random) -> str:
    """Replace (Any) / (any) placeholders with a concrete label for display."""
    s = skill.strip()
    low = s.lower()

    def sub_any(pattern: str, options: list[str]) -> str:
        if re.search(pattern, s, flags=re.I):
            pick = rng.choice(options)
            return re.sub(pattern, f"({pick})", s, flags=re.I, count=1)
        return s

    if "(any colour)" in low or "(any color)" in low:
        pick = rng.choice(_CHANN)
        return re.sub(r"\(Any Colour\)", f"({pick})", s, flags=re.I)
    if "(any one)" in low or "(any)" in low:
        if low.startswith("trade"):
            pick = rng.choice(_TRADES)
            return re.sub(r"\(Any\)|\(any one\)|\(any\)", f"({pick})", s, flags=re.I)
        if low.startswith("language"):
            pick = rng.choice(_LANGUAGES)
            return re.sub(r"\(Any\)|\(any one\)|\(any\)", f"({pick})", s, flags=re.I)
        if low.startswith("melee"):
            pick = rng.choice(_MELEE)
            return re.sub(r"\(Any\)|\(any one\)|\(any\)", f"({pick})", s, flags=re.I)
        if low.startswith("art"):
            return "Art (Painting)"
        if low.startswith("entertain"):
            pick = rng.choice(_ENTERTAIN)
            return re.sub(r"\(Any\)|\(any one\)|\(any\)", f"({pick})", s, flags=re.I)
        if low.startswith("perform"):
            pick = rng.choice(_PERFORM)
            return re.sub(r"\(Any\)|\(any one\)|\(any\)", f"({pick})", s, flags=re.I)
        if low.startswith("play"):
            pick = rng.choice(_PLAY)
            return re.sub(r"\(Any\)|\(any one\)|\(any\)", f"({pick})", s, flags=re.I)
        if low.startswith("lore"):
            return "Lore (Local)"
        if low.startswith("stealth"):
            pick = rng.choice(["Urban", "Rural", "Underground"])
            return re.sub(r"\(Any\)|\(any one\)|\(any\)", f"({pick})", s, flags=re.I)
        if low.startswith("bless"):
            return "Bless (Any Cult)"
        if low.startswith("petty magic"):
            return re.sub(r"\(Any\)", "(Any)", s)
    if "underground or urban" in low:
        pick = rng.choice(["Underground", "Urban"])
        return s.replace("Stealth (Underground or Urban)", f"Stealth ({pick})")
    if "rural or urban" in low:
        pick = rng.choice(["Rural", "Urban"])
        return s.replace("Stealth (Rural or Urban)", f"Stealth ({pick})")
    return s


def primary_characteristic(skill: str) -> str:
    sk = skill.lower()
    if sk.startswith("art"):
        return "Dex"
    if sk.startswith("athletics"):
        return "Ag"
    if sk.startswith("animal"):
        return "Int"
    if sk.startswith("bribery"):
        return "Fel"
    if sk.startswith("charm"):
        return "Fel"
    if sk.startswith("channelling"):
        return "WP"
    if sk.startswith("climb"):
        return "S"
    if sk.startswith("command"):
        return "Fel"
    if sk.startswith("consume alcohol"):
        return "T"
    if sk.startswith("cool"):
        return "WP"
    if sk.startswith("dodge"):
        return "Ag"
    if sk.startswith("drive"):
        return "Ag"
    if sk.startswith("endurance"):
        return "T"
    if sk.startswith("entertain"):
        return "Fel"
    if sk.startswith("evaluate"):
        return "Int"
    if sk.startswith("gamble"):
        return "Int"
    if sk.startswith("gossip"):
        return "Fel"
    if sk.startswith("haggle"):
        return "Fel"
    if sk.startswith("heal"):
        return "Int"
    if sk.startswith("intimidate"):
        return "S"
    if sk.startswith("intuition"):
        return "I"
    if sk.startswith("language"):
        return "Int"
    if sk.startswith("leadership"):
        return "Fel"
    if sk.startswith("lore"):
        return "Int"
    if sk.startswith("melee"):
        return "WS"
    if sk.startswith("navigation"):
        return "I"
    if sk.startswith("outdoor survival"):
        return "Int"
    if sk.startswith("perception"):
        return "I"
    if sk.startswith("perform"):
        return "Fel"
    if sk.startswith("play"):
        return "Dex"
    if sk.startswith("pray"):
        return "Fel"
    if sk.startswith("ranged"):
        return "BS"
    if sk.startswith("research"):
        return "Int"
    if sk.startswith("ride"):
        return "Ag"
    if sk.startswith("row"):
        return "S"
    if sk.startswith("sail"):
        return "Ag"
    if sk.startswith("set trap"):
        return "Dex"
    if sk.startswith("sleight"):
        return "Dex"
    if sk.startswith("stealth"):
        return "Ag"
    if sk.startswith("swim"):
        return "S"
    if sk.startswith("track"):
        return "I"
    if sk.startswith("trade"):
        return "Dex"
    if sk.startswith("leadership"):
        return "Fel"
    return "Fel"


def apply_skill_advance(skill_value: int, characteristic: int, rng: random.Random | None = None) -> int:
    """One skill advance using core thresholds (simplified continuous version)."""
    t1 = characteristic
    t2 = characteristic + 20
    t3 = characteristic + 40
    if skill_value <= t1:
        return skill_value + 3
    if skill_value <= t2:
        return skill_value + 2
    if skill_value <= t3:
        return skill_value + 1
    return skill_value + 1


def apply_n_skill_advances(start: int, characteristic: int, n: int) -> int:
    v = start
    for _ in range(n):
        v = apply_skill_advance(v, characteristic, None)
    return v


def allocate_integers(total: int, n_bins: int, cap: int, rng: random.Random) -> list[int]:
    """Randomly distribute total across n_bins with each <= cap."""
    if total > n_bins * cap:
        raise ValueError("impossible allocation")
    counts = [0] * n_bins
    left = total
    guard = 0
    while left > 0:
        guard += 1
        if guard > 100000:
            raise RuntimeError("allocation stuck")
        i = rng.randrange(n_bins)
        if counts[i] >= cap:
            continue
        counts[i] += 1
        left -= 1
    return counts


def allocate_characteristic_advances(chars: list[str], total: int, rng: random.Random) -> dict[str, int]:
    out = {c: 0 for c in chars}
    for _ in range(total):
        out[rng.choice(chars)] += 1
    return out
