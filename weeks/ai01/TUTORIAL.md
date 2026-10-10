# AI01 · 教程与练习入口

**定位**：大三上 **可选支线**（与 Week 1–2 经典建模并行）——先用 **真实 ODE** 生成数据，再让小型网络学「下一时刻状态」。只用 **numpy + matplotlib**（无 MuJoCo / RL）。

**本周教程**：**[T03](../../docs/tutorials/T03-常微分方程与仿真直觉.md) · [T05](../../docs/tutorials/T05-AI01-神经网络拟合动力学.md)**（先完成或并行 **T02**）

| 顺序 | 脚本 | 说明 |
|------|------|------|
| 1 | `ex01_preview_rollout.py` | ODE rollout 曲线（T03） |
| 2 | `ex02_fit_dynamics.py` | 主作业：填 TODO，训练 MLP（T05） |
| 3（可选） | `demo_reference_end2end.py` | 参考答案演示，改参数做实验 |

## 如何运行

在项目**根目录**，已安装依赖并设置 `PYTHONPATH`：

```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

python weeks/ai01/ex01_preview_rollout.py
python weeks/ai01/ex02_fit_dynamics.py      # 主作业：完成脚本内 TODO
python weeks/ai01/demo_reference_end2end.py # 参考答案（先不要照抄）
```

无图形界面时会自动保存 PNG 到本目录。库代码在 `src/ai01/`（`pendulum.py`、`rollout.py`、`mlp_numpy.py`）。

## DIY（任选至少一项）

在 `ex02_fit_dynamics.py` 末尾 DIY 区完成至少一项（写在注释或笔记里）：

1. 网络预测 **角加速度** `α`，再用欧拉法得 `ω⁺、θ⁺`，与直接预测状态对比。
2. 训练数据加 **高斯噪声**，观察验证集 MSE。
3. 只改 **训练样本数** `n_samples`，画粗略 MSE–样本数曲线。

自查：[`CHECKLIST.md`](CHECKLIST.md) · 校历周：[`docs/checklists/ai01-focus.md`](../../docs/checklists/ai01-focus.md) · 总教程：[`docs/tutorials/README.md`](../../docs/tutorials/README.md)
