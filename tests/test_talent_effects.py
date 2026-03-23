from wfrp_chargen.loader import default_data_dir, load_core_pack
from wfrp_chargen.talent_effects import aggregate_talent_modifiers


def test_aggregate_savvy_suave_stacks_int_fel():
    core = load_core_pack(default_data_dir())
    agg = aggregate_talent_modifiers(core, ["Savvy", "Suave"])
    assert agg["characteristics"]["Int"] == 1
    assert agg["characteristics"]["Fel"] == 1
    assert agg["wounds"] == 0


def test_hardy_stacks_wounds():
    core = load_core_pack(default_data_dir())
    agg = aggregate_talent_modifiers(core, ["Hardy", "Hardy"])
    assert agg["wounds"] == 2


def test_catalog_modifiers_override_builtin():
    core = load_core_pack(default_data_dir())
    core.talents_catalog["CustomTestTalent"] = {
        "name": "CustomTestTalent",
        "effect": "test",
        "modifiers": {"characteristics": {"WS": 2}, "wounds": 3},
    }
    agg = aggregate_talent_modifiers(core, ["CustomTestTalent"])
    assert agg["characteristics"]["WS"] == 2
    assert agg["wounds"] == 3
