# 🧩 一、range()：生成一系列数字
# ✅ 基本语法：
for i in range(5):
    print(i)  # 输出 0 到 4

for i in range(1, 6):
    print(i)  # 输出 1 到 5

for i in range(10, 0, -2):
    print(i)  # 输出 10, 8, 6, 4, 2
# 🧩 二、enumerate()：为可迭代对象添加索引
# ✅ 基本语法：
# iterable：可以是列表、字符串、元组等。
# start：索引起始值，默认是 0。
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

strings = "hello world"
for index, s in enumerate(strings, start=1):
    print(index, s)
# 输出：
# 0 apple
# 1 banana
# 2 cherry

tasks = ["修复登录 bug", "优化数据库查询", "更新用户界面", "写单元测试"]

for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")

# ✅ zip()
# 用途：将多个可迭代对象“打包”在一起，返回的是元组对，适合多个列表并行遍历。
names = ["Tom", "Jerry", "Spike"]
scores = [90, 85, 88]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# ✅ any() 和 all()
# any(iterable)：
# 只要有一个元素是 True，返回 True。常用于判断“是否有满足条件的”。
scores = [0, 0, 75]
print(any(score > 60 for score in scores))  # True
# all(iterable)：
scores = [70, 80, 90]
print(all(score > 60 for score in scores))  # True

# ✅ sorted(iterable, key=…)
words = ["apple", "banana", "cherry"]
# 按照单词长度排序
sorted_words = sorted(words, key=len)
print(sorted_words)  # ['apple', 'banana', 'cherry']

# ✅ min(iterable, key=…) / max(iterable, key=…)
# 用途：找出“最小”或“最大”的元素，支持自定义比较规则。
words = ["apple", "banana", "cherry"]
longest_word = max(words, key=len)
print(longest_word)  # 'banana'

students = [("Tom", 90), ("Jerry", 85), ("Spike", 88)]
top_student = max(students, key=lambda x: x[1])
print(top_student)  # ('Tom', 90)

# 🧠 什么是生成器表达式？- Generator Expression
# 生成器表达式是一个不会立刻生成所有结果，而是每次按需生成一个的表达式。它的语法看起来很像列表推导式，但用的是 () 而不是 []。
# ✅ 举例对比
# 列表推导式（立刻生成全部结果）：
[x * x for x in range(10)]
# 生成器表达式（按需生成）：
(x * x for x in range(10))
# 🔄 惰性计算（Lazy Evaluation）
# 惰性计算的核心思想就是：只有在需要的时候才执行计算。
# 比如处理一个很大的文件，统计字符总数：
# with open("large.txt") as f:
#     total = sum(len(line) for line in f)  # 不读入所有行，占内存极低

squares = (x * x for x in range(10))
print(next(squares))  # 0
print(next(squares))  # 1
print(next(squares))  # 4
import sys

# 列表推导式：会马上生成所有结果
list_expr = [x * x for x in range(1_000)]

# 生成器表达式：只是一个生成器对象，不生成数据
gen_expr = (x * x for x in range(1_000))

# 打印它们的内存大小
print("列表推导式占用内存（单位：字节）：", sys.getsizeof(list_expr))
print("生成器表达式占用内存（单位：字节）：", sys.getsizeof(gen_expr))

# 既然 sum(x*x for x in big_iter) 最后也要把所有结果“加起来”，
# 那和 sum([x*x for x in big_iter]) 先生成所有值、然后加，有什么内存区别？
# 生成器表达式（lazy）：一次只生成一个值，处理完就丢掉，占用的是常数级内存。
#
# 列表推导式（eager）：一次性生成所有值，占用的是线性内存（数量越多占用越多）。

# 🧠 什么是迭代器协议（Iterator Protocol）？
# 在 Python 中，迭代器协议指的是一个对象必须实现两个方法：
#
# ✅ 1. __iter__()
# 返回迭代器本身（对象要“可迭代”）
#
# ✅ 2. __next__()
# 每次调用返回下一个元素，如果没有了就抛出 StopIteration 异常。
#
# 只要一个对象同时实现了这两个方法，它就是一个合法的迭代器（iterator）。
nums = [1, 2, 3]
it = iter(nums)  # 得到一个迭代器对象

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # ❌ 抛出 StopIteration
# 🔹 iter(obj)
# 这是 Python 的内置函数，它会调用对象的 __iter__() 方法。
it = iter([1, 2, 3])  # 实际上等价于 [1, 2, 3].__iter__()


# ✅ 方法一：用普通类手动实现迭代器协议
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # 返回迭代器自身

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


# ✅ 方法二：用生成器函数（自动实现迭代器协议）
def countdown(start):
    while start > 0:
        yield start
        start -= 1


# 🧠 背后发生了什么？
# 当你使用 yield 时：
#
# Python 自动创建一个类，实现了 __iter__() 和 __next__()；
#
# 每次 next() 调用都会暂停函数运行，保存状态；
#
# 再次 next() 会从上一次的 yield 后继续执行。
import time


def concat_with_plus(n):
    s = ""
    for i in range(n):
        s += f"{i}\n"
    return s


def concat_with_yield(n):
    def gen():
        for i in range(n):
            yield f"{i}\n"

    return "".join(gen())


start = time.time()
concat_with_plus(100_000)
print("+= cost:", time.time() - start)

start = time.time()
concat_with_yield(100_000)
print("yield cost:", time.time() - start)
