"""
Build NightCafe-friendly text prompts for character portraits from chargen output.

NightCafe / SD-style prompts work well with: subject + setting + style + quality tokens,
comma-separated. See README for suggested negative prompts.
"""
from __future__ import annotations

import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wfrp_chargen.generator import GeneratedCharacter

from wfrp_chargen.dice import bonus_tens


# Species -> short visual descriptors (Old World / WFRP tone)
_SPECIES_BITS: dict[str, str] = {
    "Human (Reiklander)": "human, adult, Reikland Empire citizen, medieval Germanic fantasy",
    "Dwarf": "fantasy dwarf, stocky broad build, thick beard, dwarf proportions",
    "Halfling": "halfling, small stature, round friendly features, hairy feet, cozy rustic",
    "High Elf": "high elf, tall slender, pointed ears, elegant aloof bearing, Ulthuan aesthetic",
    "Wood Elf": "wood elf, pointed ears, wild forest ranger look, weathered, Athel Loren",
}

# Talents that suggest visible traits (name substring match, lowercased)
_TALENT_VISUAL_HINTS: list[tuple[str, str]] = [
    ("attractive", "striking pleasant features"),
    ("acute sense (sight)", "sharp perceptive eyes"),
    ("acute sense (taste)", "expressive refined face"),
    ("acute sense", "alert attentive expression"),
    ("night vision", "unusually clear eyes, faintly luminous catchlight"),
    ("nimble fingered", "nimble dexterous hands"),
    ("very strong", "obvious muscular build"),
    ("warrior born", "battle-hardened bearing"),
    ("doomed", "subtle haunted weary look"),
    ("small", "noticeably short halfling proportions"),
    ("slayer", "dramatic orange mohawk, bare torso, tattoos, grim intensity"),
    ("witch", "wild unsettling presence, talismans"),
    ("wizard", "scholarly arcane bearing"),
    ("noble blood", "aristocratic bearing"),
    ("artistic", "creative refined appearance"),
]

_DEFAULT_STYLE = (
    "character portrait, bust and shoulders, facing viewer, "
    "Warhammer Fantasy Old World, grimdark low fantasy, "
    "detailed face, cinematic lighting, "
    "oil painting style, historical fantasy illustration, "
    "muted earthy colors, slight dirt and wear"
)

_DEFAULT_NEGATIVE = (
    "anime, cartoon, chibi, child, modern clothing, sci-fi, clean studio photo, "
    "oversaturated, watermark, text, logo, extra limbs, deformed hands"
)


def _species_line(species: str) -> str:
    return _SPECIES_BITS.get(species, species.replace("(", "").replace(")", ""))


def _career_line(career: str, career_class: str) -> str:
    return f"profession: {career}, {career_class} class, Reikland / Old World setting"


def _status_line(status: str) -> str:
    s = status.strip()
    if not s:
        return ""
    return f"social station and dress: {s}"


def _stats_appearance(ch: "GeneratedCharacter") -> str:
    """Rough physique/expression from characteristic bonuses (fantasy shorthand)."""
    parts: list[str] = []
    sb = bonus_tens(ch.characteristics["S"])
    tb = bonus_tens(ch.characteristics["T"])
    fel_b = bonus_tens(ch.characteristics["Fel"])
    int_b = bonus_tens(ch.characteristics["Int"])
    ws_b = bonus_tens(ch.characteristics["WS"])

    if sb >= 4:
        parts.append("powerfully built")
    elif sb >= 3:
        parts.append("solid sturdy frame")
    elif sb <= 1:
        parts.append("slight lean build")

    if tb >= 4:
        parts.append("rugged hardy constitution")
    elif tb <= 1:
        parts.append("slender delicate frame")

    if fel_b >= 4:
        parts.append("warm commanding charisma")
    elif fel_b >= 3:
        parts.append("approachable confident expression")

    if int_b >= 4:
        parts.append("sharp intelligent gaze")
    elif int_b <= 1:
        parts.append("simple honest expression")

    if ws_b >= 4:
        parts.append("fighter's stance and scars possible")

    if not parts:
        parts.append("average build for their kind")
    return ", ".join(parts)


def _trappings_visual(trappings: list[str]) -> str:
    if not trappings:
        return ""
    raw = "; ".join(trappings)
    raw = _asciiish(raw)
    # Keep prompt length reasonable; strip dice notation clutter
    raw = re.sub(r"\b\d+d\d+\b", "some", raw, flags=re.I)
    raw = re.sub(r"\s+", " ", raw).strip()
    if len(raw) > 320:
        raw = raw[:317] + "..."
    return f"visible gear and clothing: {raw}"


def _asciiish(s: str) -> str:
    return (
        s.replace("\u2014", "-")
        .replace("\u2013", "-")
        .replace("\u00a0", " ")
    )


def _talent_visuals(talents: list[str]) -> str:
    hints: list[str] = []
    low = [t.lower() for t in talents]
    for needle, hint in _TALENT_VISUAL_HINTS:
        n = needle.lower()
        for t in low:
            if n in t:
                if hint not in hints:
                    hints.append(hint)
                break
    return ", ".join(hints)


def nightcafe_portrait_prompt(ch: "GeneratedCharacter") -> dict[str, str]:
    """
    Return NightCafe-oriented strings: ``prompt`` (main positive) and ``negative_prompt``.
    """
    chunks: list[str] = [
        _species_line(ch.species),
        _career_line(ch.career, ch.career_class),
        _stats_appearance(ch),
    ]
    st = _status_line(ch.status)
    if st:
        chunks.append(st)
    tv = _talent_visuals(ch.talents)
    if tv:
        chunks.append(tv)
    trap = _trappings_visual(ch.trappings)
    if trap:
        chunks.append(trap)
    chunks.append(f"named character concept: {ch.name}")
    chunks.append(_DEFAULT_STYLE)

    prompt = ", ".join(c for c in chunks if c)
    return {
        "prompt": prompt,
        "negative_prompt": _DEFAULT_NEGATIVE,
    }


def format_nightcafe_block(ch: "GeneratedCharacter") -> str:
    """Multi-line block for terminal output."""
    d = nightcafe_portrait_prompt(ch)
    lines = [
        "-" * 72,
        "NightCafe portrait (copy positive into your creation; negative into advanced options):",
        "",
        "POSITIVE:",
        d["prompt"],
        "",
        "NEGATIVE:",
        d["negative_prompt"],
        "-" * 72,
    ]
    return "\n".join(lines)
