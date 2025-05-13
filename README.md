
# Python Mastery Roadmap

本指南旨在帮助你系统性地掌握 Python，从基础到高级，涵盖各个领域的知识点。你可以根据自己的掌握情况逐项检查，针对薄弱点重点学习。

---

## 🟢 基础语法与核心概念

### 基础
- 变量、数据类型（int, float, str, bool）
- 条件语句（`if`, `elif`, `else`）
- 循环（`for`, `while`, `break`, `continue`）
- 列表推导式（List Comprehension）
- 函数定义与调用（`def`、返回值）
- `*args` 和 `**kwargs` 的使用场景
- 模块与导入（`import`, `from ... import ...`）

### 进阶
- 变量作用域（LEGB 规则）、闭包捕获原理
- 解包技巧（链式赋值、星号解包、交换变量）
- 真假值、短路求值、三元表达式
- `enumerate`、`zip`、`any` / `all`、`sorted(key=…)`、`min/max(key=…)`
- 内置函数背后的 C 实现 & 性能差异（`sum` vs 手写循环）

---

## 🟡 数据结构与内建类型

### 基础
- 列表（List）操作与切片
- 元组（Tuple）与不可变性
- 字典（Dict）与哈希表原理
- 集合（Set）与集合运算
- 字符串处理（格式化、正则表达式）
- 队列与栈（`collections.deque`）
- `defaultdict`, `Counter`, `OrderedDict`

### 进阶
- `slice` 对象、步长为 -1 的反向切片
- `memoryview`、`array` 模块、`bytearray` 与二进制数据
- `dict` 迭代顺序保证 (3.7+)、字典合并运算符
- `heapq`, `bisect`, `array`, `deque` 实战
- 正则表达式进阶（命名组、零宽断言、`regex` 第三方库）

---

## 🔵 函数式编程与迭代器

### 基础
- 匿名函数（`lambda`）
- `map`, `filter`, `reduce`
- 生成器（`yield`）与生成器表达式
- 迭代器协议（`__iter__`, `__next__`）
- `itertools` 模块常用函数

### 进阶
- 生成器的 `send`/`throw`/`close` 协议
- `yield from`（委托生成器）
- 可重入迭代器 vs 迭代器一次性消耗陷阱
- `itertools` 全家桶：`tee`, `groupby`, `accumulate`, `pairwise` (3.10+)

---

## 🟣 面向对象编程（OOP）

### 基础
- 类与对象的定义、`self`
- 构造函数 `__init__`
- 类变量 vs 实例变量
- 继承 & `super()`，MRO 查找顺序
- 类方法 `@classmethod` 与静态方法 `@staticmethod`

### 进阶
- 魔术方法：`__str__` `__repr__` `__eq__` `__lt__` `__hash__` …
- 抽象类 `abc.ABC`、抽象方法 `@abstractmethod`
- 协议 `typing.Protocol`（结构化子类型，PEP 544）
- 描述符协议：`__get__` `__set__` `__delete__`
- 数据类 `@dataclass`（可变/冻结、`slots=True`、`kw_only=True`）
- 元类：自定义 `type.__new__`、类装配钩子
- 协变 / 逆变类型参数
- 多重继承冲突调试、菱形继承 & MRO 可视化

---

## 🟠 装饰器与闭包

### 基础
- 闭包（Closure）原理
- 基础装饰器（无参数）
- 带参数的装饰器
- 多层装饰器嵌套
- `functools.wraps` 的作用

### 进阶
- `contextlib`-based 装饰器 (`@contextmanager`)
- 类装饰器与缓存单例模式
- 注解感知装饰器（对 `inspect.signature` 的修改）

---

## 🟤 类型注解与静态检查

### 基础
- 基本类型注解（`int`, `str`, `List[int]` 等）
- `Optional`, `Union`, `Literal`, `TypedDict`
- `Callable`, `Any`, `TypeVar`, `Generic`
- 使用 `mypy` 进行类型检查
- `pydantic` 数据验证

### 进阶
- PEP 604 (`X | Y` 联合类型)
- PEP 681 (`@dataclass_transform`), PEP 695 原生泛型类
- `typing_extensions` 前瞻：`Self`, `Never`, `Required` / `NotRequired`
- FastAPI + Pydantic 2.x 类型模型、`BaseModel` 配置
- CI 里串联 `mypy`、`ruff`、`pre-commit`、`pytest-typeguard`

---

## ⚫ 异常处理与上下文管理

### 基础
- `try-except-finally` 结构
- 自定义异常类
- `with` 语句与上下文管理器（`__enter__`, `__exit__`）
- `contextlib` 模块（`contextmanager`, `suppress`）

### 进阶
- 上下文管理器嵌套 (`ExitStack`)
- 可重入 / 可抛回异常的生成器上下文
- 自定义异常层级设计（业务 vs 系统 vs 第三方）

---

## ⚪ 模块化、打包与虚拟环境

### 基础
- Python 模块与包结构
- `__init__.py` 的作用
- 虚拟环境（`venv`, `pipenv`, `poetry`）
- `requirements.txt` 与依赖管理

### 进阶
- `pyproject.toml`、PEP 621 统一元数据
- `setuptools-scm`、`versioneer` 自动版本号
- 可执行 `zipapp` (`python -m zipapp`)
- 多解释器隔离（PEP 554 sub-interpreters）
- Docker-aware Poetry workflow，multi-stage build 最佳实践

---

## 🧩 高级特性与底层机制

### 基础
- 对象引用与可变性
- 垃圾回收机制（GC）
- 内存管理与 `sys.getsizeof`
- 装饰器与元编程
- 动态导入与反射（`getattr`, `setattr`）

### 进阶
- CPython 字节码剖析 (`dis`)、栈规模
- GIL behaviour、free-list、pymalloc
- CFFI / Cython / PyO3 扩展
- `importlib` 元钩子，延迟导入 (`importlib.metadata`, `importlib.resources`)
- 动态代码生成 (`exec`, `ast`, `types.ModuleType`)

---

## 🧪 测试、调试与质量

### 基础
- 单元测试（`unittest`, `pytest`）
- Mock 与 Fixture
- 日志记录（`logging` 模块）
- 调试工具（`pdb`, `breakpoint()`）

### 进阶
- `pytest` 高阶：参数化、标记、定制收集钩子
- `pytest-asyncio`, `pytest-httpx`, `pytest-mocker`
- 属性-基测试 (`Hypothesis`)
- 覆盖率驱动开发 (`coverage` / `pytest-cov`)
- 运行时追踪：`pyinstrument`, `scalene`, `py-spy`
- 自动化静态分析：`ruff`, `bandit`, `safety`, `dependa-bot`

---

## 🧱 架构与设计模式

### 基础
- 依赖注入（Dependency Injection）
- 控制反转（Inversion of Control）
- 常见设计模式（工厂、策略、观察者、单例等）
- SOLID 原则
- 分层架构（Controller-Service-Repository）

### 进阶
- Hexagonal / Clean Architecture in Python
- 事件溯源（Event Sourcing）与 CQRS
- Domain-Driven Design 战术模式在 Python
- 服务拆分：单体 → 微服务 → 函数计算
- 依赖注入库：`fastapi.Depends`, `punq`, `python-injector`

---

## 🌐 异步与并发

### 基础
- `async` / `await` 基础
- `asyncio` 事件循环
- 协程与任务（`create_task`, `gather`）
- 多线程与多进程（`threading`, `multiprocessing`）
- GIL 与并发模型

### 进阶
- `asyncio` 高级：自定义事件循环、优雅取消、超时处理
- Trio / Curio 对比、structured concurrency 概念
- 非阻塞 I/O in FastAPI（背景任务、WebSocket、SSE）
- `multiprocessing` + shared-memory (3.8+)、`concurrent.futures`
- Async profiling 与 可视化 (Pyroscope, Py-flame)

---

## 🌍 Web & API 开发（FastAPI 核心）

### 基础
- 路径、查询、表单、多文件上传、流式响应
- 依赖注入系统与生命周期钩子
- 自定义中间件、异常处理器、事件处理
- 后台任务、调度（Celery / RQ / APScheduler）
- OAuth2 / JWT、FastAPI-Users 集成
- OpenAPI 扩展、文档版本策略
- Async ORM (SQLAlchemy 2 async, Tortoise, Prisma)
- Alembic 自动迁移、数据库分片、读写分离
- WebSocket & SSE push，在前端 with React/Vue 消费

---

## 📊 数据处理与科学计算

### 基础
- NumPy broadcasting, ufunc, strides 调优
- pandas 高级：多索引、窗口函数、arrow 后端、pandas-api on Spark
- Polars 懒执行、DuckDB 嵌入式分析
- 可视化栈：Matplotlib, Seaborn, Plotly, Altair
- 数据序列化：Parquet, Feather, Arrow IPC, ORC

---

## 📦 常用第三方库速览

### 基础
- HTTP 客户端：httpx, aiohttp
- 消息队列：kombu/celery, aiokafka
- 任务调度：APScheduler, Celery Beat, Redis-RQ
- 配置管理：dynaconf, pydantic-settings
- 监控与可观测：structlog, loguru, OpenTelemetry SDK, prometheus_client
- 安全：passlib, pyjwt, cryptography, pynacl
- CLI 构建：click, typer, rich / textual

---

## 🚀 部署、运维与性能

### 基础
- uWSGI / Gunicorn / Hypercorn 性能调参
- ASGI servers 对比 (uvicorn, hypercorn, daphne)
- Docker health-check、multi-arch buildx
- CI/CD（GitHub Actions → Docker → AWS ECS/Lambda）
- 运行时监控：Prometheus + Grafana, Loki, Tempo
- A/B 实验、Feature Flag（Unleash, Flagsmith）
- 渐进式交付：blue-green, canary, shadow traffic

---

## 🔐 安全与最佳实践

### 基础
- OWASP Top-10 in Python Web (CSRF, SSRF, IDOR)
- 依赖漏洞扫描 (pip-audit, OSV-scanner)
- 密钥管理 (AWS KMS / Secrets Manager, dotenv)
- 审计日志、合规 (GDPR, PCI-DSS)
- Supply-chain security (Sigstore, SLSA, Reproducible builds)
