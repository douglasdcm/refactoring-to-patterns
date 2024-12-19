from src.move_accumulation_to_visitor import run_refac


def test_run_refac():
    assert run_refac() == (["string"], ["string"])
