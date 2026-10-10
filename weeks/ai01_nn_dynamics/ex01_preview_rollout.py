#!/usr/bin/env python3
"""
AI01 预习：用「真实」摆 ODE 生成一条 rollout 并画图。

不训练神经网络，只熟悉：状态是什么、力矩 u 如何驱动系统变化。

运行（项目根目录）：
    export PYTHONPATH="$(pwd)/src"
    python weeks/ai01_nn_dynamics/ex01_preview_rollout.py
"""

from __future__ import annotations

import os
import sys

# 允许未设置 PYTHONPATH 时从仓库根目录运行
_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
_SRC = os.path.join(_ROOT, "src")
if _SRC not in sys.path:
    sys.path.insert(0, _SRC)

import numpy as np
import matplotlib.pyplot as plt

from learning.pendulum import PendulumParams, rk4_step


def main() -> None:
    params = PendulumParams()
    dt = 0.02
    steps = 200

    # 初值：略偏离竖直，便于看到摆动
    state = np.array([0.25, 0.0], dtype=float)

    # 简单控制：前 100 步恒定力矩，后 100 步反向（可改数值观察）
    u_pos = 0.15
    u_neg = -0.15

    times = np.zeros(steps + 1)
    thetas = np.zeros(steps + 1)
    omegas = np.zeros(steps + 1)

    thetas[0], omegas[0] = state[0], state[1]
    for k in range(steps):
        u = u_pos if k < steps // 2 else u_neg
        state = rk4_step(state, u, dt, params)
        times[k + 1] = (k + 1) * dt
        thetas[k + 1] = state[0]
        omegas[k + 1] = state[1]

    fig, axes = plt.subplots(2, 1, figsize=(8, 5), sharex=True)
    axes[0].plot(times, thetas, color="#1f77b4", lw=2)
    axes[0].set_ylabel("摆角 θ (rad)")
    axes[0].grid(True, alpha=0.3)
    axes[0].set_title("AI01 预习：简化摆 rollout（ODE 真值）")

    axes[1].plot(times, omegas, color="#ff7f0e", lw=2)
    axes[1].set_xlabel("时间 t (s)")
    axes[1].set_ylabel("角速度 ω (rad/s)")
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    _save_or_show(fig, "ai01_rollout_preview.png")


def _save_or_show(fig: plt.Figure, filename: str) -> None:
    out_path = os.path.join(os.path.dirname(__file__), filename)
    backend = plt.get_backend().lower()
    has_display = bool(os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY"))
    if "agg" in backend or not has_display:
        fig.savefig(out_path, dpi=120)
        print(f"已保存: {out_path}")
    else:
        plt.show()


if __name__ == "__main__":
    main()
