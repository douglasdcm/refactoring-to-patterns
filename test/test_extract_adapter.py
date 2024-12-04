from src.extract_adapter import run_refac


def test_run_refac():
    assert run_refac() == ("done", "done", "done")
