# 1.basic-syntax

This folder contains notes and examples for the 1.basic-syntax module.

### 基础  
- 变量、数据类型（`int`, `float`, `str`, `bool`）
- 算术 / 比较 / 逻辑运算符：`+  -  *  /  //  %  **`；`==  !=  <  >  <=  >=`；`and  or  not`  
- 运算符优先级 & 括号、链式比较（`0 < x < 10`）  
- 条件语句（`if`, `elif`, `else`）  
- 循环（`for`, `while`, `break`, `continue`，以及 `for … else` / `while … else`）  
- Augmented assignment：`+=  -=  *=  //= …`  
- 列表推导式 / 字典推导式 / 集合推导式  
- 函数定义与调用（`def`、返回值）  
- `*args` 和 `**kwargs` 的使用场景  
- 模块与导入（`import`, `from … import …`，`__name__ == "__main__"`）  
- 字符串基础操作：切片、`join/split`、`strip`、`startswith/endswith`  
- 通用切片语法：`seq[start:stop:step]`，负索引、步长 `-1` 反转  
- `range` 与 `enumerate(start=1)`  
- `pass` 空语句与 `…` (Ellipsis) 占位  
- 文件 I/O 与 `with open()`（上下文保证句柄释放）  
- 基本异常处理：`try-except-finally`；`raise ValueError()`  
- f-string 格式化（调试 / 日志首选）  

### 进阶  
- 变量作用域（LEGB 规则）、闭包捕获原理  
- 解包技巧（链式赋值、星号解包、交换变量）  
- 真假值、短路求值、三元表达式 `x if cond else y`  
- `enumerate`、`zip`、`any` / `all`、`sorted(key=…)`、`min/max(key=…)`  
- Walrus 赋值表达式 `:=`（3.8+）  
- 生成器表达式与惰性计算（`sum(x*x for x in big_iter)`）  
- 迭代器协议：`iter()` / `next()` / `StopIteration`  
- 第一类函数：函数作为参数、返回值、存入变量  
- 简易装饰器雏形（无参 + `functools.wraps`）  
- 上下文管理器原理（`__enter__`, `__exit__`）  
- 标准库精华：`collections`、`itertools`、`functools`、`pathlib`  
- 虚拟环境与包管理：`python -m venv`、`pipenv`、`poetry`  
- 内置函数背后的 C 实现 & 性能差异（`sum` vs 手写循环）  
- `isinstance()` / 显式类型转换（`int("42")` 等）  
