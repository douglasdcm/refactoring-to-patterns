# Original code
# NOtice the xlm is built using a string handler
def client():
    xml = []
    xml.append("<orders>")
    for i in range(2):
        xml.append("<order")
        xml.append(" id=")
        xml.append(f"'order-{i}'")
        xml.append(">")
        xml.append(f"the order{i}")
        xml.append("</order>")
    xml.append("</orders>")

    return "".join(xml)


# Code refactored
# This is not the original implementation from the book, but inspired on it
# Notice the the class TagNodeLeaf does not overrides the functions to haldle child nodes
# because they don't have nodes. Any attempt to use these methods from this class results in an exception
# The TagNodeComposite implemts the "add" method and overrides the default implementation of "to_string"
class TagNode:
    def __init__(self, name) -> None:
        self._name = name
        self._output = ""

    def add_atribute(self, attribute, value):
        self._output = f" {attribute}='{value}'>"

    def add_text(self, value):
        self._output = f"{self._output}{value}"

    def add(self, child):
        raise NotImplementedError

    def list_children(self):
        raise NotImplementedError

    def to_string(self):
        raise NotImplementedError


class TagNodeLeaf(TagNode):
    def __init__(self, name) -> None:
        self._name = name
        self._output = ""

    def add_atribute(self, attribute, value):
        self._output = f" {attribute}='{value}'>"

    def add_text(self, value):
        self._output = f"{self._output}{value}"

    def to_string(self):
        return f"<{self._name}{self._output}</{self._name}>"


class TagNodeComposite(TagNode):
    children = []

    def add(self, child):
        self.children.append(child.to_string())

    def to_string(self):
        for child in self.children:
            self._output += child
        return f"<{self._name}>{self._output}</{self._name}>"


def client_refac():
    order1 = TagNodeLeaf("order")
    order1.add_atribute("id", "order-0")
    order1.add_text("the order0")

    order2 = TagNodeLeaf("order")
    order2.add_atribute("id", "order-1")
    order2.add_text("the order1")

    orders = TagNodeComposite("orders")
    orders.add(order1)
    orders.add(order2)

    return orders.to_string()
