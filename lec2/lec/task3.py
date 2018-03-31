def wrapper(func):
    def f(*args, **kwargs):
        print("Function name: " + func.__name__)
        func(*args, **kwargs)
    return f


wr = wrapper(print)
wr("Hello", "world", "!")