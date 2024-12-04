# Orignal code
# The same class hadles multiple versions of connections to a database (Super Database)
# In the refactoring we are going to split te logic in two spacialized classes. One for
# version 5.1 and other for version 5.2
class Query:
    sd52: bool = None

    # the orignal code uses overload to define the two versions of login.
    # I'm simply adding the verison number in the method name
    def login51(self, *args):
        pass

    def login52(self, *args):
        pass

    def do_query(self):
        if Query.sd52:
            pass
        else:
            pass
        return "done"


# Code refactored
class QueryRefac:
    def do_query(self):
        # Concret method
        return "done"

    def login(self, *args):
        raise NotImplementedError

    def create_query(self):
        raise NotImplementedError


class QuerySD51Refac(QueryRefac):
    def login(self, *args):
        # do login to SD version 51
        pass

    def create_query(self):
        # create query to SD 51
        pass


class QuerySD52Refac(QueryRefac):
    def login(self, *args):
        # do login to SD version 52
        pass

    def create_query(self):
        # create query to SD 52
        pass


def run_refac():
    q = Query()
    q.login51()
    q.do_query()
    q.login52()
    result_q = q.do_query()

    q51 = QuerySD51Refac()
    q51.login()
    q51.create_query()
    result_q51 = q51.do_query()

    q52 = QuerySD52Refac()
    q52.login()
    q52.create_query()
    result_q52 = q52.do_query()
    return result_q, result_q51, result_q52
