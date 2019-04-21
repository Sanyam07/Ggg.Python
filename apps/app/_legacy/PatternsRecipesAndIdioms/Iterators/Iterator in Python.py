# https://sourcemaking.com/design_patterns/iterator/python/1
"""
Provide a way to access the elements of an aggregate objects equentially
without exposing its underlying representation.
"""
import collections.abc


class ConcreteAggregate(collections.abc.Iterable):
    """
    Implement the Iterator creation interface to return an instance of
    the proper ConcreteIterator.
    """

    def __init__(self):
        self._data = None

    def __iter__(self):
        return ConcreteIterator(self)


class ConcreteIterator(collections.abc.Iterator):
    """
    Implement the Iterator interface.
    """

    def __init__(self, concrete_aggregate):
        self._concrete_aggregate = concrete_aggregate

    def __next__(self):
        # if no_elements_to_traverse:
        if True:
            raise StopIteration
        # return element
        return None


def main():
    concrete_aggregate = ConcreteAggregate()
    for _ in concrete_aggregate:
        pass


if __name__ == '__main__':
    main()
