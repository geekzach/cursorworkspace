#!/usr/bin/env python3
"""
Week 1 练习 3：列表与字典

运行：python weeks/week01/exercises/ex03_lists_dicts.py

学习目标：用列表存时间序列、用字典存物理参数（后续建模会大量使用）。
"""

from __future__ import annotations


def main() -> None:
    print("=== 列表 list：有序、可变的序列 ===")
    # 模拟采样到的 5 个摆角（单位：度，仅作练习）
    angles_deg = [2.1, 1.8, 1.2, 0.5, -0.1]
    print("摆角序列:", angles_deg)
    print("第一个采样:", angles_deg[0])
    print("最后一个采样:", angles_deg[-1])
    print("样本个数:", len(angles_deg))

    # 列表推导式：对每个角度求平方（预习 numpy 向量化前的朴素写法）
    squares = [x * x for x in angles_deg]
    print("各角度平方:", squares)

    print("\n=== 字典 dict：键值对，适合描述物理参数 ===")
    # 倒立摆相关参数（数值为示意，真实模型 Week 4+ 再建立）
    params = {
        "cart_mass_kg": 1.0,
        "pendulum_mass_kg": 0.1,
        "rod_length_m": 0.5,
        "gravity_m_s2": 9.81,
    }
    print("参数字典:")
    for key, value in params.items():
        print(f"  {key} = {value}")

    # 读取与更新
    m_cart = params["cart_mass_kg"]
    params["note"] = "Week1 仅练习数据结构"
    print(f"\n小车质量 m = {m_cart} kg")
    print("新增键 note:", params["note"])

    print("\n=== 小挑战（已写好，请阅读）===")
    times = [0.0, 0.1, 0.2, 0.3]
    values = [0.0, 0.63, 0.86, 0.95]  # 类似一阶系统响应的示意数据
    for t, y in zip(times, values):
        print(f"  t={t:.1f}s, y={y:.2f}")

    print("\n[完成] 请运行 hello_sim.py 查看 matplotlib 绘图")


if __name__ == "__main__":
    main()
