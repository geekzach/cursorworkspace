# 总教程 · Python + 控制 + ML 阅读（两轮自平衡 / 倒立摆）

**本目录 = 学习目标、知识要点、参考书目、项目挂钩提示**（不贴长教学代码）。  
**跑代码** → [`weeks/README.md`](../../weeks/README.md)（每周：`examples/` → `exercises/` → `answers/`）。  
**本周打卡** → [`docs/checklists/`](../checklists/)（文件名 **`YYYY-MM-DD.md`** = 该周周一）。

---

## 读者与前提

西电机器人大三、Python 较弱、**VS Code + WSL**、conda/venv 均可。目标：**东南 085400 / 具身智能** 复试叙事。

---

<a id="scope-rails"></a>

## 覆盖 / 不覆盖（本学期）

| **覆盖** | **不覆盖（寒假或更晚）** |
|----------|---------------------------|
| Python、NumPy、ODE、PID/状态空间入门 | PyTorch / JAX 主线 |
| `src/inverted_pendulum/` 经典主线 | 本学期 **AI 训练代码**（见 T05 只读书） |
| 李航《统计学习方法》按周阅读 | RL 实现、MuJoCo 安装（寒假） |
| T06 概念选读 | Transformer、Agent 工程 |

---

## 章节 ID

| ID | 章节 | 代码 |
|----|------|------|
| **T00** | [导读与环境](T00-导读与环境.md) | `week01/exercises/ex01` |
| **T01** | [Python 语言基础](T01-Python语言基础.md) | `week01/exercises/` |
| **T01b** | [类与对象入门](T01b-类与对象入门.md)（选做） | 自建 `my_pid_lab.py` |
| **T02** | [NumPy 与 Matplotlib](T02-NumPy与Matplotlib.md) | `week01/examples/hello_sim.py` |
| **T03** | [常微分方程与仿真直觉](T03-常微分方程与仿真直觉.md) | `week02/` |
| **T04** | [控制预备：PID 与状态空间](T04-控制预备-PID与状态空间直觉.md) | `src/inverted_pendulum/` |
| **T05** | [ML 阅读 + 寒假 AI01](T05-AI01-神经网络拟合动力学.md) | 本学期无；寒假 `weeks/ai01/` |
| **T06** | [选读：RL 与 MuJoCo](T06-选读-强化学习与MuJoCo.md) | `sim/mujoco/` |

校历与 **张宇 / 自控 / 李航** 每周范围：[`SEMESTER_PLAN.md`](../checklists/SEMESTER_PLAN.md) · 大纲对照 [`CURRICULUM.md`](../checklists/CURRICULUM.md)。

---

## 练习答案

思路核对在 **`weeks/<week>/answers/`**，不再在教程内嵌答案。  
原 `docs/tutorials/answers/` 仅保留 [索引](answers/README.md) 指向各周目录。

---

## 相关文档

[`README.md`](../../README.md) · [`ROADMAP.md`](../ROADMAP.md) · [`winter-ai.md`](../checklists/winter-ai.md)
