from src.replace_implict_tree_with_composite import client, client_refac


def test_client():
    expected = "<orders><order id='order-0'>the order0</order><order id='order-1'>the order1</order></orders>"
    assert client() == expected
    assert client_refac() == expected
