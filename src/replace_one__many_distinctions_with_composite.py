# Orginal code
# Many methods with similar implementation, but one selecting by single spec
# and the other one selecting by a list of specs
# This filter does not supports conditionals as "AND", "OR", "NOT", etc..
class Spec:
    pass


class ColorSpec(Spec):
    pass


class SizeSpec(Spec):
    pass


class ProductRepository:
    product = []

    def select_by_spec(self, spec: Spec):
        pass

    def select_by_specs(self, specs: list[Spec]):
        pass


def client():
    repository = ProductRepository()
    repository.select_by_spec(ColorSpec())
    repository.select_by_spec(SizeSpec())


# Refactored code
# Instead of pass a single spec or a list of it, a new CompositeSpec object is
# introduced to hold a list of specs in one of its parameters. Is is a way to
# maps a list to a single object an leave one unique implementation to "select_by"
class SpecRefac:
    pass


class ColorSpecRefac(SpecRefac):
    pass


class SizeSpecRefac(SpecRefac):
    pass


class OrSpecRefac(SpecRefac):
    pass


# other specs...


class CompositeSpecRefac(SpecRefac):
    specs: list[SpecRefac] = []

    def add(self, spec: SpecRefac):
        self.specs.append(spec)


class ProductRepositoryRefac:
    products = []

    def select_by(self, spec: SpecRefac):
        pass


def cleint_refac():
    # Create a single object with a list of specs
    specs = CompositeSpecRefac()
    specs.add(ColorSpec())
    specs.add(SizeSpec())
    repository = ProductRepositoryRefac()
    # passes this single object to the select_by. The method handles the specs
    # independently of the number of items in the list
    repository.select_by(specs)
