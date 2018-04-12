#!/usr/bin/env python3


def top_students(students, number):
    """Функция, возвращающая топ студентов(количество записей в топе задается параметром number) по каждому курсу.

    :param students: Список словарей с информацией о студентах, в которых ключами являются 'name', 'rate', 'course'.
    :type students: list.
    :param number: Количество записей для вывода в топе.
    :type number: int.
    :rtype None
    """
    print('\n'.join(get_top_table(students, number, course) for course in get_courses(students)))


def get_top_table(students, number, course):
    """Получить строки топ-студентов по каждому курсу.

    :param students: Список словарей с информацией о студентах, в которых ключами являются 'name', 'rate', 'course'.
    :type students: list.
    :param number: Число записей в топ-списке.
    :type number: int.
    :param course: Выбираемый курс.
    :type course: str.
    :returns Строка с информацией о топ-студентах.
    :rtype str.
    """

    return "Top-{} on {} \n".format(number, course) + \
           '\n'.join("{}, rate = {}".format(item[0], item[1]) for item in
                     get_name_rate(get_course_students(students, course))[:number])


def get_courses(students):
    """Получить все указанные курсы.

    :param students: Список словарей с информацией о студентах, в которых ключами являются 'name', 'rate', 'course'.
    :type students: list.
    :returns Множество всех объявленных курсов.
    :rtype set.
    """

    return set([i['course'] for i in students])


def get_course_students(students, course):
    """Получить отсортированный по убыванию значения оценки список студентов, у которых есть оценка по данному курсу.

    :param students: Список словарей с информацией о студентах, в которых ключами являются 'name', 'rate', 'course'.
    :type students: list.
    :param course: Выбираемый курс.
    :type course: str.
    :returns Список студентов, у которых есть запись о данном курсе.
    :rtype list.
    """

    return sorted(list(filter(lambda x: x['course'] == course, students)),
                  key=lambda y: y['rate'], reverse=True)


def get_name_rate(students):
    """Получить пары имя-оценка.

    :param students: Список словарей с информацией о студентах, в которых ключами являются 'name', 'rate', 'course'.
    :type students: list.
    :returns Список пар имя-оценка.
    :rtype list.
    """

    return list(map(lambda x: (x['name'], x['rate']), students))


def data():
    """Возвращает данные."""

    return [{'name': 'Alexey', 'rate': 2, 'course': 'Python'},
            {'name': 'Alex', 'rate': 25, 'course': 'Python'},
            {'name': 'Andrey', 'rate': 12, 'course': 'R'},
            {'name': 'Daria', 'rate': 21, 'course': 'Java'},
            {'name': 'Petr', 'rate': 10, 'course': 'Python'},
            {'name': 'Ann', 'rate': 2, 'course': 'R'},
            {'name': 'Amy', 'rate': 40, 'course': 'R'},
            {'name': 'Andrey1', 'rate': 1, 'course': 'R'}]


if __name__ == '__main__':
    top_students(data(), 3)
