from __future__ import annotations

from wfrp_chargen.dice import bonus_tens
from wfrp_chargen.generator import CHAR_ORDER, GeneratedCharacter
from wfrp_chargen.portrait_prompt import format_nightcafe_block


def _ascii_console(s: str) -> str:
    return (
        s.replace("\u2014", "-")
        .replace("\u2013", "-")
        .replace("\u2022", "-")
        .replace("\u00a0", " ")
    )


def format_character(ch: GeneratedCharacter, include_portrait: bool = True) -> str:
    lines: list[str] = []
    lines.append("=" * 72)
    lines.append(_ascii_console(f"Name: {ch.name}"))
    lines.append(_ascii_console(f"Species: {ch.species}   Career: {ch.career} ({ch.career_class})"))
    lines.append(_ascii_console(f"Status: {ch.status}"))
    lines.append("-" * 72)
    stat_bits = []
    for abbr in CHAR_ORDER:
        v = ch.characteristics[abbr]
        stat_bits.append(f"{abbr} {v} / {bonus_tens(v)}")
    lines.append("Characteristics: " + "  ".join(stat_bits))
    lines.append(
        f"Movement: {ch.movement}   Initiative: {ch.initiative}   Wounds: {ch.wounds}   "
        f"Fate: {ch.fate}   Resilience: {ch.resilience}"
    )
    if ch.talent_deltas:
        lines.append("Talent modifiers applied to sheet (characteristics / wounds / etc.):")
        td = ch.talent_deltas
        if "characteristics" in td:
            parts = [f"{k} {v:+d}" for k, v in sorted(td["characteristics"].items())]
            lines.append("  Stats: " + ", ".join(parts))
        for key in ("wounds", "movement", "initiative", "fate", "resilience"):
            if key in td and td[key]:
                lines.append(f"  {key.capitalize()}: {td[key]:+d}")
    lines.append("-" * 72)
    if ch.notes:
        lines.append("Species notes:")
        for n in ch.notes:
            lines.append(f"  - {n}")
        lines.append("-" * 72)
    lines.append("Skills (species + career advances; bases use final characteristics including talents):")
    for sk in sorted(ch.skills.keys()):
        lines.append(_ascii_console(f"  {sk}: {ch.skills[sk]}%"))
    lines.append("-" * 72)
    lines.append("Characteristic advances spent (career pool: 5 on advance list):")
    for k, v in sorted(ch.career_char_advances.items()):
        if v:
            lines.append(f"  {k}: +{v}")
    lines.append("Skill advances (career pool: 40, max 10/skill):")
    for k, v in sorted(ch.career_skill_advances.items()):
        if v:
            lines.append(f"  {k}: +{v} advances")
    lines.append("Species skill advances (3x5 + 3x3 advances):")
    for k, v in sorted(ch.species_skill_advances.items()):
        if v:
            lines.append(f"  {k}: +{v} advances")
    lines.append("-" * 72)
    lines.append("Trappings:")
    lines.append(_ascii_console("  " + "; ".join(ch.trappings)))
    lines.append("-" * 72)
    lines.append("Talents (with summary):")
    for row in ch.talent_details:
        lines.append(_ascii_console(f"  - {row['picked']}"))
        lines.append(_ascii_console(f"      Max: {row.get('max')}   Tests: {row.get('tests')}"))
        lines.append(_ascii_console(f"      {row.get('effect')}"))
    lines.append("=" * 72)
    if include_portrait:
        lines.append(format_nightcafe_block(ch))
    return "\n".join(lines)
