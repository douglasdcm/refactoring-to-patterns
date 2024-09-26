# Original code
class TestResult:
    def add_failure(self, test):
        pass

    def add_error(self, test):
        pass


class TestRunner(TestResult):
    def __init__(self) -> None:
        super().__init__()
        self._test_result = None

    def create_test_result(self):
        # hard-coded to UITestResult
        return UITestResult(self)

    def run_suite(self):
        self._test_result = self.create_test_result()
        # test_suit.run(self._test_result)

    def add_failure(self, test):
        return super().add_failure(test)


class TextTestResult(TestResult):
    def __init__(self, runner: TestRunner) -> None:
        super().__init__()
        self._runner = runner

    def add_failure(self, test):
        super().add_failure(test)
        return "F"

    def add_error(self, test):
        super().add_error(test)
        return "E"


class Test:
    pass


class UITestResult(TestResult):
    def __init__(self, runner: TestRunner) -> None:
        super().__init__()
        self._runner = runner

    def add_failure(self, test: Test):
        super().__init__()
        # Notification for test runner
        self._runner.add_failure(test)


def client():
    result = TextTestResult(TestRunner())
    return result.add_failure(Test()), result.add_error(Test())


# Refactored code
class TestListenerRefac:
    def add_error(self, test):
        raise NotImplementedError

    def add_failure(self, test):
        raise NotImplementedError


class TestResultRefac:
    def __init__(self) -> None:
        self._observers: list[TestListenerRefac] = []

    def add_observer(self, observer: TestListenerRefac):
        self._observers.append(observer)

    def add_failure(self, test):
        for observer in self._observers:
            observer.add_error(test)

    def add_error(self, test):
        for observer in self._observers:
            observer.add_error(test)


class TestRunnerRefac(TestListenerRefac):
    def __init__(self) -> None:
        super().__init__()
        self._test_result = None

    def create_test_result(self):
        result = TestResultRefac(self)
        result.add_observer(self)
        return result

    def run_suite(self):
        self._test_result = self.create_test_result()

    def add_failure(self, test):
        return "F"

    def add_error(self, test):
        return "E"


class TextTestResultRefac(TestResultRefac):

    def __init__(self, runner: TestListenerRefac) -> None:
        super().__init__()
        self._runner = runner

    def add_failure(self, test):
        super().add_failure(test)
        # Notifies the test runner
        return self._runner.add_failure(test)

    def add_error(self, test):
        super().add_error(test)
        # Notifies the test runner
        return self._runner.add_error(test)


class UITestResultRefac(TestResultRefac):
    def __init__(self, runner: TestListenerRefac) -> None:
        super().__init__()
        self._runner = runner

    def add_failure(self, test: TestResultRefac):
        super().__init__()
        # Notification for test runner
        self._runner.add_failure(test)


class TestRefac:
    pass


def client_refac():
    result = TextTestResultRefac(TestRunnerRefac())
    return result.add_failure(TestRefac()), result.add_error(Test())
