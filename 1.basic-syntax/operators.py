# 🧮 一、算术运算符（Arithmetic Operators）
# 运算符	含义	示例	结果	说明
# +	加法	3 + 2	5	字符串拼接也适用：'a' + 'b'
# -	减法	5 - 3	2
# *	乘法	4 * 2	8	字符串重复：'a' * 3 → 'aaa'
# /	真除法	5 / 2	2.5	始终返回 float
# //	地板除法	5 // 2	2	向下取整，保留整数类型
# %	取模	5 % 2	1	结果符号与被除数相同
# **	幂运算	2 ** 3	8
print(7 // 2)  # 输出 3，因为 7 ÷ 2 = 3.5，向下取整是 3
print(-7 // 2)  # 输出 -4，因为 -7 ÷ 2 = -3.5，向下取整是 -4
print(-3 % 2)
# 🧾 二、比较运算符（Comparison Operators）
# 运算符	含义	示例	结果
# ==	等于	3 == 3	True
# !=	不等于	3 != 4	True
# <	小于	2 < 3	True
# >	大于	3 > 2	True
# <=	小于等于	2 <= 2	True
# >=	大于等于	3 >= 2	True
# Python 支持 链式比较：1 < x < 5 相当于 1 < x and x < 5

# 🔗 三、逻辑运算符（Logical Operators）
# 运算符	含义	示例	结果	说明
# and	与	True and False	False	两者都为真才为真
# or	或	True or False	True	任一为真即为真
# not	非	not True	False

a = [1]
b = [1]
print(a == b)  # True
print(a is b)  # False

x = 1
y = 1
print(x is y)

result = 3 + 4 * 2  # 结果是 11，而不是 14，因为 * 优先于 +

# 优先级	运算符类别	示例
# 1	括号 ()	(a + b) * c
# 2	幂运算 **	2 ** 3 ** 2
# 3	正负号 +x, -x	-a, +b
# 4	乘除 % // * /	a * b / c
# 5	加减 + -	a + b - c
# 6	比较运算符	== != < > <= >=
# 7	逻辑 not	not a
# 8	逻辑 and	a and b
# 9	逻辑 or	a or b
# 10	赋值 =	x = y + 1
