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
    parser.add_argument(
        "--no-portrait",
        action="store_true",
        help="Omit NightCafe portrait prompt block (text) or portrait fields (JSON)",
    )
    parser.add_argument(
        "--portrait-only",
        action="store_true",
        help="Print only NightCafe positive and negative prompts (no full character sheet)",
    )
    parser.add_argument(
        "--gender",
        choices=("woman", "man", "nonbinary"),
        default=None,
        help="Force character gender (default: random; names from Faker align when possible)",
    )
    args = parser.parse_args()

    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    pack = args.data_dir or default_data_dir(root)
    core = load_core_pack(pack)
    for ep in args.extra_pack:
        merge_extra_pack(core, ep)

    rng = random.Random(args.seed)
    gender = args.gender
    if gender is None:
        gender = rng.choices(["woman", "man", "nonbinary"], weights=[42, 42, 16], k=1)[0]

    name = "Unnamed"
    try:
        from faker import Faker

        fake = Faker("de_DE")
        if gender == "woman":
            name = f"{fake.first_name_female()} {fake.last_name()}"
        elif gender == "man":
            name = f"{fake.first_name_male()} {fake.last_name()}"
        else:
            name = f"{fake.first_name()} {fake.last_name()}"
    except Exception:
        pass

    ch = generate_character(core, rng=rng, name=name, gender=gender)
    if args.portrait_only:
        from wfrp_chargen.portrait_prompt import format_nightcafe_block

        sys.stdout.write(format_nightcafe_block(ch))
        sys.stdout.write("\n")
        return 0
    if args.json:
        import json

        payload = {
            "name": ch.name,
            "gender": ch.gender,
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
        if not args.no_portrait:
            payload["nightcafe_portrait_prompt"] = ch.nightcafe_portrait_prompt
            payload["nightcafe_negative_prompt"] = ch.nightcafe_negative_prompt
        sys.stdout.write(json.dumps(payload, indent=2, ensure_ascii=False))
        sys.stdout.write("\n")
    else:
        sys.stdout.write(format_character(ch, include_portrait=not args.no_portrait))
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
