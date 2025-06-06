from collections import defaultdict

# ✅ defaultdict 功能：带默认值的字典
# 如果访问不存在的 key，会自动创建它并赋一个默认值，而不会抛出 KeyError。
#
# 🎯 使用场景：
# 字符统计
#
# 词频统计
#
# 多值映射（字典嵌套列表）
# 普通字典
d = {}
# d['a'].append(1) 会报错

# defaultdict 示例
d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
print(d)  # defaultdict(<class 'list'>, {'a': [1, 2]})

from collections import Counter

nums = [1, 2, 2, 3, 3, 3]
c = Counter(nums)
print(c)  # Counter({3: 3, 2: 2, 1: 1})
print(c[2])  # 2
print(c.most_common(1))  # [(3, 3)]
# | 写法                  | key   | value       | 实际结构                |
# | ------------------- | ----- | ----------- | ------------------- |
# | `d["a"] = [1]`      | `'a'` | `[1]`       | `{'a': [1]}`        |
# | `d["a"] += "hello"` | `'a'` | `"hello"`   | `{'a': 'hello'}`    |
# | `d["a"]["x"] = 123` | `'a'` | `{"x":123}` | `{'a': {'x': 123}}` |

import array

a = array.array("i", [1, 2, 3, 4])  # 'i' 表示整数类型
print(a[0])  # 输出 1

import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr[0])  # 输出 1

# memoryview
data = bytearray(b"hello world")
mv = memoryview(data)

print(mv[0])  # 104，对应 'h' 的 ASCII
mv[0] = 72  # 修改为大写 'H'

print(data)  # 输出: bytearray(b'Hello world')
# bytes：像字符串一样，只读
b = b"hello"  # 或 bytes("hello", "utf-8")
print(b[0])  # 输出: 104 (ASCII of 'h')
# b[0] = 72        # ❌ 报错：bytes 是不可变的
# bytearray：可读可改
ba = bytearray(b"hello")
ba[0] = 72  # 将 'h' 改为 'H'
print(ba)  # 输出: bytearray(b'Hello')
print(ba.decode())  # 输出: Hello

# 字典合并 |
a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}

c = a | b
print(c)  # {'x': 1, 'y': 99, 'z': 3}
a |= b
print(a)  # {'x': 1, 'y': 99, 'z': 3}

# heapq 实战：求前 K 个最大元素
import heapq

nums = [3, 1, 5, 12, 2, 11]
k = 3

# 用最小堆来保存最大的 k 个数
top_k = heapq.nlargest(k, nums)
print(top_k)  # 输出: [12, 11, 5]

# bisect 实战：有序列表中插入元素（保持顺序）
import bisect

grades = [60, 70, 80, 90]
new_score = 75

bisect.insort(grades, new_score)
print(grades)  # [60, 70, 75, 80, 90]

# array 实战：节省内存的大量整数处理
import array

arr = array.array("i", range(1000000))  # 'i' 表示整数
print(arr[0:5])  # array('i', [0, 1, 2, 3, 4])
print(arr.itemsize)  # 每个整数占 4 字节

# deque 实战：滑动窗口最大值
from collections import deque


def sliding_window_max(nums, k):
    dq = deque()
    result = []

    for i in range(len(nums)):
        # 移除不在窗口内的值
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # 移除比当前元素小的（保持单调递减）
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result


print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
# 输出: [3, 3, 5, 5, 6, 7]
