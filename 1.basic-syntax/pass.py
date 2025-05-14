# ✅ pass：空语句，占位用
# 📌 用法：
# pass 是一个什么都不做的语句。它通常用于：
#
# 占位：代码结构还没写好，但语法上需要有内容。
# 保持函数、类、循环等结构完整。
# 临时代码“跳过”某些逻辑。
def todo_feature():
    pass  # 以后再实现


for i in range(5):
    if i == 3:
        pass  # 暂时不处理 3
    else:
        print(i)

# ✅ ...（Ellipsis）：更“语义化”的占位符
# 📌 用法：
# ... 是 Python 中的 Ellipsis 对象，虽然它本身不会执行任何操作，但在某些场景下比 pass 更有“语义感”。
#
# 常用于函数、类、模块中表示“这里将来会有实现”。
# 在某些框架（如 FastAPI、Pydantic）中也被用作默认值或类型提示。


def future_logic(): ...


class MyClass:
    def method(self): ...


from typing import Any


def validate(data: Any) -> bool: ...
