import time


class Manager:
    def __init__(self):
        pass

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Время выполнения кода =", time.time() - self.start)
        return True


with Manager():
    x = 18 ** 10000000


