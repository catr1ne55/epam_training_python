import time
import datetime
import traceback


class Manager:
    """ Контекстный менеджер.
    Выводит в файл (указанный при конструировании менеджера) информацию по возникшей ошибке в коде,
    обернутом контекстным менеджером, дате, времени выполнения кода.
    Ошибка прокидывается выше. Если ошибки не возникло - файл не перезаписывается."""

    def __init__(self, filename):
        """ Конструктор менеджера.

        :param filename: Имя файла, в который хотим записать информацию.
        :type filename: str.
        """

        self.filename = filename

    def __enter__(self):
        """ Начинаем отсчет времени выполнения кода. """

        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Если ошибок в коде не нашлось, то с файлом ничего не происходит.
        Иначе - записываем в файл дату, время выполнения и информацию об ошибке(тип исключения и сообщение). """

        if exc_type is not None:
            current_date = datetime.datetime.now()
            working_time = time.time() - self.start
            with open(self.filename, 'w') as file:
                file.write("Дата: " + current_date.strftime("%d-%m-%Y") + '\n')
                file.write("Время выполнения кода = " + str(working_time) + '\n')
                file.write("Информация об ошибке: " + '\n' + traceback.format_exception_only(exc_type, exc_val)[0])


if __name__ == '__main__':
    with Manager('text.txt'):
        x = 18 ** 10000000
        raise Exception("Oooops! I did it again!")
