import functools


def fabric(lambda_func):
    """Фабрика декоратор. Фабрика (функция) принимает аргумент - функцию(lambda) и декоратор.
    Возвращает декоратор, который должен вызывать функцию(lambda) с аргументом - результатом декорируемого декоратора.

    :param lambda_func: Лямбда-функция, которая применяется к результату декорируемого декоратора.
    :type lambda_func: function
    :returns wrapper: Декоратор, результат выполнения которого передается лямбда-функции.
    :rtype function
    """

    def wrapper(decorator):  # decorator - принимаемый декоратор
        @functools.wraps(decorator)
        def new_decorator(*dargs, **dkwargs):  # *dargs, **dkwargs - аргументы декоратора
            wrapped = decorator(*dargs, **dkwargs)

            def new_decorated_function(decorated_function):  # decorated_function - функция, декорируемая decorator'ом
                @functools.wraps(decorated_function)
                def new_func_args(*func_args, **func_kwargs):
                    if decorator.on:
                        return lambda_func((wrapped(decorated_function))(*func_args, **func_kwargs))
                    else:
                        return lambda_func(decorated_function(*func_args, **func_kwargs))

                return new_func_args

            return new_decorated_function

        def on():  # включение декоратора
            decorator.on = True

        def off():  # отключение декоратора
            decorator.on = False

        fabric.on = on
        fabric.off = off
        on()
        return new_decorator

    return wrapper


@fabric(lambda x: x ** 2)
def repeat(times):
    """Повторить вызов times раз и вернуть среднее значение.

    :param times: Количество повторений вызова декорируемой функции.
    :type times: int
    :returns wrap_func: Функция, считающая среднее значение вызова декорируемой функции.
    :rtype function
    """

    def wrap_func(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            sum = 0
            for i in range(times):
                sum += func(*args, **kwargs)
            return int(sum / times)

        return inner

    return wrap_func


@repeat(3)
def foo(*args, **kwargs):
    """Функция, которая печатает сообщение при вызове и возвращает число 3.

    :param args: Произвольные параметры.
    :param kwargs: Произвольные параметры.
    :returns 3
    :rtype int
    """
    print("Foo called!")
    return 3


print(foo([1, 3, 5]))

fabric.off()
print(foo([1, 3, 5]))
print(foo([1, 3, 5]))

fabric.on()
print(foo([1, 3, 5]))
