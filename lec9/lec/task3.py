import contextlib
import time


class Manager(contextlib.ContextDecorator):
    def __init__(self):
        pass

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Время выполнения кода =", time.time() - self.start)
        return True


@Manager()
def func(x):
    return 2 ** x


with Manager():
    print(2 ** 100)

func(100)