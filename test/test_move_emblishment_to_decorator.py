from src.move_emblishment_to_decorator import run_refac


def test_refac():
    assert run_refac() == ("any", "any __decoded__")
