# 教程系列目录 · 两轮自平衡 / 倒立摆学习仓库

欢迎。本系列面向 **西电机器人工程大三**、Python 尚弱、在 **VS Code Remote-WSL + conda 环境 `pendulum`** 下学习的同学；目标方向是 **东南大学 085400 专硕 / 具身智能**。

**所有长文教程只在本目录**（`docs/tutorials/`）。`weeks/week01/`、`weeks/ai01_nn_dynamics/` 放练习脚本与清单；其中的 `TUTORIAL.md` 仅为**链接入口**，不重复正文。

---

## 唯一推荐阅读路径（跟读即可）

按编号顺序读 Markdown，并在对应目录跑脚本、做文末练习：

| 步 | 读 | 做（仓库根目录） |
|----|-----|------------------|
| 0 | [00 如何使用本系列](00_how_to_use.md) | 配好 conda `pendulum`，跑通 `ex01_syntax.py` |
| 1 | [01 Python 基础](01_python_basics.md) | `ex01` → `ex02` → `ex03` |
| 2 | [02 NumPy 与 Matplotlib](02_numpy_matplotlib.md) | `hello_sim.py`（改 `tau` 对比） |
| 3 | [03 ODE 直觉](03_ode_intuition.md) | `ex01_preview_rollout.py`（设 `PYTHONPATH`） |
| 4 | [04 神经网络拟合动力学](04_nn_dynamics_fit.md) | `ex02_fit_dynamics.py` 完成 TODO |

- **Week 1 结业**：完成步 0–2 + [`weeks/week01/CHECKLIST.md`](../../weeks/week01/CHECKLIST.md)。  
- **AI01 结业**（可选）：完成步 3–4 + [`weeks/ai01_nn_dynamics/CHECKLIST.md`](../../weeks/ai01_nn_dynamics/CHECKLIST.md)。  
- 步 3–4 可与步 1–2 **并行**，但建议先会 numpy 画图再碰 AI01。

**精读+练习总用时（参考）**：步 0 约 0.5 h；步 1 约 3–5 h；步 2 约 2–4 h；步 3 约 2–3 h；步 4 约 4–6 h。

---

## 每日学习安排（考研压力下偏「满负荷」）

大三上要同时扛 **考研数学 / 专业课自控** 和 **本项目**。下面按「工作日默认」设计；**具体上课空档与当周项目块**以 [`docs/checklists/`](../checklists/) 为准（如 [`2026-W42.md`](../checklists/2026-W42.md)）。

### 默认日（目标合计约 2.5–4 h，可分早晚两段）

| 块 | 时长 | 做什么 | 可检验产出 |
|----|------|--------|------------|
| **数学** | **60–90 min** | 高数/线代/概率按考研计划刷题 | 今日题号 + 1 道错题要点 |
| **自控 / 专业课** | **40–60 min** | 教材一节或真题半套；阶跃、一阶系统、根轨迹等与本项目挂钩处记一句 | 半页笔记或 3 个关键词 |
| **项目 / 本教程** | **60–90 min** | 严格按上表「推荐阅读路径」一步：读一节 MD + 跑脚本 + **必做练习至少 2 项** | 终端截图或改参记录一行 |
| **CET-6 · 单词** | **每天 20–30 min** | **课多日也要做**；不攒到周末 | 今日词表范围或 App 打卡 |

**一周节奏示例**（可按校历微调；有课表时优先用 checklist 里的时段）：

| 周一–周二 | 步 0–1（环境 + Python） |
| 周三–周四 | 步 2（numpy + `hello_sim`） |
| 周五 | 复习：重做 `clamp`、改 `tau`、口述阶跃响应 |
| 周六 | 数学加练 + 步 3（ODE / rollout） |
| 周日 | 步 4 或 AI01 TODO 一块（2 h）+ **20:30 周复盘**（当周 [`checklists`](../checklists/)） |

### _fallback 日（合计约 1–1.5 h，忙课/实验日）

仍建议 **不要三天完全零接触**，否则 conda 环境和语法手感会断：

1. **数学 30 min**（保底刷题）  
2. **自控 20 min**（只复习笔记，不新开章节）  
3. **CET-6 · 单词 20 min**（保底，不挪到周末）  
4. **项目 30–40 min**：只跑一个已学脚本 + 改一个参数 + 写一句现象（例如 `tau=1.0` 更慢）

### 执行习惯（可打勾）

- [ ] 每晚用 1 分钟写：**明天项目块对应教程第几步**  
- [ ] 项目块结束必做：**关闭 VS Code 前 commit 笔记或练习脚本到个人 fork**（本仓库作业在本地即可）  
- [ ] 连续 2 个 fallback 日后，下一个默认日把 **项目块补到 90 min**

---

## 与周清单（checklists）的关系

- 模板：[`docs/checklists/WEEKLY_TEMPLATE.md`](../checklists/WEEKLY_TEMPLATE.md)（含课表排块、**每日单词** 勾选）。  
- 当周实例：如 [`2026-W42.md`](../checklists/2026-W42.md)。  
- **周日 20:30**：用当周 checklist 复盘，并对照本节「推荐阅读路径」与 `weeks/*/CHECKLIST.md`。

---

## 仓库怎么分工（避免文件散落）

```text
weeks/week01/              # 主线练习脚本 + CHECKLIST（Week 1）
weeks/ai01_nn_dynamics/    # AI 支线脚本 + CHECKLIST
docs/tutorials/            # 中文教程全文 + answers/ 参考思路（仅此一处）
docs/checklists/           # 周学习清单（课表、CET-6 每日单词、复盘）
src/learning/              # AI01 依赖的 ODE / MLP 代码
src/inverted_pendulum/     # 倒立摆包骨架（后续周次填充）
docs/ROADMAP.md            # 阶段里程碑
```

从周次目录进来：[`weeks/week01/TUTORIAL.md`](../../weeks/week01/TUTORIAL.md) · [`weeks/ai01_nn_dynamics/TUTORIAL.md`](../../weeks/ai01_nn_dynamics/TUTORIAL.md) → 指回上表路径。

---

## 练习与答案

每节文末 **必做 ≥3、选做 1–2**。正文不贴完整作业答案：

- 核对思路：[`answers/`](answers/)  
- 代码作业：以 `weeks/` 下脚本为准（如 `ex02_fit_dynamics.py` 的 TODO）

---

## 学习心态（一句话）

**先读懂 → 改参数看现象 → 自己写一小段**；复试讲「为什么」，不是背代码。

---

## 相关文档

- 项目总览：[`README.md`](../../README.md)  
- 阶段路线图：[`docs/ROADMAP.md`](../ROADMAP.md)  
- 周学习清单：[`docs/checklists/`](../checklists/)  
- Week 1 自查：[`weeks/week01/CHECKLIST.md`](../../weeks/week01/CHECKLIST.md)  
- AI01 自查：[`weeks/ai01_nn_dynamics/CHECKLIST.md`](../../weeks/ai01_nn_dynamics/CHECKLIST.md)
