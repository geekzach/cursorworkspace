# 04 · 神经网络拟合动力学（AI01 端到端）

## 为什么学这个

经典控制说：**要有模型才能设计 LQR/PID**。当模型难推、或想快速做 **what-if**，可以让网络学 \( ( \theta, \omega, u ) \mapsto (\theta^+, \omega^+) \)——这是 **系统辨识 / 学习动力学** 的极简版，**不是强化学习**（没有奖励、没有闭环选动作）。复试具身智能方向常问：「模型从哪来？学习和经典怎么分工？」本节能让你 **指着代码和图** 答。

---

## 1. 任务定义

| 项目 | 内容 |
|------|------|
| 输入 \(x\) | 3 维：`[θ, ω, u]` |
| 输出 \(y\) | 2 维：`[θ⁺, ω⁺]`（RK4 真值一步后） |
| 损失 | MSE：\(\frac{1}{N}\sum \| \hat{y} - y \|^2\) |
| 网络 | 两层 MLP：Linear → ReLU → Linear（纯 numpy） |

**仓库地图**：

- 数据：[`src/learning/rollout.py`](../../src/learning/rollout.py)
- 模型：[`src/learning/mlp_numpy.py`](../../src/learning/mlp_numpy.py)
- 预习：[`ex01_preview_rollout.py`](../../weeks/ai01_nn_dynamics/ex01_preview_rollout.py)
- **作业**：[`ex02_fit_dynamics.py`](../../weeks/ai01_nn_dynamics/ex02_fit_dynamics.py)
- 参考演示：[`demo_reference_end2end.py`](../../weeks/ai01_nn_dynamics/demo_reference_end2end.py)（**先自己做 TODO，再对照**）

---

## 2. 数据流（端到端）

```text
generate_dataset(n_samples, dt, seed)
        │
        ▼
   X (N,3), Y (N,2)
        │
        ▼
train_val_split (80/20)
        │
        ▼
MLP(in=3, hidden=?, out=2)
        │
        ▼
for epoch: train_epoch (mini-batch SGD)
        │
        ▼
evaluate_mse on 验证集
        │
        ▼
散点图：真值 vs 预测（应贴近 y=x 对角线）
```

每一步你都在 `ex02_fit_dynamics.py` 的 `main()` 里能对应到代码行。

---

## 3. MLP 在做什么（不背 PyTorch）

结构（见 `mlp_numpy.py`）：

```text
X  --[W1,b1]--> Z1 --ReLU--> A1 --[W2,b2]--> Y_pred
```

- **`forward`**：存中间量 `_X, _Z1, _A1` 供反向传播。
- **`backward`**：对 MSE 求梯度，更新 `W1,b1,W2,b2`（学习率 `lr`）。
- **`train_epoch`**：打乱样本，按 `batch_size` 切块，多 batch 平均 loss。

**你要会的**：改 `hidden_dim`、`learning_rate`、`n_epochs`、`batch_size`、`n_samples`，看 **验证 MSE** 与散点图变化。

**不必先会的**：手写反向传播推导（能指认「链式法则从输出误差往回传」即可）。

---

## 4. 逐步完成 `ex02` 的 TODO

### TODO 1：超参数

在文件顶部已有默认值，建议流程：

1. 先用默认跑通（完成 TODO 2、3 后）。
2. 将 `hidden_dim` 改为 `8` 与 `32` 各训一次，记录 **训练后验证 MSE**。
3. 将 `learning_rate` 改为 `0.1` 看是否发散（loss 变大或 `nan`）。

### TODO 2：训练日志

把：

```python
if (epoch + 1) % 10 == 0 or epoch == 0:
    pass  # <-- 把 pass 换成你的 print
```

改成例如（格式可自定，但要含 epoch、train_loss、val_mse）：

```python
print(f"epoch {epoch + 1:3d}  train_loss={train_loss:.6f}  val_mse={val_mse:.6f}")
```

**预期**：每 10 轮一行；`val_mse` 总体应随训练下降（偶有抖动）。

### TODO 3：散点图

对 `axes[0]`、`axes[1]`：

1. `scatter(真值列, 预测列, s=8, alpha=0.5)`
2. `plot([lo, hi], [lo, hi], 'k--')` 作对角线
3. `set_xlabel` / `set_ylabel` / `set_title` / `grid`

数据用已有的 `y_true_plot`、`y_pred_plot`（前 500 验证点）。

**成功标准**：点云沿对角线分布；训练前若画散点应很散，训练后明显收紧。

---

## 5. 运行命令

```bash
cd /path/to/cursorworkspace   # 仓库根
conda activate pendulum
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

python weeks/ai01_nn_dynamics/ex02_fit_dynamics.py
```

无 GUI 时输出：`已保存: .../ai01_fit_student.png`。

对照参考（做完作业再看）：

```bash
python weeks/ai01_nn_dynamics/demo_reference_end2end.py
```

---

## 6. 和复试叙事怎么挂钩

| 话题 | 你可以说 |
|------|----------|
| 模型来源 | 仿真 ODE 积分 → 监督标签，比纯黑盒 RL 可解释 |
| 与 PID | 都是「系统怎么动」；PID 用线性近似，NN 可拟合 `sin(θ)` 非线性 |
| 与 LQR | LQR 要线性化 A、B 矩阵；NN 是另一套近似动力学，寒假可对比 |
| 与 RL | 本实验 **不开环选 u**；RL 在仿真里最大化奖励、闭环决策（ROADMAP 阶段四） |
| 局限 | 一步预测准 ≠ 长 rollout 准；分布外状态可能崩 |

---

## 7. README 中的 DIY（选做延伸）

在 `ex02` 末尾或笔记里至少做一项：

1. 预测 **角加速度 α**，再欧拉积分得 ω⁺、θ⁺，与直接预测状态比 MSE。
2. 给 `Y` 加高斯噪声再训练，看验证 MSE。
3. 扫 `n_samples` = 1000 / 4000 / 8000，手画 MSE–样本数折线。

---

## 常见踩坑

| 现象 | 原因 | 处理 |
|------|------|------|
| 验证 MSE 不降 | lr 太大或 epoch 太少 | 降 lr、增 epoch、看日志 |
| 训练 loss 很低、验证很高 | 过拟合 / 样本太少 | 增 `n_samples`、减 `hidden_dim` |
| 图仍显示「请完成 TODO」 | 只改了 title 没 scatter | 完成 3a/3b |
| `nan` | lr 过大 | `learning_rate=0.001` 重试 |
| 照抄 `demo_reference_end2end` | 失去练习 | 仅对照参数与绘图结构 |

---

## 本节练习

### 必做

1. 完成 `ex02_fit_dynamics.py` **全部 TODO**，保存 `ai01_fit_student.png`，记录 **训练前 / 训练后** 验证 MSE。
2. 固定其他超参，只把 `n_samples` 从 4000 改为 1000，再训一次，比较验证 MSE（写一句结论）。
3. 打开 `mlp_numpy.py`，在 `forward` 里找到 **ReLU** 对应哪一行；在 `backward` 里找到 **dW2** 对应哪一行（指认即可）。

### 选做

1. 实现 TODO 2 同时把每 epoch 的 `val_mse` 存进 list，用 matplotlib 画 **epoch–val_mse** 曲线。
2. 完成 README 中一项 DIY，写 5 行实验记录。
3. 对照 [`CHECKLIST.md`](../../weeks/ai01_nn_dynamics/CHECKLIST.md) 全部打勾。

---

**参考思路（含 TODO 核对要点，非完整作业粘贴）**：[`answers/04_nn_dynamics_fit.md`](answers/04_nn_dynamics_fit.md)  
**回到目录**：[教程 README](README.md)
