from src.unify_interfaces_with_adapter import client, client_refac


def test_client():
    expected = ("add dom below", "add xml")
    assert client() == expected
    assert client_refac() == expected
