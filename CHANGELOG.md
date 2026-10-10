# Changelog

## 2026-10-10 · 课程结构重整

### 教程（`docs/tutorials/`）

- 各章改为 **学习目标、知识要点、推荐读物、项目挂钩**；移除长段内嵌教学代码。
- 可运行代码统一指向 `weeks/<week>/{examples,exercises,answers}/`。
- **T05**：本学期仅 **李航《统计学习方法》** 阅读计划；AI 编码推迟至寒假（见 `winter-ai.md`）。

### 练习代码（`weeks/`）

- **week01**：`examples/`（`hello_sim.py`）、`exercises/`（`ex01`–`ex03`）、`answers/`（T01–T02 思路）。
- **week02**：`examples/ex01_preview_rollout.py`（自 `ai01` 迁出）；`answers/03_ode_intuition.md`。
- **week03**：`answers/05_pid_state_space.md`（T04）。
- **ai01**：`exercises/ex02`、`answers/demo_reference` — 标注 **寒假** 使用。

### 计划与清单（`docs/checklists/`）

- 周文件由 `YYYY-Www.md` 重命名为 **`YYYY-MM-DD.md`**（该周周一）。
- 删除归档 **`2026-W41.md`**。
- **`SEMESTER_PLAN.md`**：补充每周 **张宇**、**自控**、**李航** 复习范围；移除本学期 AI 编码排期。
- 新增 **`winter-ai.md`**；删除 **`ai01-focus.md`**。

### 路线图

- **`docs/ROADMAP.md`**：M1.6 / AI 编码移至寒假阶段二；阶段一强调经典主线 + ML 只读。

### 验证

- `python weeks/week01/exercises/ex01_syntax.py`
- `python weeks/week01/examples/hello_sim.py`
- `python weeks/week02/examples/ex01_preview_rollout.py`
