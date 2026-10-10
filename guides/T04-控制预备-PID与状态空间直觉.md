# T04 · 控制预备：PID 与状态空间直觉

**预计**：跨多周（见 [`plan/SEMESTER_PLAN.md`](../plan/SEMESTER_PLAN.md)） · **代码**：`code/inverted_pendulum/`

## 学什么

负反馈框图；离散 PID；平衡点线性化 \(\dot{x} \approx A x + B u\)；闭环仿真习惯；LQR 代价函数 **预习**（寒假深化）。

## 推荐资源

| 资源 | 范围 |
|------|------|
| [Feedback Systems](https://fbsbook.org/) | Ch 7 PID、Ch 8 状态反馈（选节） |
| 胡寿松《自动控制原理》 | 跟课 + 按 SEMESTER_PLAN「自控」列复习 |
| [python-control](https://python-control.readthedocs.io/) | 选做：`step_response` 对照直觉 |

## 与项目

按周推进 `model.py` → `controllers/pid.py` → `simulation.py`；12 月中旬前至少一张 PID 闭环角度曲线。

**验收**：复盘能指代码注释对应公式；能口头说明「倒立摆 ≈ 平衡车等效模型」。
