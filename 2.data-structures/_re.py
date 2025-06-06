# 一、字符串格式化
# Python 提供了三种主流的字符串格式化方式：
name = "Guan"
age = 30
# 使用 % 操作符（老式风格）
print("My name is %s and I am %d years old." % (name, age))
#  使用 str.format() 方法（推荐）
print("My name is {} and I am {} years old.".format(name, age))
print("My name is {0} and I am {1} years old. {0} is a good name.".format(name, age))
# 使用 f-strings（Python 3.6+ 推荐）
print(f"My name is {name} and I am {age} years old.")
import re

# | 函数             | 功能           |
# | -------------- | ------------ |
# | `re.search()`  | 搜索第一次匹配      |
# | `re.match()`   | 从字符串起始位置匹配   |
# | `re.findall()` | 找到所有匹配项，返回列表 |
# | `re.sub()`     | 替换           |
# | `re.split()`   | 分割           |
# | 表达式     | 含义              | 示例              |       |       |
# | ------- | --------------- | --------------- | ----- | ----- |
# | `.`     | 匹配任意字符（换行除外）    | `a.c` 可匹配 `abc` |       |       |
# | `\d`    | 数字（0-9）         | `\d{3}` 匹配3位数   |       |       |
# | `\w`    | 单词字符（字母、数字、下划线） | `\w+` 匹配单词      |       |       |
# | `\s`    | 空白字符（空格、制表符等）   |                 |       |       |
# | `^`     | 开头              | `^Hello`        |       |       |
# | `$`     | 结尾              | `world$`        |       |       |
# | `[...]` | 匹配字符集中的任意字符     | `[aeiou]` 匹配元音  |       |       |
# | \`a     | b\`             | 匹配a或b           | \`cat | dog\` |
# | `(…)`   | 分组提取            | `(\d+)-(\d+)`   |       |       |
# 提取手机号
text = "My number is 0412-345-678"
match = re.search(r"\d{4}-\d{3}-\d{3}", text)
print(match.group())  # 输出: 0412-345-678
# 替换敏感词
text = "This is a badword."
clean_text = re.sub(r"badword", "***", text)
print(clean_text)  # 输出: This is a ***
# 提取所有邮箱地址
emails = re.findall(
    r"\b[\w.-]+@[\w.-]+\.\w+\b", "Contact us: test@example.com, admin@abc.org"
)
print(emails)


text = "My name is Alice and I'm 25 years old"
pattern = r"My name is (?P<name>\w+) and I'm (?P<age>\d+)"
# | 正则符号 | 含义                                    |
# | ---- | ------------------------------------- |
# | `\w` | 匹配一个**字母、数字或下划线**（相当于 `[a-zA-Z0-9_]`） |
# | `+`  | 匹配**一个或多个**前面的字符                      |
# \d 数字
# \.	只匹配英文句号 . 本身
match = re.search(pattern, text)
print(match.group("name"))  # Alice
print(match.group("age"))  # 25

print(re.findall(r"\w+(?=\.)", "file.txt, another.pdf"))
print(
    re.findall(r"\b\w+\b(?!\.com)", "abc.com def.net ghi.org")
    # 输出: ['def', 'ghi']
)
