from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Any

from wfrp_chargen.dice import bonus_tens, clamp_stat, d100, roll_2d10_plus_20
from wfrp_chargen.loader import CoreData, lookup_talent_detail
from wfrp_chargen.skill_rules import (
    allocate_characteristic_advances,
    allocate_integers,
    apply_n_skill_advances,
    primary_characteristic,
    resolve_skill_label,
)
from wfrp_chargen.talent_effects import aggregate_talent_modifiers


CHAR_ORDER = ["WS", "BS", "S", "T", "I", "Ag", "Dex", "Int", "WP", "Fel"]


@dataclass
class GeneratedCharacter:
    name: str
    species: str
    career: str
    career_class: str
    characteristics: dict[str, int]
    initiative: int
    movement: int
    wounds: int
    fate: int
    resilience: int
    species_skill_advances: dict[str, int] = field(default_factory=dict)
    career_skill_advances: dict[str, int] = field(default_factory=dict)
    career_char_advances: dict[str, int] = field(default_factory=dict)
    skills: dict[str, int] = field(default_factory=dict)
    talents: list[str] = field(default_factory=list)
    talent_details: list[dict[str, Any]] = field(default_factory=list)
    trappings: list[str] = field(default_factory=list)
    status: str = ""
    notes: list[str] = field(default_factory=list)
    talent_deltas: dict[str, Any] = field(default_factory=dict)


def _roll_species(core: CoreData, rng: random.Random) -> str:
    r = d100(rng)
    for row in core.species_roll:
        if row["d100_from"] <= r <= row["d100_to"]:
            return row["species"]
    raise RuntimeError(f"species roll {r} out of range")


def _career_from_table(core: CoreData, species: str, rng: random.Random) -> tuple[str, str, str]:
    r = d100(rng)
    rows = core.career_tables.get(species)
    if not rows:
        raise KeyError(f"No career table for species: {species}")
    for row in rows:
        if row["d100_from"] <= r <= row["d100_to"]:
            return row["career"], row["career_class"], row["base_trappings"]
    raise RuntimeError(f"Career roll {r} missing for {species}")


def _random_talent_name(core: CoreData, rng: random.Random) -> str:
    r = d100(rng)
    for band in core.random_talents["rolls"]:
        if band["d100_from"] <= r <= band["d100_to"]:
            tid = band["talent_id"]
            entry = core.talents_catalog.get(tid)
            if entry:
                return str(entry["name"])
            return tid.replace("_", " ").title()
    raise RuntimeError(f"Random talent roll {r} out of range")


def _resolve_species_talent_entries(core: CoreData, species_key: str, rng: random.Random) -> tuple[list[str], list[str]]:
    spec = core.species[species_key]
    names: list[str] = []
    notes: list[str] = []
    for entry in spec.get("talents", []):
        if isinstance(entry, str):
            names.append(entry)
            continue
        if not isinstance(entry, dict):
            continue
        if "note" in entry:
            notes.append(str(entry["note"]))
            continue
        if "fixed" in entry:
            names.append(str(entry["fixed"]))
            continue
        if "choose_one" in entry:
            names.append(str(rng.choice(list(entry["choose_one"]))))
            continue
        if "random_table" in entry:
            table = entry["random_table"]
            count = int(entry.get("count", 1))
            if table != "core_random_talents":
                notes.append(f"Unknown random_table {table}")
                continue
            for _ in range(count):
                names.append(_random_talent_name(core, rng))
    return names, notes


def _pick_species_skills(spec: dict[str, Any], rng: random.Random) -> dict[str, int]:
    pool = list(spec["skills"])
    rng.shuffle(pool)
    n5 = int(spec["skill_allocation"]["plus5_advances"])
    n3 = int(spec["skill_allocation"]["plus3_advances"])
    picks = pool[: n5 + n3]
    adv: dict[str, int] = {}
    for s in picks[:n5]:
        adv[s] = adv.get(s, 0) + 5
    for s in picks[n5 : n5 + n3]:
        adv[s] = adv.get(s, 0) + 3
    return adv


def _starting_wounds(spec: dict[str, Any], chars: dict[str, int]) -> int:
    sb = bonus_tens(chars["S"])
    tb = bonus_tens(chars["T"])
    wb = bonus_tens(chars["WP"])
    wspec = spec["wounds"]
    total = sb + 2 * tb + wb + int(wspec.get("flat_adjust", 0))
    if wspec.get("subtract_strength_bonus"):
        total -= sb
    return max(1, total)


def generate_character(
    core: CoreData,
    rng: random.Random | None = None,
    name: str | None = None,
) -> GeneratedCharacter:
    rng = rng or random.Random()
    species_name = _roll_species(core, rng)
    spec = core.species[species_name]
    career_name, career_class, base_trappings = _career_from_table(core, species_name, rng)
    career = core.careers.get(career_name)
    if not career:
        raise KeyError(f"Unknown career in data: {career_name}")

    base_chars = {k: roll_2d10_plus_20(rng) for k in CHAR_ORDER}
    mods = spec.get("modifiers", {})
    chars = {k: clamp_stat(base_chars[k] + int(mods.get(k, 0))) for k in CHAR_ORDER}

    adv_chars_keys = list(career["advance_characteristics"])
    char_adv = allocate_characteristic_advances(adv_chars_keys, 5, rng)
    for abbr, n in char_adv.items():
        if n:
            chars[abbr] = clamp_stat(chars[abbr] + n)

    species_talents, species_notes = _resolve_species_talent_entries(core, species_name, rng)
    career_talent_options = list(career["talents"])
    chosen_career_talent = str(rng.choice(career_talent_options))
    all_talents = list(species_talents) + [chosen_career_talent]

    talent_deltas = aggregate_talent_modifiers(core, all_talents)
    for abbr in CHAR_ORDER:
        d = int(talent_deltas["characteristics"].get(abbr, 0))
        if d:
            chars[abbr] = clamp_stat(chars[abbr] + d)

    wounds = _starting_wounds(spec, chars) + int(talent_deltas.get("wounds", 0))
    wounds = max(1, wounds)
    movement = int(spec["movement"]) + int(talent_deltas.get("movement", 0))
    movement = max(1, movement)
    fate = int(spec["fate"]) + int(talent_deltas.get("fate", 0))
    fate = max(0, fate)
    resilience = int(spec["resilience"]) + int(talent_deltas.get("resilience", 0))
    resilience = max(0, resilience)
    initiative = (
        bonus_tens(chars["Ag"])
        + bonus_tens(chars["I"])
        + int(spec.get("initiative_bonus", 0))
        + int(talent_deltas.get("initiative", 0))
    )

    resolved_skills: dict[str, str] = {}
    for sk in career["skills"]:
        resolved_skills[sk] = resolve_skill_label(sk, rng)

    class_skill_names = list(resolved_skills.values())
    idx_map = {i: n for i, n in enumerate(class_skill_names)}
    alloc = allocate_integers(40, len(class_skill_names), 10, rng)
    career_skill_advances = {idx_map[i]: alloc[i] for i in range(len(class_skill_names))}

    species_skill_picks = _pick_species_skills(spec, rng)
    species_skill_advances: dict[str, int] = {}
    for sk, adv in species_skill_picks.items():
        lbl = resolve_skill_label(sk, rng)
        species_skill_advances[lbl] = species_skill_advances.get(lbl, 0) + adv

    final_skills: dict[str, int] = {}
    for _raw, lbl in resolved_skills.items():
        char_abbr = primary_characteristic(lbl)
        start = chars[char_abbr]
        n_class = career_skill_advances.get(lbl, 0)
        n_spec = species_skill_advances.get(lbl, 0)
        final_skills[lbl] = apply_n_skill_advances(start, chars[char_abbr], n_class + n_spec)

    for lbl, n_spec in species_skill_advances.items():
        if lbl in final_skills:
            continue
        if n_spec <= 0:
            continue
        char_abbr = primary_characteristic(lbl)
        start = chars[char_abbr]
        final_skills[lbl] = apply_n_skill_advances(start, chars[char_abbr], n_spec)

    details: list[dict[str, Any]] = []
    for t in all_talents:
        d = lookup_talent_detail(core, t)
        details.append(
            {
                "picked": t,
                "name": d.get("name", t),
                "max": d.get("max"),
                "tests": d.get("tests"),
                "effect": d.get("effect"),
            }
        )

    trap_parts = [base_trappings, career.get("trappings", "")]
    trappings = [p.strip() for p in trap_parts if p.strip()]

    display_name = name or "Unnamed"
    return GeneratedCharacter(
        name=display_name,
        species=species_name,
        career=career_name,
        career_class=career_class,
        characteristics=chars,
        initiative=initiative,
        movement=movement,
        wounds=wounds,
        fate=fate,
        resilience=resilience,
        species_skill_advances=species_skill_advances,
        career_skill_advances=career_skill_advances,
        career_char_advances=char_adv,
        skills=final_skills,
        talents=all_talents,
        talent_details=details,
        trappings=trappings,
        status=str(career.get("status", "")),
        notes=species_notes,
        talent_deltas=_summarize_talent_deltas(talent_deltas),
    )


def _summarize_talent_deltas(raw: dict[str, Any]) -> dict[str, Any]:
    """Return a JSON-friendly summary (drop zero characteristic entries)."""
    ch = {k: v for k, v in raw["characteristics"].items() if v}
    out: dict[str, Any] = {}
    if ch:
        out["characteristics"] = ch
    for key in ("wounds", "movement", "initiative", "fate", "resilience"):
        v = int(raw.get(key, 0))
        if v:
            out[key] = v
    return out
