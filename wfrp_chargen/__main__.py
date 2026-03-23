from __future__ import annotations

import argparse
import os
import random
import sys

from wfrp_chargen.format_text import format_character
from wfrp_chargen.generator import generate_character
from wfrp_chargen.loader import default_data_dir, load_core_pack, merge_extra_pack


def main() -> int:
    parser = argparse.ArgumentParser(description="WFRP 4e random character generator (core data pack).")
    parser.add_argument("--seed", type=int, default=None, help="RNG seed (optional)")
    parser.add_argument("--data-dir", default=None, help="Override core pack directory")
    parser.add_argument("--extra-pack", action="append", default=[], help="Additional pack directory to merge")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    args = parser.parse_args()

    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    pack = args.data_dir or default_data_dir(root)
    core = load_core_pack(pack)
    for ep in args.extra_pack:
        merge_extra_pack(core, ep)

    rng = random.Random(args.seed)
    name = None
    try:
        from faker import Faker

        fake = Faker("de_DE")
        name = f"{fake.first_name()} {fake.last_name()}"
    except Exception:
        name = "Unnamed"

    ch = generate_character(core, rng=rng, name=name)
    if args.json:
        import json

        payload = {
            "name": ch.name,
            "species": ch.species,
            "career": ch.career,
            "career_class": ch.career_class,
            "status": ch.status,
            "characteristics": ch.characteristics,
            "movement": ch.movement,
            "initiative": ch.initiative,
            "wounds": ch.wounds,
            "fate": ch.fate,
            "resilience": ch.resilience,
            "skills": ch.skills,
            "talents": ch.talents,
            "talent_details": ch.talent_details,
            "trappings": ch.trappings,
            "notes": ch.notes,
            "talent_deltas": ch.talent_deltas,
        }
        sys.stdout.write(json.dumps(payload, indent=2, ensure_ascii=False))
        sys.stdout.write("\n")
    else:
        sys.stdout.write(format_character(ch))
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
