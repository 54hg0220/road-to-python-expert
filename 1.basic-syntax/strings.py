# 🧩 一、字符串基础操作
# 1. 切片（slicing）
text = "hello world"
print(text[0:5])  # 输出 'hello'
print(text[6:])  # 输出 'world'
# start：起始索引（包含）
# stop：结束索引（不包含）
# step：步长（默认为 1）
# sequence[start:stop:step]
print(text[::-1])  # dlrow olleh
text = "abcdefg"
print(text[::2])  # 输出 'aceg'，每隔一个取一个
print(text[::-1])  # 输出 'gfedcba'，反转字符串
print(text[1:6:2])  # 输出 'bdf'
# ✅ 负索引（从右往左数）：
text = "hello"
print(text[-1])  # 输出 'o'，最后一个字符
print(text[-2:])  # 输出 'lo'
# 2. join()：把列表拼成字符串
words = ["Python", "is", "awesome"]
print(" ".join(words))  # 输出 'Python is awesome'
print("".join(words))
# 3. split()：把字符串拆成列表
text = "apple,banana,orange"
print(text.split(","))  # 输出 ['apple', 'banana', 'orange']
# 4. strip()：去除首尾空白或指定字符
text = "  hello  "
print(text.strip())  # 输出 'hello'

url = "https://example.com/"
print(url.strip("/"))  # 输出 'https:example.com'
# 5. startswith() / endswith()：判断前缀或后缀
filename = "report.pdf"
print(filename.endswith(".pdf"))  # True
print(filename.startswith("report"))  # True

# f string
name = "Guan"
age = 28
print(f"My name is {name} and I am {age} years old.")
# 输出：My name is Guan and I am 28 years old.

pi = 3.1415926
print(f"{pi:.2f}")  # 保留两位小数：3.14
print(f"{pi:10.2f}")  # 宽度10，右对齐：      3.14
print(f"{pi:<10.2f}")  # 宽度10，左对齐：3.14
