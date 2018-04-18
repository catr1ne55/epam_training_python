import time
import contextlib


@contextlib.contextmanager
def Manager():
    start = time.time()
    yield
    print("Время выполнения кода =", time.time() - start)


with Manager():
    x = 2 ** 1000