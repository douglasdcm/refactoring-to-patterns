# Original code
# Similar methods differs from the object instantiation. All the rest is the same
class TestCase:
    pass


class DOMBuilder:
    def __init__(self, orders) -> None:
        pass

    def calc(self):
        return 42


class XMLBuilder:
    def __init__(self, orders) -> None:
        pass

    def calc(self):
        return 42


class DOMTest(TestCase):
    def run_dom_test(self):
        expected = 42
        builder = DOMBuilder("orders")  # different object created
        assert builder.calc() == expected


class XMLTest(TestCase):
    def run_xml_test(self):
        expected = 42
        builder = XMLBuilder("orders")  # different object created
        assert builder.calc() == expected


# Code refactored
# The instantiation of the DOMBuilder or XMLBuilder is the only difference in both tests.
# It was created an OutputBuilder like an interface for both classes (it is not necessary
# given that Python uses duck type).
# In TestCase a new method called "create_builder" was introduced to be implemented by the
# children classes. This is the step executed in runtime for each type of test. This is the
# polymorphism. When both tests (DOMTest and XMLTest) are executed, the instance returned
# from the "create_builder" depends on the implementation. Is can be DOMBuilder or
# XMLBuilder.
class OutputBuilder:
    def calc(self):
        raise NotImplementedError()


class DOMBuilderRefac(OutputBuilder):
    def calc(self):
        return 42


class XMLBuilderRefac(OutputBuilder):
    def calc(self):
        return 42


class TestCaseRefac:
    def create_builder(self):
        raise NotImplementedError()

    def run_test(self):
        expected = 42
        builder = self.create_builder()  # different object created
        assert builder.calc() == expected


class DOMTestRefac(TestCaseRefac):
    def create_builder(self) -> OutputBuilder:
        return DOMBuilderRefac()


class XMLTestRefac(TestCaseRefac):
    def create_builder(self):
        return XMLBuilderRefac()


def run():
    dom_tc = DOMTestRefac()
    dom_tc.run_test()

    xml_tc = XMLTestRefac()
    xml_tc.run_test()
