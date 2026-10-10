# 总教程 · Python + 控制 + AI（两轮自平衡 / 倒立摆）

**完整教程序列只在本目录**（`docs/tutorials/`）。  
**本周打卡**（读哪几章、每日单词、每周听力固定槽）→ [`docs/checklists/`](../checklists/)（如 [`2026-W42.md`](../checklists/2026-W42.md)）。  
**跑代码** → `weeks/week01/`、`weeks/ai01/` + `src/`；`weeks/*/TUTORIAL.md` 仅为链接入口。

---

## 读者与前提

西电机器人大三、Python 较弱、**VS Code + WSL**、可用 **conda 环境 `pendulum`**（等价步骤见 [T00 §0.3](T00-导读与环境.md#env-setup)）。目标：**东南大学 085400 专硕 / 具身智能**。

---

<a id="scope-rails"></a>

## 参考与路线说明

本仓库走 **机器人 / 经典控制友好** 的 Python + ML 路径：**先能仿真与讲清模型，再谈学习**；工具从 **NumPy 手写小网络** 起步，不第一周就上 PyTorch / 强化学习 / Agent 框架。

与外部自学的关系（建议并行阅读，不必全做完再动本仓库）：

| 资源 | 用途 |
|------|------|
| [Arjun Virk · ML Bible（from-scratch 路线）](https://www.arjunvirk.com/writing/ml-guide) | 强调 **基础数学与经典 ML → 神经网络** 的顺序；本教程 AI 部分对齐其精神：**理解再写代码**，而非先堆 trendy 工具。你可把 Virk 书中「Classical ML / NN 数学」作课外加深；**不必**在本项目里学 Transformer、Vision、Agent 章节。 |
| [Python 官方教程](https://docs.python.org/3/tutorial/) | T01 语法与模块习惯的对照 |
| [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html) | T02 数组、广播、向量化（控制里状态就是向量） |
| 教材 *Feedback Systems*（Åström & Murray，[免费在线版](https://fbsbook.org/)）或本校《自动控制原理》 | T03–T04 状态空间、反馈、PID/LQR 的体系化补充 |

**控制 + 学习的技术顺序（本仓库强制节奏）**

```text
Python / NumPy（T01–T02）
    → ODE 与仿真 rollout（T03）
    → 经典控制直觉 PID / 状态空间（T04）+ inverted_pendulum 主线
    → 监督学习最小集：划分数据、MSE、过拟合、train/val（T05 前半概念）
    → 系统辨识 / 学习动力学：MLP 拟合一步 ẋ 或 x⁺（T05 + AI01）
    → 寒假后：MuJoCo + LQR；再谈 RL 闭环（T06 / ROADMAP 阶段四，非 Week 1）
```

### 本教程覆盖 / 不覆盖

| **覆盖**（校历周清单只应指向这些） | **不覆盖**（避免学半截走错方向） |
|-----------------------------------|----------------------------------|
| Python 3、科学计算绘图、项目目录与 conda/venv | 深度学习框架（PyTorch / TensorFlow / JAX） |
| NumPy 向量/矩阵运算 **直觉**（为状态空间与 MLP 服务） | 完整考研线代课（仅教程内用到的 2–4 维状态） |
| ODE、欧拉 / RK4 / `solve_ivp`、简化摆 rollout | 把 RL 当第一周入门；T06 仅为**选读概念** |
| PID、框图、线性化与 \(A,B\) **入门** | 大模型、Transformer、RAG、Agent 工程 |
| 监督学习：**训练/验证集、MSE、过拟合、隐藏层容量** | 端到端黑盒「直接出电机指令」跳过建模 |
| AI01：**仿真生成标签 → NumPy MLP 拟合动力学**（系统 ID 思想） | MuJoCo 安装、PPO 训练实现（见 ROADMAP 寒假后） |
| 与平衡车/倒立摆相关的复试叙事挂钩 | 替代本校自控/数学课的系统学习 |

本周打卡 [`docs/checklists/`](../checklists/) 的 **「本周教程 ID」** 必须落在上表 **覆盖** 列；若本周忙，用 **T00–T02** 保底，**不要**为了「赶 AI」跳过 ODE 与经典控制主线。

---

## 推荐阅读路径（章节 ID）

| ID | 章节 | 练习代码 |
|----|------|----------|
| **T00** | [导读与环境](T00-导读与环境.md) | 根目录 `README.md` 环境段 |
| **T01** | [Python 语言基础](T01-Python语言基础.md) | `weeks/week01/ex01`–`ex03` |
| **T02** | [NumPy 与 Matplotlib](T02-NumPy与Matplotlib.md) | `weeks/week01/hello_sim.py` |
| **T03** | [常微分方程与仿真直觉](T03-常微分方程与仿真直觉.md) | `weeks/ai01/ex01_preview_rollout.py` |
| **T04** | [控制预备：PID 与状态空间直觉](T04-控制预备-PID与状态空间直觉.md) | `src/inverted_pendulum/`（逐步实现） |
| **T05** | [AI01：神经网络拟合动力学](T05-AI01-神经网络拟合动力学.md) | `weeks/ai01/ex02_fit_dynamics.py` |
| **T06** | [选读：强化学习与 MuJoCo](T06-选读-强化学习与MuJoCo.md) | `sim/mujoco/`（寒假） |

- **Week 1 结业**：**T00–T02** + [`weeks/week01/CHECKLIST.md`](../../weeks/week01/CHECKLIST.md)（脚本自查，不重复教程正文）。  
- **AI01 结业**（可选）：在 **T02 熟练、T03 rollout 已跑通** 后做 **T05**；禁止「Week 1 只追 RL/大模型」。清单见 [`weeks/ai01/CHECKLIST.md`](../../weeks/ai01/CHECKLIST.md)。  
- **经典控制主线（后续周次）**：**T03 → T04**，配合 `src/inverted_pendulum/`；**T06** 仅在寒假前/复试准备作概念浏览。

**精读+练习参考用时**：T00 约 0.5 h；T01 3–5 h；T02 2–4 h；T03 2–3 h；T05 4–6 h；T04/T06 按周次穿插。

---

## 与校历周清单的关系

| 你想… | 打开 |
|--------|------|
| 学完整教程 | 本目录 T00 起按 ID 读 |
| 本周读哪几章（如 **T00–T02**） | 当周 [`docs/checklists/YYYY-Www.md`](../checklists/) 顶部「本周教程」行 |
| 大纲周次 ↔ 章节 ID 对照 | [`docs/checklists/CURRICULUM.md`](../checklists/CURRICULUM.md) |
| 课表、**CET-6 每日单词**、**每周听力固定槽**、周日复盘 | 同上 ISO 周文件或 [`WEEKLY_TEMPLATE.md`](../checklists/WEEKLY_TEMPLATE.md) |

**CET-6**：**单词** 每天 **20–30 min**（每日打卡）；**听力** 每周 **2–3 个固定槽**（与单词分开，写在当周文件顶部）。

---

## 仓库分工

完整目录树见根目录 [`README.md` §仓库结构](../../README.md#repo-tree)。本教程对应练习入口：[`weeks/week01/TUTORIAL.md`](../../weeks/week01/TUTORIAL.md) · [`weeks/ai01/TUTORIAL.md`](../../weeks/ai01/TUTORIAL.md)

---

## 练习与答案

每章 **必做 / 选做** 在正文末尾。完整作业代码以 `weeks/` 为准；思路核对见 [`answers/`](answers/)（标注对应 **T** 章节）。

---

## 相关文档

- [`README.md`](../../README.md) · [`docs/ROADMAP.md`](../ROADMAP.md) · [`docs/checklists/`](../checklists/)
