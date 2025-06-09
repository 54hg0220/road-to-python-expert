# 1. 基本类型注解
# 使用 int, str, bool, List[int], Dict[str, float] 等对函数参数和返回值进行注解：
def greet(name: str) -> str:
    return f"Hello, {name}"


from typing import List


def average(scores: List[int]) -> float:
    return sum(scores) / len(scores)


# 2. Optional, Union, Literal, TypedDict
# Optional[X]: 表示值可以是 X 或 None，等同于 Union[X, None]
#
# Union[X, Y]: 值可以是 X 或 Y
#
# Literal: 限制值只能取特定的字面量
#
# TypedDict: 给字典添加类型约束
from typing import Optional, Union, Literal, TypedDict


def get_user(age: Optional[int]) -> str: ...


def process(value: Union[int, str]) -> None: ...


def vote(choice: Literal["yes", "no"]) -> bool:
    return choice == "yes"


class UserInfo(TypedDict):
    name: str
    age: int


# 3. Callable, Any, TypeVar, Generic
# Callable: 类型为函数，参数类型和返回值类型都可注解
#
# Any: 跳过类型检查
#
# TypeVar: 用于泛型
#
# Generic: 构建支持泛型的类
from typing import Callable, Any, TypeVar, Generic

F = Callable[[int, str], bool]
T = TypeVar("T")


def func(f: F) -> bool:
    return f(1, "x")


class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value


# # 4. 使用 mypy 进行类型检查
# # mypy 是主流 Python 静态类型检查工具：
# def square(x: int) -> int:
#     return x * x
#
#
# square("hello")  # mypy 会报错

# 5. pydantic 数据验证
# Pydantic 利用类型注解自动进行 数据解析 + 校验：
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


u = User(name="Tom", age="20")  # 自动将 "20" 转为 int


# 6. PEP 604 (X | Y 联合类型)
# Python 3.10+ 可以用 int | str 替代 Union[int, str]：
def parse(value: int | str) -> str:
    return str(value)


# 7. PEP 681, PEP 695
# PEP 681：@dataclass_transform 支持自定义类作为数据模型基础（用于框架如 SQLModel / Pydantic）
#
# PEP 695：Python 3.12 引入的语法，支持原生泛型类定义：
# PEP 695 原生泛型（Python 3.12+）
class Box[T]:
    def __init__(self, content: T): ...


# 8. typing_extensions 前瞻特性
# Self: 注明方法返回当前实例（如链式调用）
#
# Never: 表示永远不会返回（如异常抛出）
#
# Required / NotRequired: 用于 TypedDict 指定字段是否必须
from typing_extensions import Self


class Chain:
    def do(self) -> Self:
        return self


# 9. FastAPI + Pydantic 2.x 模型
# FastAPI 使用 pydantic 的 BaseModel 来声明请求/响应数据结构，Pydantic v2 支持更快、更灵活的校验：
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float


# @app.post("/items/")
# def create_item(item: Item): ...
