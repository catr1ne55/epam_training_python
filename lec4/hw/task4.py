def top_students(students, number):
    """Функция, возвращающая топ студентов(количество записей в топе задается параметром number) по каждому курсу.

    :param students: Список словарей с информацией о студентах, в которых ключами являются 'name', 'rate', 'course'.
    :type students: list.
    :param number: Количество записей для вывода в топе.
    :type number: int.
    :rtype None
    """
    for course in set([i['course'] for i in students]):
        print("Top-{} on {}".format(number, course))
        for item in map(lambda x: (x['name'], x['rate']),
                        sorted(list(filter(lambda x: x['course'] == course, students)),
                               key=lambda y: y['rate'], reverse=True)[:number]):
            print("{}, rate = {}".format(item[0], item[1]))


data = [{'name': 'Alexey', 'rate': 2, 'course': 'Python'},
        {'name': 'Alex', 'rate': 25, 'course': 'Python'},
        {'name': 'Andrey', 'rate': 12, 'course': 'R'},
        {'name': 'Daria', 'rate': 21, 'course': 'Java'},
        {'name': 'Petr', 'rate': 10, 'course': 'Python'},
        {'name': 'Ann', 'rate': 2, 'course': 'R'},
        {'name': 'Amy', 'rate': 40, 'course': 'R'},
        {'name': 'Andrey1', 'rate': 1, 'course': 'R'}]

top_students(data, 1)
