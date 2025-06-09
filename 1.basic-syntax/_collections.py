from collections import Counter, defaultdict, deque, namedtuple

c = Counter("abacaba")
print(c)  # Counter({'a': 4, 'b': 2, 'c': 1})

d = defaultdict(list)
d["a"].append(1)
d["b"].append(2)
print(d)

dq = deque([1, 2, 3])
dq.appendleft(0)  # O(1)
print(dq)

Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x, p.y)

# 多用 Counter 简化频率类代码；
#
# defaultdict 是处理嵌套结构的神器；
#
# 如果需要环形队列，deque 是更高效的替代；
#
# 对象 + 元组兼得的简洁结构可用 namedtuple，但推荐 Python 3.7+ 用 dataclass 替代。

# ✅ 核心概念 & 场景
# 它提供了很多“懒计算”的迭代工具。适用于生成器、组合、排列、无限序列、数据流等处理。
from itertools import product, permutations, chain, groupby

list(product([1, 2], repeat=2))  # [(1,1), (1,2), (2,1), (2,2)]
list(chain([1, 2], [3, 4]))  # [1, 2, 3, 4]

data = [("A", 1), ("A", 2), ("B", 3)]
for k, g in groupby(data, key=lambda x: x[0]):
    print(k, list(g))

from itertools import islice

data = [10, 20, 30, 40, 50, 60, 70]
result = islice(data, 2, 5)
print(list(result))  # 输出: [30, 40, 50]
print(data[2:5])

# itertools 更适合用于数据处理 pipeline；
#
# islice 替代列表切片；
#
# groupby 必须预先排序。
