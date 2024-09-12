from src.replace_stat_altering_conditionals_with_state import run_refac, run_original


def test_refac():
    expected = ("CLAIMED", "UNIX_CLAIMED")
    assert run_original() == expected
    assert run_refac() == expected
