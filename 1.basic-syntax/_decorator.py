import functools


def my_decorator(func):
    @functools.wraps(func)  # 保留原函数的元信息
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[DEBUG] {func.__name__} returned {result}")
        return result

    return wrapper


@my_decorator
def add(x, y):
    """Add two numbers."""
    return x + y


add(3, 4)
