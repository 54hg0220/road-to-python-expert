sum([1, 2, 3, 4, 5])
# 背后实际调用的是 CPython 源码中的 C 函数（bltinmodule.c）：
# static PyObject *
# builtin_sum(PyObject *self, PyObject *args)
# {
#     // 省略参数校验部分
#     PyObject *iterable, *start = NULL;
#     // 省略初始化细节
#     // 然后会进入一个高效的迭代器处理逻辑
#     while ((item = PyIter_Next(iter)) != NULL) {
#         // sum = sum + item
#         PyObject *new_sum = PyNumber_Add(sum, item);
#         // ...
#     }
# }

# 这个 PyNumber_Add() 是对 + 运算的 C 层封装，
# 会检查对象是否支持加法运算（nb_add 方法），直接调对应对象的方法，
# 不会走 Python 的解释器字节码，因此效率远高于普通 Python 层的 for 循环加法。
import time

data = list(range(10_000_000))

start = time.time()
total = sum(data)
print("sum:", time.time() - start)

start = time.time()
total = 0
for i in data:
    total += i
print("loop:", time.time() - start)

# | 功能   | 内置函数/语法糖    | 是否 C 实现 | 推荐使用 |
# | ----  | ----------------- | ------- | ---- |
# | 求和   | `sum()`          | ✅       | ✅    |
# | 排序   | `sorted()`       | ✅       | ✅    |
# | 最大值  | `max()`           | ✅       | ✅    |
# | 遍历   | `enumerate()`     | ✅       | ✅    |
# | 映射   | `map()`           | ✅       | ✅    |
# | 过滤   | `filter()`        | ✅       | ✅    |
# | 条件检查 | `any()` / `all()` | ✅       | ✅    |
data = list(range(10_000_000))

# 使用内置 max 函数
start = time.time()
max_value_builtin = max(data)
builtin_time = time.time() - start

# 使用手写 for 循环找最大值
start = time.time()
max_value_loop = data[0]
for num in data:
    if num > max_value_loop:
        max_value_loop = num
loop_time = time.time() - start

print("loop time:", loop_time)
print("builtin_time:", builtin_time)
