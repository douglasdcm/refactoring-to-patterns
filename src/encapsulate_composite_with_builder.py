# Original code
# This code constructs nested nodes like a DOM object. For example
# <activity>
#   <flavours>
#     ...
#   </flavours>
# </activity>
# Notice the complex construction with many instantiations of TagNode objects in the "do" method
# Depending on the size of the nested nodes, the contruction bacames bigger and more complex
class TagNode:
    def add(self, child_node):
        pass


class CatalogWriter:

    def do(self):
        activity_tag = TagNode("activity")
        flavors_tag = TagNode("flavours")
        activity_tag.add(flavors_tag)

        flavors_tag = TagNode("flavor")
        flavors_tag.add(flavors_tag)


# Code refatored
# All the instantiation now is replaced by a builder that hides the implementation details,
# gives meaninful names to methods and reduces the complexity of the creation of DOM objects
#
class TagNodeRefact:
    def __init__(self, root_tag):
        pass

    def add(self, child_node):
        pass


class TagBuilderRefac:
    def __init__(self) -> None:
        self._root: TagNodeRefact = TagNodeRefact()

    def add_child(self, tag_node):
        self._root.add(tag_node)

    def add_to_parent(self, parent: TagNodeRefact, child: str):
        parent.add(child)

    def to_xml(self):
        pass


class CatalogWriterRefac:
    def do(self):
        builder = TagBuilderRefac("root")
        builder.add_child("flavours")
        builder.add_to_parent("flavours", "flavor")
        builder.to_xml()
