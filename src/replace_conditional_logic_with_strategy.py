# Original code
# There are many coonditions to return the correct calculation. If a new calculation is ncessary,
# then a condition has to br added
def risk_factory():
    return 1


def get_unused_percentage():
    return 1


def outstanding_risk_amount():
    return 1


def risk_factory():
    return 1


def unused_risk_amount():
    return 1


def unused_risk_factory():
    return 1


class Loan:
    expiricy = None
    maturity = None
    commitment = 0
    duration = 0

    def capital():

        if Loan.expiricy == None and Loan.maturity != None:
            return Loan.commitment * Loan.duration * risk_factory()
        if Loan.expiricy != None and Loan.maturity == None:
            if get_unused_percentage() != 1.0:
                return (
                    Loan.commitment
                    * get_unused_percentage()
                    * Loan.duration
                    * risk_factory()
                )
        else:
            return (
                outstanding_risk_amount() * Loan.duration * risk_factory()
                + unused_risk_amount() * Loan.duration() * unused_risk_factory()
            )

        return 0.0


# Code refactored
# The conditions from capital where removed. Now the object Loan receives the concrete CapitalStrategy object and executes
# the method capital of each the concrete class. To get the correct Loan, like TermLoan, the client calls the helper
# method "new_term_loan", "new_advide_line" or new_revolver_loan" (check the unit test). If a new Loan is added, it is
# necessary to add a new "creater" method
class LoanRefac:
    expiricy = None
    maturity = None
    commitment = 1
    duration = 1

    def __init__(self, capital_strategy) -> None:
        self._capital_strategy = capital_strategy

    def capital(self):
        # polimorphysm
        return self._capital_strategy.capital(self)

    @staticmethod
    def new_term_loan():
        return LoanRefac(CapitalStrategyTermRefac())

    @staticmethod
    def new_advised_line():
        return LoanRefac(CapitalStrategyAdvisedRefac())

    @staticmethod
    def new_revolver_loan():
        return LoanRefac(CapitalStrategyRevolverRefac())


class CapitalStrategyRefac:
    @staticmethod
    def capital(loan: LoanRefac):
        return NotImplementedError()

    def get_commitment(self):
        return 1


class CapitalStrategyAdvisedRefac(CapitalStrategyRefac):
    @staticmethod
    def capital(loan: LoanRefac):
        return loan.commitment * loan.duration * risk_factory()


class CapitalStrategyRevolverRefac(CapitalStrategyRefac):
    @staticmethod
    def capital(loan: LoanRefac):
        pass


class CapitalStrategyTermRefac(CapitalStrategyRefac):
    @staticmethod
    def capital(loan: LoanRefac):
        def duration():
            return 1

        def risk_factor_for(loan: LoanRefac):
            pass

        return loan.get_commitment() * duration(loan) * risk_factor_for(loan)
