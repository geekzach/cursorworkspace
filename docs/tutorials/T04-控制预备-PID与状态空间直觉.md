# T04 · 控制预备：从阶跃到 PID 与状态空间（讲义）

**章节 ID**：T04  
**预计用时**：7–10 天（Week 3–5，与建模并行）  
**前置**：T02 阶跃响应 · T03 ODE 与仿真循环  
**代码落点**：`src/inverted_pendulum/controllers/pid.py`、`model.py`、`simulation.py`

**技术路径（本仓库）**：一阶阶跃图 → 开环 ODE → **闭环 PID** → 线性化 \(A,B\) →（寒假后）LQR。可选：`python-control` 的 `tf` / `step_response` **仅作对照**，不替代自己写 ODE。

---

## 4.0 本章目标

- 能画闭环框图并用 \(e=r-y\) 语言描述平衡车  
- 能实现 **离散 PID**（带限幅与简单 anti-windup 意识）  
- 理解 \(\dot{x}\approx A\delta x + B\delta u\) 在 \(\theta=0\) 的含义  
- 能把 T02 的阶跃响应与「整定 PID」联系起来

---

## 4.1 闭环框图

```text
设定值 r ──(+)──► 控制器 ──► 被控对象 ──► 输出 y
              ▲                    │
              └── 反馈 ◄── 传感器 ──┘
```

- **误差** \(e = r - y\)（单输入单输出最简形式）  
- **平衡车**：\(r\) 常为期望倾角 0；\(y\) 来自 IMU 的 \(\theta\) 或融合状态

```python
r = 0.0
theta = 0.05   # 测量
e = r - theta
print("e =", e)
```

**练习 ⭐**：`theta=-0.03` 时，误差符号是什么？P 控制 `u=Kp*e` 希望车往哪边加速？

---

## 4.2 PID 三项物理直觉

\[
u = K_p e + K_i \int e\,dt + K_d \frac{de}{dt}
\]

| 项 | 直觉 | 倒立摆/平衡车 |
|----|------|----------------|
| P | 误差大 → 力大 | 倾角偏离直立则加力 |
| I | 消常值偏差 | 慢漂移；实物注意 windup |
| D | 抑制变化快 | 用角速度 \(\dot{\theta}\) 作 D 时常更稳 |

### 4.2.1 离散实现（仿真里真要写）

```python
class PID:
    def __init__(self, Kp, Ki, Kd, u_min=-10.0, u_max=10.0):
        self.Kp, self.Ki, self.Kd = Kp, Ki, Kd
        self.u_min, self.u_max = u_min, u_max
        self.integral = 0.0
        self.prev_e = 0.0

    def step(self, e, dt):
        self.integral += e * dt
        de_dt = (e - self.prev_e) / dt if dt > 0 else 0.0
        u = self.Kp * e + self.Ki * self.integral + self.Kd * de_dt
        u = max(self.u_min, min(self.u_max, u))
        self.prev_e = e
        return u
```

**常见错误 vs 推荐**

```python
# ❌ 只有 P，却指望消除常值扰动 —— 需 I 或前馈
# ❌ D 对噪声 e 直接差分 —— 实物要滤波或用 -Kd*theta_dot
# ✅ 仿真可先对真状态求导；实物用陀螺仪角速度
```

**练习 ⭐**：`Kp=2, Ki=0, Kd=0.5`, `e` 从 0.1 变到 0.05，手算一步 `u`（给定 `dt=0.01`）。

---

## 4.3 与一阶阶跃（T02）的关系

一阶系统 \(G(s)=K/(\tau s+1)\) 的阶跃告诉你 **「多快跟上」**。高阶/非线性系统没有单一 \(\tau\)，但 PID 试凑仍看：

1. 上升是否够快  
2. 超调是否过大  
3. 是否振荡发散  

**实验建议**：三组 \((K_p,K_i,K_d)\) + 同一初始角下的 \(\theta(t)\) 截图，写 3 句对比。

---

## 4.4 状态空间与线性化

非线性 \(\dot{x}=f(x,u)\) 在平衡点 \((x_0,u_0)\)（直立：\(\theta=0\)）：

\[
\delta\dot{x} \approx A\,\delta x + B\,\delta u
\]

```python
import numpy as np
# 数值线性化示意（概念）：A_ij ≈ ∂f_i/∂x_j |_{x0,u0}
# 具体实现将在 model.py 中用偏导或自动差分
x0 = np.zeros(4)
u0 = 0.0
```

本周只需：**状态维数、平衡点、\(A,B\) 物理意义**（A：自由演化；B：输入通道）。

**练习 ⭐**：对 2 维系统 \(x=[q,\dot{q}]\)，若 \(\dot{q}=v,\ \dot{v}=-q\)，写出 \(A\) 矩阵。

---

## 4.5 可选：`python-control` 阶跃对照

安装（见根 `requirements.txt` 注释）后：

```python
# 选做 — 与自写 ODE 对照同一传递函数
# from control import tf, step_response
# G = tf([1], [0.5, 1])
# t, y = step_response(G)
```

用于验证你对 T02 解析解的理解；**期末项目仍要以自己的 `solve_ivp` / 仿真循环为准**。

---

## 4.6 与仓库里程碑

| 周次（见 SEMESTER_PLAN） | 任务 |
|--------------------------|------|
| Week 3 | PID 框图 + `pid.py` 骨架填 `step` |
| Week 4 | `model.py` 中 \(f\) 与线性化 |
| Week 5 | `simulation.py` 闭环 + 与开环对比 |

---

## 4.7 渐进练习

### ⭐

1. 画闭环框图照片，标 \(r,y,e,u\)。  
2. 5 句话解释 P/I/D。  
3. 读 `pid.py` 骨架，列出要实现的 3 个方法名。

### 🔶

1. 对质量–弹簧加 P 控制 `u=-Kp*q`，扫 `Kp`，画 `q(t)`。  
2. 预习 `lqr.py` 文档字符串（Week 5）。  
3. 读一篇 cart-pole PID 博客，记录反馈量是全状态还是仅角度。

---

## 必做

- [ ] 框图 + P/I/D 口述。  
- [ ] 离散 PID 类或函数能在纸上跑 3 步。  
- [ ] 说明平衡点 \(\theta=0\) 对线性化的意义。

## 选做

- [ ] `python-control` 阶跃与 T02 图对比。  
- [ ] 质量–弹簧闭环仿真脚本。

---

**上一章**：[T03](T03-常微分方程与仿真直觉.md) · **下一章**：[T05 · AI01](T05-AI01-神经网络拟合动力学.md)
