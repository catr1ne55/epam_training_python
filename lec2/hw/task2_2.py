def select(*field_name: str) -> list:
    """ This function selects fields to be displayed.

     :param field_name: The fields to select.
     :type field_name: str
     :returns Selected fields.
     :rtype list
     """
    selected_fields = []
    for field in field_name:
        selected_fields.append(field)
    return selected_fields


def field_filter(field_name: str, *collection: list) -> dict:
    """ This function chooses certain values of given field.

    :param field_name: The field where the search will be implemented.
    :type field_name: str
    :param collection: The values of chosen field.
    :type collection: list
    :returns Selected field with it's values.
    :rtype dict
    """
    fields2filter = {}
    for c in collection:
        fields2filter[field_name] = c
    return fields2filter


def query(collection: list, select, *field_filters) -> list:
    """ This function handles requests to the given collection.

    :param collection: The given collection(list of dictionaries).
    :type collection: list
    :param select: The fields to display after getting the result.
    :type select: list
    :param field_filters: One or more filters to choose suitable parameters.
    :type dict
    :returns Filtered list which contains nly selected fields.
    :rtype list

    """
    result = []
    fields = {}
    for ff in field_filters:
        fields.update(ff)
    for c in collection:
        append2 = True
        for keys, values in fields.items():
            if c[keys] not in values:
                append2 = False
        if append2 is True:
            current = {}
            for key in select:
                current[key] = c[key]
            result.append(current)
    return result


friends = [{'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'email': 'email@email.com'},
           {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email1@email1.com'},
           {'name': 'Эми', 'gender': 'Женский', 'sport': 'Баскетбол', 'email': 'email2@email1.com'}]

res = query(friends, select('name', 'gender', 'sport'), field_filter('sport', ['Баскетбол']),
            field_filter('gender', ['Мужской', 'Женский']))
print(res)
