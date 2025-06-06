# lambda function
f = lambda x, y: x + y
print(f(2, 3))  # 输出 5

from functools import reduce

# map(func, iterable)：对 iterable 中每个元素应用 func。
#
# filter(func, iterable)：筛选使 func(x) 为 True 的元素。
#
# reduce(func, iterable)：将 iterable 从左到右累积合并（需 from functools import reduce）。
print(list(map(lambda x: x**2, [1, 2, 3])))  # [1, 4, 9]
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3])))  # [2]
print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))  # 10


# 3. 生成器（yield）与生成器表达式
# yield 把函数变成生成器函数，返回一个惰性迭代器。
#
# 可中断、恢复状态，适合节省内存。
def gen():
    yield 1
    yield 2


g = gen()
print(next(g))  # 1
print(next(g))  # 2
g = (x * x for x in range(3))
for i in g:
    print(i)  # 0 1 4


# 4. 迭代器协议（__iter__, __next__）
# 任何实现了 __iter__() 和 __next__() 方法的对象都是迭代器：
class MyIter:
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < 3:
            val = self.i
            self.i += 1
            return val
        else:
            raise StopIteration


# 5. itertools 常用函数（基础）
import itertools

# print(list(itertools.count(10, 2)))  # 无限迭代器：10, 12, 14, ...
# print(list(itertools.cycle("AB")))  # 无限轮转：A B A B ...
print(list(itertools.repeat(42, 3)))  # [42, 42, 42]
print(list(itertools.chain("AB", "CD")))  # ['A', 'B', 'C', 'D']


# 6. 生成器的 send / throw / close
def my_gen():
    val = yield "start"
    yield f"received {val}"


g = my_gen()
print(next(g))  # "start"
print(g.send("hello"))  # "received hello"
g.close()


# 7. yield from（委托生成器）
# 将子生成器的值“代理”给外部调用者，语法糖：
def subgen():
    yield 1
    yield 2


def delegator():
    yield from subgen()
    yield 3


print(list(delegator()))  # [1, 2, 3]


import itertools

# tee：复制迭代器为多个独立副本
a, b = itertools.tee(range(3))
print(list(a))  # [0, 1, 2]
print(list(b))  # [0, 1, 2]

# groupby：按 key 分组（注意：要先排序）
data = [("a", 1), ("a", 2), ("b", 3)]
for k, g in itertools.groupby(data, key=lambda x: x[0]):
    print(k, list(g))

# accumulate：累计求和 / 累计乘积等
from operator import mul

print(list(itertools.accumulate([1, 2, 3, 4])))  # [1, 3, 6, 10]
print(list(itertools.accumulate([1, 2, 3, 4], mul)))  # [1, 2, 6, 24]

# pairwise（3.10+）：成对组合前后项
print(list(itertools.pairwise("ABCD")))  # [('A', 'B'), ('B', 'C'), ('C', 'D')]
