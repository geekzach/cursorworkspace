# 两轮自平衡小车 · 学习项目（复试准备）

面向准备 **东南大学 085400 电子信息（专硕）** 的本科同学：以 **两轮自平衡小车** 为最终目标（**先 MuJoCo 仿真、再实物**），从 **倒立摆（cart-pole）** 打好 Python、建模与经典控制基础；可选 **AI01** 支线（NumPy MLP 拟合一步动力学，**非 RL**）。

## 三个入口

| | 链接 | 说明 |
|---|------|------|
| **教程** | [`docs/tutorials/`](docs/tutorials/README.md) | 中文讲义 **T00–T06**、**T01b**；思路核对 [`answers/`](docs/tutorials/answers/) |
| **校历打卡** | [`docs/checklists/`](docs/checklists/) | [`SEMESTER_PLAN.md`](docs/checklists/SEMESTER_PLAN.md)（2026-W42 起）· 当周 `YYYY-Www.md`（课表、CET-6、复盘） |
| **代码** | [`weeks/`](weeks/README.md) · [`src/`](src/) | 按周练习脚本；库 `inverted_pendulum/`、`ai01/` |

**路线图** [`docs/ROADMAP.md`](docs/ROADMAP.md) · **周日 20:30** 打开当周校历文件复盘。

> **仓库进度（2026-10）**：Week 1 练习可用；`src/inverted_pendulum/` 为骨架；MuJoCo / LQR 实物 / RL **尚未实现**（见 ROADMAP）。

---

## 环境（最短）

在项目**根目录**：

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\Activate.ps1
pip install -U pip && pip install -r requirements.txt
```

导入 `inverted_pendulum` / `ai01` 时：

```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
```

VS Code + WSL、conda 等等价步骤见 **[T00 §0.3](docs/tutorials/T00-导读与环境.md#env-setup)**。跑脚本与周目录说明见 **[`weeks/README.md`](weeks/README.md)**。

---

本项目为学习用途的教学脚手架。祝复试顺利。
