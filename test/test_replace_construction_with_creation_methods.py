from src.replace_construction_with_creation_methods import (
    PublicLoan,
    PrivateLoan,
    LoanFactory,
)


def test_main_refactoring():
    assert isinstance(
        PublicLoan().create_term_loan(
            commitment="any", risk_rating="any", maturity="any"
        ),
        PublicLoan,
    )
    assert isinstance(
        PublicLoan().create_term_loan_capital(
            capital_strategy="any",
            commitment="any",
            outstanding="any",
            risk_rating="any",
            maturity="any",
        ),
        PublicLoan,
    )


def test_refactoring_variation():
    assert isinstance(
        LoanFactory().create_term_loan(
            commitment="any", risk_rating="any", maturity="any"
        ),
        PrivateLoan,
    )
    assert isinstance(
        LoanFactory().create_term_loan_capital(
            capital_strategy="any",
            commitment="any",
            outstanding="any",
            risk_rating="any",
            maturity="any",
        ),
        PrivateLoan,
    )
