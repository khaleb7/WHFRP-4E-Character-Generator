from wfrp_chargen.generator import generate_character
from wfrp_chargen.loader import default_data_dir, load_core_pack
from wfrp_chargen.portrait_prompt import nightcafe_portrait_prompt


def test_portrait_prompt_contains_species_and_style():
    core = load_core_pack(default_data_dir())
    ch = generate_character(core, name="Test Character")
    assert ch.nightcafe_portrait_prompt
    assert ch.nightcafe_negative_prompt
    p = ch.nightcafe_portrait_prompt.lower()
    assert "warhammer" in p or "old world" in p
    assert "human" in p or "dwarf" in p or "halfling" in p or "elf" in p


def test_nightcafe_dict_keys():
    core = load_core_pack(default_data_dir())
    ch = generate_character(core, name="X")
    d = nightcafe_portrait_prompt(ch)
    assert set(d.keys()) == {"prompt", "negative_prompt"}
