# 代码区（自学产出放这里）

在**仓库根目录**运行脚本，路径以 `code/...` 开头。

## 目录

| 路径 | 用途 |
|------|------|
| `week01/exercises/` | Python 入门练习（`ex01`–`ex03`） |
| `week01/examples/` | 环境检查示例 `hello_sim.py` |
| `week02/examples/` | ODE + RK4 预习 `ex01_preview_rollout.py` |
| `week02/` | 自建 `msd_ode.py` 等（按 [T03](../guides/T03-常微分方程与仿真直觉.md)） |
| `inverted_pendulum/` | 倒立摆包骨架（`model` / `simulation` / `controllers` / `plotting`），由你逐步实现 |

面试用响应图可放入 [`docs/figures/`](../docs/figures/)。

## 环境（Windows + conda）

```powershell
conda activate <你的环境名>
pip install -U pip && pip install -r requirements.txt
$env:PYTHONPATH = "$PWD\code"
python code/week01/exercises/ex01_syntax.py
```

## 环境（Linux / venv）

```bash
source .venv/bin/activate
pip install -U pip && pip install -r requirements.txt
export PYTHONPATH="${PYTHONPATH}:$(pwd)/code"
python code/week01/exercises/ex01_syntax.py
```
