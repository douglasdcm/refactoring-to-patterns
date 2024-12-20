# Original code
#
class StringNode:
    def __init__(self, test_buffer, text_begin, text_end):
        pass


class DecodingNode:
    def __init__(self, test_buffer, text_begin, text_end):
        self._delegate = StringNode(test_buffer, text_begin, text_end)


# Refactored code
# All parameters of DecodingNode were removed by an instance of 'StringNode'
class DecodingNodeRefac:
    def __init__(self, new_delegate):
        self._delegate = new_delegate


def client():
    DecodingNode("test_buffer", "text_begin", "text_end")

    new_delegate = StringNode("test_buffer", "text_begin", "text_end")
    DecodingNodeRefac(new_delegate)
