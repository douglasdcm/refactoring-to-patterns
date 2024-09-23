# Orginal code
# There is some code duplication classes CapitalStrategyAdiviseLine and CapitalStrategyTermLoan.
class Loan:
    def get_commitment(self) -> float:
        return 2

    def get_unused_percentage(self) -> float:
        return 3


class CapitalStrategy:
    def capital(self, loan: Loan) -> float:
        return 1

    def duration(self, loan: Loan) -> float:
        return 1

    def risk_factor_for(self, loan: Loan) -> float:
        return 1


class CapitalStrategyAdiviseLine(CapitalStrategy):
    def capital(self, loan: Loan) -> float:
        return (
            loan.get_commitment()
            * loan.get_unused_percentage()
            * self.duration(loan)
            * self.risk_factor_for(loan)
        )


class CapitalStategyTermLoan(CapitalStrategy):
    def capital(self, loan: Loan) -> float:
        return loan.get_commitment() * self.duration(loan) * self.risk_factor_for(loan)

    def duration(self, loan: Loan) -> float:
        pass


def client():
    loan = Loan()
    capital = CapitalStrategyAdiviseLine()
    return capital.capital(loan)


# Refactored code
# Moved the basic logic to the CapitaStrategy. Each part of the formula is calculated
# by a function that returns numerical values. The default value returned is 1, so that
# if the method in not overriden by the subclass, then this method does not impacts the
# final result
class LoanRefac:
    def get_commitment(self):
        return 2

    def get_unused_percentage(self):
        return 3


class CapitalStrategyRefac:
    # Template method withe the structure pf the calculation
    def capital(self, loan: LoanRefac) -> float:
        return (
            self.risk_amount_for(loan)
            * self.duration(loan)
            * self.risk_factor_for(loan)
        )

    # default value in case he function is not overriden
    def duration(self, loan: LoanRefac):
        return 1

    def risk_factor_for(self, loan: LoanRefac):
        return 1

    def risk_amount_for(self, loan: LoanRefac):
        return 1


class CapitalStrategyAdiviseLineRefac(CapitalStrategyRefac):
    # Overrides part of the calculation
    def risk_amount_for(self, loan: LoanRefac):
        return loan.get_commitment() * loan.get_unused_percentage()


class CapitalStrategyTermRefac(CapitalStrategyRefac):
    def duration(self, loan: LoanRefac):
        loan.get_commitment() * self.duration()

    def risk_amount_for(self, loan: LoanRefac):
        return loan.get_commitment()


def client_refac():
    loan = LoanRefac()
    capital = CapitalStrategyAdiviseLineRefac()
    # Calls the templae method
    return capital.capital(loan)
