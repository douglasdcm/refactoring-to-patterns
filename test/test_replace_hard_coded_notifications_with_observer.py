from src.replace_hard_coded_notifications_with_observer import client, client_refac


def test_client():
    expected = ("F", "E")
    assert client() == expected
    assert client_refac() == expected
