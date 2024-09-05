# Original code
# An old class receives new methods to fullfill new requirements, but these new methods are not
# part of the core responsibilitie of the class or is duplicated code
# It is the case of the method "to_plain_text_string". It is there for convinience, not as the
# main purpose of the class
class TextBuffer:
    @staticmethod
    def to_string():
        return "any"


class Translate:
    @staticmethod
    def decode(result):
        return result + "__decoded__"


class StrignNode:

    def __init__(self, should_decode) -> None:
        self._should_decode = should_decode

    def to_plain_text_string(self):
        result = TextBuffer.to_string()
        if self._should_decode:
            result = Translate.decode(result)
        return result


# client
def run():
    StrignNode(should_decode=True).to_plain_text_string()


# Refactored code
# The method to decode the text is placed in the DecodingNode class. This is the decorator as
# it receives a StringNode class, wrapps it and returns the DecodingNode that implements the
# same interface Node as StringNode
class TextBufferRefac:
    @staticmethod
    def to_string():
        return "any"


class TranslateRefac:
    @staticmethod
    def decode(text_buffer):
        return (
            f"{text_buffer.to_plain_text_string()} __decoded__"  # StringNodeRefac obj
        )


class Node:
    def to_plain_text_string(self):
        raise NotImplementedError()


class StringNodeRefac(Node):
    def create_string_node(self, should_decode):
        if should_decode:
            return DecodingNodeRefac(self)  # this class is the decorator
        return self

    def to_plain_text_string(self):
        return "any"

    def should_decode(self):
        # This value is "hard-coded" because there is another class to decode the text
        return False


class DecodingNodeRefac(Node):
    def __init__(self, text_buffer: Node) -> None:
        self._text_buffer: Node = text_buffer

    def should_decode(self):
        return True

    def to_plain_text_string(self):
        return TranslateRefac.decode(self._text_buffer)


# client
def run_refac():
    string_node = StringNodeRefac().create_string_node(should_decode=True)
    # in this case the string_node is a DecodingNode object
    decoded = string_node.to_plain_text_string()

    string_node = StringNodeRefac().create_string_node(should_decode=False)
    # in this case the string_node is a StringNode object
    # the method "to_plain_ext_string" runs by polymorphism
    encoded = string_node.to_plain_text_string()

    return encoded, decoded
