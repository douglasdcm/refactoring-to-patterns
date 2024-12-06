from src.replace_implicit_language_with_interpreter import client


def test_run_refac():
    assert client() == [1, 1, 1, 0, 0, 1, 2, 2]
