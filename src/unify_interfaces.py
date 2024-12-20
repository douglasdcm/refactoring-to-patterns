# Original code
# You need a superclass or interface to have the same interface
# for a set o subclasses
class AbstractNode:
    def to_plain_text_string(self):
        pass

    def to_htlm(self):
        pass

    def to_string(self):
        pass

    def element_begin(self):
        pass

    def element_end(self):
        pass

    def set_parameter(self):
        pass

    def get_parameter(self):
        pass


class StringNode(AbstractNode):
    def accept(self, text_extractor):
        pass


# Refactored code
# Unify the interface including the "accept" method in the AbstractNode
# All subclasses of AbstractNode has the same type so can be processed
# polymorphically
# Note: in Python it is not necesary to share the same interface. It is necessary
# to have the same methods (duck type)
class AbstractNode:
    def to_plain_text_string(self):
        pass

    def to_htlm(self):
        pass

    def to_string(self):
        pass

    def element_begin(self):
        pass

    def element_end(self):
        pass

    def set_parameter(self):
        pass

    def get_parameter(self):
        pass

    def accept(self, text_extractor):
        pass


class StringNode(AbstractNode):
    def accept(self, text_extractor):
        pass
