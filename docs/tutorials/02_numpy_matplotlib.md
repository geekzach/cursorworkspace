# 02 · NumPy 与 Matplotlib

## 为什么学这个

一阶阶跃、摆角曲线、训练误差散点——**复试 PPT 里全是图**。用纯 Python `list` 也能画，但仿真与神经网络数据是 **成千上万维向量**；`numpy` 做数组运算，`matplotlib` 出图，是 Week 1 的 `hello_sim.py` 和 AI01 的共同语言。

---

## 1. NumPy 数组 `ndarray`

```python
import numpy as np

t = np.linspace(0.0, 3.0, 300)   # 300 个等间隔点，含 0 和 3
y = np.zeros_like(t)               # 与 t 同形状的全 0
```

| 概念 | 含义 |
|------|------|
| `shape` | 各维长度，如 `(300,)` 或 `(4000, 3)` |
| `dtype` | 元素类型，常用 `float64` |
| 向量化 | `y = K * (1 - np.exp(-t/tau))` 一次算整条曲线，无需 `for` |

**仓库对照**：[`weeks/week01/hello_sim.py`](../../weeks/week01/hello_sim.py) 中 `np.linspace`、`first_order_step_response`。

---

## 2. 一阶阶跃响应（控制预习）

传递函数常写 \(G(s) = \dfrac{K}{\tau s + 1}\)。单位阶跃下：

\[
y(t) = K\left(1 - e^{-t/\tau}\right), \quad t \ge 0
\]

- **K**：稳态增益（图中水平虚线）。
- **τ**：时间常数；**τ 越大，爬升越慢**。

**动手**：在 `hello_sim.py` 里改 `tau = 0.5` → `1.0` 或 `0.2`，重新运行，对比 PNG 或图窗。

**预期现象**：

| τ | 约 63% 稳态时刻 | 直观 |
|---|-----------------|------|
| 0.2 s | ~0.2 s | 快 |
| 0.5 s | ~0.5 s | 默认 |
| 1.0 s | ~1.0 s | 慢 |

这与一阶系统「时间常数」定义一致，后面 PID 整定会再见到类似「快慢」。

---

## 3. Matplotlib 基本流程

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4.5))
plt.plot(t, y, linewidth=2, label=r"$y(t)$")
plt.xlabel("时间 t (s)")
plt.ylabel("输出 y")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("out.png", dpi=120)  # 无 GUI 时常用
```

**仓库对照**：`hello_sim.py` 的 `main()` 绘图与 `_save_or_show` 逻辑（有 DISPLAY 则 `show()`，否则存盘）。

**子图**（AI01 会用到）：

```python
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
axes[0].scatter(x_true, x_pred, s=8, alpha=0.5)
axes[1].plot(t, omega)
```

---

## 4. 广播（broadcasting）直觉

形状兼容时，标量与数组运算「自动展开」：

```python
tau = 0.5
y = 1.0 * (1.0 - np.exp(-t / tau))  # t 是 (300,)，tau 是标量
```

**踩坑**：两个数组相乘要形状能广播，例如 `(N,3)` 与 `(3,)` 常可；`(N,2)` 与 `(N,3)` 不行。

---

## 5. 与 AI01 数据的衔接

`generate_dataset` 返回：

- `X.shape == (n_samples, 3)` → `[θ, ω, u]`
- `Y.shape == (n_samples, 2)` → `[θ⁺, ω⁺]`

列是 **特征维**，行是 **样本**。训练时对整批矩阵做 `X @ W`（见 04 节），这就是 numpy 的价值。

---

## 常见踩坑

1. **`import numpy as np` 写成 `import numpy`** —— 惯例用 `np`，与全仓库一致。
2. **`plt.show()` 在 SSH 无显示** —— 用 `savefig`，本仓库脚本已处理。
3. **改图不刷新** —— 多次 `plot` 在同一 figure 上会叠线；新开图用 `plt.figure()` 或 `subplots`。
4. **`linspace` 点数太少** —— 曲线锯齿；阶跃响应 200–500 点通常够。
5. **单位混用** —— 本仓库角度用 **弧度 rad**；练习列表里有时是 **度** 仅作示意，建模时务必统一。

---

## 本节练习

### 必做

1. 运行 `python weeks/week01/hello_sim.py`，保存/查看 `week01_step_response.png`，在图旁标注 **K、τ、稳态值**。
2. 在同一脚本里设 `tau=0.2` 与 `tau=1.0` 各跑一次（或复制两行 `y` 画在同一张图两条曲线），肉眼看 **谁更快到 0.63×K**。
3. 写 8 行以内脚本：用 `np.linspace(0, 2*np.pi, 100)` 画 `sin(theta)`，横轴 `theta`，存为 `my_sin.png`。

### 选做

1. 读 `hello_sim.py` 里 `os.environ.get("DISPLAY")` 判断逻辑，说明 WSL 下你机器走「弹窗」还是「存盘」。
2. 用 `np.random.default_rng(0).uniform(-1, 1, size=5)` 生成 5 个数，算 `np.mean` 与 `np.std`，预习 AI01 随机采样。

---

**参考思路**：[`answers/02_numpy_matplotlib.md`](answers/02_numpy_matplotlib.md)  
**下一节**：[03 ODE 直觉](03_ode_intuition.md)
