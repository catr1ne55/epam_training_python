#!/usr/bin/env python3


import abc


class Vehicle(metaclass=abc.ABCMeta):
    """Абстрактный класс, описывающий транспортное средство.
    В качестве атрибутов имеет количество колес т.с..

    """
    wheels = 0

    def __init__(self, year, model, base_price, km):
        """Конструктор класса.

        :param year: Год выпуска т.с..
        :type year: int.
        :param model: Модель т.с..
        :type model: str.
        :param base_price: Стоимость т.с. при условии, что не было пройдено нулевое расстояние.
        :type base_price: int.
        :param km: пройденное расстояние.
        :type km: int.
        """
        self.base_price = base_price
        self.year = year
        self.model = model
        self.km = km

    @abc.abstractmethod
    def vehicle_type(self):
        """Абсрактный метод, возвращающий тип т.с.."""
        pass

    @classmethod
    def is_motorcycle(cls):
        """Проверяет, является ли т.с. мотоциклом."""
        return cls.wheels == 2

    def purchase_price(self):
        """Возвращает стоимость т.с. в зависимости от количества пройденных километров."""
        return self.base_price - (.10 * self.km)


class Car(Vehicle):
    """Класс, описывающий автомобиль."""

    wheels = 4

    def vehicle_type(self):
        return "Car"


class Motorcycle(Vehicle):
    """Класс, описывающий мотоцикл."""

    wheels = 2

    def vehicle_type(self):
        return "Motorcycle"


class Truck(Vehicle):
    """Класс, описывающий грузовик."""

    wheels = 4

    def vehicle_type(self):
        return "Truck"


class Bus(Vehicle):
    """Класс, описывающий автобус."""

    wheels = 4

    def vehicle_type(self):
        return "Bus"


if __name__ == '__main__':
    car = Car(2001, 'o', 15000, 200)
    print(car.is_motorcycle())
    print(car.vehicle_type())
    print(car.purchase_price())
