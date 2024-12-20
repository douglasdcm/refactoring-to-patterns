# Original code
# When you have many constructors that contain duplicated code
# Note: this may not make muck sense in Python as it does not suppost
# native method overload, but the idea may be useful for methods
# with similar implementaion and different number of parameters
class Loan:
    def loan1(self, notional, outstanding, rating, expiricy):
        self._notional = notional
        self._outstanding = outstanding
        self._rating = rating
        self._expiricy = expiricy

    def loan2(self, notional, outstanding, rating, expiricy, maturity):
        self._notional = notional
        self._outstanding = outstanding
        self._rating = rating
        self._expiricy = expiricy
        self._maturity = maturity

    def loan3(self, strategy, notional, outstanding, rating, expiricy, maturity):
        self._strategy = strategy
        self._notional = notional
        self._outstanding = outstanding
        self._rating = rating
        self._expiricy = expiricy
        self._maturity = maturity


# Refacoted code
# One method call the other avoiding code duplication
class LoanRefac:
    def loan1(self, notional, outstanding, rating, expiricy):
        self.loan2(notional, outstanding, rating, expiricy, None)

    def loan2(self, notional, outstanding, rating, expiricy, maturity):
        self.loan3("any-strategy", notional, outstanding, rating, expiricy, maturity)

    def loan3(self, strategy, notional, outstanding, rating, expiricy, maturity):
        self._strategy = strategy
        self._notional = notional
        self._outstanding = outstanding


def run_refac():
    l1 = Loan()
    l1.loan1("notional", "outstanding", "rating", "expiricy")
    l2 = Loan()
    l2.loan1("notional", "outstanding", "rating", "expiricy")
    return l1, l2
