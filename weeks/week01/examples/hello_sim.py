#!/usr/bin/env python3
"""
Week 1 预览：一阶系统阶跃响应（最简单的「仿真 + 画图」）

这不是倒立摆，只是让你熟悉 matplotlib，并建立「系统对输入的响应」直觉。

一阶系统（传递函数）常写成：G(s) = K / (tau*s + 1)
- K：增益（稳态值比例）
- tau：时间常数（越大响应越慢）

运行（在项目根目录）：
    python weeks/week01/examples/hello_sim.py

会弹出图形窗口；若无图形界面，脚本会把图保存为 week01_step_response.png。
"""

from __future__ import annotations

import os

import numpy as np
import matplotlib.pyplot as plt


def first_order_step_response(
    t: np.ndarray,
    K: float = 1.0,
    tau: float = 0.5,
) -> np.ndarray:
    """
    计算阶跃输入（幅度 1）下，一阶系统的输出 y(t)。

    解析解：y(t) = K * (1 - exp(-t/tau))， t >= 0
    """
    return K * (1.0 - np.exp(-t / tau))


def main() -> None:
    # ----- 参数（可改 tau 观察曲线变化）-----
    K = 1.0
    tau = 0.5  # 秒；改成 1.0 或 0.2 再运行对比

    # 时间轴：从 0 到 3 秒，共 300 个点
    t = np.linspace(0.0, 3.0, 300)
    y = first_order_step_response(t, K=K, tau=tau)

    # ----- 绘图 -----
    plt.figure(figsize=(8, 4.5))
    plt.plot(t, y, color="#1f77b4", linewidth=2, label=rf"$y(t)$, $\tau$={tau}s")
    plt.axhline(K, color="gray", linestyle="--", linewidth=1, label=f"稳态值 K={K}")
    plt.xlabel("时间 t (s)")
    plt.ylabel("输出 y")
    plt.title("Week 1 预习：一阶系统单位阶跃响应")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    # 有图形界面则弹出窗口；无 DISPLAY 或使用 Agg 后端时保存图片
    out_path = os.path.join(os.path.dirname(__file__), "week01_step_response.png")
    backend = plt.get_backend().lower()
    has_display = bool(os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY"))
    if "agg" in backend or not has_display:
        plt.savefig(out_path, dpi=120)
        print(f"已保存阶跃响应图: {out_path}")
    else:
        plt.show()

    print("说明：")
    print("  - 曲线从 0 逐渐趋近 K=1，这就是「阶跃响应」。")
    print("  - tau 是时间常数：tau 越大，接近稳态越慢。")
    print("  - 后续周次会用类似思路分析倒立摆线性化后的环节。")


if __name__ == "__main__":
    main()
