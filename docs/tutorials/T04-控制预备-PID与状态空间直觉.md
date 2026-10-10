# T04 · 控制预备：PID 与状态空间直觉

**章节 ID**：T04  
**预计用时**：7–10 天（跨多周，见 [`SEMESTER_PLAN.md`](../checklists/SEMESTER_PLAN.md)）  
**代码**：[`src/inverted_pendulum/`](../../src/inverted_pendulum/)（`model.py`、`controllers/pid.py`、`simulation.py`）  
**思路**：[`weeks/week03/answers/05_pid_state_space.md`](../../weeks/week03/answers/05_pid_state_space.md)

---

## 学习目标

能画 **负反馈框图**、写 PID 离散更新、理解 **平衡点线性化** \(\dot{x} \approx A x + B u\)；能读 LQR 在干什么（寒假深化）。

## 知识要点

| 块 | 要点 |
|----|------|
| 反馈 | 设定值、误差、饱和与抗积分饱和（概念） |
| PID | P/I/D 物理意义；与二阶系统阶跃指标联系 |
| 状态空间 | \(x, u, y\)；能控/能观 **口头定义** |
| 线性化 | 在 \(\theta \approx 0\) 展开；\(A,B\) 与代码注释一一对应 |
| 仿真闭环 | 传感器 → PID → 力矩 → plant → 状态反馈 |
| LQR（预习） | 代价 \(x^T Q x + u^T R u\)；全状态反馈 vs 输出反馈 |

## 推荐读物

| 资源 | 范围 |
|------|------|
| *Feedback Systems* | Ch 7 PID、Ch 8 状态反馈（选节） |
| 胡寿松《自动控制原理》 | 时域 + 根轨迹 + 状态空间（跟课，以 SEMESTER_PLAN 复习范围为准） |
| `python-control` 文档 | **选做**：`tf`、`step_response` 对照直觉 |

## 与项目的联系

- **M1.4–M1.5**：至少一张 PID 闭环角度曲线 + 「倒立摆 ≈ 轮轴支点平衡车」示意图。  
- `lqr.py` 与寒假 MuJoCo 共用同一状态定义习惯。

## 练习与验收

按周在 [`SEMESTER_PLAN.md`](../checklists/SEMESTER_PLAN.md) 推进 `model.py` → `pid.py` → `simulation.py`；每周复盘能 **指代码行** 对应公式。

---

**上一章**：[T03](T03-常微分方程与仿真直觉.md) · **下一章**：[T05](T05-AI01-神经网络拟合动力学.md)（寒假编码）· **选读**：[T06](T06-选读-强化学习与MuJoCo.md)
