"""
Build NightCafe-friendly text prompts for character portraits from chargen output.

NightCafe / SD-style prompts work well with: subject + gender + trappings + background + style.
See README for suggested negative prompts.
"""
from __future__ import annotations

import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wfrp_chargen.generator import GeneratedCharacter

from wfrp_chargen.dice import bonus_tens

# Species -> fragment used after gender (when not using full human line)
_SPECIES_SUBJECT: dict[str, str] = {
    "Human (Reiklander)": "Reiklander human",
    "Dwarf": "dwarf",
    "Halfling": "halfling",
    "High Elf": "high elf",
    "Wood Elf": "wood elf",
}

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

# career_class -> wealth tier -> background (environment matches social station)
_CLASS_BACKDROP: dict[str, dict[str, str]] = {
    "Academics": {
        "brass": "cramped garret study, chipped desk, single tallow candle, cheap parchment, plaster cracks",
        "silver": "respectable townhouse study, filled bookshelves, inkwell and quill, tall window with city view",
        "gold": "grand library or collegiate hall, marble or carved wood, tall windows, lectern, scholarly opulence",
        "unknown": "quiet interior with books, writing tools, and academic clutter",
    },
    "Burghers": {
        "brass": "crowded workshop or market stall corner, tools and sawdust, worn timber, busy street glimpsed",
        "silver": "merchant house room, counting desk, scales, ledger, neat bourgeois order",
        "gold": "guild hall or fine shop interior, carved wood, brass fixtures, prosperity on display",
        "unknown": "urban Reikland interior, trade and craft cues, modest prosperity",
    },
    "Courtiers": {
        "brass": "servants' passage or modest court outbuilding, plain livery hook, unadorned stone",
        "silver": "antechamber with modest heraldic motif, polished floor, waiting bench",
        "gold": "palace gallery or ballroom edge, marble, painted ceiling, banners and heraldry, aristocratic splendor",
        "unknown": "courtly interior suggesting rank without extreme wealth",
    },
    "Peasants": {
        "brass": "mud-flecked village lane, thatched roofs blurred behind, subsistence rural poverty",
        "silver": "village square or better croft, cleaner timber, small garden or well",
        "gold": "prosperous farmstead porch or bailiff's timber hall, well-kept rural wealth",
        "unknown": "Old World rural backdrop, fields or village, honest soil and weather",
    },
    "Rangers": {
        "brass": "campfire embers, rolled bedroll, forest edge at dusk, mud on boots",
        "silver": "roadside post or toll shelter, maintained gear rack, cleared path visible",
        "gold": "captain's tent flap or warden lodge, maps, quality leather, command of the wilds",
        "unknown": "wilderness margin, road or trail, travel kit and weathered gear",
    },
    "Riverfolk": {
        "brass": "slick river dock planks, coiled rope, river mist, tar and timber",
        "silver": "wharf office or boatyard shed, tariff slate, oars and tackle orderly",
        "gold": "river guild or pilot house interior, brass instruments, paneled walls, river wealth",
        "unknown": "Reikland riverfront atmosphere, water and wood, labor and tide",
    },
    "Rogues": {
        "brass": "narrow rain-slick alley, weak torch, broken cobbles, criminal desperation",
        "silver": "back-room parlor, gaming table, velvet worn at edges, respectable vice",
        "gold": "well-appointed study with a crooked smile, stolen luxuries hinted, urbane crime",
        "unknown": "urban shadows, Old World city grit, closed doors and secrets",
    },
    "Warriors": {
        "brass": "militia yard or levy field, practice post, mud, cheap arms rack",
        "silver": "stone barracks interior, clean kit lines, regimented order",
        "gold": "knight's hall or officer pavilion silk, ancestral shield on wall, command presence",
        "unknown": "military or martial backdrop, steel and discipline, Empire soldiery",
    },
}

_DEFAULT_STYLE = (
    "character portrait, bust and shoulders, subject in foreground sharp, "
    "background softly focused but readable, "
    "Warhammer Fantasy Old World, grimdark low fantasy, "
    "detailed face, cinematic lighting, "
    "oil painting style, historical fantasy illustration, "
    "muted earthy colors, slight dirt and wear"
)

_DEFAULT_NEGATIVE = (
    "anime, cartoon, chibi, child, modern clothing, sci-fi, clean studio photo, "
    "oversaturated, watermark, text, logo, extra limbs, deformed hands, "
    "blank white background, plain backdrop"
)


def _parse_wealth_tier(status: str) -> str:
    u = status.upper()
    if "GOLD" in u:
        return "gold"
    if "SILVER" in u:
        return "silver"
    if "BRASS" in u:
        return "brass"
    return "unknown"


def _social_class_background(career_class: str, status: str) -> str:
    tier = _parse_wealth_tier(status)
    by_class = _CLASS_BACKDROP.get(career_class)
    if not by_class:
        return (
            f"background environment reflecting {career_class} station and Old World society, "
            f"wealth hint from status: {status or 'unspecified'}"
        )
    line = by_class.get(tier) or by_class.get("unknown", "")
    status_bit = _asciiish(status.strip()) if status.strip() else "ordinary station"
    return (
        f"BACKGROUND (match social class): {line}. "
        f"Overall tone fits Empire status '{status_bit}' — environment must not look wealthier than their tier."
    )


def _gender_species_subject(gender: str, species: str) -> str:
    g = (gender or "nonbinary").lower().strip()
    if g not in ("woman", "man", "nonbinary"):
        g = "nonbinary"
    sp = _SPECIES_SUBJECT.get(species, species.replace("(", "").replace(")", "").strip().lower())

    if species == "Dwarf":
        if g == "woman":
            return (
                "SUBJECT: portrait of an adult dwarf woman, fantasy dwarf anatomy, "
                "facial hair or braided beard as you prefer for dwarf women, sturdy features"
            )
        if g == "man":
            return "SUBJECT: portrait of an adult dwarf man, full thick beard, fantasy dwarf anatomy, sturdy features"
        return (
            "SUBJECT: portrait of an adult dwarf, androgynous or ambiguous gender presentation, "
            "fantasy dwarf anatomy, styled facial hair optional"
        )

    if species == "Halfling":
        if g == "woman":
            return "SUBJECT: portrait of an adult female halfling, small stature, warm homely features, hairy feet implied"
        if g == "man":
            return "SUBJECT: portrait of an adult male halfling, small stature, cheerful rustic features, hairy feet implied"
        return "SUBJECT: portrait of an adult halfling, androgynous presentation, small stature, rustic halfling features"

    if species == "High Elf":
        if g == "woman":
            return "SUBJECT: portrait of an adult high elf woman, pointed ears, tall elegant features, aloof Ulthuan bearing"
        if g == "man":
            return "SUBJECT: portrait of an adult high elf man, pointed ears, tall elegant features, aloof Ulthuan bearing"
        return "SUBJECT: portrait of an adult high elf, androgynous elegant features, pointed ears"

    if species == "Wood Elf":
        if g == "woman":
            return "SUBJECT: portrait of an adult wood elf woman, pointed ears, weathered forest ranger beauty"
        if g == "man":
            return "SUBJECT: portrait of an adult wood elf man, pointed ears, weathered forest ranger look"
        return "SUBJECT: portrait of an adult wood elf, androgynous wild features, pointed ears"

    # Human (Reiklander)
    if g == "woman":
        return "SUBJECT: portrait of an adult Reiklander human woman, Empire citizen, medieval Germanic fantasy"
    if g == "man":
        return "SUBJECT: portrait of an adult Reiklander human man, Empire citizen, medieval Germanic fantasy"
    return (
        "SUBJECT: portrait of an adult Reiklander human, androgynous gender presentation, "
        "Empire citizen, medieval Germanic fantasy"
    )


def _stats_appearance(ch: "GeneratedCharacter") -> str:
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
    return "face and body: " + ", ".join(parts)


def _clean_trapping_text(s: str) -> str:
    raw = _asciiish(s.strip())
    raw = re.sub(r"\b\d+d\d+\b", "several", raw, flags=re.I)
    raw = re.sub(r"\s+", " ", raw).strip()
    return raw


def _trappings_detailed(trappings: list[str]) -> str:
    """Explicit trapping list for the image model — class gear vs career gear."""
    if not trappings:
        return ""
    labels = [
        "CLOTHING AND BASE KIT (species or starting class)",
        "CAREER TRAPPINGS AND TOOLS (clearly worn, held, or strapped on)",
    ]
    parts: list[str] = []
    for i, raw in enumerate(trappings):
        lab = labels[i] if i < len(labels) else f"ADDITIONAL GEAR ({i + 1})"
        cleaned = _clean_trapping_text(raw)
        if not cleaned:
            continue
        parts.append(f"{lab}: {cleaned}")
    if not parts:
        return ""
    joined = ". ".join(parts)
    max_len = 900
    if len(joined) > max_len:
        joined = joined[: max_len - 3] + "..."
    return (
        "TRAPPINGS (render faithfully, not generic fantasy armor): "
        + joined
        + ". Every trapping listed should appear in the frame or on the body."
    )


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
    if not hints:
        return ""
    return "notable appearance from talents: " + ", ".join(hints)


def nightcafe_portrait_prompt(ch: "GeneratedCharacter") -> dict[str, str]:
    """
    Return NightCafe-oriented strings: ``prompt`` (main positive) and ``negative_prompt``.
    """
    chunks: list[str] = [
        _gender_species_subject(ch.gender, ch.species),
        _social_class_background(ch.career_class, ch.status),
        _trappings_detailed(ch.trappings),
        f"profession: {ch.career}, {ch.career_class} class, Reikland / Old World",
        _stats_appearance(ch),
    ]
    if ch.status.strip():
        chunks.append(f"in-world rank title: {_asciiish(ch.status.strip())}")
    tv = _talent_visuals(ch.talents)
    if tv:
        chunks.append(tv)
    chunks.append(f"character name (concept only, do not paint text): {ch.name}")
    chunks.append(_DEFAULT_STYLE)

    prompt = ". ".join(c for c in chunks if c)
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
