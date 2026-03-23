import random

from wfrp_chargen.skill_rules import allocate_integers, allocate_characteristic_advances


def test_allocate_integers_sum_and_cap():
    rng = random.Random(42)
    bins = allocate_integers(40, 8, 10, rng)
    assert sum(bins) == 40
    assert all(b <= 10 for b in bins)
    assert len(bins) == 8


def test_allocate_characteristics_five_total():
    rng = random.Random(1)
    out = allocate_characteristic_advances(["WS", "T", "Fel"], 5, rng)
    assert sum(out.values()) == 5
