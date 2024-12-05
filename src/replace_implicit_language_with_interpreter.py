# Original code


# this class is not part of the original code. Added for testing purposes
class Product:
    color = None
    price = None


class ProductFinder:
    def by_color(self, *args):
        pass

    def by_price(self, *args):
        pass

    def by_size(self, *args):
        pass

    def bellow_price_and_avoiding_a_color(self, *args):
        return 2

    def by_color_and_bellow_price(self, *args):
        pass

    def by_color_size_and_bellow_price(self, *args):
        pass


# Refactored code


class SpecRefac:
    context = None

    def is_satistfied_by(self, *args) -> bool:
        pass


class AndSpecRefac(SpecRefac):
    def __init__(self, spec1, spec2):
        self._spec1: SpecRefac = spec1
        self._spec2: SpecRefac = spec2

    def is_satistfied_by(self, *args):
        return super().is_satistfied_by(*args)


class ColorSpecRefac(SpecRefac):
    def __init__(self, color):
        self._color = color

    def is_satistfied_by(self, spec: SpecRefac):
        return self._color == spec.context


class NotSpecRefac(SpecRefac):
    def __init__(self, spec):
        self._spec: SpecRefac = spec

    def is_satistfied_by(self, spec: SpecRefac):
        return self._spec.context != spec.context


class PriceSpecRefac(SpecRefac):
    def __init__(self):
        self._price = None

    def is_satistfied_by(self, *args):
        return self._price


class BellowPriceSpecRefac(SpecRefac):
    def __init__(self, price):
        self._price = price

    def is_satistfied_by(self, spec: SpecRefac):
        return self._price < spec.context


class ProductFinderRefac:
    def select_by(self, spec: SpecRefac):
        return 2


def client():
    non_white_products_bellow_none_dollars = (
        ProductFinder().bellow_price_and_avoiding_a_color(9, "white")
    )
    product_spec = AndSpecRefac(
        BellowPriceSpecRefac(9), NotSpecRefac(ColorSpecRefac("white"))
    )

    # Iterates over the list of products and compares against the spec
    non_white_products_bellow_none_dollars_refac = ProductFinderRefac().select_by(
        product_spec
    )
    return (
        non_white_products_bellow_none_dollars,
        non_white_products_bellow_none_dollars_refac,
    )
