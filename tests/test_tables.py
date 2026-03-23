import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CORE = os.path.join(ROOT, "data", "packs", "core")


def _load(name: str):
    with open(os.path.join(CORE, name), encoding="utf-8") as f:
        return json.load(f)


def test_career_tables_cover_d100():
    doc = _load("career_tables.json")
    for species, rows in doc["species"].items():
        covered = set()
        for r in rows:
            for x in range(r["d100_from"], r["d100_to"] + 1):
                assert x not in covered, f"{species} overlap on {x}"
                covered.add(x)
        missing = [x for x in range(1, 101) if x not in covered]
        assert not missing, f"{species} missing {missing}"


def test_random_talents_cover_d100():
    doc = _load("random_talents.json")
    covered = set()
    for r in doc["rolls"]:
        for x in range(r["d100_from"], r["d100_to"] + 1):
            assert x not in covered, f"overlap on {x}"
            covered.add(x)
    missing = [x for x in range(1, 101) if x not in covered]
    assert not missing, f"missing {missing}"


def test_species_roll_covers_d100():
    doc = _load("species.json")
    covered = set()
    for r in doc["species_roll"]:
        for x in range(r["d100_from"], r["d100_to"] + 1):
            assert x not in covered
            covered.add(x)
    assert covered == set(range(1, 101))


def test_careers_have_eight_skills_and_four_talents():
    doc = _load("careers.json")
    for name, c in doc["careers"].items():
        assert len(c["skills"]) == 8, name
        assert len(c["talents"]) == 4, name
        assert len(c["advance_characteristics"]) == 3, name
