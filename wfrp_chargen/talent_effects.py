from __future__ import annotations

from typing import Any

from wfrp_chargen.loader import CoreData, lookup_talent_detail

_CHAR_KEYS = ["WS", "BS", "S", "T", "I", "Ag", "Dex", "Int", "WP", "Fel"]

# Resolved talent display name -> mechanical deltas (core rulebook style; confirm at your table).
_BUILTIN: dict[str, dict[str, Any]] = {
    "Savvy": {"characteristics": {"Int": 1}},
    "Suave": {"characteristics": {"Fel": 1}},
    "Coolheaded": {"characteristics": {"WP": 1}},
    "Lightning Reflexes": {"characteristics": {"Ag": 1}},
    "Nimble Fingered": {"characteristics": {"Dex": 1}},
    "Sturdy": {"characteristics": {"T": 1}},
    "Very Resilient": {"characteristics": {"T": 1}},
    "Very Strong": {"characteristics": {"S": 1}},
    "Warrior Born": {"characteristics": {"WS": 1}},
    "Hardy": {"wounds": 1},
    "Strong Legs": {"movement": 1},
    "Quick Witted": {"initiative": 1},
    "Luck": {"fate": 1},
    "Iron Jaw": {"characteristics": {"T": 1}},
    "Strong-minded": {"characteristics": {"WP": 1}},
    "Resolute": {"characteristics": {"WP": 1}},
    "Artistic": {"characteristics": {"Dex": 1}},
    "Craftsman (Any)": {"characteristics": {"Dex": 1}},
    "Craftsman (Apothecary)": {"characteristics": {"Dex": 1}},
    "Super Numerate": {"characteristics": {"Int": 1}},
    "Noble Blood": {"characteristics": {"Fel": 1}},
    "Fleet Footed": {"movement": 1},
    "Sprinter": {"movement": 1},
}


def _empty_aggregate() -> dict[str, Any]:
    return {
        "characteristics": {k: 0 for k in _CHAR_KEYS},
        "wounds": 0,
        "movement": 0,
        "initiative": 0,
        "fate": 0,
        "resilience": 0,
    }


def _normalize_modifiers(raw: dict[str, Any]) -> dict[str, Any] | None:
    if not raw:
        return None
    out = _empty_aggregate()
    ch = raw.get("characteristics") or raw.get("chars")
    if isinstance(ch, dict):
        for k, v in ch.items():
            kk = str(k)
            if kk in out["characteristics"]:
                out["characteristics"][kk] += int(v)
    for key in ("wounds", "movement", "initiative", "fate", "resilience"):
        if key in raw and raw[key] is not None:
            out[key] += int(raw[key])
    if any(out["characteristics"].values()) or sum(out[k] for k in ("wounds", "movement", "initiative", "fate", "resilience")):
        return out
    return None


def _piece_from_builtin(name: str) -> dict[str, Any] | None:
    b = _BUILTIN.get(name.strip())
    if not b:
        return None
    out = _empty_aggregate()
    if "characteristics" in b:
        for k, v in b["characteristics"].items():
            if k in out["characteristics"]:
                out["characteristics"][k] += int(v)
    for key in ("wounds", "movement", "initiative", "fate", "resilience"):
        if key in b:
            out[key] += int(b[key])
    return out


def talent_piece(core: CoreData, talent_display_name: str) -> dict[str, Any] | None:
    detail = lookup_talent_detail(core, talent_display_name)
    mod = detail.get("modifiers")
    if isinstance(mod, dict):
        n = _normalize_modifiers(mod)
        if n:
            return n
    return _piece_from_builtin(talent_display_name)


def merge_talent_pieces(target: dict[str, Any], piece: dict[str, Any]) -> None:
    for k in _CHAR_KEYS:
        target["characteristics"][k] += piece["characteristics"].get(k, 0)
    for key in ("wounds", "movement", "initiative", "fate", "resilience"):
        target[key] += piece[key]


def aggregate_talent_modifiers(core: CoreData, talent_names: list[str]) -> dict[str, Any]:
    agg = _empty_aggregate()
    for name in talent_names:
        piece = talent_piece(core, name)
        if piece:
            merge_talent_pieces(agg, piece)
    return agg
