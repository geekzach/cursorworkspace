# 两轮自平衡小车 — 学习路线图

面向 **东南大学 085400 电子信息（专硕）** 复试准备，方向倾向 **具身智能 / 嵌入式控制**。本项目以 **「先仿真、后实物」** 为主线：用倒立摆打好数学与经典控制基础，再在 MuJoCo 中搭建两轮自平衡小车，最后落地 MCU 实物，并可选做强化学习实验与复试答辩材料串联。

> **当前进度（2026 年 10 月）**：**Week 1**（`weeks/week01/`）练习可用；**Week 2** 含 T03 示例 `ex01`；`src/inverted_pendulum/` 仍为包骨架。  
> MuJoCo、LQR 闭环、实物、RL **均未实现**。  
> **校历与教程映射**（周一日期文件 `2026-10-12` → `2027-02-01`）：[`docs/checklists/SEMESTER_PLAN.md`](checklists/SEMESTER_PLAN.md)。

---

## 设计原则

1. **先仿真、后硬件**：在主机上验证模型与控制律，再移植到 MCU。  
2. **分层架构**：MCU **&lt; 1 ms** 级电流/力矩环；主机仿真、整定、学习实验。  
3. **从成熟开源起步**：先读懂再改。  
4. **复试可讲**：每阶段留 **图、公式、曲线**。

---

## 阶段一：大三上（2026.10 — 2027.01）— 倒立摆基础

**主题**：Python、ODE、拉格朗日建模、线性化、PID；**ML 只读书**（李航《统计学习方法》，见 T05 / SEMESTER_PLAN）。

| 里程碑 | 内容 | 产出物（建议） |
|--------|------|----------------|
| M1.1 | Week 1–2：语法、NumPy、简单 ODE | `week01`/`week02` CHECKLIST |
| M1.2 | cart-pole 动力学 → 状态方程 | 笔记 + `model.py` |
| M1.3 | 线性化、开环仿真 | 状态曲线图 |
| M1.4 | PID 整定 | 阶跃/扰动响应图 |
| M1.5 | 口头说明：**倒立摆 ≈ 平衡车等效模型** | 一页示意图 |

**AI 编码（原 M1.6）**：移至 **寒假**，与 MuJoCo / 项目并行 — `weeks/ai01/`、[`winter-ai.md`](checklists/winter-ai.md)。本学期 **不写** 训练代码。

**与本仓库**：`weeks/<week>/{examples,exercises,answers}/` + `src/inverted_pendulum/`。教程无长代码，见 [`docs/tutorials/README.md`](tutorials/README.md)。

---

## 阶段二：寒假（2027.01 — 2027.02）— MuJoCo 仿真 + 可选 AI01

**主题**：MJCF 平衡车、LQR；可选 **NumPy MLP 一步动力学**（AI01）。

| 里程碑 | 内容 |
|--------|------|
| M2.1 | MuJoCo 安装、demo 可复现 |
| M2.2 | 两轮平衡车 MJCF |
| M2.3 | 线性化 \(A,B\) 与阶段一对照 |
| M2.4 | LQR 仿真稳定 |
| M2.5 | 参数扫掠图 |
| **M2.6**（可选） | AI01：`ex02` val MSE 合理；对比经典模型 |

---

## 阶段三：大三下（2027.03 — 2027.06）— 实物硬件

（略，同前：ESP32/STM32、IMU、PID/LQR 移植、仿真对比。）

---

## 阶段四：2027 暑假前 — 强化学习（加分项）

在 MuJoCo 中简单 RL，与 LQR 对比；可回顾寒假 AI01 的「一步拟合 vs 闭环策略」。

---

## 复试 PPT 建议叙事线

建模 → 经典 PID → LQR → MuJoCo → 实物 → 学习控制（可选）。

---

## 仓库目录（规划）

```text
weeks/week01|02/     examples → exercises → answers
weeks/ai01/          寒假 AI 编码
docs/tutorials/      学习目标 + 书目（无长教学代码）
docs/checklists/     YYYY-MM-DD.md 周打卡
src/inverted_pendulum/
src/ai01/
sim/mujoco/
```

---

祝复习与实验顺利。
