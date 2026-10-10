"""
从简化摆模型生成 (s, u) -> s_next 的监督学习数据集。
"""

from __future__ import annotations

import numpy as np

from .pendulum import PendulumParams, rk4_step


def generate_dataset(
    n_samples: int,
    dt: float = 0.02,
    params: PendulumParams | None = None,
    seed: int = 42,
) -> tuple[np.ndarray, np.ndarray]:
    """
    随机采样初始状态与控制，用真实 ODE 积分得到下一时刻状态。

    返回
    -----
    X : (n_samples, 3)  列依次为 [theta, omega, u]
    Y : (n_samples, 2)  列依次为 [theta_next, omega_next]
    """
    if params is None:
        params = PendulumParams()
    rng = np.random.default_rng(seed)

    X = np.zeros((n_samples, 3), dtype=float)
    Y = np.zeros((n_samples, 2), dtype=float)

    for i in range(n_samples):
        # 小角度附近 + 少量大角度，便于 NN 学习 sin 非线性
        theta = rng.uniform(-0.8, 0.8)
        omega = rng.uniform(-2.0, 2.0)
        u = rng.uniform(-0.5, 0.5)
        state = np.array([theta, omega], dtype=float)
        next_state = rk4_step(state, u, dt, params)

        X[i, :] = (theta, omega, u)
        Y[i, :] = next_state

    return X, Y


def train_val_split(
    X: np.ndarray,
    Y: np.ndarray,
    val_ratio: float = 0.2,
    seed: int = 0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """打乱后划分训练 / 验证集。"""
    n = X.shape[0]
    rng = np.random.default_rng(seed)
    idx = rng.permutation(n)
    n_val = int(n * val_ratio)
    val_idx = idx[:n_val]
    train_idx = idx[n_val:]
    return X[train_idx], Y[train_idx], X[val_idx], Y[val_idx]
