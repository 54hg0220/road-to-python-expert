# 4.oop - 面向对象编程（OOP）
# 基础
# 类与对象的定义、self
# 构造函数 __init__
# 类变量 vs 实例变量
# 继承 & super()，MRO 查找顺序
# 类方法 @classmethod 与静态方法 @staticmethod
# 进阶
# 魔术方法：__str__ __repr__ __eq__ __lt__ __hash__ …
# 抽象类 abc.ABC、抽象方法 @abstractmethod
# 协议 typing.Protocol（结构化子类型，PEP 544）
# 描述符协议：__get__ __set__ __delete__
# 数据类 @dataclass（可变/冻结、slots=True、kw_only=True）
# 元类：自定义 type.__new__、类装配钩子
# 协变 / 逆变类型参数
# 多重继承冲突调试、菱形继承 & MRO 可视化


# 1. 类与对象的定义，self
# 类是对象的模板，对象是类的实例。
class Person:
    def say_hello(self):
        print("Hello")


p = Person()
p.say_hello()


# 2. 构造函数 __init__
# 构造函数在对象创建时自动调用，用于初始化对象的属性。\
class Person:
    def __init__(self, name):
        self.name = name


# 3. 类变量 vs 实例变量
# 类变量：所有实例共享，定义在类体中。
#
# 实例变量：每个实例独立拥有，通常在 __init__ 中定义。
#
class Example:
    class_var = 0  # 类变量

    def __init__(self):
        self.instance_var = 1  # 实例变量


# 4. 继承 & super()，MRO 查找顺序
class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")


dog1 = Dog()
dog1.speak()
# super() 调用父类方法。
#
# MRO（Method Resolution Order）：Python 使用 C3 线性化算法确定多继承中方法查找顺序，可用 类.__mro__ 或 help(类) 查看。


# 5. 类方法 @classmethod 与静态方法 @staticmethod
# @classmethod: 第一个参数是类 (cls)，可用于构造工厂函数。
#
# @staticmethod: 无 self/cls，更像普通函数，只是放在类里以归类。
class Example:
    @classmethod
    def create(cls):
        return cls()

    @staticmethod
    def add(x, y):
        return x + y


# 6. 魔术方法
# 常见有：
#
# __str__：用户友好字符串
#
# __repr__：开发者友好字符串
#
# __eq__, __lt__：比较运算符重载
#
# __hash__：可哈希对象
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# 7. 抽象类 abc.ABC 与 @abstractmethod
# 用于定义接口和模板方法，不能直接实例化。
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# 8. 协议 typing.Protocol（PEP 544）
# 结构化子类型，不强制继承，只要求“结构兼容”。
from typing import Protocol


class Drawable(Protocol):
    def draw(self) -> None: ...


class Circle:
    def draw(self):
        print("Drawing")


# 8. 协议 typing.Protocol（PEP 544）
# 结构化子类型，不强制继承，只要求“结构兼容”。
from typing import Protocol


class Drawable(Protocol):
    def draw(self) -> None: ...


class Circle:
    def draw(self):
        print("Drawing")


# 9. 描述符协议 __get__ __set__ __delete__
# 控制属性访问的底层机制（如 property 就是描述符）。
class Descriptor:
    def __get__(self, instance, owner):
        return "value"


# 10. 数据类 @dataclass
# 自动生成 __init__、__repr__、__eq__ 等方法。
from dataclasses import dataclass


@dataclass(frozen=True, slots=True, kw_only=True)
class Point:
    x: int
    y: int


from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int


b1 = Book("Python Basics", "Guan", 300)
b2 = Book("Python Basics", "Guan", 300)

print(b1)  # 自动生成 __repr__
print(b1 == b2)  # 自动生成 __eq__


# 等价于手写的：
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, pages={self.pages})"

    def __eq__(self, other):
        return (
            self.title == other.title
            and self.author == other.author
            and self.pages == other.pages
        )


# 11. 元类
# 类的类，本质上类是由 type 创建的。
#
# 可以通过重写 type.__new__ 实现类的自动注册、修改。
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)


# 12. 协变 / 逆变类型参数
# 泛型中类型参数的兼容性控制：
#
# 协变（+T）：子类可替代父类
#
# 逆变（-T）：父类可替代子类
from typing import TypeVar

T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


# 13. 多重继承冲突调试、菱形继承 & MRO 可视化
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.__mro__)  # 查看方法解析顺序


class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"👤 {self.username}"

    def __repr__(self):
        return f"User(username={self.username!r})"


u = User("guan")
print(str(u))  # __str__ -> 用户看到的
print(repr(u))  # __repr__ -> 开发调试用


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return (self.name, self.age) == (other.name, other.age)

    def __lt__(self, other):  # for sorting
        return self.age < other.age

    def __hash__(self):
        return hash((self.name, self.age))  # allows using in set/dict


p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
p3 = Person("Bob", 25)

print(p1 == p2)  # True
print(p1 < p3)  # False
print(set([p1, p2, p3]))  # 去重成功（需要 __hash__ 和 __eq__）
