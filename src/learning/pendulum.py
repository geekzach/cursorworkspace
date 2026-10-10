"""
单摆 / 倒立摆「支点固定」简化模型（2 维状态）。

用于 AI01：在完整 cart-pole 实现之前，先用可解析的 ODE 生成 rollout 数据。
状态 x = [theta, omega]^T：
  - theta：摆角（rad），竖直向上为 0，向右倾为正（与多数教材一致）
  - omega：角速度 (rad/s)

控制 u：施加在摆上的力矩 (N·m)，正方向与 theta 增加方向一致。

连续时间动力学（点质量摆，含阻尼）：
  d(theta)/dt = omega
  d(omega)/dt = -(g/L) * sin(theta) - b * omega + u / (m * L^2)

这是倒立摆去掉小车自由度后的常见简化；大三上理解「真实模型 vs 学习近似」即可。
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class PendulumParams:
    """物理参数（国际单位制）。"""

    m: float = 0.2  # 摆锤质量 kg
    L: float = 0.5  # 摆长 m
    g: float = 9.81
    b: float = 0.02  # 粘性阻尼系数 N·m·s/rad


def pendulum_deriv(_t: float, state: np.ndarray, u: float, p: PendulumParams) -> np.ndarray:
    """
    返回状态导数 d(state)/dt，形状 (2,)。
    """
    theta, omega = float(state[0]), float(state[1])
    theta_dot = omega
    omega_dot = -(p.g / p.L) * np.sin(theta) - p.b * omega + u / (p.m * p.L ** 2)
    return np.array([theta_dot, omega_dot], dtype=float)


def rk4_step(state: np.ndarray, u: float, dt: float, p: PendulumParams) -> np.ndarray:
    """固定力矩 u 下，用 RK4 积分一步。"""
    s = np.asarray(state, dtype=float)

    def f(y: np.ndarray) -> np.ndarray:
        return pendulum_deriv(0.0, y, u, p)

    k1 = f(s)
    k2 = f(s + 0.5 * dt * k1)
    k3 = f(s + 0.5 * dt * k2)
    k4 = f(s + dt * k3)
    return s + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
