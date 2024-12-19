# Original code
# The TextExtractor has lots of conditons to handle Nodes, like StringNode
# The idea if the rectoring is distribute the logic into Visitor classes


# Interface
class Node:
    pass


class LinkTag(Node):
    pass


class Tag(Node):
    pass


class StringNode(Node):
    pass


class TextExtractor:
    def extract_text(self, nodes: list[Node]):
        result = []
        for node in nodes:
            if isinstance(node, StringNode):
                result.append("string")
            elif isinstance(node, LinkTag):
                result.append("linktag")
            elif isinstance(node, Tag):
                result.append("tag")
            else:
                result.append("other")
        return result


# Code refactored
# Interface
class NodeVisitorRefac:
    def visit_link_tag(self, node):
        return "linktag"

    def visit_tag(self, node):
        return "tag"

    def visit_string_node(self, node: object):
        return "string"


class NodeRefac:
    def accept(self, node: NodeVisitorRefac):
        pass


class LinkTagRefac(NodeRefac):
    def accept(self, node: NodeVisitorRefac):
        return node.visit_link_tag(self)


class TagRefac(NodeRefac):
    def accept(self, node: NodeVisitorRefac):
        return node.visit_tag(self)


class StringNodeRefac(NodeRefac):
    def accept(self, node: NodeVisitorRefac):
        return node.visit_string_node(self)


class TextExtractorVisitorRefac(NodeVisitorRefac):
    def extract_text(self, nodes: list[NodeRefac]):
        result = []
        for node in nodes:
            result.append(node.accept(self))
        return result


def run_refac():
    result1 = TextExtractor().extract_text([StringNode()])
    result2 = TextExtractorVisitorRefac().extract_text([StringNodeRefac()])
    return result1, result2
