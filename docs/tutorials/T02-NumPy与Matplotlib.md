# T02 · NumPy 与 Matplotlib（零基础科学计算讲义）

**章节 ID**：T02  
**预计用时**：5–7 天（与 T01 末尾、Week 1–2 重叠）  
**前置**：T01 能写 `for` 循环与函数；环境能 `import numpy, matplotlib`  
**配套脚本**：[`weeks/week01/hello_sim.py`](../../weeks/week01/hello_sim.py)

**外部对照**：[NumPy 快速入门](https://numpy.org/doc/stable/user/quickstart.html)（建议中英文对照看「数组创建、索引、广播」三节）。本章用 **控制/仿真** 语境把同一套概念写厚。

---

## 如何使用本章

学习顺序（与 T01 相同：**先跑通再讲**）：

```text
pip/venv 已 OK → 运行 hello_sim.py → 读 §2.5 阶跃响应 → 每节抄代码改参数
    → 完成练习 → 再读 T03 的 ODE
```

**本章结束时你应该能**：

- 创建 `ndarray`，理解 `shape` 与 `dtype`  
- 用向量化代替大部分 `for` 数值循环  
- 写 `A @ x` 表示二维状态方程（预习 T04）  
- 用 Matplotlib 画 `t-y` 曲线并保存图片（复试 PPT 素材）

---

## 2.1 为什么仿真必须用 NumPy（而不是纯 Python 列表）

假设你要算 10000 个时间点的一阶响应 \(y(t)=1-e^{-t/\tau}\)。

**纯 Python 列表**（慢、难读）：

```python
import math
t_list = [i * 0.001 for i in range(10000)]
y_list = []
for t in t_list:
    y_list.append(1.0 - math.exp(-t / 0.5))
```

**NumPy**（快、像写公式）：

```python
import numpy as np
t = np.linspace(0.0, 10.0, 10000)
y = 1.0 - np.exp(-t / 0.5)
```

倒立摆以后状态是 **4 维向量 × 上万时间步**；AI01 的 rollout 要生成成千上万样本。**列表能写，但你会痛苦**——这就是 NumPy 存在的原因。

**练习 ⭐**：在 REPL `import numpy as np`，`print(np.__version__)`。

---

## 2.2 第一个数组：从 list 到 ndarray

```python
import numpy as np

angles = [2.1, 1.8, 1.2]
a = np.array(angles)
print(a, type(a), a.dtype, a.shape)
```

要点：

- `ndarray` **元素类型一致**（全是 float 或全是 int）  
- `shape` 是元组：一维长度 3 为 `(3,)`，注意逗号  
- `dtype` 常见 `float64`、`int64`

```python
b = np.array([1, 2, 3])      # int
c = np.array([1.0, 2, 3])    # float
print(b.dtype, c.dtype)
```

**常见错误 vs 推荐**

```python
# ❌ 以为 np.array 还能像 list 随意混类型当「对象数组」——初学先避免
# np.array([1, "two"])

# ✅ 数值仿真统一 float
x = np.array([0.0, 0.1, 0.2], dtype=float)
```

**练习 ⭐**：`np.array([0, 1, 2])` 与 `np.array([0.0, 1.0, 2.0])` 的 `dtype` 分别是什么？

---

## 2.3 创建数组的常用工厂

控制仿真里反复出现的几种：

```python
import numpy as np

zeros = np.zeros(3)              # [0., 0., 0.]  初值状态
I2 = np.eye(2)                   # 2x2 单位阵
t = np.linspace(0.0, 3.0, 300)   # 0~3 秒，300 点（含端点）
t2 = np.arange(0.0, 3.0, 0.01)   # 步长 0.01，右端可能不含 3.0
ones = np.ones((2, 2))           # 2x2 全 1
```

`linspace` vs `arange`：

- 想要 **固定点数** 画图 → `linspace(0, T, N)`  
- 想要 **固定步长 dt** 仿真 → `np.arange(0, T, dt)` 或 `range(int(T/dt))`

**练习 ⭐**：`np.linspace(0, 1, 5)` 打印 5 个数；手算是否含 0 和 1。  
**练习 🔶**：`dt=0.001`, `T=1.0`，用 `arange` 生成 `t`，`len(t)` 是多少？

---

## 2.4 形状 shape、重塑 reshape、转置

```python
import numpy as np
A = np.array([[0.0, 1.0],
              [-1.0, -0.5]])
print(A.shape)    # (2, 2)
print(A.T)        # 转置

v = np.array([1.0, 2.0])
print(v.shape)    # (2,)
```

**列向量习惯**（以后写 \(x\in\mathbb{R}^2\)）：

```python
v_col = v.reshape(2, 1)   # (2, 1)
v_row = v.reshape(1, 2)   # (1, 2)
```

**常见错误 vs 推荐**

```python
# ❌ 以为 len(A) 是元素总数
# len(A) 对 2d 数组是「行数」

# ✅ 元素总数
print(A.size)
```

**练习 ⭐**：创建 `2×2` 矩阵 `[[0,1],[-2,-3]]`，打印 `shape` 与 `A[1,0]`。

---

## 2.5 索引与切片（一维）

与 Python list 类似，但支持 **布尔索引**（以后筛数据用）：

```python
import numpy as np
y = np.array([0.0, 0.63, 0.86, 0.95, 1.0])
print(y[0], y[-1], y[1:3])   # 切片 1:3 不含 3

mask = y < 0.9
print(mask, y[mask])
```

**练习 ⭐**：对 `t = np.linspace(0, 2, 5)`，打印 `t[2:]` 和 `t[t > 1.0]`。

---

## 2.6 二维索引与「行/列」

```python
import numpy as np
M = np.array([[1, 2, 3],
              [4, 5, 6]])
print(M[0, 1])    # 2
print(M[1, :])    # 第二行
print(M[:, 0])    # 第一列
```

状态空间常写 \(x\in\mathbb{R}^n\)；多个时间步可堆成 `(n_steps, n_state)` 矩阵（每行一个时刻）。

---

## 2.7 向量化：同一操作作用于每个元素

```python
import numpy as np
theta = np.array([0.0, 0.1, -0.05, 0.2])
s = np.sin(theta)          # 每个元素 sin
e = 0.0 - theta            # 期望 0 减测量
u = 2.0 * e                # 标量乘数组
```

对比 **错误写法**（慢，仅教学对比）：

```python
# ❌ 不必这样
s_slow = np.array([np.sin(t) for t in theta])

# ✅
s = np.sin(theta)
```

**练习 ⭐**：`tau=0.5`，`t=np.linspace(0,3,100)`，一行算 `y = 1 - np.exp(-t/tau)`。

---

## 2.8 广播 broadcasting（必须搞懂）

规则直觉：**从尾部对齐 shape，某维为 1 或相等则可广播**。

```python
import numpy as np
t = np.linspace(0, 1, 5)      # shape (5,)
tau = np.array([0.2, 0.5, 1.0])  # shape (3,)
# 想画三条不同 tau 的曲线：需要 (3,5) 的网格
T, Tau = np.meshgrid(t, tau, indexing="ij")  # 进阶；初学可用循环
```

更简单的广播例子：

```python
a = np.array([[1], [2], [3]])   # (3, 1)
b = np.array([10, 20])          # (2,)
# a + b 会按规则广播——若维度对不上会 ValueError
```

初学阶段若广播报错，**用 `reshape` 明确形状** 比硬记规则更快：

```python
v = np.array([1.0, 2.0])
c = 3.0
print(v * c)   # 标量广播到每个元素
```

**练习 🔶**：`a=np.ones((3,1))` 与 `b=np.ones(4)` 相加 **不会报错**（广播成 `(3,4)`）。改试 `np.ones((3,2)) + np.ones(4)`：尾维 `2` 与 `4` 既不相等也不为 1，才会 `ValueError`。

---

## 2.9 矩阵乘法与状态方程（控制核心）

线性系统 \(\dot{x} = A x + B u\) 在离散时间演示里常写：

```python
import numpy as np
A = np.array([[0.0, 1.0],
              [-4.0, -0.5]])
B = np.array([[0.0],
              [1.0]])
x = np.array([0.1, 0.0])
u = 0.0

x_dot = A @ x + (B[:, 0] * u)   # B 是列向量时也可 B @ np.array([u])
print(x_dot)
```

符号 `@` 是矩阵乘；`**` 是逐元素幂，不要混：

```python
M = np.array([[1, 2], [3, 4]])
print(M * M)      # 逐元素
print(M @ M)      # 矩阵乘
```

**常见错误 vs 推荐**

```python
# ❌ 用 * 做矩阵乘
# x_dot = A * x   # 逐元素，物理意义错

# ✅
x_dot = A @ x
```

**练习 ⭐**：给定 `A=[[0,1],[-1,-1]]`, `x=[1,0]`，手算 `A@x` 再用 NumPy 验证。  
**练习 🔶**：`u=1.0`，`B=[[0],[1]]`，算 `A@x + B.flatten()*u`（维数对齐练习）。

---

## 2.10 聚合：sum、mean、max、argmax

```python
import numpy as np
err = np.array([0.1, -0.05, 0.02, 0.0])
print(np.abs(err).max())
print(err.mean())
```

仿真后常看 `np.max(np.abs(theta))` 是否超过安全角。

**练习 ⭐**：对 100 个 `np.random.default_rng(0).normal(0, 0.01, 100)` 求 `mean` 与 `std`（预习噪声）。

---

## 2.11 Matplotlib 入门：为什么控制论文全是曲线

**最小工作流**（与 `hello_sim.py` 一致）：

1. 用 NumPy 算 `t`, `y`  
2. `plt.plot(t, y)`  
3. 坐标轴标签、图例、网格  
4. `plt.show()` 或 `plt.savefig`

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0.0, 3.0, 300)
tau = 0.5
y = 1.0 - np.exp(-t / tau)

plt.figure(figsize=(8, 4.5))
plt.plot(t, y, linewidth=2, label=rf"$\tau$={tau}")
plt.axhline(1.0, color="gray", linestyle="--", label="稳态 1.0")
plt.xlabel("时间 t (s)")
plt.ylabel("输出 y")
plt.title("一阶系统单位阶跃响应")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("/tmp/step_demo.png", dpi=120)
print("saved")
```

在项目根运行官方脚本：

```bash
python weeks/week01/hello_sim.py
```

**常见错误 vs 推荐**

```python
# ❌ 不 plt.figure 反复 plot 叠在一起看不清
# ✅ 每张图 figure 一次，或 plt.clf()

# ❌ 无 DISPLAY 的服务器上 plt.show() 什么都不出
# ✅ 像 hello_sim 一样 savefig
```

**练习 ⭐**：改 `hello_sim.py` 里 `tau=1.0`，重新运行，描述曲线变快还是变慢。

---

## 2.12 一阶阶跃响应：公式、代码、物理语言

传递函数常写 \(G(s)=\dfrac{K}{\tau s + 1}\)。**单位阶跃**输入下：

\[
y(t) = K\left(1 - e^{-t/\tau}\right),\quad t\ge 0
\]

| 符号 | 含义 |
|------|------|
| \(K\) | 稳态增益（曲线最终趋近值） |
| \(\tau\) | 时间常数（越大上升越慢） |

`hello_sim.py` 中函数：

```python
def first_order_step_response(t, K=1.0, tau=0.5):
    return K * (1.0 - np.exp(-t / tau))
```

**与自控课的联系**：PID 整定、电机电流环、速度环常先看成「一阶或近似一阶」环节；你会反复看到「阶跃响应」「超调」「调节时间」——本章只建立 **「输入突变 → 输出曲线」** 直觉。

### 2.12.1 实验：多 τ 对比（必做）

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0.0, 5.0, 400)
for tau in (0.2, 0.5, 1.0):
    y = 1.0 - np.exp(-t / tau)
    plt.plot(t, y, label=rf"tau={tau}")
plt.xlabel("t (s)")
plt.ylabel("y")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("weeks/week01/compare_tau.png", dpi=120)
```

**练习 ⭐**：在笔记写：**τ 增大 2 倍，曲线是更慢还是更快？**  
**练习 🔶**：在 \(t=\tau\) 处，解析值 \(y(\tau)=1-e^{-1}\approx 0.632\)；用 NumPy 验证 `1-np.exp(-1)`。

### 2.12.2 可选：用 ODE 数值积分离线（预习 T03）

同一系统 \(\dot{y}=(K-y)/\tau\) 在 \(y(0)=0\) 时等价于上式。T03 会用 `solve_ivp`；这里可用欧拉：

```python
import numpy as np
tau, K, dt = 0.5, 1.0, 0.01
y = 0.0
ys = []
for _ in range(int(3.0 / dt)):
    y += dt * ((K - y) / tau)
    ys.append(y)
# 与解析解在 t=3 对比
t_end = 3.0
y_analytic = K * (1 - np.exp(-t_end / tau))
print("Euler last", ys[-1], "analytic", y_analytic)
```

若 `dt` 太大，欧拉会偏——这就是 T03 要讲的内容。

---

## 2.13 子图 subplot（多状态一起画）

倒立摆以后要同时画角度与角速度：

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 200)
theta = 0.1 * np.cos(2 * np.pi * 0.5 * t)   # 示意波形
omega = -0.1 * 2 * np.pi * 0.5 * np.sin(2 * np.pi * 0.5 * t)

fig, axes = plt.subplots(2, 1, sharex=True, figsize=(8, 5))
axes[0].plot(t, theta)
axes[0].set_ylabel("theta (rad)")
axes[0].grid(True, alpha=0.3)
axes[1].plot(t, omega)
axes[1].set_ylabel("omega (rad/s)")
axes[1].set_xlabel("t (s)")
axes[1].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("/tmp/two_subplots.png", dpi=120)
```

**练习 🔶**：把 `hello_sim` 的阶跃图放在 `subplot(2,1,1)`，下面子图画 `dy/dt` 的数值差分（预习）。

---

## 2.14 随机数与可复现（AI01 / 实验必备）

```python
import numpy as np
rng = np.random.default_rng(seed=42)
noise = rng.normal(loc=0.0, scale=0.01, size=100)
print(noise.mean(), noise.std())

rng2 = np.random.default_rng(seed=42)
print(np.allclose(noise, rng2.normal(0, 0.01, 100)))
```

**固定 seed** 不是为了「造假」，而是 **对比两次改代码后曲线是否变好**。

**练习 ⭐**：`seed=0` 与 `seed=1` 各生成 5 个随机数，观察不同。

---

## 2.15 与纯 Python 列表的互操作

```python
import numpy as np
lst = [1.0, 2.0, 3.0]
a = np.asarray(lst)
a[0] = 99.0
print(lst)   # list 不变，asarray 复制了新 buffer 视情况——初学用 np.array(lst) 当拷贝
```

从 CSV 读数据时常 `np.loadtxt`（后续周次）；Week 1 知道 `array` 即可。

---

## 2.16 性能直觉（不必背 benchmark）

```python
import numpy as np
n = 200_000
# %timeit 在 IPython 里更好；这里只示意
a = np.linspace(0, 1, n)
b = np.sin(a)
```

向量化的意义：**同样公式，步数上万时差距巨大**。不要对所有逻辑强行向量化——**外层时间步循环 + 内层向量状态** 在初学阶段完全 OK。

---

## 2.17 渐进式综合练习

### 第 1 组 ⭐（数组基础）

1. `np.zeros(4)` 当作 `[x, x_dot, theta, theta_dot]` 占位，改第 3 个为 `0.1`。  
2. `t=np.linspace(0,2,41)`，`len(t)` 与步长近似多少？  
3. `y=1-np.exp(-t/0.5)`，求 `y[-1]`。

### 第 2 组 ⭐（画图）

1. 复刻 `hello_sim` 的图，标题改成你自己的名字。  
2. 同图三条 τ 曲线 + legend（§2.12.1）。  
3. 保存到 `weeks/week01/my_step.png`。

### 第 3 组 ⭐（线性代数）

1. `A=[[0,1],[-2,-3]]`, `x=[1,0]`，算 `A@x`。  
2. `x=np.linspace(0,1,3)`，`y=2*x+1`，用 `plt.plot` 画折线。

### 第 4 组 🔶（贴近项目）

1. 读 `hello_sim.py` 全文，在注释里标出「哪行创建 t」「哪行调用向量化 exp」。  
2. 写函数 `step_response(t, K, tau)` 返回数组，被 `main` 调用。  
3. 用 `np.max(np.abs(y-K))` 估计稳态误差（应接近 0）。

### 第 5 组 🔶（为 T03 铺路）

1. 欧拉积分 \(\dot{y}=-y/\tau\)，`y0=1`, `dt=0.1` 与 `0.01` 各跑 50 步，比较与解析解误差。  
2. 写下：为什么仿真要选 `dt` 远小于 `tau`？

---

## 2.18 与平衡车 / 倒立摆的映射表

| 本章概念 | 现在例子 | 后续 `inverted_pendulum` |
|----------|----------|---------------------------|
| `t = np.linspace(...)` | 阶跃时间轴 | 仿真时间轴 |
| 状态向量 | `np.zeros(4)` | `[x, ẋ, θ, θ̇]` |
| `A @ x` | 2×2 演示 | 线性化 \(A,B\) |
| `plt.plot` | 阶跃 | 角度、力矩、相平面 |
| `rng.normal` | 噪声 | 传感器噪声、AI01 数据 |

---

## 2.19 自测清单

1. `shape (5,)` 与 `(5, 1)` 有何区别？  
2. `A @ x` 与 `A * x` 有何区别？  
3. 一阶系统 \(\tau\) 变大，阶跃响应变快还是变慢？  
4. 无图形界面时如何保存图？  
5. 为什么固定 `random seed`？

---

## 必做

- [ ] 运行 `hello_sim.py`，完成 §2.12 全部 ⭐ 练习。  
- [ ] 完成 **第 1–3 组**综合练习。  
- [ ] 在交互环境亲手输入 §2.7、§2.9 各一遍。  
- [ ] 保存至少 **一张** 自己生成的 `.png` 到 `weeks/week01/`。

## 选做

- [ ] NumPy 官方 Quickstart 全文 + 每节 1 个实验。  
- [ ] 完成第 4、5 组。  
- [ ] 预习 `scipy.integrate.solve_ivp` 文档首页（T03 用）。  
- [ ] 安装并试 `python-control` 的 `step_response`（仅当 T04 选做需要）。

---

**上一章**：[T01](T01-Python语言基础.md) · **下一章**：[T03 · 常微分方程与仿真直觉](T03-常微分方程与仿真直觉.md)
