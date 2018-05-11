#!/usr/bin/env python3


import abc
import functools


class Course:
    """
    Course field descriptor.
    """

    def __get__(self, instanse, owner):
        if instanse:
            return owner._course

        def inner(other):
            return owner._course / other._course
        return inner

    def __set__(self, instance, value):
        assert value > 0, "Sets only non-negative values!"
        instance.__class__._course = value


@functools.total_ordering
class Currency(metaclass=abc.ABCMeta):
    """
    Abstract class which represents currency.
    """

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.to(self.__class__).value

    def __lt__(self, other):
        return self.value < other.to(self.__class__).value

    def __add__(self, other):
        return self.__class__(self.value + other.to(self.__class__).value)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __sub__(self, other):
        return self.__class__(self.value - other.to(self.__class__).value)

    def __mul__(self, number):
        return self.__class__(self.value * number)

    __rmul__ = __mul__

    def __truediv__(self, number):
        return self.__class__(self.value / number)

    @property
    def currency(self):
        """
        Return kind of currency.
        """
        return self.__class__.__name__

    def to(self, other_currency):
        """
        Transforms currency into another one.

        :param other_currency: Other currency class to convert into.
        :return: Other currency with converted value of given one.
        """
        return other_currency(self.value * self.course / other_currency(0).course)


class Euro(Currency):
    """
    Class which represents Euro.
    """

    def __init__(self, value):
        """
        Initialize the instance of Euro.
        Course contains the euro-dollar exchange rate by default.

        :param value: Value to set.
        """
        super().__init__(value)
        if not hasattr(self.__class__, '_course'):
            course = Course()
            self.__class__.course = course
            self.course = 74/62

    def __str__(self):
        return '{} €​'.format(self.value)


class Dollar(Currency):
    """
    Class which represents Dollar.
    """

    def __init__(self, value):
        """
        Initialize the instance of Dollar.
        Course contains the dollar-dollar exchange rate by default.

        :param value: Value to set.
        """
        super().__init__(value)
        if not hasattr(self.__class__, '_course'):
            course = Course()
            self.__class__.course = course
            self.course = 1

    def __str__(self):
        return '{} $​​​'.format(self.value)


class Rubble(Currency):
    """
    Class which represents Rubble.
    """

    def __init__(self, value):
        """
        Initialize the instance of Rubble.
        Course contains the rubble-dollar exchange rate by default.

        :param value: Value to set.
        """
        super().__init__(value)
        if not hasattr(self.__class__, '_course'):
            course = Course()
            self.__class__.course = course
            self.course = 62

    def __str__(self):
        return '{} ₽​​​'.format(self.value)


if __name__ == '__main__':
    rub = Rubble(100)
    dlr = Dollar(50)
    eur = Euro(10)
    print(rub / 5 + eur)
    print(eur + 10 * dlr)
    print(sum([Euro(i) for i in range(5)]))
    print(dlr)
    print(eur.currency)
    print(dlr > eur)
    print(rub != dlr)


