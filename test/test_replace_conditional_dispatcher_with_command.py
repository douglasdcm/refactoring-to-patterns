from src.replace_conditional_method_with_command import client, client_refac


def test_client():
    expected = "execute new"
    assert client() == expected
    assert client_refac() == expected
