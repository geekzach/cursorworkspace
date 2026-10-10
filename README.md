# 两轮自平衡小车 · 学习项目（复试准备）

面向准备 **东南大学 085400 电子信息（专硕）** 的本科同学：以 **两轮自平衡小车** 为最终目标（**先 MuJoCo 仿真、再实物**），从 **倒立摆（cart-pole）** 打好 Python、建模与经典控制基础；**本学期** ML 按 **[T05](docs/tutorials/T05-AI01-神经网络拟合动力学.md)** 自学李航《统计学习方法》，**寒假**再写 `weeks/ai01/` 代码。

## 三个入口

| 去哪 | 链接 | 说明 |
|------|------|------|
| **学教程** | [`docs/tutorials/`](docs/tutorials/README.md) | 目标 / 书目 / 要点（**无长代码**） |
| **本周打卡** | [`docs/checklists/`](docs/checklists/) | [`SEMESTER_PLAN.md`](docs/checklists/SEMESTER_PLAN.md) · 当周 `YYYY-MM-DD.md` |
| **跑代码** | [`weeks/`](weeks/README.md) · [`src/`](src/) | `examples` → `exercises` → `answers` |

**路线图** [`docs/ROADMAP.md`](docs/ROADMAP.md) · **周日 20:30** 复盘。

> **仓库进度（2026-10）**：`week01` / `week02` 示例可用；`src/inverted_pendulum/` 骨架；MuJoCo / LQR / RL 未实现。

---

## 环境（最短）

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip && pip install -r requirements.txt
python weeks/week01/exercises/ex01_syntax.py
```

`src` 包：`export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"`。详见 **[T00 §0.3](docs/tutorials/T00-导读与环境.md#env-setup)**。

---

本项目为学习用途的教学脚手架。祝复试顺利。
