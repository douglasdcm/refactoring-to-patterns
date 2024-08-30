from src.replace_conditional_logic_with_strategy import (
    LoanRefac,
)


def test_refac():
    loan = LoanRefac.new_advised_line()
    assert loan.capital() == 1
