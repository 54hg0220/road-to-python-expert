# 🔹 什么是文件 I/O？
# 文件 I/O 是指程序与文件之间的 读写操作。在 Python 中，最常用的方式是使用 open() 函数打开文件，然后进行读取或写入。
#
# 🔹 with open() 是什么？
# with open() 是一种 上下文管理器（context manager） 的写法，它的好处是：
#
# 自动管理资源：文件用完后会自动关闭，不需要你手动调用 file.close()。
# 更安全：即使中途出错，文件也能被正确关闭，避免资源泄露。
# 读取文件内容
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 写入文件内容
with open("output.txt", "w") as file:
    file.write("Hello, Python!")

# 语法部分	含义
# with	启动一个上下文环境
# open('文件名', '模式')	打开文件，模式如 'r'（读）、'w'（写）、'a'（追加）等
# as file	将打开的文件对象赋值给变量 file
# file.read() / file.write()	进行读写操作
# 自动关闭	with 代码块结束后，文件会自动关闭

file.read()  # 读取整个文件内容
file.readline()  # 读取一行
file.readlines()  # 读取所有行，返回列表

file.write("text")  # 写入字符串
file.writelines([...])  # 写入多个字符串（不自动换行）

with open("data.txt", "r", encoding="utf-8") as f:
    ...


with open("example.txt", "r", encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())
