isinstance(42, int)  # True
isinstance("hello", str)  # True
isinstance(3.14, float)  # True
isinstance([1, 2, 3], list)  # True
isinstance(42, (int, float))  # True
print(isinstance("hello", str))
# | 函数        | 说明           | 示例                            |
# | --------- | ------------ | ----------------------------- |
# | `int()`   | 转换为整数        | `int("42") → 42`              |
# | `float()` | 转换为浮点数       | `float("3.14") → 3.14`        |
# | `str()`   | 转换为字符串       | `str(42) → "42"`              |
# | `bool()`  | 转换为布尔值       | `bool(0) → False`             |
# | `list()`  | 转换为列表（可迭代对象） | `list("abc") → ['a','b','c']` |
print(int("42"))
# int("abc")  # ValueError: invalid literal for int()
print(int(3.7))  # → 3 （向下取整）
bool("")  # → False
bool("False")  # → True 这是个坑，非空字符串都是 True
