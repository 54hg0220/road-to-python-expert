# 🧠 一、变量作用域与 LEGB 规则
# Python 查找变量的顺序遵循 LEGB 规则，这是四个作用域的缩写：
#
# 缩写	含义	举例
# L	Local（局部作用域）	函数内部定义的变量
# E	Enclosing（闭包作用域）	嵌套函数外层函数的变量
# G	Global（全局作用域）	模块级别定义的变量
# B	Built-in（内建作用域）	Python 内建的名字，如 len()、range()

# 🔍 查找顺序：当你访问一个变量时，Python 会按 L → E → G → B 的顺序查找。
x = "global"


def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # 输出 local

    inner()


outer()
