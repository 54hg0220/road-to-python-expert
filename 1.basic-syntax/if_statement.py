# 条件表达式的真值判断
# Python 中，以下值会被视为 False：
#
# None
# False
# 0（包括 0.0, 0j）
# 空序列或集合：'', [], {}, set(), range(0)
# 自定义对象中 __bool__() 或 __len__() 返回 False 或 0

# 🧪 四、简洁写法：三元表达式（条件表达式）

x = 5
result = "正数" if x > 0 else "非正数"

# if 0 < x < 10 是合法的链式比较，等价于 0 < x and x < 10
