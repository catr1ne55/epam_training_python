def add(name, number, td):
    """ This function adds person's name and number into telephone directory."""
    if name not in td.keys():
        td.setdefault(name, [number])
    else:
        td[name].append(number)


def print_number(*names, td):
    """ This function prints name and number(can be more than one), if they are in telephone directory."""
    print('%-20s%-15s' % ('Имя', 'Номер'))
    for name in names:
        if name in td.keys():
            for tel_num in td[name]:
                print('%-20s%-15s' % (name, tel_num))


def delete(name, td):
    """ This function deletes name and its telephone number if the name is in telephone directory
        or print the message otherwise."""
    if name not in td.keys():
        print("Такого имени нет в справочнике!")
    else:
        del td[name]


telephone_directory = {}


while True:
    action = input("Что Вы хотите сделать: add, print, delete, exit? > ")
    if action == "exit":
        print("Работа завершена.")
        break
    elif action == "add":
        name = input("Введите имя > ")
        number = input("Введите номер > ")
        add(name, number, telephone_directory)
    elif action == "print":
        names = input("Введите имена через запятую > ").split(",")
        print_number(*names, td=telephone_directory)
    elif action == "delete":
        name = input("Введите имя > ")
        delete(name, telephone_directory)

