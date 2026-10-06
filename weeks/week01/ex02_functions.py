#!/usr/bin/env python3
"""
Week 1 练习 2：函数

运行：python weeks/week01/ex02_functions.py

学习目标：定义函数、参数、返回值；为后续「控制器计算 u = f(error)」打基础。
"""

from __future__ import annotations


def greet(student_name: str) -> str:
    """返回一句问候语。类型注解（str）可帮助阅读，初学可先忽略。"""
    return f"你好，{student_name}！继续加油准备控制复试。"


def clamp(value: float, low: float, high: float) -> float:
    """
    把 value 限制在 [low, high] 区间内。

    控制里常用：限制控制力矩/电压不超过物理上限（饱和）。
    """
    if value < low:
        return low
    if value > high:
        return high
    return value


def mean_of_three(a: float, b: float, c: float) -> float:
    """三个数的算术平均。"""
    return (a + b + c) / 3.0


def main() -> None:
    print("=== 练习 2：函数调用 ===")
    print(greet("同学"))

    # 模拟「控制量」被限制在 ±10
    raw_command = 15.0
    safe_command = clamp(raw_command, -10.0, 10.0)
    print(f"\n原始指令 {raw_command} -> 限幅后 {safe_command}")

    avg = mean_of_three(1.0, 2.0, 3.0)
    print(f"\n1, 2, 3 的平均值 = {avg}")

    # 默认参数示例
    def step_size(dt: float = 0.01) -> float:
        """仿真时间步长，默认 0.01 s（后续仿真会用到类似概念）。"""
        return dt

    print(f"\n默认仿真步长 dt = {step_size()} 秒")
    print(f"自定义步长 dt = {step_size(0.001)} 秒")

    print("\n[完成] 请继续 ex03_lists_dicts.py")


if __name__ == "__main__":
    # 只有直接运行本文件时才执行 main；被其他文件 import 时不会自动运行
    main()
