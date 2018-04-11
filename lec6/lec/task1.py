#!/usr/bin/env python3


class Price:
    """Класс-дескриптор."""

    def __init__(self):
        """Конструктор. Создает словарь для хранения instance'ов класса-владельца."""

        self.values = {}

    def __get__(self, instance, owner):
        """Получения значения атрибута.

        :param instance: представитель класса Book.
        :type instance: Book.
        :param owner: class Book.
        :type owner: type.
        """

        return self.values.get(instance)

    def __set__(self, instance, value):
        """Изменение значения атрибута.

        :param instance: представитель класса Book.
        :type instance: Book.
        :param value: новое значение цены, должно быть от 0 до 100.
        :type value: int.
        """

        if not 0 < value < 100:
            raise ValueError("Price must be between 0 and 100.")
        self.values[instance] = value

    def __delete__(self, instance):
        """Удаление атрибута.
        :param instance: представитель класса Book.
        :type instance: Book.

        """
        del self.values[instance]


class Book:
    """Класс для описания библиотеки."""

    price = Price()

    def __init__(self, author, title, price):
        """Конструктор класса.

        :param author: Автор книги.
        :type author: str.
        :param title: Название книги.
        :type title: str.
        :param price: Стоимость книги.
        :type price: int.
        """
        self.author = author
        self.title = title
        self.price = price


if __name__ == '__main__':
    b = Book("12", "123", 11)
    print(b.price)
    b.price = 12
    print(b.price)
    b1 = Book("12", "143", 16)
    print(b1.price)
    print(b.price)
    b.price = -12
