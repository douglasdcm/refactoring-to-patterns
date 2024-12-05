from src.replace_implicit_language_with_interpreter import client


def test_run_refac():
    assert client() == (2, 2)
