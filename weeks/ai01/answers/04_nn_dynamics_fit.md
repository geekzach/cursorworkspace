# 04 AI01 · 参考思路

## 训练是否成功（量级参考）

环境、种子与默认超参下，**训练前**验证 MSE 常在 **0.05–0.5**（随机权重）；**训练后**可降到 **1e-3 ~ 1e-2** 量级。若训练后仍 >0.05，查学习率与 epoch。

`n_samples=1000` 时验证 MSE 通常 **高于** 4000 样本（方差更大），除非碰巧划分 easier。

## TODO 2 写法示例

```python
if (epoch + 1) % 10 == 0 or epoch == 0:
    print(f"epoch {epoch + 1:3d}  train_loss={train_loss:.6f}  val_mse={val_mse:.6f}")
```

## TODO 3 写法要点（请自己敲进 ex02，勿整文件替换）

对 `col=0`（θ⁺）与 `col=1`（ω⁺）循环或手写两次：

```python
for ax, col, name in zip(axes, [0, 1], ["θ⁺", "ω⁺"]):
    ax.scatter(y_true_plot[:, col], y_pred_plot[:, col], s=8, alpha=0.5)
    lo = min(y_true_plot[:, col].min(), y_pred_plot[:, col].min())
    hi = max(y_true_plot[:, col].max(), y_pred_plot[:, col].max())
    ax.plot([lo, hi], [lo, hi], "k--", lw=1, alpha=0.6)
    ax.set_xlabel(f"真值 {name}")
    ax.set_ylabel(f"预测 {name}")
    ax.set_title(name)
    ax.grid(True, alpha=0.3)
```

完成后删除标题里的「请完成 TODO」占位文字。

## DIY 提示

- **加噪声**：`Y_train_noisy = Y_train + rng.normal(0, sigma, Y_train.shape)`，只在训练集加。
- **预测 α**：网络 `out_dim=1` 预测 `alpha`，再 `omega_next = omega + dt*alpha`，`theta_next = theta + dt*omega_next`（欧拉）；与真 `Y` 比 MSE。

## mlp_numpy 指认

- ReLU：`relu(self._Z1)` 或 `self._A1 = relu(self._Z1)`
- `dW2`：`dW2 = self._A1.T @ dY`
