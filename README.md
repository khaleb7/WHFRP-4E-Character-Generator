# WHFRP 4E Character Generator

Python 3 generator for **Warhammer Fantasy Roleplay 4th edition** using a **data pack** layout so you can add careers, species tables, talents, and random tables from other books without rewriting the engine.

## Development

This project was built with **Cursor-driven development**: requirements, architecture, and large refactors were iterated using [Cursor](https://cursor.com) (AI-assisted planning and coding). Git history and tests document *what* shipped; the **product plan** for scope and future updates lives in the repo at **[docs/PLAN_WFRP4e_Chargen.md](docs/PLAN_WFRP4e_Chargen.md)**. Update that file when you change goals or layout so the next pass (human or AI) starts from the same page.

## Quick start

```bash
pip install -r requirements.txt
python -m wfrp_chargen
python -m wfrp_chargen --seed 42 --json
```

- **Text sheet (default):** human-readable output with **talent summaries** (paraphrased mechanics; confirm against your rulebook).
- **`--json`:** machine-readable character (same data).
- **NightCafe portrait prompts:** each run appends a **positive** and **negative** prompt tailored to species, career, rough build from stats, notable talents, trappings, and grimdark Old World style. Use with [NightCafe](https://creator.nightcafe.studio/) or any SD-compatible tool.

```bash
python -m wfrp_chargen --portrait-only --seed 1    # prompts only, easy to copy-paste
python -m wfrp_chargen --no-portrait             # full sheet without portrait block
```

JSON includes `nightcafe_portrait_prompt` and `nightcafe_negative_prompt` unless `--no-portrait` is set. Customize wording in [`wfrp_chargen/portrait_prompt.py`](wfrp_chargen/portrait_prompt.py).

## Layout

- [docs/PLAN_WFRP4e_Chargen.md](docs/PLAN_WFRP4e_Chargen.md) — saved product plan for future updates (Cursor-originated; edit in-repo).
- `wfrp_chargen/` — engine (rolls, species/career resolution, advance allocation, formatting, [`portrait_prompt.py`](wfrp_chargen/portrait_prompt.py) for NightCafe).
- `data/packs/core/` — core JSON: `species.json`, `careers.json`, `career_tables.json`, `random_talents.json`, `talents_catalog.json`.
- `scripts/extract_rulebook_text.py` — optional PDF text extraction for comparing tables to JSON.
- `scripts/build_core_data.py` — rebuild `career_tables.json` (validated d100 coverage).
- `scripts/export_careers_json.py` — rebuild `careers.json` from the embedded career table.
- `WFRP.py` — legacy Python 2 script (superseded by `wfrp_chargen`).

## Rulebook PDF helper

Set **`WFRP_RULEBOOK_PDF`** to your local PDF (for example `z:\gback\wf.pdf`), install `pypdf`, then extract pages for manual diff against the JSON:

```bash
set WFRP_RULEBOOK_PDF=z:\gback\wf.pdf
python scripts/extract_rulebook_text.py --pages 120-135 --out build/snippet.txt
```

## Adding another book (expansion pack)

Create `data/packs/<id>/` with any of the same filenames. Merge at runtime:

```bash
python -m wfrp_chargen --extra-pack data\packs\my_expansion
```

Merge rules (see `loader.merge_extra_pack`):

- `species.json` — species entries and optional replacement `species_roll`.
- `careers.json` — careers merged **by career name** (later pack wins).
- `career_tables.json` — species tables merged **by species key**.
- `random_talents.json` — replaces the previous random table document (use a new `table_id` if you add alternate tables; engine currently uses `core_random_talents`).
- `talents_catalog.json` — merged **by talent id / key**.

## Tests

```bash
pytest tests -q
```

## What gets randomized (core)

- d100 **species**, d100 **career** (per species table).
- **Characteristics:** 2d10+20 each, then **species modifiers** (clamped).
- **Career:** 5 characteristic advances across the career’s three advance stats; **40** skill advances across **8** class skills (**max 10** each); **one** career talent from four options.
- **Species skills:** six distinct species skills get **3×5** and **3×3** advances (as `+3%` steps per advance per core skill rules).
- **Species talents:** fixed, random-table rolls, and **OR** choices resolved at random.
- **Wounds:** `Strength Bonus + 2×Toughness Bonus + Willpower Bonus`, plus species **flat** adjust; Halfling **Small** subtracts **Strength Bonus** again (per species data).
- **Initiative (sheet line):** `Agility Bonus + Intelligence Bonus + species initiative_bonus` (elf line uses the `initiative_bonus` field for the +20 case).

### Talent modifiers (automatic)

Recognized talents apply **characteristic bumps**, **+Wounds**, **+Movement**, **+Initiative**, **+Fate**, etc.:

- Built-in map: [`wfrp_chargen/talent_effects.py`](wfrp_chargen/talent_effects.py) (by resolved talent **name**).
- Optional override in [`data/packs/core/talents_catalog.json`](data/packs/core/talents_catalog.json): add `"modifiers": {"characteristics": {"Int": 1}, "wounds": 1}` (same shape as built-ins).

**Wounds** use the formula with **final** characteristics (after talent stat bumps), then add extra wound pips from **Hardy** / `modifiers.wounds`. **Skills** start from **final** characteristics before advances. The text sheet lists **talent_deltas** so you can see what was applied. Purely situational talents stay description-only until you extend the map or JSON.

## License

See [LICENSE](LICENSE). Game mechanics are the property of their respective rights holders; JSON summaries are paraphrases for personal play aids.
