# 总教程 · Python + 控制 + AI（两轮自平衡 / 倒立摆）

**完整教程序列只在本目录**（`docs/tutorials/`）。  
**本周读哪几章、每天 CET-6 单词块** → [`docs/checklists/`](../checklists/)（如 [`2026-W42.md`](../checklists/2026-W42.md)）。  
**可运行练习** → `weeks/week01/`、`weeks/ai01_nn_dynamics/`；`weeks/*/TUTORIAL.md` 仅为链接入口。

---

## 读者与前提

西电机器人大三、Python 较弱、**VS Code + WSL**、可用 **conda 环境 `pendulum`**（等价步骤见 [T00 §0.3](T00-导读与环境.md#env-setup)）。目标：**东南大学 085400 专硕 / 具身智能**。

---

## 推荐阅读路径（章节 ID）

| ID | 章节 | 练习代码 |
|----|------|----------|
| **T00** | [导读与环境](T00-导读与环境.md) | 根目录 `README.md` 环境段 |
| **T01** | [Python 语言基础](T01-Python语言基础.md) | `weeks/week01/ex01`–`ex03` |
| **T02** | [NumPy 与 Matplotlib](T02-NumPy与Matplotlib.md) | `weeks/week01/hello_sim.py` |
| **T03** | [常微分方程与仿真直觉](T03-常微分方程与仿真直觉.md) | `weeks/ai01_nn_dynamics/ex01_preview_rollout.py` |
| **T04** | [控制预备：PID 与状态空间直觉](T04-控制预备-PID与状态空间直觉.md) | `src/inverted_pendulum/`（逐步实现） |
| **T05** | [AI01：神经网络拟合动力学](T05-AI01-神经网络拟合动力学.md) | `weeks/ai01_nn_dynamics/ex02_fit_dynamics.py` |
| **T06** | [选读：强化学习与 MuJoCo](T06-选读-强化学习与MuJoCo.md) | `sim/mujoco/`（寒假） |

- **Week 1 结业**：**T00–T02** + [`weeks/week01/CHECKLIST.md`](../../weeks/week01/CHECKLIST.md)（脚本自查，不重复教程正文）。  
- **AI01 结业**（可选）：**T03 + T05**（T02 打底）+ [`weeks/ai01_nn_dynamics/CHECKLIST.md`](../../weeks/ai01_nn_dynamics/CHECKLIST.md)。  
- **经典控制主线（后续周次）**：**T03 → T04**，配合 `src/inverted_pendulum/`。

**精读+练习参考用时**：T00 约 0.5 h；T01 3–5 h；T02 2–4 h；T03 2–3 h；T05 4–6 h；T04/T06 按周次穿插。

---

## 与校历周清单的关系

| 你想… | 打开 |
|--------|------|
| 学完整教程 | 本目录 T00 起按 ID 读 |
| 本周读哪几章（如 **T00–T02**） | 当周 [`docs/checklists/YYYY-Www.md`](../checklists/) 顶部「本周教程」行 |
| 大纲周次 ↔ 章节 ID 对照 | [`docs/checklists/CURRICULUM.md`](../checklists/CURRICULUM.md) |
| 课表、**CET-6 每日单词**、周日复盘 | 同上 ISO 周文件或 [`WEEKLY_TEMPLATE.md`](../checklists/WEEKLY_TEMPLATE.md) |

**CET-6 · 单词**：每天 **20–30 min**，课多日也不攒到周末（模板与各周清单已留打卡位）。

---

## 仓库分工

```text
docs/tutorials/            # 总教程 T00–T06 + answers/ 参考思路
docs/checklists/           # 校历周清单（教程只链接，不嵌正文）
weeks/week01/              # Week 1 脚本 + 薄 CHECKLIST
weeks/ai01_nn_dynamics/    # AI01 脚本 + 薄 CHECKLIST
src/learning/              # AI01：摆 ODE、rollout、NumPy MLP
src/inverted_pendulum/     # 倒立摆包骨架
docs/ROADMAP.md            # 阶段里程碑
```

入口：[`weeks/week01/TUTORIAL.md`](../../weeks/week01/TUTORIAL.md) · [`weeks/ai01_nn_dynamics/TUTORIAL.md`](../../weeks/ai01_nn_dynamics/TUTORIAL.md)

---

## 练习与答案

每章 **必做 / 选做** 在正文末尾。完整作业代码以 `weeks/` 为准；思路核对见 [`answers/`](answers/)（标注对应 **T** 章节）。

---

## 相关文档

- [`README.md`](../../README.md) · [`docs/ROADMAP.md`](../ROADMAP.md) · [`docs/checklists/`](../checklists/)
