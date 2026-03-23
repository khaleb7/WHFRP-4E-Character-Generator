from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from typing import Any


@dataclass
class CoreData:
    species: dict[str, Any]
    species_roll: list[dict[str, Any]]
    careers: dict[str, Any]
    career_tables: dict[str, list[dict[str, Any]]]
    random_talents: dict[str, Any]
    talents_catalog: dict[str, dict[str, Any]]
    extra_talent_blurbs: dict[str, dict[str, Any]] = field(default_factory=dict)


def _read_json(path: str) -> Any:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_core_pack(pack_dir: str) -> CoreData:
    species_doc = _read_json(os.path.join(pack_dir, "species.json"))
    careers_doc = _read_json(os.path.join(pack_dir, "careers.json"))
    tables_doc = _read_json(os.path.join(pack_dir, "career_tables.json"))
    rand_doc = _read_json(os.path.join(pack_dir, "random_talents.json"))
    cat_doc = _read_json(os.path.join(pack_dir, "talents_catalog.json"))

    return CoreData(
        species=species_doc.get("species", {}),
        species_roll=species_doc.get("species_roll", []),
        careers=careers_doc.get("careers", {}),
        career_tables=tables_doc.get("species", {}),
        random_talents=rand_doc,
        talents_catalog=cat_doc.get("talents", {}),
        extra_talent_blurbs=_builtin_career_talent_blurbs(),
    )


def merge_extra_pack(core: CoreData, pack_dir: str) -> None:
    """Merge an expansion pack directory over core (same file names)."""
    for name in ("species.json", "careers.json", "career_tables.json", "random_talents.json", "talents_catalog.json"):
        path = os.path.join(pack_dir, name)
        if not os.path.isfile(path):
            continue
        doc = _read_json(path)
        if name == "species.json":
            core.species.update(doc.get("species", {}))
            if "species_roll" in doc:
                core.species_roll = doc["species_roll"]
        elif name == "careers.json":
            core.careers.update(doc.get("careers", {}))
        elif name == "career_tables.json":
            core.career_tables.update(doc.get("species", {}))
        elif name == "random_talents.json":
            core.random_talents = doc
        elif name == "talents_catalog.json":
            core.talents_catalog.update(doc.get("talents", {}))


def default_data_dir(repo_root: str | None = None) -> str:
    root = repo_root or os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return os.path.join(root, "data", "packs", "core")


def _builtin_career_talent_blurbs() -> dict[str, dict[str, Any]]:
    """Short paraphrases for common career talents not duplicated in JSON."""
    g = "See core rulebook for tests, max, and full wording."
    names = [
        "Concoct",
        "Craftsman (Apothecary)",
        "Etiquette (Scholar)",
        "Artist",
        "Gunner",
        "Tinker",
        "Blather",
        "Speedreader",
        "Bless (Any)",
        "Stone Soup",
        "Panhandle",
        "Bookish",
        "Field Dressing",
        "Strike to Stun",
        "Holy Visions",
        "Carouser",
        "Super Numerate",
        "Aethyric Attunement",
        "Petty Magic (Any)",
        "Second Sight",
        "Gregarious",
        "Craftsman (Any)",
        "Strong Back",
        "Very Strong",
        "Resistance (Disease)",
        "Very Resilient",
        "Alley Cat",
        "Beneath Notice",
        "Dealmaker",
        "Strike Mighty Blow",
        "Night Vision",
        "Etiquette (Servants)",
        "Drilled",
        "Tenacious",
        "Etiquette (Any)",
        "Beat Blade",
        "Distract",
        "Feint",
        "Step Aside",
        "Etiquette (Nobles)",
        "Noble Blood",
        "Strong-minded",
        "Menacing",
        "Shadow",
        "Embezzle",
        "Numismatics",
        "Strider (Woodlands)",
        "Strider (Any)",
        "Trapper",
        "Break and Enter",
        "Animal Affinity",
        "Seasoned Traveller",
        "Trick-Riding",
        "Public Speaking",
        "Berserk Charge",
        "Frenzy",
        "Fleet Footed",
        "Sprinter",
        "Fisherman",
        "Marksman",
        "Coolheaded",
        "Resolute",
        "Dirty Fighting",
        "Strong Swimmer",
        "Waterman",
        "Criminal",
        "Combat Aware",
        "Etiquette (Criminals)",
        "Crack the Whip",
        "Lightning Reflexes",
        "Roughrider",
        "Diceman",
        "Warrior Born",
        "Infighter",
        "Iron Jaw",
        "Reversal",
        "Dirty Fighting",
        "Dual Wielder",
        "Fearless (Everything)",
        "Slayer",
        "Etiquette (Cultists)",
        "Cardsharp",
        "Diceman",
        "Etiquette (Any)",
        "Witch!",
        "Petty Magic",
    ]
    out: dict[str, dict[str, Any]] = {}
    for n in names:
        out[n] = {"name": n, "max": "varies", "tests": "varies", "effect": g}
    return out


def lookup_talent_detail(core: CoreData, display_name: str) -> dict[str, Any]:
    if display_name in core.talents_catalog:
        return dict(core.talents_catalog[display_name])
    for _k, v in core.talents_catalog.items():
        if isinstance(v, dict) and v.get("name") == display_name:
            return dict(v)
    if display_name in core.extra_talent_blurbs:
        return dict(core.extra_talent_blurbs[display_name])
    return {"name": display_name, "max": "?", "tests": "?", "effect": "See core rulebook."}
