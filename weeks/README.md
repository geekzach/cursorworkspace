# 练习代码索引（`weeks/`）

**教程全文**只在 [`docs/tutorials/`](../docs/tutorials/README.md)。本目录放**可运行脚本**；脚本自查用各子目录的 `CHECKLIST.md`，校历打卡在 [`docs/checklists/`](../docs/checklists/)。

```bash
# 在项目根目录；已激活 venv 并 pip install -r requirements.txt
python weeks/week01/ex01_syntax.py
```

`weeks/ai01/*.py` 会自动把 `src` 加入 `sys.path`。在 **REPL / 自写草稿** 里 `import ai01` 则需要：

```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
```

---

## week01 · 大纲 Week 1（主线）

**教程**：**[T00](../docs/tutorials/T00-导读与环境.md) · [T01](../docs/tutorials/T01-Python语言基础.md) · [T02](../docs/tutorials/T02-NumPy与Matplotlib.md)**（类加练 **[T01b](../docs/tutorials/T01b-类与对象入门.md)** 可选）

| 脚本 | 对应 |
|------|------|
| `ex01_syntax.py` → `ex02_functions.py` → `ex03_lists_dicts.py` | T01 |
| `hello_sim.py` | T02 |

```bash
python weeks/week01/ex01_syntax.py
python weeks/week01/ex02_functions.py
python weeks/week01/ex03_lists_dicts.py
python weeks/week01/hello_sim.py
```

自查：[`week01/CHECKLIST.md`](week01/CHECKLIST.md)

---

## ai01 · 可选支线（与 Week 1–2 并行）

**教程**：**[T03](../docs/tutorials/T03-常微分方程与仿真直觉.md) · [T05](../docs/tutorials/T05-AI01-神经网络拟合动力学.md)**（须 **T02**；见 [`docs/checklists/ai01-focus.md`](../docs/checklists/ai01-focus.md)）

| 顺序 | 脚本 | 说明 |
|------|------|------|
| 1 | `ex01_preview_rollout.py` | ODE rollout（T03） |
| 2 | `ex02_fit_dynamics.py` | 主作业：完成脚本内 TODO（T05） |
| 3（可选） | `demo_reference_end2end.py` | 参考答案演示 |

```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

python weeks/ai01/ex01_preview_rollout.py
python weeks/ai01/ex02_fit_dynamics.py
python weeks/ai01/demo_reference_end2end.py
```

库：`src/ai01/`（`pendulum.py`、`rollout.py`、`mlp_numpy.py`）。无图形界面时 PNG 保存在本目录。

### AI01 DIY（`ex02` 末尾任选至少一项）

1. 网络预测角加速度 `α`，再用欧拉法得 `ω⁺、θ⁺`，与直接预测状态对比。  
2. 训练数据加高斯噪声，观察验证集 MSE。  
3. 只改训练样本数 `n_samples`，画粗略 MSE–样本数曲线。

自查：[`ai01/CHECKLIST.md`](ai01/CHECKLIST.md)

---

## week02 · 大纲 Week 2（占位）

**教程**：**T02** 巩固 + **T03** ODE（见 [`week02/README.md`](week02/README.md)）。练习脚本 **待添加**；现阶段可跑 `ai01/ex01` 或按 T03 自建 `msd_ode.py`。

自查 stub：[`week02/CHECKLIST.md`](week02/CHECKLIST.md)

---

## 后续周次（规划）

| 目录 | 状态 |
|------|------|
| `week03/` … | 大三上逐步添加（见 [`CURRICULUM.md`](../docs/checklists/CURRICULUM.md)） |

倒立摆仿真包：[`src/inverted_pendulum/`](../src/inverted_pendulum/) · 寒假 MuJoCo 占位：[`sim/mujoco/`](../sim/mujoco/README.md)
