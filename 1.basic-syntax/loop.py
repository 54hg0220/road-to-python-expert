# ✅ 使用建议
# 场景	推荐结构
# 遍历固定集合或范围	for
# 条件驱动的循环	while
# 提前退出循环	break
# 跳过某些迭代	continue
# 检查是否完整执行循环	for/while ... else

# 什么时候用 match-case 比较合适？
# ✅ 推荐使用场景：
# 多个值的条件判断（替代多个 if-elif）：
command = input("Enter")
match command:
    case "start":
        ...
    case "stop":
        ...

point = (0, 1)
match point:
    case (0, 0):
        print("原点")
    case (x, 0):
        print(f"x轴上的点：{x}")
    case (0, y):
        print(f"y轴上的点:{y}")
