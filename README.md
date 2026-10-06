# 倒立摆 / 小车摆控制仿真（复试准备）

面向准备**东南大学（SEU）控制相关方向研究生复试**的本科同学：用 Python 从零搭建**倒立摆（cart-pole）控制仿真**，逐步掌握 **PID → 状态空间与 LQR → 观测器** 等经典内容，最终在面试中能清晰讲解模型、控制器设计与仿真结果。

> **当前进度**：**Week 1 — Python 基础与环境搭建**。  
> 高级控制（真实倒立摆动力学、PID/LQR 闭环、动画演示）**尚未实现**，仅保留 `src/inverted_pendulum/` 下的包骨架供后续周次填充。

---

## 项目目标

| 阶段 | 目标 |
|------|------|
| 复试展示 | 可运行的仿真：平衡倒立摆、对比不同控制策略、能画状态曲线 |
| 知识串联 | 经典控制（PID）与现代控制（LQR、全状态反馈）与「能写进 PPT 的推导」 |
| 工程能力 | Python + numpy/scipy/matplotlib，代码可读、可复现 |

---

## 技术栈

- **语言**：Python 3.10+
- **数值与科学计算**：`numpy`、`scipy`
- **绘图**：`matplotlib`
- **后续（约 Week 3–4）**：`python-control`（传递函数、状态空间、LQR 设计）

依赖版本见 [`requirements.txt`](requirements.txt)。

---

## 学习路径概览（建议 6–8 周）

| 周次 | 主题 | 本仓库内容 |
|------|------|------------|
| **Week 1** | Python 语法、函数、列表/字典；一阶阶跃响应预览 | [`weeks/week01/`](weeks/week01/) |
| Week 2 | numpy、向量、简单 ODE 数值解 | （待添加） |
| Week 3 | 传递函数、框图、PID 概念与整定入门 | 骨架 → `controllers/pid.py` |
| Week 4 | 状态空间、线性化倒立摆模型 | 骨架 → `model.py` |
| Week 5 | LQR 设计、闭环仿真 | `controllers/lqr.py`、`simulation.py` |
| Week 6 | 观测器 / 输出反馈、噪声与鲁棒性讨论 | 扩展模块 |
| Week 7–8 | 动画、参数扫掠、复试答辩材料整理 | `plotting.py`、文档与图表 |

每周目录计划包含：练习脚本、中文注释、`CHECKLIST.md` 自查清单。

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

## 仓库结构

```text
.
├── README.md                 # 本文件
├── requirements.txt        # Python 依赖（固定版本）
├── weeks/
│   └── week01/               # 第一周教材与练习
│       ├── CHECKLIST.md
│       ├── ex01_syntax.py
│       ├── ex02_functions.py
│       ├── ex03_lists_dicts.py
│       └── hello_sim.py
└── src/
    └── inverted_pendulum/    # 仿真包骨架（后续实现）
        ├── model.py
        ├── simulation.py
        ├── plotting.py
        └── controllers/
            ├── pid.py
            └── lqr.py
```

---

## 许可与说明

本项目为**学习用途**的教学脚手架；物理参数与控制器参数在后续周次会给出推荐取值与参考文献（如经典 cart-pole 方程、MATLAB/`python-control` 文档）。

祝复试顺利。
