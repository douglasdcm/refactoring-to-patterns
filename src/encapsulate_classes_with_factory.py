# Original code
# The "run" method (the client) access different classes from the same module. However, the
# classes have the same base subper class and follow the same interface. So, it should
# be simple to access the superclass which decided what to do according to the "type" passed.
class AttributeDescriptor:
    pass


class BooleanDescriptor(AttributeDescriptor):
    def __init__(self, type) -> None:
        print(f"The type is {type}")


class DefaultDescriptor(AttributeDescriptor):
    def __init__(self, type) -> None:
        print(f"The type is {type}")


class ReferenceDescriptor(AttributeDescriptor):
    def __init__(self, type) -> None:
        print(f"The type is {type}")


def run():
    DefaultDescriptor("integer")
    DefaultDescriptor("date")
    DefaultDescriptor("string")

    ReferenceDescriptor("class")


# Code refactored
# Now the superclass is used to return itself with different implementations according to the
# method choosen. For example, if the method "for_interger" is selected, them the superclass
# is returned with the implementation related to intergers. The same applies for "for_class"
# and other methods
class AttributeDescriptorRefac:
    def for_boolean(self):
        return DefaultDescriptorRefac("boolean")

    def for_class(self):
        return ReferenceDescriptorRefac("class")

    def for_date(self):
        return DefaultDescriptorRefac("date")

    def for_integer(self):
        return DefaultDescriptorRefac("integer")

    def for_string(self):
        return DefaultDescriptorRefac("string")


class BooleanDescriptorRefac(AttributeDescriptorRefac):
    def __init__(self, type) -> None:
        super().__init__()


class DefaultDescriptorRefac(AttributeDescriptorRefac):
    def __init__(self, type) -> None:
        super().__init__()


class ReferenceDescriptorRefac(AttributeDescriptorRefac):
    def __init__(self, type) -> None:
        super().__init__()


def run_refac():
    AttributeDescriptorRefac().for_integer()
    AttributeDescriptorRefac().for_date()
    default = AttributeDescriptorRefac().for_string()

    reference = AttributeDescriptorRefac().for_class()
    return default, reference
