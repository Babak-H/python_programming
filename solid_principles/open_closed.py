# Open Closed Principle
# when you add functionality to a class, you add it via extension, NOT modification
# Open for extension, Closed for modification, instead of modifying a class, extend it
# (inherit from it in a new class)

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    # this style breaks open-close principle (need modification for any change!)
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p


class Specification:
    '''
    Specification
    base class (similar to Java interface)
    '''

    def is_satisfied(self, item):
        pass

    # &
    def __and__(self, other):
        # self in here is probably a specification object
        return AndSpecification(self, other)


class Filter:
    '''
    Filter
    base class (similar to Java interface)
    spec: object of Specification class
    '''

    def filter(self, item, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        # make sure each item satisfies every single specification
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                # yield holds the item for you to do what you like with it
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.MEDIUM)

    products = [apple, tree, house]

    myFilter = BetterFilter()
    green = ColorSpecification(Color.GREEN)
    large = SizeSpecification(Size.LARGE)

    for p in myFilter.filter(products, green):
        print(p.name)

    # large_green = AndSpecification(green, large)
    large_green = large & green  # & is same as __and__
    for p in myFilter.filter(products, large_green):
        print(p.name)
