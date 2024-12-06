from src.replace_type_code_with_class import client


def test_run_refac():
    assert client() == ("CLAIMED", "CLAIMED")
