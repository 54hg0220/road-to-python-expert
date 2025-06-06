# 1. 创建列表
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True]
# 2. 访问元素（索引从 0 开始）
print(fruits[0])  # "apple"
print(fruits[-1])  # "cherry"，负数表示从后往前数
# 3. 修改元素
fruits[1] = "orange"  # 修改第二个元素
# 4. 添加元素
fruits.append("grape")  # 追加到末尾
fruits.insert(1, "lemon")  # 插入到指定位置
print(fruits)
# 5. 删除元素
fruits.remove("orange")  # 删除指定元素
fruits.pop()  # 删除最后一个元素并返回它
del fruits[0]  # 删除指定索引的元素
print(fruits.pop())

len(fruits)  # 获取长度
"apple" in fruits  # 判断是否存在
fruits.index("apple")  # 获取索引
fruits.sort()  # 排序（默认升序）
fruits.reverse()  # 倒序

# 列表切片（Slicing）
# list[start:stop:step]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers[2:5]  # [2, 3, 4]
numbers[:4]  # [0, 1, 2, 3]
numbers[6:]  # [6, 7, 8, 9]
numbers[::2]  # [0, 2, 4, 6, 8]：每隔一个取一个
numbers[::-1]  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]：倒序

# 1. 复制列表
# new_list = old_list[:]  # 切片复制
# 2. 替换多个值
# numbers[1:4] = [10, 11, 12]
# 3. 删除多个值
# numbers[2:5] = []  # 删除索引 2 到 4 的元素
