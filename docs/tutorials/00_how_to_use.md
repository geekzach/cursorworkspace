# 00 · 如何使用本教程系列

## 为什么学这个

你最终要做的是 **两轮自平衡小车**：仿真里站稳、实物里用 IMU + 电机闭环。大三上从 **倒立摆（cart-pole）** 入手，是因为数学结构和平衡车在小角度下很像——复试老师常问「摆和车怎么对应」。本系列不代替课堂，而是把 **本仓库里已经写好的脚本** 串成一条能跟走的路：环境 → Python → 画图 → ODE →（可选）用神经网络拟合动力学。

---

## 本系列长什么样

- **语言**：全文中文；代码与仓库一致，以 **Python 3.10+** 为准。
- **风格**：像耐心的同学 + 严谨的助教——公式只写到「能写代码、能答辩」的深度。
- **每节固定板块**：
  - 为什么学这个
  - 概念 + 小例子（含预期输出或图该长什么样）
  - 常见踩坑
  - 本节练习（必做 ≥3，选做 1–2）
- **答案**：见 [`answers/`](answers/)，正文只给思路提示。

---

## 你的环境：WSL + VS Code + conda `pendulum`

### 1. 克隆与打开

```bash
# 示例路径，按你本机改
cd ~/projects
git clone https://github.com/geekzach/cursorworkspace.git
cd cursorworkspace
```

在 VS Code 里用 **Remote - WSL** 打开该文件夹，终端提示符前一般有 `(pendulum)` 或你激活的环境名。

### 2. Conda 环境（推荐与课程一致）

```bash
conda create -n pendulum python=3.11 -y
conda activate pendulum
pip install -U pip
pip install -r requirements.txt
python -c "import numpy, scipy, matplotlib; print('OK')"
```

若你用 `venv` 而非 conda，见根目录 [`README.md`](../../README.md) 的 SETUP 小节，效果相同。

### 3. 工作目录永远是「项目根」

运行脚本时当前目录应为仓库根（能看到 `weeks/`、`src/`、`requirements.txt`）：

```bash
python weeks/week01/ex01_syntax.py
```

**踩坑**：在 `weeks/week01/` 里执行 `python ex01_syntax.py` 有时也能跑，但后续 AI01 依赖根目录相对路径，请养成 **总在根目录运行** 的习惯。

### 4. PYTHONPATH（AI01 与 `src/learning` 必知）

Week 1 脚本不强制要求；从 AI01 起需要能 `import learning`：

```bash
# Linux / WSL（每次新开终端要再执行，或写入 ~/.bashrc）
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
```

**VS Code 做法**：`.vscode/settings.json` 里可为该工作区设置 `terminal.integrated.env.linux` 的 `PYTHONPATH`，或把 `src` 标为「源码根」。AI01 脚本里已有一段 `sys.path.insert`，**未设 PYTHONPATH 时多数情况仍能跑**——但面试/大作业里建议显式理解路径。

### 5. 图形界面

- WSL2 + Windows 11 常已支持 WSLg，运行 `hello_sim.py` 可能弹出图窗。
- 无显示时脚本会 **自动保存 PNG** 到脚本同目录（如 `week01_step_response.png`），属正常现象。

---

## 怎么「读」一节教程

1. **先扫标题**，知道本节要服务哪几个 `.py` 文件。
2. **打开对应脚本**，教程里的行号/函数名与仓库对照看。
3. **做必做练习**——改参数、加打印、自己写 5–15 行，比复制粘贴多十倍。
4. **打勾** [`weeks/week01/CHECKLIST.md`](../../weeks/week01/CHECKLIST.md) 或 AI01 清单。

---

## 提交与自查（心理清单）

本仓库作业以 **本地运行 + 笔记** 为主，无自动批改。交作业/写学习日志前可自问：

| 检查项 | 是/否 |
|--------|--------|
| 能在根目录一条命令跑通对应脚本，无 `ModuleNotFoundError` | |
| 改过至少一个参数并**用文字**记录现象（如 τ 变大响应变慢） | |
| 能脱离代码用 30 秒口述本节核心概念 | |
| 练习里标「自己写」的段落确实出自你的手（可丑，但要能跑） | |
| AI01：TODO 已完成，图保存成功，验证 MSE 比训练前明显下降 | |

---

## 与 C 语言、OOP 的关系

- 你学过 C 到指针：**变量是名字、函数像子程序、数组连续存**——Python 里 `list` 更像「可变的堆上数组」，没有指针算术，但 **「传的是引用」** 在改 list/dict 时要注意（见 01 节）。
- **OOP 本系列不先讲**：`class MLP` 在 AI01 里会出现，教程 04 只要求 **会调用、会改超参**；寒假 MCU 阶段再用 C 写控制环。

---

## 仓库地图（你现在该关心什么）

```text
weeks/week01/          # 现在：语法、函数、列表、阶跃响应
weeks/ai01_nn_dynamics/  # 可选：ODE 数据 + MLP 拟合
src/learning/          # AI01 用的摆模型、rollout、numpy MLP
src/inverted_pendulum/ # 骨架：Week 4+ 再填动力学与 PID/LQR
docs/tutorials/        # 你正在读的系列
```

---

## 常见踩坑

| 现象 | 可能原因 | 处理 |
|------|----------|------|
| `python: command not found` | 未激活 conda / 未选解释器 | VS Code 右下角选 `pendulum` 的 Python |
| `No module named 'numpy'` | 依赖未装在当前环境 | `pip install -r requirements.txt` |
| `No module named 'learning'` | 未设 PYTHONPATH 且未从 AI01 脚本运行 | 根目录 + `export PYTHONPATH=...` |
| 图不弹出 | 无 DISPLAY | 看终端「已保存 xxx.png」 |
| 中文乱码（少见） | 终端编码 | 优先看保存的 PNG；源码已是 UTF-8 |

---

## 本节练习

### 必做

1. 按上文创建/激活 `pendulum`，运行 `python weeks/week01/ex01_syntax.py`，把终端 **最后两行** 抄进你的笔记。
2. 在根目录执行 `python -c "import os; print(os.getcwd())"`，确认路径是仓库根。
3. 阅读 [`docs/ROADMAP.md`](../ROADMAP.md) 的「阶段一」表格，用三句话写：本项目 **寒假前** 要达成什么、**暂不** 做什么。

### 选做

1. 为仓库写一段一行 `alias` 或 shell 函数：`pendulum_cd` = `cd 仓库根 && conda activate pendulum && export PYTHONPATH=...`。
2. 在 VS Code 里安装 Python 扩展，对 `hello_sim.py` 试一次「在终端中运行 Python 文件」，确认解释器是 conda `pendulum`。

---

**下一节**：[01 Python 基础（控制向）](01_python_basics.md)
