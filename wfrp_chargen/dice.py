from __future__ import annotations

import random
from typing import Callable, Optional


def d10(rng: random.Random) -> int:
    return rng.randint(1, 10)


def d100(rng: random.Random) -> int:
    return rng.randint(1, 100)


def roll_2d10_plus_20(rng: random.Random) -> int:
    return d10(rng) + d10(rng) + 20


def clamp_stat(value: int, lo: int = 1, hi: int = 100) -> int:
    return max(lo, min(hi, value))


def bonus_tens(stat: int) -> int:
    return stat // 10
