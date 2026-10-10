# 大纲周次 ↔ 教程章节 ID

校历每周具体打卡见 `YYYY-Www.md`；**学期周次与里程碑**见 [`SEMESTER_PLAN.md`](SEMESTER_PLAN.md)。此处只说明 **建议读哪些 T 章节**（全文在 `docs/tutorials/`）。  
**覆盖 / 不覆盖** 边界见 [`docs/tutorials/README.md`](../tutorials/README.md#scope-rails) 中「本教程覆盖 / 不覆盖」。

| 大纲周次 | 本周教程 ID | 主要脚本 / 代码 |
|----------|-------------|-----------------|
| Week 1 | **T00–T02**（**T01b** 类/PID 加练，选做） | `weeks/week01/` |
| Week 2 | **T02–T03** | `weeks/ai01/ex01_preview_rollout.py`（`week02/` 尚未建） |
| Week 3 | **T04**（§4.1–4.4） | `controllers/pid.py` |
| Week 4 | **T03–T04** | `model.py` |
| Week 5 | **T04** + ROADMAP LQR | `lqr.py`、`simulation.py` |
| **AI01**（可选） | **T03 → T05**（须 **T02** 打底） | `weeks/ai01/` |
| 寒假及以后 | **T06**（选读）+ ROADMAP 阶段二–四 | `sim/mujoco/`；RL **实现** 在阶段四 |

**AI01 最低前置**：能读 NumPy 形状、跑通 rollout、理解 train/val 与过拟合（T05 §5.2）— 与 [ML 基础路线](https://www.arjunvirk.com/writing/ml-guide) 的「先 classical / NN 数学，再工程堆栈」一致。
