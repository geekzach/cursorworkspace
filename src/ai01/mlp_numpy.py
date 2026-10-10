"""
纯 numpy 实现的两层 MLP（用于动力学拟合，无 PyTorch）。

结构：input -> Linear -> ReLU -> Linear -> output
提供前向、反向传播与简单 mini-batch 训练循环。
"""

from __future__ import annotations

import numpy as np


def relu(x: np.ndarray) -> np.ndarray:
    return np.maximum(0.0, x)


def relu_grad(x: np.ndarray) -> np.ndarray:
    return (x > 0.0).astype(float)


class MLP:
    """输入维度 in_dim，隐藏 hidden_dim，输出 out_dim。"""

    def __init__(self, in_dim: int, hidden_dim: int, out_dim: int, seed: int = 0) -> None:
        rng = np.random.default_rng(seed)
        # He / Xavier 简化：小随机初始化
        self.W1 = rng.normal(0, 0.5, size=(in_dim, hidden_dim))
        self.b1 = np.zeros(hidden_dim)
        self.W2 = rng.normal(0, 0.5, size=(hidden_dim, out_dim))
        self.b2 = np.zeros(out_dim)

        # 训练时缓存
        self._X: np.ndarray | None = None
        self._Z1: np.ndarray | None = None
        self._A1: np.ndarray | None = None

    def forward(self, X: np.ndarray) -> np.ndarray:
        """X: (batch, in_dim) -> (batch, out_dim)"""
        self._X = X
        self._Z1 = X @ self.W1 + self.b1
        self._A1 = relu(self._Z1)
        return self._A1 @ self.W2 + self.b2

    def backward(self, Y_true: np.ndarray, lr: float) -> float:
        """
        对当前 batch 做一次 MSE 损失的梯度下降。
        返回该 batch 的均方误差。
        """
        if self._X is None or self._A1 is None or self._Z1 is None:
            raise RuntimeError("请先调用 forward")

        Y_pred = self._A1 @ self.W2 + self.b2
        batch = Y_true.shape[0]
        loss = float(np.mean((Y_pred - Y_true) ** 2))

        dY = (2.0 / batch) * (Y_pred - Y_true)
        dW2 = self._A1.T @ dY
        db2 = np.sum(dY, axis=0)

        dA1 = dY @ self.W2.T
        dZ1 = dA1 * relu_grad(self._Z1)
        dW1 = self._X.T @ dZ1
        db1 = np.sum(dZ1, axis=0)

        self.W2 -= lr * dW2
        self.b2 -= lr * db2
        self.W1 -= lr * dW1
        self.b1 -= lr * db1
        return loss

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self.forward(X)


def train_epoch(
    model: MLP,
    X: np.ndarray,
    Y: np.ndarray,
    lr: float,
    batch_size: int,
    seed: int = 0,
) -> float:
    """一个 epoch：随机 mini-batch SGD，返回平均训练 loss。"""
    n = X.shape[0]
    rng = np.random.default_rng(seed)
    perm = rng.permutation(n)
    losses: list[float] = []
    for start in range(0, n, batch_size):
        idx = perm[start : start + batch_size]
        xb = X[idx]
        yb = Y[idx]
        model.forward(xb)
        losses.append(model.backward(yb, lr))
    return float(np.mean(losses)) if losses else 0.0


def evaluate_mse(model: MLP, X: np.ndarray, Y: np.ndarray) -> float:
    pred = model.predict(X)
    return float(np.mean((pred - Y) ** 2))
