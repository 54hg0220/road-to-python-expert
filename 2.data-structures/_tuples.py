# 元组是 Python 中的内置数据结构，它与列表（List）非常相似，但是：
#
# 元组是不可变的（immutable）：创建之后就不能修改其内容。
#
# 用 小括号 () 表示（列表用方括号 []）。
my_tuple = (1, 2, 3)
# 你也可以省略括号：
my_tuple = 1, 2, 3  # 也是元组

# 要创建一个单元素元组，必须加逗号：
t = (1,)  # 是元组
not_t = 1  # 是整数

# t = (1, 2, 3)
# t[0] = 5       # ❌ 报错：'tuple' object does not support item assignment
# t.append(4)    # ❌ 报错：'tuple' object has no attribute 'append'


# 1. 访问元素（和列表一样）
t = (10, 20, 30)
print(t[1])  # 20
# 2. 切片
t[1:]  # (20, 30)
t[::-1]  # (30, 20, 10)
# 3. 解包（unpacking）
a, b, c = t
print(a)


# 4. 与函数结合使用（返回多个值）
def get_point():
    return (3, 4)


x, y = get_point()

# 不希望数据被修改时使用（如：函数参数、字典键等）
#
# 数据结构固定（如：数据库记录、坐标等）
#
# 更高性能（相比列表，元组更轻量）
import sys

l = [1, 2, 3]
t = (1, 2, 3)

print(sys.getsizeof(l))  # 比如输出 88
print(sys.getsizeof(t))  # 比如输出 64

# PyListObject 包含：
#
# 元素指针数组指针（ob_item）
#
# 已使用的元素数（ob_size）
#
# 已分配容量（allocated）👉 支持动态扩展
#
# PyTupleObject 是固定大小，内部直接是一个对象指针数组，没有冗余字段。
