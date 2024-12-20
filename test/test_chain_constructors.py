from src.chain_constructors import run_refac


def test_run_refac():
    l1, l2 = run_refac()
    assert l1._notional == l2._notional
    assert l1._outstanding == l2._outstanding
    assert l1._expiricy == l1._expiricy
