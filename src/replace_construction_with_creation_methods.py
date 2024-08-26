# original code
# Context: many classes were created to simulate the feature present in Java or C++ which allows
# the user to overload the constructor with many diffrent signatures. As it is not natively
# possible in Python, many classes were created.
# Each class instantiates different types of Loan objects depending on the signature.
# It is difficult to the client of the class to know the correct class to use.
class Loan1:
    def __init__(self, commitment, risk_rating, maturity) -> None:
        self.commitment = commitment
        self.risk_rating = risk_rating
        self.maturity = maturity


class Loan2:
    def __init__(self, commitment, risk_rating, maturity, expiricy) -> None:
        self.commitment = commitment
        self.risk_rating = risk_rating
        self.maturity = maturity
        self.expiricy = expiricy


class Loan3:
    def __init__(
        self, commitment, outstanding, risk_rating, maturity, expiricy
    ) -> None:
        self.commitment = commitment
        self.outstanding = outstanding
        self.risk_rating = risk_rating
        self.maturity = maturity
        self.expiricy = expiricy


class Loan4:
    def __init__(
        self, capital_strategy, commitment, risk_rating, maturity, expiricy
    ) -> None:
        self.capital_strategy = capital_strategy
        self.commitment = commitment
        self.risk_rating = risk_rating
        self.maturity = maturity
        self.expiricy = expiricy


class Loan5:
    def __init__(
        self, commitment, outstanding, risk_rating, maturity, expiricy
    ) -> None:
        self.commitment = commitment
        self.risk_rating = risk_rating
        self.maturity = maturity
        self.outstanding = outstanding
        self.expiciry = expiricy


# Refactored code
# Exposes one public class with many methods that returns a Loan object. Each method has meaninful names to help
# the client of the class.
class PublicLoan:

    def __init__(
        self,
        capital_strategy=None,
        commitment=None,
        outstanding=None,
        risk_rating=None,
        maturity=None,
        expiricy=None,
    ) -> None:
        self.capital_strategy = capital_strategy
        self.commitment = commitment
        self.outstanding = outstanding
        self.risk_rating = risk_rating
        self.maturity = maturity
        self.expiricy = expiricy

    def create_term_loan(self, commitment, risk_rating, maturity):
        return PublicLoan(
            capital_strategy=None,
            commitment=commitment,
            outstanding=None,
            risk_rating=risk_rating,
            maturity=maturity,
            expiricy=None,
        )

    def create_term_loan_capital(
        self, capital_strategy, commitment, outstanding, risk_rating, maturity
    ):
        return PublicLoan(
            capital_strategy=capital_strategy,
            commitment=commitment,
            outstanding=outstanding,
            risk_rating=risk_rating,
            maturity=maturity,
            expiricy=None,
        )

    def create_revolver(self, commitment, outstanding, risk_rating, expiricy):
        return PublicLoan(
            capital_strategy=None,
            commitment=commitment,
            outstanding=outstanding,
            risk_rating=risk_rating,
            maturity=None,
            expiricy=expiricy,
        )

    def create_revolver_capital(
        self, capital_strategy, commitment, risk_rating, expiricy
    ):
        return PublicLoan(
            capital_strategy=capital_strategy,
            commitment=commitment,
            outstanding=None,
            risk_rating=risk_rating,
            maturity=None,
            expiricy=expiricy,
        )

    def create_RCTL(self, commitment, outstanding, risk_rating, maturity, expiricy):
        return PublicLoan(
            capital_strategy=None,
            commitment=commitment,
            outstanding=outstanding,
            risk_rating=risk_rating,
            maturity=maturity,
            expiricy=expiricy,
        )

    def create_RCTL(
        self, capital_strategy, commitment, outstanding, risk_rating, maturity, expiricy
    ):
        return PublicLoan(
            capital_strategy=capital_strategy,
            commitment=commitment,
            outstanding=outstanding,
            risk_rating=risk_rating,
            maturity=maturity,
            expiricy=expiricy,
        )


# Variation: if the number of creation methods increases and it distracts the client from the main
# purpose of the class it is interesting to add a Factory class to abstract the construction of the
# main class. The LoanFactory is exposed to the client and has all the methods to create different types
# of Loans. The PrivateLoan class now is responsible just for the Loan actions.
class PrivateLoan:
    def __init__(
        self, capital_strategy, commitment, outstanding, risk_rating, maturity, expiricy
    ) -> None:
        self.capital_strategy = capital_strategy
        self.commitment = commitment
        self.outstanding = outstanding
        self.risk_rating = risk_rating
        self.maturity = maturity
        self.expiricy = expiricy

    def calculate_capital(self, *args, **kwargs):
        # do some Loan calculation #
        pass

    def calculate_income(self, *args, **kwargs):
        pass

    def calculate_ROC(self, *args, **kwargs):
        pass

    def calculate_outstanding(self, *args, **kwargs):
        pass


class LoanFactory:

    def create_term_loan(self, commitment, risk_rating, maturity):
        return PrivateLoan(
            capital_strategy=None,
            commitment=commitment,
            outstanding=None,
            risk_rating=risk_rating,
            maturity=maturity,
            expiricy=None,
        )

    def create_term_loan_capital(
        self, capital_strategy, commitment, outstanding, risk_rating, maturity
    ):
        return PrivateLoan(
            capital_strategy=capital_strategy,
            commitment=commitment,
            outstanding=outstanding,
            risk_rating=risk_rating,
            maturity=maturity,
            expiricy=None,
        )

    def create_revolver(self, commitment, outstanding, risk_rating, expiricy):
        return PrivateLoan(
            capital_strategy=None,
            commitment=commitment,
            outstanding=outstanding,
            risk_rating=risk_rating,
            maturity=None,
            expiricy=expiricy,
        )

    def create_revolver_capital(
        self, capital_strategy, commitment, risk_rating, expiricy
    ):
        return PrivateLoan(
            capital_strategy=capital_strategy,
            commitment=commitment,
            outstanding=None,
            risk_rating=risk_rating,
            maturity=None,
            expiricy=expiricy,
        )

    def create_RCTL(self, commitment, outstanding, risk_rating, maturity, expiricy):
        return PrivateLoan(
            capital_strategy=None,
            commitment=commitment,
            outstanding=outstanding,
            risk_rating=risk_rating,
            maturity=maturity,
            expiricy=expiricy,
        )

    def create_RCTL(
        self, capital_strategy, commitment, outstanding, risk_rating, maturity, expiricy
    ):
        return PrivateLoan(
            capital_strategy=capital_strategy,
            commitment=commitment,
            outstanding=outstanding,
            risk_rating=risk_rating,
            maturity=maturity,
            expiricy=expiricy,
        )
