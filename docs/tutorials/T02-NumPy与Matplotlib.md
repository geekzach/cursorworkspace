# T02 · NumPy 与 Matplotlib

**章节 ID**：T02  
**预计用时**：2–4 天（Week 1 末 ~ Week 2 初）

---

## 2.1 线性代数直觉（只学够用）

控制系统里 **状态是向量**，线性化后是 **矩阵** \(A,B\)。你不需要先修完整考研线代，但要习惯：

- **向量**：`x = np.array([q, qd])`，形状 `(2,)`  
- **矩阵乘向量**：`x_dot = A @ x + B * u`（`@` 是矩阵乘法）  
- **元素级运算**：`np.sin(theta)` 对数组每个元素计算（广播）

这与 [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html) 的「数组基础」「广播」一致；更深理论可结合 Virk [ML Bible](https://www.arjunvirk.com/writing/ml-guide) 中的神经网络数学章 **课外**阅读，本仓库 T05 只用到 **小矩阵乘**。

---

## 2.2 为什么不用纯 Python 列表算仿真

倒立摆状态是向量 **x ∈ ℝⁿ**，时间轴上有成千上万个采样点。用列表做 `x[i+1] = x[i] + ...` 会又慢又难读。

**NumPy** 提供：

- `ndarray`：同质数值数组  
- **向量化**：对整个数组一次运算（底层 C/Fortran）  
- 与 SciPy、Matplotlib 无缝衔接

---

## 2.3 数组创建与形状

```python
import numpy as np

t = np.linspace(0.0, 3.0, 300)   # 300 个等间隔时间点
x = np.zeros(2)                    # 状态 [位置, 速度] 占位
A = np.array([[0, 1], [-1, -0.5]])  # 2x2 矩阵（以后会来自线性化）
```

要点：

- `shape`：`(300,)` 与 `(2, 2)` 不同，矩阵乘法用 `@` 或 `np.dot`。  
- **dtype** 默认 `float64`，与控制仿真足够。

---

## 2.4 向量化与广播

```python
y = np.exp(-t / 0.5)          # 对每个 t 元素计算
z = 2.0 * y + 1.0             # 标量与数组广播
```

避免：

```python
# 慢且丑：除非教学演示，不要用
for i in range(len(t)):
    y[i] = np.exp(-t[i] / 0.5)
```

---

## 2.5 Matplotlib：仿真结果的「证据」

复试 PPT 需要曲线图。最小工作流：

1. 用 NumPy 算 `t`, `y`  
2. `plt.plot(t, y)`  
3. 坐标轴标签、图例、网格  
4. 无显示器时 `plt.savefig`

**必读脚本**：`weeks/week01/hello_sim.py`。

### 2.5.1 一阶阶跃响应在说什么

传递函数常写 \(G(s) = \dfrac{K}{\tau s + 1}\)。单位阶跃下：

\[
y(t) = K\left(1 - e^{-t/\tau}\right), \quad t \ge 0
\]

- **K**：稳态增益（曲线最终趋近的值）  
- **τ**：时间常数（越大上升越慢）

这不是倒立摆，而是让你熟悉 **「输入阶跃 → 输出曲线」** 这一自控语言。后面 PID 整定看的也是这类响应。

### 2.5.2 实验建议

把 `tau` 改为 `0.2`、`1.0` 各运行一次，保存两张图，笔记里写一句对比。

---

## 2.6 随机数与可复现（预习）

以后做 AI01 或 RL 会用到：

```python
rng = np.random.default_rng(seed=42)
noise = rng.normal(0.0, 0.01, size=t.shape)
```

固定 `seed` 便于对比实验与复试演示。

---

## 2.7 与平衡车/倒立摆的联系

| 概念 | 在本章 | 在后续 |
|------|--------|--------|
| 时间数组 `t` | 阶跃响应 | `simulation.py` 主循环 |
| 状态向量 | 标量 `y` | `[x, θ, ẋ, θ̇]` |
| 画图 | 单曲线 | 多子图：角度、力矩、相平面 |

---

## 必做

- [ ] 运行 `hello_sim.py`，读懂 `first_order_step_response` 的解析公式与代码对应。  
- [ ] 改 `tau`，观察曲线变化，能口头解释。  
- [ ] 在 Python 交互环境或临时脚本里：`np.linspace`、`np.zeros`、`np.exp` 各试一次。

## 选做

- [ ] 在同一张图上画 `tau=0.2` 与 `tau=1.0` 两条曲线并加图例。  
- [ ] 阅读 NumPy 快速入门「数组基础」一节。

---

**上一章**：[T01](T01-Python语言基础.md) · **下一章**：[T03 · 常微分方程与仿真直觉](T03-常微分方程与仿真直觉.md)
