from collections import deque

dq = deque()
# | 方法                 | 作用             |
# | ------------------ | -------------- |
# | `append(x)`        | 在右侧添加元素（栈/队列尾） |
# | `appendleft(x)`    | 在左侧添加元素        |
# | `pop()`            | 从右侧弹出元素（栈尾）    |
# | `popleft()`        | 从左侧弹出元素（队首）    |
# | `extend(iter)`     | 右侧批量添加         |
# | `extendleft(iter)` | 左侧批量添加         |
# | `clear()`          | 清空队列/栈         |
dq.appendleft(1)
dq.appendleft(2)
print(dq)

stack = deque()

# 入栈
stack.append("a")
stack.append("b")
stack.append("c")
# stack.appendleft("a")
# stack.appendleft("b")
# stack.appendleft("c")

# 出栈
print(stack)
print(stack.pop())  # 输出: c
print(stack.pop())  # 输出: b

# FIFO
queue = deque()

# 入队
queue.append("a")
queue.append("b")
queue.append("c")

# 出队
print(queue.popleft())  # 输出: a
print(queue.popleft())  # 输出: b

# ⏱ 四、为什么不推荐用 list？
# 用 list 实现队列会有性能问题，因为 list.pop(0) 是 O(n) 时间复杂度（需要移动所有元素），而 deque.popleft() 是 O(1)，更高效。
