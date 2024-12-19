import pytest
from src.introduce_null_object import run_refac


def test_refac():
    n1, n2, n3 = run_refac()
    assert n1.move_down()
    assert n2.move_down()
    with pytest.raises(NotImplementedError):
        assert n3.move_down()
