# T04 · 控制预备：PID 与状态空间直觉

**预计**：跨多周（见 [`plan/SEMESTER_PLAN.md`](../plan/SEMESTER_PLAN.md)） · **代码**：`code/inverted_pendulum/`

## 学什么

负反馈框图；离散 PID；平衡点线性化 \(\dot{x} \approx A x + B u\)；闭环仿真习惯。LQR 放到大三下，和田玉平第 7 章（能控性、极点配置、观测器）一起学，见 [`plan/复试与项目.md`](../plan/复试与项目.md)。

## 推荐资源

| 资源 | 范围 |
|------|------|
| [Feedback Systems](https://fbsbook.org/) | Ch 7 PID、Ch 8 状态反馈（选节） |
| 田玉平《自动控制原理》（第 2 版） | 按 SEMESTER_PLAN「田玉平 · 835/5c5」列复习（考研主轴） |
| 胡寿松《自动控制原理》 | **课内对照**：作业、期末，与田玉平章节对照记 3 条差异即可 |
| [python-control](https://python-control.readthedocs.io/) | 选做：`step_response` 对照直觉 |

## 与项目

按周推进 `model.py` → `controllers/pid.py` → `simulation.py`；12 月中旬前至少一张 PID 闭环角度曲线。

**验收**：复盘能指代码注释对应公式；能口头说明「倒立摆 ≈ 平衡车等效模型」。
