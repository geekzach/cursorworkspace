# 两轮自平衡小车 · 学习项目（复试准备）

面向准备 **东南大学 085400 电子信息（专硕）** 复试的本科同学（机器人 / 自动化背景）：以 **两轮自平衡小车** 为最终目标 — **先在 MuJoCo 中仿真，再制作实物** — 分阶段掌握 Python、建模、经典与现代控制，并可选衔接 **具身智能** 方向的学习控制实验。

**当前阶段仍从「倒立摆（cart-pole）」入手**：倒立摆是平衡车在数学上的经典等效模型（轮轴支点、小角度近似等），便于在大三上打好 **拉格朗日建模、线性化、PID** 基础，再平滑过渡到仿真小车与硬件。

## 一眼看懂（三件事）

| | 打开什么 | 说明 |
|---|----------|------|
| **学教程** | [`docs/tutorials/`](docs/tutorials/README.md) | 中文长文 **T00–T06**（只在这里读全文） |
| **周打卡** | [`docs/checklists/`](docs/checklists/) | 校历周：本周 **T 章节 ID**、课表、**CET-6 每日单词**、复盘 |
| **代码练习** | [`weeks/`](weeks/week01/) | 可运行脚本；`TUTORIAL.md` / `CHECKLIST.md` 链回教程，不重复正文 |

路线图 [`docs/ROADMAP.md`](docs/ROADMAP.md) · 思路核对 [`docs/tutorials/answers/`](docs/tutorials/answers/) · **周日 20:30** 用当周 `YYYY-Www.md` 复盘。

> **当前进度**：**Week 1**（`weeks/week01/`）。**可选 AI01**（`weeks/ai01/` + `src/ai01/`，ROADMAP **M1.6**）。  
> 倒立摆完整闭环、MuJoCo、LQR 实物、强化学习 **尚未实现**；`src/inverted_pendulum/` 为骨架，`sim/mujoco/` 为寒假占位。

---

## 项目目标（升级后）

| 维度 | 说明 |
|------|------|
| **最终系统** | 两轮自平衡小车：MuJoCo 仿真 → ESP32/STM32 实物（IMU + 编码器电机） |
| **复试展示** | 能讲清：建模 → PID → LQR → 仿真 → 实物对比 →（可选）学习控制 |
| **工程习惯** | 先仿真后硬件；MCU 实时控制（&lt;1 ms 级）、主机负责仿真/调参/学习 |
| **当前落地** | 完成 Week 1 练习；按周次推进倒立摆 Python 仿真（见下表） |

更完整的分阶段里程碑、复试 PPT 结构与暂定硬件 BOM 见 **[`docs/ROADMAP.md`](docs/ROADMAP.md)**。

---

## 学习路线概览（按学期）

| 时间 | 阶段 | 重点 | 本仓库 |
|------|------|------|--------|
| **大三上**（2026.10 — 2027.01） | 倒立摆基础 + **可选 AI01** | Python、拉格朗日建模、线性化、PID；理解「摆 ≈ 平衡车模型」；**并行**可做 NN 拟合简化动力学 | `weeks/week01/` 起，填充 `src/inverted_pendulum/`；AI 见 `weeks/ai01/` + `src/ai01/` |
| **寒假**（2027.01 — 2027.02） | MuJoCo 仿真 | MJCF 两轮平衡车、**LQR** 平衡控制 | 计划使用 [`sim/mujoco/`](sim/mujoco/)（占位）；**暂不**在 `requirements.txt` 加入 mujoco |
| **大三下**（2027.03 — 2027.06） | 实物硬件 | ESP32/STM32（**C**）、IMU + 电机，移植 PID/LQR，仿真 vs 实物 | 文档与笔记为主；代码可另建 `firmware/` 等（后续） |
| **2027 暑假前** | 学习控制 | MuJoCo 中简单 **RL** 平衡实验，与 LQR 对比，衔接具身智能 | 文档规划见 ROADMAP；实现放在寒假/下学期之后 |

### 大三上 · 周次安排（与倒立摆脚手架对齐）

| 周次 | 主题 | 本仓库内容 |
|------|------|------------|
| **Week 1** | Python 语法、函数、列表/字典；一阶阶跃响应预览 | [`weeks/week01/`](weeks/week01/) |
| **AI01**（可选，与 Week 1–2 并行） | ODE rollout → 小型 MLP 拟合一步动力学 | [`weeks/ai01/`](weeks/ai01/) |
| Week 2 | numpy、向量、简单 ODE 数值解 | （待添加） |
| Week 3 | 传递函数、框图、PID 概念与整定入门 | 骨架 → `controllers/pid.py` |
| Week 4 | 状态空间、线性化倒立摆模型 | 骨架 → `model.py` |
| Week 5 | LQR 设计、闭环仿真（Python） | `controllers/lqr.py`、`simulation.py` |
| Week 6+ | 观测器、动画、参数扫掠、整理推导笔记 | `plotting.py`、文档与图表 |

每周目录计划包含：练习脚本、中文注释、`CHECKLIST.md` 自查清单。

---

## 技术栈

- **语言**：Python 3.10+（大三上仿真）；实物阶段 MCU 使用 **C**
- **数值与科学计算**：`numpy`、`scipy`
- **绘图**：`matplotlib`
- **后续（约 Week 3–5）**：`python-control`（传递函数、状态空间、LQR 设计）
- **寒假起（主机）**：MuJoCo（安装与版本见 `docs/ROADMAP.md`，**尚未**列入 `requirements.txt`）

依赖版本见 [`requirements.txt`](requirements.txt)。

---

## 环境配置（SETUP）

在项目**根目录**执行：

```bash
# 1. 创建虚拟环境（推荐）
python3 -m venv .venv

# 2. 激活虚拟环境
# Linux / macOS:
source .venv/bin/activate
# Windows (PowerShell):
# .venv\Scripts\Activate.ps1

# 3. 安装依赖
pip install -U pip
pip install -r requirements.txt

# 4. 验证（可选）
python -c "import numpy, scipy, matplotlib; print('OK')"
```

无需把本仓库安装成包即可运行 Week 1 脚本；后续若使用 `import inverted_pendulum`，可在根目录设置：

```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
```

（Windows 下可用 `set PYTHONPATH=...` 或在 IDE 中将 `src` 标记为源码根目录。）

---

## Week 1：如何运行练习

在已激活虚拟环境、已 `pip install -r requirements.txt` 的前提下：

```bash
# 基础语法
python weeks/week01/ex01_syntax.py
python weeks/week01/ex02_functions.py
python weeks/week01/ex03_lists_dicts.py

# 控制直觉预习：一阶系统阶跃响应曲线
python weeks/week01/hello_sim.py
```

完成度对照：[`weeks/week01/CHECKLIST.md`](weeks/week01/CHECKLIST.md)。

---

## AI01（可选）：神经网络拟合动力学

与经典 PID / 建模 **并列** 的轻量支线（numpy only，无 MuJoCo / RL）。适合大三上想提前接触「控制 + 学习」、复试讲故事。

```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

python weeks/ai01/ex01_preview_rollout.py
python weeks/ai01/ex02_fit_dynamics.py   # 主作业：完成脚本内 TODO
python weeks/ai01/demo_reference_end2end.py  # 参考答案演示
```

教程与运行：[`weeks/ai01/TUTORIAL.md`](weeks/ai01/TUTORIAL.md) · 清单：[`CHECKLIST.md`](weeks/ai01/CHECKLIST.md)。

---

<a id="repo-tree"></a>

## 仓库结构

```text
.
├── README.md                 # 本文件
├── docs/
│   ├── ROADMAP.md            # 分阶段路线图、复试 PPT、暂定 BOM
│   ├── checklists/           # 周学习清单（模板 + 当周实例；课表与每日单词）
│   └── tutorials/            # 中文教程全文（唯一位置；含 answers/）
├── requirements.txt          # Python 依赖（固定版本）
├── sim/
│   └── mujoco/               # 寒假 MuJoCo 占位（见目录内 README）
├── weeks/
│   ├── week01/               # 主线 Week 1 练习（长文教程在 docs/tutorials/）
│   │   ├── TUTORIAL.md       # 薄链接入口
│   │   ├── CHECKLIST.md
│   │   └── ex*.py, hello_sim.py
│   └── ai01/                 # 可选 AI01（教程 T03 + T05）
│       ├── TUTORIAL.md       # 运行命令 + DIY（无单独 README）
│       ├── CHECKLIST.md
│       └── ex*.py, demo_reference_end2end.py
└── src/
    ├── ai01/                 # AI01 库：摆 ODE、rollout、NumPy MLP
    └── inverted_pendulum/    # 倒立摆仿真包骨架（大三上逐步实现）
        ├── model.py
        ├── simulation.py
        ├── plotting.py
        └── controllers/
            ├── pid.py
            └── lqr.py
```

---

## 许可与说明

本项目为**学习用途**的教学脚手架；物理参数与控制器参数在后续周次会给出推荐取值与参考文献（如经典 cart-pole 方程、平衡车简化模型、MuJoCo / `python-control` 文档）。

祝复试顺利。
