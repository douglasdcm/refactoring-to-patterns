from src.form_template_method import client, client_refac


def test_clinte():
    expected = 6
    assert client() == expected
    assert client_refac() == expected
