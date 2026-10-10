#!/usr/bin/env python3
"""
Week 2 示例：用简化摆 ODE 生成一条 rollout 并画图（不依赖其他包目录）。

运行（项目根目录）：
    python code/week02/examples/ex01_preview_rollout.py
"""

from __future__ import annotations

import os

import matplotlib.pyplot as plt
import numpy as np


class PendulumParams:
    g: float = 9.81
    l: float = 0.5
    m: float = 1.0
    b: float = 0.1


def pendulum_deriv(state: np.ndarray, u: float, p: PendulumParams) -> np.ndarray:
    theta, omega = state[0], state[1]
    alpha = (u - p.b * omega - p.m * p.g * p.l * np.sin(theta)) / (p.m * p.l**2)
    return np.array([omega, alpha], dtype=float)


def rk4_step(state: np.ndarray, u: float, dt: float, p: PendulumParams) -> np.ndarray:
    k1 = pendulum_deriv(state, u, p)
    k2 = pendulum_deriv(state + 0.5 * dt * k1, u, p)
    k3 = pendulum_deriv(state + 0.5 * dt * k2, u, p)
    k4 = pendulum_deriv(state + dt * k3, u, p)
    return state + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)


def main() -> None:
    params = PendulumParams()
    dt = 0.02
    steps = 200
    state = np.array([0.25, 0.0], dtype=float)
    u_pos, u_neg = 0.15, -0.15

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
    axes[0].set_title("简化摆 rollout（ODE + RK4）")

    axes[1].plot(times, omegas, color="#ff7f0e", lw=2)
    axes[1].set_xlabel("时间 t (s)")
    axes[1].set_ylabel("角速度 ω (rad/s)")
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    _save_or_show(fig, "week02_rollout_preview.png")


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
