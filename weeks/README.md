# 练习代码索引（`weeks/`）

**教程**只在 [`docs/tutorials/`](../docs/tutorials/README.md)（目标与书目，无长代码）。  
**每周目录结构**：`examples/`（示例）→ `exercises/`（练习）→ `answers/`（思路核对）。  
校历打卡：[`docs/checklists/`](../docs/checklists/)（`YYYY-MM-DD.md` = 周一日期）。

```bash
# 项目根目录；已激活 venv 并 pip install -r requirements.txt
python weeks/week01/exercises/ex01_syntax.py
python weeks/week01/examples/hello_sim.py
```

`weeks/ai01/` 与 `src/ai01/`：**寒假**再练（见 [`winter-ai.md`](../docs/checklists/winter-ai.md)）。REPL 导入 `ai01` 时需 `export PYTHONPATH="$(pwd)/src"`。

---

## week01 · 大纲 Week 1

**教程**：**T00–T02**（**T01b** 选做）

| 类型 | 文件 |
|------|------|
| exercises | `ex01_syntax.py` → `ex02_functions.py` → `ex03_lists_dicts.py` |
| examples | `hello_sim.py` |
| answers | `01_python_basics.md`、`02_numpy_matplotlib.md` |

自查：[`week01/CHECKLIST.md`](week01/CHECKLIST.md)

---

## week02 · 大纲 Week 2

**教程**：**T02** 巩固 + **T03**

| 类型 | 文件 |
|------|------|
| examples | `ex01_preview_rollout.py`（简化摆 rollout） |
| exercises | 自建 `msd_ode.py` 等（见 T03） |
| answers | `03_ode_intuition.md` |

自查：[`week02/CHECKLIST.md`](week02/CHECKLIST.md)

---

## week03 · 控制预备（答案占位）

**教程**：**T04** · 思路 [`week03/answers/05_pid_state_space.md`](week03/answers/05_pid_state_space.md)  
代码主线：`src/inverted_pendulum/`

---

## ai01 · 寒假 AI 编码（本学期跳过）

**教程**：[T05](../docs/tutorials/T05-AI01-神经网络拟合动力学.md) · [`winter-ai.md`](../docs/checklists/winter-ai.md)

| 类型 | 文件 |
|------|------|
| exercises | `ex02_fit_dynamics.py` |
| answers | `demo_reference_end2end.py`、`04_nn_dynamics_fit.md` |

自查：[`ai01/CHECKLIST.md`](ai01/CHECKLIST.md)

---

倒立摆包：[`src/inverted_pendulum/`](../src/inverted_pendulum/) · MuJoCo：[`sim/mujoco/`](../sim/mujoco/README.md)
