# 字典是 键-值对（key-value pair） 的集合：
person = {"name": "Alice", "age": 30}
# 键是唯一的（key must be unique）
#
# 键必须是可哈希的（不可变类型，如 str、int、tuple）
#
# 查找/插入速度非常快（平均 O(1)）

# 哈希表是一种使用**哈希函数（hash function）**将键映射到数组索引的数据结构。
# 操作流程如下：
# 1. 哈希函数计算出键的 hash 值 → hash(key)
#
# 2. 根据 hash 值定位到数组的某个槽位（slot） → index = hash(key) % array_size
#
# 3. 将键值对放入这个槽中。

# key = "name"
# hash("name") → 984328423
# index = 984328423 % 8 → 7

# 为啥要哈希成很大的数？	为了更好地分散 key，减少冲突（高质量 hash 函数）
# 最终还要 % 表的大小？	因为底层表大小有限，需要映射到数组索引范围

# 如果哈希表初始大小是 8，那么所有 key 都 hash(key) % 8，就只能落在 8 个槽位 里。
# Python 的字典不是“永远只有 8 个槽位”，而是会随着元素增加而自动扩容，比如：
#
# 当前元素数	容量大小
# 0	8
# >5	16
# >11	32

# 四、Python 字典的底层结构（CPython 实现）
# // 伪结构
# typedef struct {
#     PyObject **keys;      // 键表
#     PyObject **values;    // 值表（值存储分离）
#     uint64_t *hashes;     // 哈希值表（加快查找）
#     size_t size;          // 当前使用的槽数
#     size_t capacity;      // 总槽数
# } PyDictObject;
# 查找流程图解（简化）
# put("name", "Alice"):
#   1. h = hash("name")
#   2. index = h % size
#   3. slot[index] 是否为空？
#      - 空：直接放入
#      - 不空：线性探测找下一个空槽
# 六、dict 的哈希要求（键必须可哈希）
# 哈希必须满足：
#
# __hash__() 方法返回 hash 值（int）
#
# __eq__() 用于判断两个键是否“相等”
# 七。性能与扩容机制
# 初始容量通常是 8
#
# 负载因子（load factor） 超过 2/3 就会自动扩容（通常翻倍）
#
# 扩容后会重新哈希所有键（rehash）
