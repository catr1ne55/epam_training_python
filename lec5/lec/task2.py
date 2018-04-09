#!/usr/bin/env python3
class SchoolMember:
    """Класс, описывающий человека, имеющего какое-либо отношение к школе(сотрудник, ученик и т.п.)."""

    def __init__(self, name, age):
        """Конструктор класса.

        :param name: Имя и фамилия человека.
        :type name: str.
        :param age: Возраст человека.
        :type age: int.
        """
        self.name = name
        self.age = age
        print('Создан SchoolMember: ' + self.name)

    def show(self):
        """Выводит на экран информацию о представителе класса SchoolMember.

        :param self: Представитель SchoolMember.
        :type self: SchoolMember
        :returns Nothing.
        :rtype None.
        """
        attributes = self.__dict__
        str2shw = ''
        for key in attributes.keys():
            str2shw += (key + ': ' + str(attributes[key]) + " ")
        print(str2shw)


class Teacher(SchoolMember):
    """Класс, наследник класса SchoolMember, отражает школьного учителя."""

    def __init__(self, name, age, salary):
        """Конструктор класса.

        :param name: Имя и фамилия учителя.
        :type name: str.
        :param age: Возраст учителя.
        :type age: int.
        :param salary: Зарплата учителя.
        :type salary: int.

        """
        super().__init__(name, age)
        self.salary = salary
        print('Создан Teacher: ' + self.name)


class Student(SchoolMember):
    """Класс, наследник класса SchoolMember, отражает ученика школы."""

    def __init__(self, name, age, grade):
        """ Конструктор класса.

        :param name: Имя и фамилия ученика.
        :type name: str.
        :param age: Возраст ученика.
        :type age: int.
        :param grade: Оценка ученика.
        :type grade: int.

        """
        super().__init__(name, age)
        self.grade = grade
        print('Создан Student: ' + self.name)


persons = [Teacher("Mr.Teacher", 40, 30), Student("Some Student", 16, 10)]
for p in persons:
    p.show()
