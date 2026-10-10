# AI01 · 教程入口

神经网络拟合动力学的**完整讲解**在：

1. [`docs/tutorials/03_ode_intuition.md`](../../docs/tutorials/03_ode_intuition.md) — 摆 ODE、RK4、rollout  
2. [`docs/tutorials/04_nn_dynamics_fit.md`](../../docs/tutorials/04_nn_dynamics_fit.md) — 数据集、MLP、训练、TODO、复试叙事  

**建议顺序**：先完成或并行 Week 1 的 `hello_sim.py`，再读 03 → 跑 `ex01` → 读 04 → 做 `ex02`。

```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

python weeks/ai01_nn_dynamics/ex01_preview_rollout.py
python weeks/ai01_nn_dynamics/ex02_fit_dynamics.py
# 作业完成后对照：
python weeks/ai01_nn_dynamics/demo_reference_end2end.py
```

本目录说明与 DIY：[`README.md`](README.md) · 清单：[`CHECKLIST.md`](CHECKLIST.md)  
教程总目录：[`docs/tutorials/README.md`](../../docs/tutorials/README.md)
