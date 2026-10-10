"""
AI01 支线库：简化摆 ODE、rollout 数据集、NumPy MLP。

与经典 PID / 建模并列，为后续 ROADMAP 阶段四 RL 打底；仅依赖 numpy。
"""

from .pendulum import PendulumParams, pendulum_deriv, rk4_step
from .rollout import generate_dataset
from .mlp_numpy import MLP

__all__ = [
    "PendulumParams",
    "pendulum_deriv",
    "rk4_step",
    "generate_dataset",
    "MLP",
]
