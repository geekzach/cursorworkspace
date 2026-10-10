#!/usr/bin/env python3
"""
AI01 主作业：训练小型 MLP，拟合一步动力学 (θ, ω, u) -> (θ⁺, ω⁺)。

请完成文件中所有 TODO，再运行本脚本。

运行（项目根目录）：
    export PYTHONPATH="$(pwd)/src"
    python weeks/ai01_nn_dynamics/ex02_fit_dynamics.py
"""

from __future__ import annotations

import os
import sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
_SRC = os.path.join(_ROOT, "src")
if _SRC not in sys.path:
    sys.path.insert(0, _SRC)

import numpy as np
import matplotlib.pyplot as plt

from learning.mlp_numpy import MLP, evaluate_mse, train_epoch
from learning.rollout import generate_dataset, train_val_split


def mse_per_dimension(Y_true: np.ndarray, Y_pred: np.ndarray) -> tuple[float, float]:
    """分别计算 θ 与 ω 维度的均方误差。"""
    err_theta = float(np.mean((Y_pred[:, 0] - Y_true[:, 0]) ** 2))
    err_omega = float(np.mean((Y_pred[:, 1] - Y_true[:, 1]) ** 2))
    return err_theta, err_omega


def main() -> None:
    # ========== TODO 1：数据与超参数（请修改并理解每个量的作用）==========
    n_samples = 4000  # 可改：例如 1000 / 8000，观察验证误差
    dt = 0.02
    seed = 42

    # TODO 1a：填写训练超参数（建议先与下面默认值接近，再自己调）
    hidden_dim = 16  # TODO：隐藏层神经元个数，试试 8、32
    learning_rate = 0.01  # TODO：学习率，过大可能发散
    n_epochs = 80  # TODO：训练轮数
    batch_size = 64  # TODO：mini-batch 大小

    print("=== AI01：生成数据集（真实 ODE）===")
    X, Y = generate_dataset(n_samples=n_samples, dt=dt, seed=seed)
    X_train, Y_train, X_val, Y_val = train_val_split(X, Y, val_ratio=0.2, seed=seed)

    model = MLP(in_dim=3, hidden_dim=hidden_dim, out_dim=2, seed=seed)

    print("=== 训练前（随机初始化）验证 MSE ===")
    mse_before = evaluate_mse(model, X_val, Y_val)
    print(f"  验证集 MSE = {mse_before:.6f}")

    print("=== 开始训练 ===")
    for epoch in range(n_epochs):
        train_loss = train_epoch(
            model,
            X_train,
            Y_train,
            lr=learning_rate,
            batch_size=batch_size,
            seed=seed + epoch,
        )
        val_mse = evaluate_mse(model, X_val, Y_val)

        # TODO 2：每 10 个 epoch 打印一行日志（取消下面 pass，写成 print）
        # 提示：打印 epoch、train_loss、val_mse
        if (epoch + 1) % 10 == 0 or epoch == 0:
            pass  # <-- 把 pass 换成你的 print

    print("=== 训练后 ===")
    mse_after = evaluate_mse(model, X_val, Y_val)
    print(f"  验证集 MSE = {mse_after:.6f}")

    Y_pred = model.predict(X_val)
    err_theta, err_omega = mse_per_dimension(Y_val, Y_pred)
    print(f"  分维度 MSE: θ={err_theta:.6f}, ω={err_omega:.6f}")

    # ========== TODO 3：绘图（真值 vs 预测）==========
    # 要求：两个子图——左：θ⁺ 真值 vs 预测（散点）；右：ω⁺ 同理
    # 点的数量可只用验证集前 500 个点，避免太密
    n_plot = min(500, X_val.shape[0])
    y_true_plot = Y_val[:n_plot]
    y_pred_plot = Y_pred[:n_plot]

    fig, axes = plt.subplots(1, 2, figsize=(9, 4))

    # TODO 3a：在 axes[0] 上画 θ⁺：横轴真值、纵轴预测（plt.scatter）
    # TODO 3b：在 axes[1] 上画 ω⁺
    # TODO 3c：各子图加 xlabel/ylabel、标题、对角线 y=x 参考线（可选）
    axes[0].set_title("θ⁺  （请完成 TODO 3a）")
    axes[1].set_title("ω⁺  （请完成 TODO 3b）")

    plt.suptitle("AI01：一步动力学预测（完成 TODO 后应看到沿对角线分布）")
    plt.tight_layout()
    _save_or_show(fig, "ai01_fit_student.png")

    # ========== DIY 区（见 README）==========
    # 在这里尝试：加噪声、改 n_samples、或预测角加速度等，并写一两句观察结论。


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
