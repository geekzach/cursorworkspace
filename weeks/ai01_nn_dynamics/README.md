# AI01：用小型神经网络拟合摆动力学

**定位**：大三上 **可选支线**（与 Week 1–2 经典建模并行），面试可讲「**控制 + 学习**」——先用**真实 ODE**生成数据，再让网络学「下一时刻状态」。

不引入 MuJoCo / 强化学习；只用 **numpy + matplotlib**（见根目录 `requirements.txt`）。

---

## 你要完成什么

1. **理解数据从哪来**：简化摆 ODE（`src/learning/pendulum.py`）在随机初值与力矩下积分，得到 `(θ, ω, u) → (θ⁺, ω⁺)`。
2. **自己写一小段**：在 `ex02_fit_dynamics.py` 里补全 **TODO**（损失打印、超参数、对比图等）。
3. **看图说话**：训练后画出「真实下一状态 vs 网络预测」的误差，能解释过拟合 / 数据量 / 隐藏层大小的影响。

完整可运行示例（**参考答案**，先不要照抄）：`demo_reference_end2end.py`。

---

## 建议学习顺序

| 顺序 | 脚本 | 说明 |
|------|------|------|
| 1 | `ex01_preview_rollout.py` | 只看 ODE rollout 曲线，建立「仿真生成数据」直觉 |
| 2 | `ex02_fit_dynamics.py` | 主作业：填 TODO，训练 MLP，保存误差图 |
| 3（可选） | `demo_reference_end2end.py` | 对照参考实现，改参数做实验 |

完成度见 [`CHECKLIST.md`](CHECKLIST.md)。

---

## 如何运行

在项目**根目录**，已安装依赖并（推荐）设置 `PYTHONPATH`：

```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

# 预习：单条轨迹
python weeks/ai01_nn_dynamics/ex01_preview_rollout.py

# 主作业（需先完成 TODO）
python weeks/ai01_nn_dynamics/ex02_fit_dynamics.py

# 参考答案（端到端演示）
python weeks/ai01_nn_dynamics/demo_reference_end2end.py
```

无图形界面时会自动保存 PNG 到本目录。

---

## 与主线 / 复试的关系

- **现在**：神经网络是 **开环一步预测**（监督学习），与 PID 用的「模型」是同一类信息——描述系统怎么动。
- **寒假后**：完整 cart-pole / MuJoCo 模型更复杂，仍可沿用「仿真 rollout → 拟合」思路。
- **阶段四（ROADMAP M4）**：强化学习会在仿真里 **闭环** 选控制；本支线只打底 **函数逼近**，不抢 Week 1 基础时间。

---

## DIY 任务（自己写）

在 `ex02_fit_dynamics.py` 末尾的 DIY 区任选至少一项（写在注释或笔记里）：

1. 把网络输出改成预测 **角加速度** `α`，再用欧拉法得到 `ω⁺、θ⁺`，与直接预测状态对比误差。
2. 给训练数据加 **高斯噪声**，观察验证集 MSE 如何变化。
3. 固定网络结构，只改 **训练样本数** `n_samples`，画 MSE–样本数 粗略曲线（几个点即可）。

---

## 代码地图

```text
src/learning/
  pendulum.py      # 简化摆 ODE + RK4
  rollout.py       # 随机采样生成数据集
  mlp_numpy.py     # 两层 MLP（已实现反向传播，可读）
weeks/ai01_nn_dynamics/
  ex01_preview_rollout.py
  ex02_fit_dynamics.py   # 你的主战场
  demo_reference_end2end.py
```
