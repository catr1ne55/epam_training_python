#!/usr/bin/env python3


class prop:
    """Класс-дескриптор, применяемый как декоратор."""

    def __init__(self, method):
        """Конструктор класса.

        :param method: Метод-атрибут класса владельца.
        :type method: function
        """
        self.method = method

    def __get__(self, instance, owner):
        """Получение значения атрибута.

        :param instance: представитель класса.
        :type instance: Something.
        :param owner: class Something.
        :type owner: type.
        """
        return self.method(instance)


class Something:
    """Просто класс."""

    def __init__(self, x):
        """Конструктор класса.

        :param x: Число.
        :type x: int.
        """
        self.x = x
    @prop
    def attr(self):
        """Возведение в квадрат."""
        return self.x ** 2


if __name__ == '__main__':
    s = Something(10)
    print(s.attr)
    s1 = Something(5)
    print(s1.attr)
