# 🧩 一、列表推导式（List Comprehension）
# ✅ 语法结构：
# [表达式 for 变量 in 可迭代对象 if 条件]
squares = [x**2 for x in range(5)]
# 输出: [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]
# 输出: [0, 2, 4, 6, 8]

# 🧩 二、字典推导式（Dict Comprehension）
# ✅ 语法结构：
# {键表达式: 值表达式 for 变量 in 可迭代对象 if 条件}
squares = {x: x**2 for x in range(5)}
# 输出: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 反转字典
original = {"a": 1, "b": 2}
reversed_dict = {v: k for k, v in original.items()}
# 输出: {1: 'a', 2: 'b'}

# 🧩 三、集合推导式（Set Comprehension）
# ✅ 语法结构：
# {表达式 for 变量 in 可迭代对象 if 条件}
unique_squares = {x**2 for x in [1, 2, 2, 3, 3, 3]}
# 输出: {1, 4, 9}

# 类型	语法结构	特点
# 列表推导式	[表达式 for 变量 in 可迭代对象 if 条件]	结果是列表，允许重复
# 字典推导式	{键: 值 for 变量 in 可迭代对象 if 条件]	结果是字典，键唯一
# 集合推导式	{表达式 for 变量 in 可迭代对象 if 条件]	结果是集合，自动去重

users = [
    {"name": "Alice", "email": "Alice@Example.com"},
    {"name": "Bob", "email": "BOB@Example.com"},
]

emails = [user["email"].lower() for user in users]
# 输出: ['alice@example.com', 'bob@example.com']

logs = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "127.0.0.1"]
unique_ips = {ip for ip in logs if not ip.startswith("127.")}
# 输出: {'192.168.1.1', '10.0.0.1'}

matrix = [[1, 2, 3], [4, 5, 6]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# 输出: [[1, 4], [2, 5], [3, 6]]

text = "Python is great and python is fun"
unique_words = {word.lower() for word in text.split()}
print(unique_words)
# 输出: {'python', 'is', 'great', 'and', 'fun'}
