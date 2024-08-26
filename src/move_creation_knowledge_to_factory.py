# Original code
# Context: data and code used to instantiate a class is sprawled across numerous classes
class StringNode:
    def __init__(self) -> None:
        pass

    def new():
        StringNode()


class StringParser:
    def should_decode_string_nodes(self):
        pass

    def should_remove_escape_character(self):
        pass

    def create_string_node(self, *args):
        a_string_node = StringNode()


class Parser:
    def find_string(self):
        a_string_parser = StringParser()
        a_string_parser.should_decode_string_nodes()
        a_string_parser.should_remove_escape_character()


class Client:
    def set_decode_string_nodes(self, yes: bool):
        a_parser = Parser()

    def set_remove_escape_characteres(yes: bool):
        a_parser = Parser()

    def parse_url(sefl, url):
        a_parser = Parser()
        a_parser.find_string()


def run():
    a_client = Client()
    a_client.set_decode_string_nodes(True)
    a_client.set_remove_escape_characteres(True)
    a_client.parse_url("any")

    a_parser = Parser()
    a_parser.find_string()

    a_string_parser = StringParser()
    a_string_parser.create_string_node()

    a_string_node = StringNode()
    a_string_node.new()


# Code refactored
# The method NodeFactory.create_string_node has all the code to create ajd configure Nodes
class NodeRefacored:
    pass


class DecodingStringNodeRefactored(NodeRefacored):
    def __init__(self, string_node) -> None:
        pass


class StringNodeRefactored(NodeRefacored):
    pass


class NodeFactory:
    def set_decode_string_nodes(self, decision):
        self._decode_string_node = decision

    def decode_string_nodes(self):
        return self._decode_string_node

    def create_string_node(self, should_decode) -> NodeRefacored:
        if should_decode:
            return DecodingStringNodeRefactored(StringNodeRefactored())
        return StringNodeRefactored()

    def set_remove_escape_characters(self, decision: bool):
        self._set_remove_escape_characters = decision


class StringParserRefactored:

    def find_string(self, parser):
        a_node_factory = NodeFactory()
        a_node_factory.create_string_node(parser.should_decode_nodes())


class PaserRefactored:
    def __init__(self) -> None:
        self._node_factory = NodeFactory()

    def should_decode_nodes(self):
        return self._node_factory.decode_string_nodes()

    def set_node_factory(self, a_node_factory):
        self._node_factory = a_node_factory

    def get_node_factory(self):
        return self._node_factory

    def parse(self, url):
        a_parser = StringParserRefactored()
        a_parser.find_string(self)


def run_refactored():
    a_node_factory = NodeFactory()
    a_node_factory.set_decode_string_nodes(True)
    a_node_factory.set_remove_escape_characters(True)
    a_parser = PaserRefactored()
    a_parser.set_node_factory(a_node_factory)
    a_parser.parse(url="any")

    return True
