# T04 · 控制预备：从阶跃到 PID 与状态空间（零基础讲义）

**章节 ID**：T04  
**预计用时**：7–10 天（Week 3–5；见 [`SEMESTER_PLAN.md`](../checklists/SEMESTER_PLAN.md)）  
**前置**：T02 阶跃响应 · T03 ODE/`solve_ivp`/仿真循环 · T01 §1.14 / [T01b](T01b-类与对象入门.md) 的 `PID` 类  
**代码落点**：`src/inverted_pendulum/controllers/pid.py`、`model.py`、`simulation.py`

**技术路径（scope rails）**：

```text
T02 一阶阶跃 → T03 开环 ODE → 本章 PID 闭环 → 线性化 A,B → Week5 LQR 预习
可选对照：python-control 的 tf/step_response（不替代自写仿真）
不覆盖：RL、MPC、LQR 完整推导（寒假/Week5）、PyTorch
```

---

## 如何使用本章

1. 每节 **先跑代码**（可用纯 Python float，再迁 NumPy）。  
2. 标 ⭐ 必做；🔶 进阶。  
3. 离散 PID 建议用 **类**（与 T01b 一致），不要每步 `new PID()`。

**本章结束时你应该能**：画闭环框图；实现带限幅的离散 PID；对质量–弹簧做 P/PD 闭环并画 `q(t)`；解释 \(\theta=0\) 平衡点与 \(A,B\) 含义。

---

## 4.0 本章目标对照表

| 能力 | 验收 |
|------|------|
| 框图语言 | 口述 \(r,y,e,u\) 在平衡车上的含义 |
| 离散 PID | `step(e,dt)` 手算 3 步与代码一致 |
| 与阶跃关系 | 说清「快/稳/不抖」与 \(K_p,K_i,K_d\) 方向 |
| 状态空间 | 写出 2×2 示例的 \(A,B\) |
| 线性化 | 说明为何在 \(\theta=0\) 展开 |
| 仓库 | 能读 `pid.py` 骨架并填 `step` |

---

## 4.1 开环 vs 闭环（先建立对比）

### 4.1.1 开环（T03 已做）

控制量 \(u(t)\) **与你的程序事先写死**，不看输出：

```python
u = 0.5   # 或 u = sin(t)
# plant.step(dt, u)
```

问题：扰动、参数变化、初值不同 → 输出不可控。

### 4.1.2 闭环（本章核心）

测量输出 \(y\)，与设定 \(r\) 比较，用 **控制器** 算 \(u\)：

\[
e = r - y,\quad u = C(e)
\]

```python
r = 0.0          # 期望摆角直立
theta = 0.08     # IMU 测量
e = r - theta
u = Kp * e
```

**练习 ⭐**：`theta = -0.05`，`e` 为正还是负？若 `Kp>0`，`u` 符号希望怎样「推」摆回去？（口头即可。）

### 4.1.3 框图

```text
设定值 r ──(+)──► 控制器 C ──► 被控对象 P ──► 输出 y
              ▲                         │
              └── 反馈 ◄── 传感器 ──────┘
```

减号在求和点：\(e=r-y\)。若传感器有偏差，等价于扰动（实物常见）。

---

## 4.2 反馈带来的「纠错」直觉

```python
Kp = 2.0
for theta in (0.2, 0.1, 0.05, 0.01):
    e = 0.0 - theta
    u = Kp * e
    print(f"theta={theta:.2f}  e={e:.2f}  u={u:.2f}")
```

角度仍为正时 \(e<0\)，\(u<0\)（符号取决于你定义的「正力矩方向」——全项目要一致）。

**常见错误 vs 推荐**

```python
# ❌ e = y - r  （符号全反，正反馈发散）
# ✅ e = r - y   （与多数教材一致，除非框图标明反相）
```

---

## 4.3 PID 三项：连续公式与物理含义

\[
u(t) = K_p e(t) + K_i \int_0^t e(\tau)\,d\tau + K_d \frac{de}{dt}
\]

| 项 | 作用 | 平衡车/倒立摆 |
|----|------|----------------|
| \(K_p e\) | 偏离大 → 力大 | 倾角大则加力矩 |
| \(K_i \int e\) | 消 **恒定** 偏差 | 慢漂移；易 windup |
| \(K_d \dot{e}\) | 抑制 **变化太快** | 常用 \(-K_d \dot{\theta}\) |

### 4.3.1 只有 P：为何会有稳态误差

对一阶对象，纯 P 往往 **达不到** \(r\)（除非增益无穷）。需要 I 或前馈。

**练习 ⭐**：T01b 闭环里 `Ki=0` 时，最后 `y` 是否小于 `r`？写一句原因。

### 4.3.2 D 项：对测量微分 vs 对误差微分

仿真有真 \(\dot{\theta}\) 时：

```python
u_d = -Kd * theta_dot   # 等价于对「希望 θ 不变」的阻尼
```

对噪声大的 \(e\) 直接差分会抖——实物要滤波。

---

## 4.4 离散 PID 实现（与仿真 `dt` 绑定）

### 4.4.1 完整类（复习 + 增强）

```python
class PID:
    def __init__(self, Kp, Ki, Kd, u_min=-10.0, u_max=10.0):
        self.Kp, self.Ki, self.Kd = Kp, Ki, Kd
        self.u_min, self.u_max = u_min, u_max
        self.integral = 0.0
        self.prev_error = 0.0

    def reset(self):
        self.integral = 0.0
        self.prev_error = 0.0

    def step(self, error: float, dt: float) -> float:
        self.integral += error * dt
        d_error = (error - self.prev_error) / dt if dt > 0 else 0.0
        u_raw = self.Kp * error + self.Ki * self.integral + self.Kd * d_error
        u = max(self.u_min, min(self.u_max, u))
        self.prev_error = error
        return u
```

### 4.4.2 手算一步（考试式）

`Kp=2, Ki=0, Kd=1`, `dt=0.1`, 上一拍 `e=0.2`, 本拍 `e=0.1`：

- `d_error = (0.1-0.2)/0.1 = -1`  
- `u = 2*0.1 + 0 + 1*(-1) = -0.8`

**练习 ⭐**：用代码 `PID(2,0,1).step(0.1, 0.1)` 前先 `step(0.2,0.1)` 一次，核对是否 `-0.8`。

### 4.4.3 积分饱和（anti-windup 意识）

当 `u` 顶到 `u_max` 但误差仍大，积分继续涨 → 退饱和时超调巨大。

```python
def step_with_conditional_integral(self, error, dt):
    u_raw = self.Kp * error + self.Ki * self.integral + self.Kd * 0.0
    u = max(self.u_min, min(self.u_max, u_raw))
    # 简化 anti-windup：仅当未饱和时积分
    if u == u_raw:
        self.integral += error * dt
    self.prev_error = error
    return u
```

初学可用完整版；实物必须认真处理 windup。

**常见错误 vs 推荐**

```python
# ❌ dt 单位是 ms 却当 s 用（积分差 1000 倍）
# ❌ 每步新建 PID
# ✅ 固定 dt 与 T03 仿真一致；调参前 reset()
```

---

## 4.5 与 T02 一阶阶跃的整定语言

\(G(s)=\dfrac{K}{\tau s+1}\) 阶跃响应：

- **快**：\(\tau\) 小或闭环带宽高  
- **稳**：不超调、不发散  
- **准**：稳态贴 \(r\)

高阶/非线性系统试 PID 时仍问这三句，并 **截图对比**。

### 4.5.1 实验记录模板

| 组 | Kp | Ki | Kd | 现象（一句话） |
|----|----|----|-----|----------------|
| 1 | | 0 | 0 | |
| 2 | | | 0 | |
| 3 | | | | |

**练习 ⭐**：填表三组（可用 T01b 一阶 plant）。

---

## 4.6 质量–弹簧闭环（NumPy + 欧拉）

与 T03 同一 `f`，加 P 控制 \(u=-K_p q\)（调节位置到 0）：

```python
import numpy as np

def simulate_mass_spring_pd(Kp, Ki=0.0, Kd=0.0, dt=0.001, T=5.0):
    m, b, k = 1.0, 0.2, 4.0
    x = np.array([0.15, 0.0])
    pid = PID(Kp, Ki, Kd, u_min=-5, u_max=5)
    r = 0.0
    hist_q = []
    t = 0.0
    n = int(T / dt)
    for _ in range(n):
        q, qd = x
        e = r - q
        u = pid.step(e, dt)
        qdd = (u - b * qd - k * q) / m
        x = x + dt * np.array([qd, qdd])
        hist_q.append(q)
        t += dt
    return np.array(hist_q), t


# 需先定义 PID 类；或从 my_pid_lab 导入
q, _ = simulate_mass_spring_pd(Kp=3.0)
print("final q", q[-1])
```

**练习 ⭐**：`Kp=1,5,15` 各画 `q` 末 2 s 曲线（`matplotlib`）。  
**练习 🔶**：加 `Kd` 用 `qd` 作 D（改 `step` 传入 `-qd` 作微分项）。

---

## 4.7 状态空间：线性系统统一写法

\[
\dot{x} = A x + B u
\]

- \(x\in\mathbb{R}^n\)：状态  
- \(u\in\mathbb{R}^m\)：输入（常 \(m=1\)）  
- \(A\)：自然演化；\(B\)：输入如何进导数

### 4.7.1 2 维示例

\[
\dot{q}=v,\ \dot{v}=-q \Rightarrow
A=\begin{bmatrix}0&1\\-1&0\end{bmatrix},\ B=\begin{bmatrix}0\\0\end{bmatrix}
\]

```python
import numpy as np
A = np.array([[0, 1], [-1, 0]])
x = np.array([0.1, 0.0])
print(A @ x)
```

### 4.7.2 质量–弹簧的 \(A,B\)（\(u\) 为外力）

```python
m, b, k = 1.0, 0.2, 4.0
A = np.array([[0, 1], [-k/m, -b/m]])
B = np.array([[0], [1/m]])
```

**练习 ⭐**：手算 `A @ [0.1, 0]` 与 T03 `mass_spring_rhs` 在 `qd=0` 时是否一致。

### 4.7.3 cart-pole 预览（4 维）

\(x=[x,\dot{x},\theta,\dot{\theta}]^\top\)。**线性化**在 \(\theta=0\) 附近：

\[
\delta\dot{x} \approx A\,\delta x + B\,\delta u
\]

本周 **不要求** 推出具体 \(A\) 数字；要求知道 **何时线性化、平衡点取直立**。

---

## 4.8 非线性线性化（概念 + 数值思路）

\(\dot{x}=f(x,u)\) 在 \((x_0,u_0)\)：

\[
A = \left.\frac{\partial f}{\partial x}\right|_{x_0,u_0},\quad
B = \left.\frac{\partial f}{\partial u}\right|_{x_0,u_0}
\]

```python
# 数值差分示意（2 维），不要在 Week3 硬背 Jacobian 手算
import numpy as np

def f(x, u):
    q, qd = x
    m, b, k = 1.0, 0.2, 4.0
    return np.array([qd, (u - b*qd - k*q)/m])

x0 = np.array([0.0, 0.0])
u0 = 0.0
eps = 1e-6
A_col0 = (f(x0 + [eps, 0], u0) - f(x0, u0)) / eps
A_col1 = (f(x0 + [0, eps], u0) - f(x0, u0)) / eps
A_num = np.column_stack([A_col0, A_col1])
print("A_num\n", A_num)
```

**练习 🔶**：与 §4.7.2 解析 \(A\) 对比差值。

---

## 4.9 可控性直觉（一句话）

能否通过 \(u\) 在有限时间内把状态「推」到你想要的方向？cart-pole 在 \(\theta=0\) 附近 **通常可控**——这是后面 LQR 能用的前提。深入定理 Week5+；现在记住 **\(B\) 非零且合理**。

---

## 4.10 可选：`python-control` 与自写 ODE 对照

安装后（见根 `requirements.txt` 注释）：

```python
# 选做 — 验证 T02 一阶阶跃
# from control import tf, step_response
# import matplotlib.pyplot as plt
# G = tf([1.0], [0.5, 1.0])   # K=1, tau=0.5
# t, y = step_response(G)
# plt.plot(t, y); plt.grid(True); plt.savefig("/tmp/control_pkg_step.png")
```

**期末项目验收仍用** `solve_ivp` 或固定步长自写循环。

---

## 4.11 全状态反馈 vs 只用角度（预习）

| 策略 | 反馈量 | 说明 |
|------|--------|------|
| 仅 PD on \(\theta\) | \(\theta,\dot{\theta}\) | 常见入门 |
| 全状态 | \(x,\dot{x},\theta,\dot{\theta}\) | LQR 常用 |
| 输出反馈 | 仅部分可测 | 实物 IMU+编码器 |

读 cart-pole 博客时 **记录作者用哪些量**。

---

## 4.12 与 `src/inverted_pendulum/controllers/pid.py`

打开骨架，预期你会实现类似：

- `__init__`：增益与限幅  
- `reset`：清积分  
- `step` 或 `compute`：输入 \(e\) 或 \((r, y)\)，输出 \(u\)

**练习 ⭐**：列出文件中已有函数名，用 5 行注释写每个应做什么。

---

## 4.13 与 SEMESTER_PLAN 周次

| 周 | 本章重点 |
|----|----------|
| W46 | §4.1–4.4 框图 + PID 类 |
| W47–W48 | §4.7–4.8 + `model.py` |
| W49–W50 | §4.6 闭环仿真 + 整定表 |

---

## 4.14 渐进式综合练习

### 第 1 组 ⭐

1. 画闭环框图并标 \(r,y,e,u\)。  
2. 手算 PID 一步（§4.4.2）。  
3. 五句话解释 P/I/D。

### 第 2 组 ⭐

1. 完成 T01b `run_closed_loop`。  
2. §4.6 `simulate_mass_spring_pd` 跑 `Kp=5`。  
3. 填 §4.5.1 对比表。

### 第 3 组 🔶

1. 数值 \(A\) 与解析 \(A\) 对比。  
2. `python-control` 阶跃与 T02 图叠在一起。  
3. 读一篇 cart-pole PID 博文做笔记。

### 第 4 组 🔶

在 `pid.py` 实现最小 `PIDController.step`（可 PR 到项目主线），并用 `simulation.py` 占位测试（若已有接口）。

---

## 4.15 自测

1. \(e=r-y\) 还是 \(y-r\)？  
2. 纯 P 为何可能有稳态误差？  
3. `integral` 为何要在 `reset` 清零？  
4. \(A,B\) 各一句话物理意义？  
5. 为何在 \(\theta=0\) 线性化？

---

## 必做

- [ ] §4.1–4.4 + T01b 闭环。  
- [ ] 第 1、2 组练习。  
- [ ] 读 `pid.py` 骨架。  
- [ ] 自测 1–4。

## 选做

- [ ] 第 3、4 组。  
- [ ] 质量–弹簧 PD 曲线 png 存入复试素材夹。

---

## 4.16 传感器与反馈信号（实物预习）

| 信号 | 来源 | 仿真里常当作 |
|------|------|----------------|
| \(\theta\) | IMU 融合 | `state[2]` |
| \(\dot{\theta}\) | 陀螺仪 | `state[3]` |
| \(\dot{x}\) | 编码器微分 | `state[1]` |

闭环时 **你能测什么就反馈什么**；不能测的状态需要观测器（超纲，仅知道名词）。

```python
# 仿真中「全状态已知」的 PD 示例
theta, theta_dot = 0.1, -0.2
Kp, Kd = 10.0, 1.0
u = -(Kp * theta + Kd * theta_dot)   # 驱动角回到 0
print("u", u)
```

**练习 ⭐**：`theta>0` 且 `theta_dot>0`（远离直立且还在倒），`u` 应更负还是更正？与 §4.2 符号一致检查。

---

## 4.17 扰动与鲁棒性（定性）

```python
# 仿真中加常值扰动力矩
u_disturb = 0.05
# 在 plant 的 qdd 或 omega_dot 里 + u_disturb
```

纯 P 可能扛不住；加 I 可把均值拉回。**不要**在本节引入随机 RL 抗扰。

**练习 🔶**：质量–弹簧加 `u_disturb=0.1`，比较 `Ki=0` 与 `Ki=0.5` 稳态 `q`。

---

## 4.18 离散时间 vs 连续时间 PID

自控课公式是连续的；代码是 **每 dt 调用一次 `step`**。若实物控制周期 1 ms，则 `dt=0.001`。

| 连续 | 离散近似 |
|------|----------|
| \(\int e\,dt\) | `integral += e*dt` |
| \(\dot{e}\) | `(e-prev_e)/dt` |

当 `dt` 变小时，同一 \(K_p\) 行为会变——**调参要在目标 `dt` 下进行**。

**练习 ⭐**：同一 `Kp`，`dt=0.1` 与 `0.01` 跑 T01b 闭环，最后 `y` 是否接近？

---

## 4.19 从 PID 到 LQR（只建立期待）

| PID | LQR |
|-----|-----|
| 试错整定 \(K_p,K_i,K_d\) | 给定 \(Q,R\) 解 Riccati 得 \(K\) |
| 常只反馈部分状态 | 常 \(u=-Kx\) 全状态 |
| 实现简单 | 需可信线性模型 |

Week 5 读 `lqr.py`；寒假 MuJoCo 闭环。**本章不要求推 Riccati 方程**。

---

## 4.20 常见问答（复习用）

**Q：能只用角度 PID 稳住 cart-pole 吗？**  
A：很多入门方案可以，但全状态或 LQR 更系统；仿真里先试 PD on \(\theta,\dot{\theta}\)。

**Q：限幅会不会让系统不稳定？**  
A：饱和是非线性，可能诱发 windup；要限幅 + anti-windup。

**Q：线性化模型不准怎么办？**  
A：小角度工作、增益保守、或回到非线性仿真试凑；学习控制是更远选项。

---

## 4.21 额外渐进练习（第 5 组）

1. ⭐ 用 `matplotlib` 画 §4.6 的 `q(t)` 与 `u(t)` 双子图。  
2. ⭐ 写函数 `run_pid_sweep(Kp_list)` 返回各组末值 `q[-1]`。  
3. 🔶 对 `theta` 非线性摆（`sin`）在 `theta0=0.05` 仅用 P，说明为何线性化 PID 增益不能照搬到大角。  
4. 🔶 抄录本校自控教材框图符号与本书符号对应表（一页笔记）。

---

**上一章**：[T03](T03-常微分方程与仿真直觉.md) · **下一章**：[T05 · AI01](T05-AI01-神经网络拟合动力学.md)
