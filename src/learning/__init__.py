"""
轻量「学习」辅助模块（大三上 AI 支线）。

与经典 PID / 建模并列：用神经网络拟合简单动力学，为后续阶段四 RL 打底。
当前仅依赖 numpy；不引入 PyTorch / 强化学习框架。
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
