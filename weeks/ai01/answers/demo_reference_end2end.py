#!/usr/bin/env python3
"""
【参考答案 / 演示】AI01 端到端：数据 → 训练 MLP → 误差图。

作业请优先完成 ex02_fit_dynamics.py 中的 TODO；本文件仅供对照与调参实验。

运行（项目根目录）：
    export PYTHONPATH="$(pwd)/src"
    python weeks/ai01/answers/demo_reference_end2end.py
"""

from __future__ import annotations

import os
import sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
_SRC = os.path.join(_ROOT, "src")
if _SRC not in sys.path:
    sys.path.insert(0, _SRC)

import numpy as np
import matplotlib.pyplot as plt

from ai01.mlp_numpy import MLP, evaluate_mse, train_epoch
from ai01.rollout import generate_dataset, train_val_split


def main() -> None:
    n_samples = 6000
    dt = 0.02
    seed = 42
    hidden_dim = 24
    learning_rate = 0.008
    n_epochs = 100
    batch_size = 64

    X, Y = generate_dataset(n_samples=n_samples, dt=dt, seed=seed)
    X_train, Y_train, X_val, Y_val = train_val_split(X, Y, val_ratio=0.2, seed=seed)

    model = MLP(in_dim=3, hidden_dim=hidden_dim, out_dim=2, seed=seed)
    mse_before = evaluate_mse(model, X_val, Y_val)
    print(f"训练前验证 MSE: {mse_before:.6f}")

    for epoch in range(n_epochs):
        train_loss = train_epoch(
            model,
            X_train,
            Y_train,
            lr=learning_rate,
            batch_size=batch_size,
            seed=seed + epoch,
        )
        if (epoch + 1) % 20 == 0:
            val_mse = evaluate_mse(model, X_val, Y_val)
            print(f"epoch {epoch + 1:3d}  train_loss={train_loss:.6f}  val_mse={val_mse:.6f}")

    mse_after = evaluate_mse(model, X_val, Y_val)
    print(f"训练后验证 MSE: {mse_after:.6f}")

    Y_pred = model.predict(X_val)
    n_plot = min(500, Y_val.shape[0])
    y_t = Y_val[:n_plot]
    y_p = Y_pred[:n_plot]

    fig, axes = plt.subplots(1, 2, figsize=(9, 4))
    for ax, col, name in zip(axes, [0, 1], ["θ⁺", "ω⁺"]):
        ax.scatter(y_t[:, col], y_p[:, col], s=8, alpha=0.5, c="#1f77b4")
        lo = min(y_t[:, col].min(), y_p[:, col].min())
        hi = max(y_t[:, col].max(), y_p[:, col].max())
        ax.plot([lo, hi], [lo, hi], "k--", lw=1, alpha=0.6)
        ax.set_xlabel(f"真值 {name}")
        ax.set_ylabel(f"预测 {name}")
        ax.set_title(name)
        ax.grid(True, alpha=0.3)

    plt.suptitle("AI01 参考：一步动力学 MLP 拟合（验证集散点）")
    plt.tight_layout()
    _save_or_show(fig, "ai01_fit_reference.png")


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
