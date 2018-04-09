#!/usr/bin/env python3
import datetime


class Wine:
    """Класс, описывающий партию вина.
    Объект включает в себя название, марку, страну производства, дату производства и заметку.

    """

    def __init__(self, name: str, mark: str, country: str, date: datetime.date, note: str):
        """Конструктор класса.

        :param self: Представитель класса Wine.
        :type self: Wine.
        :param name: Название вина.
        :type name: str.
        :param mark: Марка вина.
        :type mark: str.
        :param country: Страна-производитель вина.
        :type country: str.
        :param date: Дата производства вина.
        :type date: datetime.date.
        :param note: Примечание.
        :type note: str.

        """
        self.name = name
        self.mark = mark
        self.country = country
        self.date = date
        self.note = note

    def count(self, current_date: datetime.date) -> int:
        """Возвращает выдержку вина в годах.

        :param self: Представитель класса Wine.
        :type self: Wine.
        :param current_date: Текущая дата.
        :type current_date: datetime.date.
        :returns years: Выдержка вина.
        :rtype int.
        """
        years = (current_date - self.date).days // 365
        return years


v = Wine('a', 'bb', 'F', datetime.date(1956, 11, 10), 'short note')
v.note = "sfsfsfs"
print(v.note)
print(v.count(datetime.date(2000, 11, 2)))
