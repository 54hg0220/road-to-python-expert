# 1. 闭包（Closure）原理
# 定义：闭包是一个函数记住了它定义时的作用域变量（自由变量），即使外层函数已经返回。
def outer(msg):
    def inner():
        print(msg)

    return inner


fn = outer("Hello")  # outer 返回了 inner，但 inner 仍然记得 msg="Hello"
fn()  # 输出：Hello


# 2. 基础装饰器（无参数）
# 装饰器本质上就是一个接收函数作为参数、返回新函数的函数。
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")

    return wrapper


@my_decorator
def say_hi():
    print("Hi!")


say_hi()
# 输出：
# Before function call
# Hi!
# After function call


# 3. 带参数的装饰器
# 需要多一层包装函数来接受参数。
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet():
    print("Hello!")


greet()


# 4. 多层装饰器嵌套
# 多个装饰器从内到外执行装饰过程，从外到内执行函数调用：
def deco1(f):
    def wrapper(*args, **kwargs):
        print("deco1")
        return f(*args, **kwargs)

    return wrapper


def deco2(f):
    def wrapper(*args, **kwargs):
        print("deco2")
        return f(*args, **kwargs)

    return wrapper


@deco1
@deco2
def say():
    print("Hi!")


from functools import wraps


# 5. functools.wraps 的作用
# 保留被装饰函数的元信息（如 __name__, __doc__）。
# 当你使用装饰器时，如果没有使用 @functools.wraps，被装饰的函数会变成你定义的那个“包裹函数”（通常叫 wrapper），从而丢失原函数的一些重要属性，比如：
#
# __name__（函数名）
#
# __doc__（函数注释）
#
# __annotations__（参数类型标注）
def deco(func):
    @wraps(func)
    def wrapper():
        """wrapper doc"""
        return func()

    return wrapper


@deco
def say_hi():
    """say_hi doc"""
    print("Hi")


print(say_hi.__name__)  # say_hi
print(say_hi.__doc__)  # say_hi doc


say()
# 输出：
# deco1
# deco2
# Hi!

#  1. @contextmanager 装饰器
# 来自 contextlib，可以将一个生成器函数变成上下文管理器。
from contextlib import contextmanager


@contextmanager
def open_file(path):
    f = open(path, "r")
    try:
        yield f
    finally:
        f.close()


with open_file("test.txt") as f:
    print(f.read())


# 2. 类装饰器（缓存 / 单例模式）
# 类也可以作为装饰器 —— 利用 __call__ 方法：
class Singleton:
    _instance = None

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        if not Singleton._instance:
            Singleton._instance = self.cls(*args, **kwargs)
        return Singleton._instance


@Singleton
class Database:
    def __init__(self):
        print("Connecting to DB")


db1 = Database()
db2 = Database()
print(db1 is db2)  # True

# 3. 注解感知装饰器（inspect.signature）
# 装饰器可以检查并修改函数签名。
import inspect
from functools import wraps


def type_check(func):
    sig = inspect.signature(func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            expected_type = func.__annotations__.get(name)
            if expected_type and not isinstance(value, expected_type):
                raise TypeError(f"{name} must be {expected_type}")
        return func(*args, **kwargs)

    return wrapper


@type_check
def add(x: int, y: int) -> int:
    return x + y


add(1, 2)  # OK
add("1", "2")  # TypeError
# 类型检查、签名增强
