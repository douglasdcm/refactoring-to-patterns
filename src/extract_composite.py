# Original code
class Node:
    def to_plain_text(self):
        pass


# Composite 1
class FormTag:
    def to_plain_text(self):
        pass


# Composite 2
class LinkTag:
    def to_plain_text(self):
        # similar implementation of FormTag
        pass


# Other composites...


# Refactored code
class Node:
    def to_plain_text(self):
        raise NotImplementedError


class CompositeTag:
    def to_plain_text(self):
        # Extracted from other composites. Almost the same of Extract Class from Martin Fowler
        pass


class FormTag(CompositeTag):
    pass


class LinkTag(CompositeTag):
    pass
