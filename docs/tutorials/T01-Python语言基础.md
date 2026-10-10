# T01 · Python 语言基础

**章节 ID**：T01  
**预计用时**：5–8 天（每天约 1 h）  
**代码**：[`weeks/week01/exercises/`](../../weeks/week01/exercises/) · 示例无（先跑练习） · 思路 [`weeks/week01/answers/01_python_basics.md`](../../weeks/week01/answers/01_python_basics.md)

---

## 学习目标

读得懂仓库脚本、能独立写 **30–50 行** 仿真辅助代码（循环、函数、容器、简单 `class`）。

## 知识要点

| 块 | 要掌握什么 |
|----|------------|
| 运行方式 | REPL、脚本、`python weeks/...` 一律在**仓库根目录** |
| 类型与运算 | `int/float/bool`、`//` `%` `**`、比较与逻辑 |
| 流程 | `if/for/while`、`break/continue`、缩进 |
| 函数 | 参数、返回值、`def`、文档字符串 |
| 容器 | `list` / `dict` / `tuple`；遍历与切片 |
| 模块 | `import`、把常数放进 `dict` 传参（为 PID 参数字典打底） |
| 类（入门） | `class`、`__init__`、`self`；能读简单 `PID` 类（详见 **T01b**） |
| 文件与错误 | 打开文件、`try/except` 基础；常见 `IndentationError` / `NameError` |

## 推荐读物

| 资源 | 建议章节 |
|------|----------|
| [Python 官方教程（中文）](https://docs.python.org/zh-cn/3/tutorial/) | 第 1–5 章、第 9 章前半（类） |
| [Real Python — Python Basics](https://realpython.com/python-basics/) | 选读：函数、列表推导 |

## 与项目的联系

- 倒立摆状态 `(θ, θ̇)` 在代码里就是 **浮点数或 NumPy 向量**（T02）。  
- 控制器参数 `Kp, Ki, Kd` 适合放在 **字典** 里扫参（T04 / `pid.py`）。  
- MCU 上写 C，**大三上主机侧** 用 Python 做验证与画图。

## 练习与验收

1. 按顺序跑通并改参数：`ex01_syntax.py` → `ex02_functions.py` → `ex03_lists_dicts.py`。  
2. 自写：`clamp(x, lo, hi)`、用 `for` 累加列表、用 `dict` 存仿真参数。  
3. 选做：**[T01b](T01b-类与对象入门.md)** + `week01/exercises/` 中自建的 `my_pid_lab.py`。

**必做勾选**：见 [`weeks/week01/CHECKLIST.md`](../../weeks/week01/CHECKLIST.md)。

---

**上一章**：[T00](T00-导读与环境.md) · **下一章**：[T02](T02-NumPy与Matplotlib.md)
