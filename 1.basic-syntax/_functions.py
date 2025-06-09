# 1️⃣ 默认参数和关键字参数
# ✅ 默认参数（Default Parameters）
# 你可以为函数参数设置默认值，这样在调用函数时可以省略这些参数。
def greet(name, message="你好"):
    return f"{message}，{name}！"


print(greet("小明"))  # 输出：你好，小明！
print(greet("小红", "欢迎"))  # 输出：欢迎，小红！


# ✅ 关键字参数（Keyword Arguments）
# 调用函数时，可以通过“参数名=值”的方式传参，顺序可以不一致。
def introduce(name, age, city):
    print(f"{name}，{age}岁，来自{city}")


introduce(age=28, name="小李", city="上海")


# 2️⃣ 可变参数（*args, **kwargs）
# ✅ *args：接收任意数量的位置参数（变成元组）
def add_all(*args):
    return sum(args)


print(add_all(1, 2, 3, 4))  # 输出 10


# ✅ **kwargs：接收任意数量的关键字参数（变成字典）
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# 对所有传进去的args 进行同样的操作
def log_message(level, *args):
    message = " ".join(str(arg) for arg in args)
    print(f"[{level.upper()}] {message}")


log_message("info", "Guan", "logged", "in")

print_info(name="小王", age=30, city="北京")


def send_notification(*recipients, **options):
    message = options.get("message", "您有一条新通知")
    urgent = options.get("urgent", False)
    method = options.get("method", "email")

    for recipient in recipients:
        print(f"发送给 {recipient}：{message}（方式：{method}，紧急：{urgent}）")


send_notification(
    "Guan",
    "Wei",
    "Ash",
)


# ✅ 混合使用顺序（推荐记忆口诀）：
# **普通参数 → 默认参数 → *args → kwargs

# 3️⃣ 匿名函数（lambda）
# lambda 是一种简洁的函数定义方式，适合写一些简单的一行函数。
add = lambda x, y: x + y
print(add(3, 5))  # 输出 8

names = ["Alice", "Bob", "Charlie"]
# 按名字长度排序
sorted_names = sorted(names, key=lambda name: len(name))
print(sorted_names)  # 输出 ['Bob', 'Alice', 'Charlie']

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # 输出 [1, 4, 9, 16]

nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # 输出 [2, 4, 6]


def greet(name):
    return f"Hello, {name}!"


def call_func(func, value):
    return func(value)


print(call_func(greet, "Alice"))  # 输出：Hello, Alice!
