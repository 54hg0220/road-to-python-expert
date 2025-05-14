# 条件表达式的真值判断
# Python 中，以下值会被视为 False：
#
# None
# False
# 0（包括 0.0, 0j）
# 空序列或集合：'', [], {}, set(), range(0)
# 自定义对象中 __bool__() 或 __len__() 返回 False 或 0
if []:
    print("空列表是真的")
else:
    print("空列表是假的")  # ✅ 输出这个


# ⚡ 二、短路求值（Short-circuit Evaluation）
# Python 的 and 和 or 运算符具有短路行为，即：
#
# A and B：如果 A 是假，直接返回 A，不再计算 B
# A or B：如果 A 是真，直接返回 A，不再计算 B
# 示例：
def test():
    print("执行了 test()")
    return True


False and test()  # 不会执行 test()
True or test()  # 也不会执行 test()

name = input("请输入名字：") or "匿名用户"
print(name)

# 🧪 四、简洁写法：三元表达式（条件表达式）

x = 5
result = "正数" if x > 0 else "非正数"

# if 0 < x < 10 是合法的链式比较，等价于 0 < x and x < 10
