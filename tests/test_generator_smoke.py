import random

from wfrp_chargen.generator import generate_character
from wfrp_chargen.loader import default_data_dir, load_core_pack


def test_generate_many_seeds():
    root = default_data_dir()
    core = load_core_pack(root)
    for seed in range(50):
        ch = generate_character(core, rng=random.Random(seed), name="Test")
        assert ch.wounds >= 1
        assert len(ch.skills) >= 8
        assert ch.talents
        assert len(ch.talent_details) == len(ch.talents)
