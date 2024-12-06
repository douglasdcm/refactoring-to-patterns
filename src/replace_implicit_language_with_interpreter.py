# Original code


# this class is not part of the original code. Added for testing purposes
class Product:
    def __init__(self, code, name, color, price, size):
        self.code = code
        self.name = name
        self.color = color
        self.price = price
        self.size = size


class ProductFinder:

    def __init__(self, product_repository):
        self._product_repostory: list[Product] = product_repository

    def by_color(self, color):
        result = []
        for p in self._product_repostory:
            if p.color == color:
                result.append(p)
        return result

    def by_price(self, price):
        result = []
        for p in self._product_repostory:
            if p.price == price:
                result.append(p)
        return result

    def by_size(self, size):
        result = []
        for p in self._product_repostory:
            if p.size == size:
                result.append(p)
        return result

    def bellow_price_and_avoiding_a_color(self, color, price):
        result = []
        for p in self._product_repostory:
            if p.color != color and p.price < price:
                result.append(p)
        return result

    def by_color_and_bellow_price(self, color, price):
        result = []
        for p in self._product_repostory:
            if p.color == color and p.price < price:
                result.append(p)
        return result

    def by_color_size_and_bellow_price(self, color, size, price):
        result = []
        for p in self._product_repostory:
            if p.color == color and p.size == size and p.price < price:
                result.append(p)
        return result


# Refactored code
# Code duplicatin removed and the combinations like 'below_price_and_color' wher converted to a
# language 'and_spec(price_spec, color_spec)'


class SpecRefac:
    context = None

    def is_satisfied_by(self, p: Product) -> bool:
        raise NotImplementedError


class AndSpecRefac(SpecRefac):
    def __init__(self, spec1, spec2):
        self._spec1: SpecRefac = spec1
        self._spec2: SpecRefac = spec2

    def is_satisfied_by(self, p):
        return self._spec1.is_satisfied_by(p) and self._spec2.is_satisfied_by(p)


class ColorSpecRefac(SpecRefac):
    def __init__(self, color):
        self._color = color

    def is_satisfied_by(self, product: Product):
        return product.color == self._color


class NotSpecRefac(SpecRefac):
    def __init__(self, spec):
        self._spec: SpecRefac = spec

    def is_satisfied_by(self, product: Product):
        return not self._spec.is_satisfied_by(product)


class PriceSpecRefac(SpecRefac):
    def __init__(self, price):
        self._price = price

    def is_satisfied_by(self, p: Product):
        return p.price == self._price


class SizeSpecRefac(SpecRefac):
    def __init__(self, size):
        self._size = size

    def is_satisfied_by(self, p):
        return p.size == self._size


class BelowPriceSpecRefac(SpecRefac):
    def __init__(self, price):
        self._price = price

    def is_satisfied_by(self, spec: SpecRefac):
        return self._price < spec.context

    def is_satisfied_by(self, p):
        return p.price < self._price


class ProductFinderRefac:
    def __init__(self, product_repository):
        self._product_repostory: list[Product] = product_repository

    def select_by(self, spec: SpecRefac):
        result = []
        for p in self._product_repostory:
            if spec.is_satisfied_by(p):
                result.append(p)
        return result


# This client imulates all the test cases present in the book. Notice all the methods from ProductFinder,
# like 'bellow_price_and_avoiding_a_color' were refactored and now the specification is passed as a parameter
# to the 'select_by' method
def client():
    fire_truck = Product("123a", "fire truck", "red", 8.95, "medium")
    barbie_classic = Product("123b", "barbie classic", "yellow", 15.95, "small")
    frisbee = Product("123d", "frisbee", "pink", 9.99, "large")
    baseball = Product("123e", "baseball", "white", 8.95, "not applicable")
    toy_convertible = Product(
        "123", "toy porsche convertible", "red", 230.00, "not applicable"
    )

    repository = [fire_truck, barbie_classic, frisbee, baseball, toy_convertible]

    non_white_products_bellow_none_dollars = ProductFinder(
        repository
    ).bellow_price_and_avoiding_a_color("white", 9)
    product_spec = AndSpecRefac(
        BelowPriceSpecRefac(9), NotSpecRefac(ColorSpecRefac("white"))
    )

    # Iterates over the list of products and compares against the spec
    non_white_products_bellow_none_dollars_refac = ProductFinderRefac(
        repository
    ).select_by(product_spec)

    by_color_size_and_bellow_price = ProductFinderRefac(repository).select_by(
        spec=AndSpecRefac(
            SizeSpecRefac("small"),
            AndSpecRefac(ColorSpecRefac("red"), BelowPriceSpecRefac(10)),
        )
    )

    by_color_and_bellow_price = ProductFinderRefac(repository).select_by(
        AndSpecRefac(ColorSpecRefac("white"), BelowPriceSpecRefac(100))
    )

    bellow_price_and_avoiding_a_color = ProductFinderRefac(repository).select_by(
        AndSpecRefac(ColorSpecRefac("yellow"), NotSpecRefac(BelowPriceSpecRefac(20)))
    )

    by_size = ProductFinderRefac(repository).select_by(SizeSpecRefac("small"))

    by_color = ProductFinderRefac(repository).select_by(ColorSpecRefac("red"))

    by_price = ProductFinderRefac(repository).select_by(PriceSpecRefac(8.95))

    products = (
        non_white_products_bellow_none_dollars,
        non_white_products_bellow_none_dollars_refac,
        by_color_and_bellow_price,
        bellow_price_and_avoiding_a_color,
        by_color_size_and_bellow_price,
        by_size,
        by_color,
        by_price,
    )

    result = []
    for p in products:
        result.append(len(p))
    return result
