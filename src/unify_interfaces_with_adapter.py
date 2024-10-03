# Original code
# The classes for XML and DOM are very similar, but one point of attention is that XML colaborates with TagNode and
# DOM colaborates with Element
class Child:
    pass


class AbstractBuilder:

    def add_below(self, child: Child):
        raise NotImplementedError

    def add(child: Child):
        raise NotImplementedError


class TagNode:
    def add_attribute(self):
        pass

    def add(self, child: Child):
        pass


class XMLBuilder(AbstractBuilder):
    node = TagNode()

    def add(self, child: Child):
        return "add xml"


class Element:
    def set_attribute(self):
        pass

    def append_child(self):
        pass


class DOMBuilder(AbstractBuilder):
    element = Element()

    def add_below(self, child: Child):
        return "add dom below"


def client():
    dom = DOMBuilder()
    result1 = dom.add_below(None)
    xml = XMLBuilder()
    result2 = xml.add(None)
    return result1, result2


# Refactored code
# The class XMLNode is used by XLM and DOM classes. Notice the class TagNode, which is used by XML, implements the
# XMLNode class. The same way, the class Element implements the XMLNode. It allows the XLM and DOM classes to use/point
# their implementation to the same interface (XMLNode) and not the the concret classes TagNode or Element
class XMLNodeRefac:
    def add(self):
        raise NotImplementedError

    def add_attribute(self):
        raise NotImplementedError

    def add_value(self):
        raise NotImplementedError


class ChildRefac:
    pass


class AbstractBuilderRefac:

    def add(self, child: ChildRefac):
        raise NotImplementedError


class TagNodeRefac(XMLNodeRefac):
    def add_attribute(self):
        pass

    def add(self, child: ChildRefac):
        return "add xml"


class XMLBuilderRefac(AbstractBuilderRefac):
    node: XMLNodeRefac = TagNodeRefac()

    def add(self, child: ChildRefac):
        return self.node.add(child)


class ElementRefac:
    def set_attribute(self):
        pass

    def append_child(self):
        return "add dom below"


class ElementAdapterRefac(XMLNodeRefac):
    def __init__(self, element: ElementRefac) -> None:
        self.__element = element

    def get_element(self):
        return self.__element

    def add_below(self, child: ChildRefac):
        return self.get_element().append_child()


class DOMBuilderRefac(AbstractBuilderRefac):
    # It was replaced Element by ElementAdapter, hence XMLNodeRefac
    element: XMLNodeRefac = ElementAdapterRefac(ElementRefac())

    def add_below(self, child: ChildRefac):
        # It is omited, but this method called Element directly, but now it calls the Element through the ElementAdapter
        # example: self.element.get_element().append_child()
        # The indirection is done by the methos "get_elemment"
        return self.element.add_below(child)


def client_refac():
    dom = DOMBuilderRefac()
    result1 = dom.add_below(None)
    xml = XMLBuilderRefac()
    result2 = xml.add(None)
    return result1, result2
