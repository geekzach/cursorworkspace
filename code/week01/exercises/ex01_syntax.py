#!/usr/bin/env python3
"""
Week 1 练习 1：Python 语法入门

运行方式（在项目根目录）：
    python code/week01/exercises/ex01_syntax.py

学习目标：变量、基本类型、条件与循环。
"""

# --- 变量与类型 ---
name = "东南大学复试准备"  # 字符串 str
week = 1  # 整数 int
hours_per_day = 1.5  # 浮点数 float
is_ready = False  # 布尔 bool

print("=== 练习 1：基本输出 ===")
print("项目名称:", name)
print("当前周次:", week, "每天学习约", hours_per_day, "小时")

# --- 条件语句 if / elif / else ---
score = 85
if score >= 90:
    level = "优秀"
elif score >= 60:
    level = "及格及以上"
else:
    level = "需加强"
print("\n模拟自测分数", score, "->", level)

# --- for 循环：遍历一段整数 ---
print("\n=== 用 for 打印 1 到 5 的和 ===")
total = 0
for i in range(1, 6):  # 1, 2, 3, 4, 5
    total = total + i
    print("  加上", i, "后累计 =", total)
print("最终结果 total =", total)

# --- while 循环（了解即可）---
print("\n=== while 倒计时示例 ===")
countdown = 3
while countdown > 0:
    print("  还剩", countdown, "秒…")
    countdown = countdown - 1
print("  开始今天的学习！")

print("\n[完成] 若你能读懂上述输出，请继续 ex02_functions.py")
