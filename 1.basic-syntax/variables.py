# 变量（Variables）
# 定义方式：Python 是动态类型语言，不需要声明变量类型。
x = 10
name = "Alice"

# PEP 8 命名规范（Naming Conventions）
# 1. 变量名 / 函数名
# 使用 小写字母 + 下划线（snake_case）
user_name = "Alice"


def calculate_total():
    pass


# 2. 类名
# 使用 首字母大写的驼峰式命名（CapWords / PascalCase）
# 示例：
class UserProfile:
    pass


# 3. 常量名
# 使用 全大写字母 + 下划线
MAX_RETRIES = 5
PI = 3.14159

# 4. 私有变量 / 函数
# 使用 单下划线前缀 表示“内部使用”
_internal_value = 42


def _helper_function():
    pass


# 5. 强制私有（不建议使用）
# 使用 双下划线前缀，会触发名称重整（name mangling）
class MyClass:
    def __init__(self):
        self.__private_attr = 10


# 6. 模块名 / 包名
# 使用 小写字母，可以包含下划线

# 不可变对象示例 immutable
a = 10
b = a
a = a + 1
print(a, b)  # 输出: 11 10（a 和 b 指向不同的对象）

# 可变对象示例 mutable
list1 = [1, 2, 3]
list2 = list1
list1.append(4)
print(list1, list2)  # 输出: [1, 2, 3, 4] [1, 2, 3, 4]（list2 也被修改了）

# Python 中变量是如何管理内存的？
# 1. 变量是对象的引用（引用语义）
a = [1, 2, 3]
b = a  # b 和 a 指向同一个列表对象

# 2. 对象的内存结构
# 每个对象在内存中都有以下组成：
# 类型信息（type）：对象的类型（如 int, list）
# 引用计数（refcount）：有多少变量引用了这个对象
# 值内容（value）：对象实际存储的数据

import sys

x = [1, 2, 3]
b = x
print(sys.getrefcount(x))  # 通常会多一个引用，因为 getrefcount() 本身也引用了 x

# 4. 垃圾回收机制（Garbage Collection）
# 除了引用计数，Python 还使用 垃圾回收器（GC） 来处理 循环引用 的情况。
# Python 的 GC 使用 分代回收算法（Generational GC）
# 对象被分为三代（0、1、2），新对象在第 0 代，存活越久越可能被提升到更高代
# 使用 gc 模块可以手动控制垃圾回收
# 🧠 为什么需要垃圾回收？
# Python 使用 引用计数（Reference Counting） 来管理内存：每个对象都有一个引用计数器，记录有多少个变量或对象引用它。
#
# 当引用计数为 0 时，对象会被立即销毁。

import gc


class Node:
    def __init__(self, name):
        self.name = name
        self.partner = None

    def __del__(self):
        print(f"{self.name} 被销毁")


# 创建两个对象
a = Node("A")
b = Node("B")

# 形成循环引用
a.partner = b
b.partner = a

# 删除变量引用
del a
del b

# 手动触发垃圾回收
print("开始垃圾回收")
gc.collect()
print("垃圾回收完成")

# 5. 小整数缓存机制（Integer Caching）
# Python 会缓存常用的小整数（通常是 -5 到 256）和短字符串，以提高性能。
a = 100
b = 100
print(a is b)  # True，小整数缓存

x = 1000
y = 1000
# >>> x = 1000
# >>> y = 1000
# >>> x is y
# False
print(x is y)  # False，超出缓存范围
print(id(x), id(y))  # 它们可能在编译阶段就把 1000 作为常量池中的同一个对象处理。

# ✅ 总结：什么时候你需要关心 is 和对象内存地址？
# 场景	是否需要关心
# 判断是否为 None	✅ 使用 is
# 判断两个变量是否是同一个对象	✅ 使用 is
# 判断两个变量值是否相等	❌ 使用 ==
# 调试对象引用问题	✅ 使用 id() 和 is
# 写性能敏感代码（缓存、单例）	✅ 可能需要

# 6. 内存池机制（Memory Pool）
# Python（CPython 实现）使用 内存池机制（如 pymalloc） 来优化小对象的内存分配，减少频繁的系统调用。
# 🧠 为什么需要内存池机制？
# 在 Python 中，对象的创建和销毁非常频繁，尤其是小对象（如整数、字符串、列表等）。如果每次都向操作系统申请和释放内存，会带来：
#
# 性能开销大（系统调用慢）
# 内存碎片化严重
# 为了解决这个问题，CPython 实现了一个高效的内存管理机制 —— pymalloc 内存池机制。
# 🧱 pymalloc 内存池机制简介
# 📌 核心思想：
# 将小对象的内存分配交给 Python 自己管理，而不是频繁调用操作系统的 malloc/free。
#
# 📦 内存分配结构：
# Arena（竞技场）：2^20 字节（1MB）的大块内存，从操作系统申请。
# Pool（池）：Arena 被划分为多个 Pool，每个 Pool 大约 4KB。
# Block（块）：Pool 被划分为多个 Block，每个 Block 是实际分配给对象的内存单元。
# 🧩 Block 的大小：
# 只适用于 小对象（≤ 512 字节）
# Block 大小从 8 字节到 512 字节不等，按 8 字节对齐

# 当你写下：
x = 42
# Python 会从内存池中找一个大小合适的 Block（比如 16 字节）
# 如果没有，就从 Pool 中分配
# 如果 Pool 也满了，就从 Arena 中分配新的 Pool
print(sys.getsizeof(10))  # 小整数
print(sys.getsizeof("ok"))  # 小字符串
print(sys.getsizeof([]))  # 空列表
print(sys.getsizeof([0] * 1000))  # 大对象（可能超过 512 字节）
# 🧠 一、Python 中“一切皆对象”
# 在 Python 中，所有数据都是对象（object），包括整数、字符串、函数、类、模块等。
#
# 每个对象在内存中都有一个结构，通常包含：
#
# 组成部分	说明
# ob_refcnt	引用计数（用于内存管理）
# ob_type	对象类型（如 int、str）
# ob_size	对象大小（如列表长度）
# ob_data	实际数据内容

# 🧱 二、内存分配机制
# 1. 小对象（≤ 512 字节）
# 使用 pymalloc 内存池机制
# 分配自定义的内存块（Block）来提高效率
# 2. 大对象（> 512 字节）
# 直接调用操作系统的 malloc() 分配内存
# 不走内存池机制

# 🔁 三、变量与对象的关系（引用模型）
x = [1, 2, 3]
# x 是一个变量名，存储在栈（stack）中
# [1, 2, 3] 是一个对象，存储在堆（heap）中
# x 实际上是一个指针，指向堆中的对象

# 特性	C int	Python int
# 类型	原始类型	对象
# 存储位置	栈	堆
# 占用内存	通常 4 字节	通常 ≥ 28 字节
# 包含内容	仅值	引用计数、类型信息、值
# 性能	高效	相对较慢
