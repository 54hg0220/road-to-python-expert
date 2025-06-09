# 上下文管理器（Context Manager）是 Python 中用于管理资源的机制，比如文件、数据库连接、锁等。它的核心原理就是通过实现两个特殊方法：
#
# __enter__()
# __exit__()
# 这两个方法配合 with 语句使用，可以确保资源在使用后被正确释放，即使中间发生异常也能自动清理。
from contextlib import contextmanager


class MyContext:
    def __enter__(self):
        print("进入上下文")
        return self  # 可以返回任何对象

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出上下文")
        if exc_type:
            print(f"发生异常：{exc_type}, {exc_val}")
        return False  # 如果返回 True，异常会被吞掉


with MyContext() as ctx:
    print("处理中间逻辑")
    # raise ValueError("测试异常")  # 可以试试抛出异常

# ✅ 总结
# 结构	说明
# with add_log_handler(...)	使用上下文管理器
# __enter__()	设置日志捕获环境
# __exit__()	恢复原始日志状态
# capfd.readouterr()	捕获标准输出/错误（pytest 提供）

import time
from contextlib import contextmanager


# 模拟资源获取函数
def acquire_resource(timeout=10):
    print(f"[连接数据库] 正在连接...（超时：{timeout}s）")
    time.sleep(1)  # 模拟连接耗时
    return {"connection": "db_connection_object", "timeout": timeout}


# 模拟资源释放函数
def release_resource(resource):
    print(f"[释放数据库] 连接已关闭：{resource['connection']}")


# 上下文管理器
@contextmanager
def managed_resource(*args, **kwargs):
    resource = acquire_resource(*args, **kwargs)
    try:
        yield resource
    finally:
        release_resource(resource)


# 使用上下文管理器
with managed_resource(timeout=5) as conn:
    print(f"[处理中] 使用连接：{conn['connection']}")
    # raise Exception("模拟异常")  # 即使这里抛异常也会释放资源
