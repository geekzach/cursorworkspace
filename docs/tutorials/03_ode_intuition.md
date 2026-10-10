# 03 · ODE 直觉（控制学生版）

## 为什么学这个

倒立摆、平衡车的核心不是背公式，而是：**状态现在在哪、受力矩后下一瞬间怎么变**。连续时间用 **常微分方程（ODE）** 写 \(\dot{x} = f(x, u)\)；计算机用 **离散步长 `dt`** 一步步积分，这叫 **仿真（simulation）** 或 **rollout**。AI01 用真 ODE 生成标签，PID/LQR 以后也在同一类模型上闭环。

---

## 1. 状态向量

简化摆（本仓库 AI01）：

\[
x = \begin{bmatrix} \theta \\ \omega \end{bmatrix}
\]

- \(\theta\)：摆角（rad），竖直向上为 0。
- \(\omega\)：角速度 (rad/s)。
- 控制 \(u\)：施加力矩 (N·m)。

**仓库对照**：[`src/learning/pendulum.py`](../../src/learning/pendulum.py) 文件头注释与 `PendulumParams`。

连续动力学（含阻尼）：

\[
\dot\theta = \omega,\quad
\dot\omega = -\frac{g}{L}\sin\theta - b\omega + \frac{u}{mL^2}
\]

函数 `pendulum_deriv` 返回 \([\dot\theta, \dot\omega]\)。

---

## 2. 从 ODE 到代码：导数函数

```python
def pendulum_deriv(_t, state, u, p):
    theta, omega = state[0], state[1]
    theta_dot = omega
    omega_dot = -(p.g / p.L) * np.sin(theta) - p.b * omega + u / (p.m * p.L ** 2)
    return np.array([theta_dot, omega_dot])
```

- **`sin(θ)`**：大角度非线性；小角度 \(\sin\theta \approx \theta\) 才得到线性化模型（Week 4）。
- **`b·ω`**：阻尼，否则数值上可能「永动机」。
- **`u/(mL²)`**：力矩换算成角加速度贡献。

---

## 3. 数值积分：为什么需要 RK4

电脑没有「真正的连续时间」，只有：

\[
x_{k+1} \approx x_k + \text{（用 } f \text{ 估的增量）}
\]

**欧拉法**（最粗）：\(x_{k+1} = x_k + dt \cdot f(x_k)\) —— 步长大时易漂、不稳定。

**RK4（四阶龙格–库塔）**：在一步内用 4 次导数估计，**精度更好**，本仓库 `rk4_step` 采用此法。你 **不必背系数**，只需知道：

> 给定 `state, u, dt, params`，`rk4_step` 给出 **下一时刻状态**。

**仓库对照**：`pendulum.py` 的 `rk4_step`；[`weeks/ai01_nn_dynamics/ex01_preview_rollout.py`](../../weeks/ai01_nn_dynamics/ex01_preview_rollout.py) 里 `for` 循环调用。

**预习运行**：

```bash
export PYTHONPATH="$(pwd)/src"
python weeks/ai01_nn_dynamics/ex01_preview_rollout.py
```

**预期图**：

- 上图 \(\theta(t)\)：前段恒正力矩角增大，后段反向力矩角回落。
- 下图 \(\omega(t)\)：与力矩切换对应变化。

改 `u_pos = 0.15` 为 `0.3`，振幅应明显变大。

---

## 4. Rollout = 开环仿真一条轨迹

```
初值 x0 ──► [u0,u1,...] ──► x1,x2,...,xT
           每步 rk4_step
```

**闭环控制**（以后）：\(u_k = \text{PID}(e_k)\) 每步依赖传感器。  
**AI01 数据**：每样本随机 \((\theta,\omega,u)\)，只积分 **一步** 得 \((\theta^+,\omega^+)\)——监督学习标签来自 **真模型**。

**仓库对照**：[`src/learning/rollout.py`](../../src/learning/rollout.py) 的 `generate_dataset`。

---

## 5. 步长 `dt` 怎么选

| dt 太大 | dt 合适（本仓库 0.02 s） |
|---------|---------------------------|
| 轨迹失真、能量不守恒感 | 与力矩变化尺度匹配 |
| NN 一步预测误差被积分放大 | 实物控制周期常 1–5 ms 量级，仿真可先用 10–20 ms 学概念 |

---

## 6. 和完整倒立摆的关系

`src/inverted_pendulum/model.py` 尚未实现 cart-pole；AI01 是 **去掉小车自由度** 的摆，便于先练「ODE → 数据 → 拟合」。复试可说：「支线用简化 ODE，主线寒假前补全 cart-pole / MuJoCo。」

---

## 常见踩坑

1. **角度单位** —— 全程 rad；`sin` 里若是度会全错。
2. **竖直向上 θ=0** —— 有的教材以下垂为 0，读文献要核对。
3. **只改 `dt` 不改 `u` 尺度** —— 大步长下同一 `u` 可能数值爆炸，先减小 `dt` 试。
4. **混淆「一步数据集」与「长 rollout」** —— `ex01` 是长轨迹；`generate_dataset` 是单步样本集合。
5. **忘记 PYTHONPATH** —— `ex01` 自带 `sys.path` 插入，一般能跑；自己写新脚本时要记得。

---

## 本节练习

### 必做

1. 运行 `ex01_preview_rollout.py`，描述 **力矩从正变负** 的时刻附近，\(\theta\) 曲线有何变化（两三句话）。
2. 打开 `pendulum.py`，指出 **阻尼项** 在公式里对应哪一行代码。
3. 在 Python 交互里：`from learning.pendulum import PendulumParams, rk4_step`（先 `export PYTHONPATH`），初值 `[0.1, 0.0]`，`u=0`，`dt=0.02`，调用一次 `rk4_step`，打印结果（θ 应略大于 0.1，因 ω 从 0 开始被重力项拉动）。

### 选做

1. 把 `ex01` 里 `steps` 改成 400，观察总时长变化（\(T = steps \cdot dt\)）。
2. 阅读 `rollout.py` 中 `theta = rng.uniform(-0.8, 0.8)`，解释为何采样范围不是 \([-π, π]\) 全覆盖（提示：大角度更难一步预测、训练稳定性）。

---

**参考思路**：[`answers/03_ode_intuition.md`](answers/03_ode_intuition.md)  
**下一节**：[04 神经网络拟合动力学](04_nn_dynamics_fit.md)
