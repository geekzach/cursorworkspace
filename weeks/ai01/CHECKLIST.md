# AI01 · 脚本自查（短清单）

教程：**[T03](../../docs/tutorials/T03-常微分方程与仿真直觉.md) + [T05](../../docs/tutorials/T05-AI01-神经网络拟合动力学.md)**。与 Week 1 并行、**可选**。

## 环境

- [ ] 已能运行 `weeks/week01/` 下脚本（说明 numpy / matplotlib 可用）
- [ ] 已设置 `export PYTHONPATH="$(pwd)/src"`（或在 IDE 把 `src` 标为源码根）
- [ ] 成功运行 `ex01_preview_rollout.py` 并看到/保存轨迹图

## 概念（能用自己的话说明）

- [ ] 什么是 **rollout**：给定模型与输入序列，一步步积分得到状态轨迹
- [ ] 本作业监督信号是什么：真实 ODE 积分得到的 **下一时刻状态**
- [ ] 网络输入 / 输出各是哪几个量（θ, ω, u → θ⁺, ω⁺）
- [ ] MSE 损失在衡量什么；训练集与验证集为何要分开

## 练习 `ex02_fit_dynamics.py`

- [ ] 找到并完成所有 **TODO**（超参数、打印、绘图）
- [ ] 训练后验证集 MSE 明显低于「未训练随机权重」（若否，检查学习率与 epoch）
- [ ] 能解释 `hidden_dim` 变大时训练/验证误差的大致变化（试改 1–2 次）

## 对照与扩展

- [ ] 浏览 `src/ai01/mlp_numpy.py` 中 `forward` / `backward`（不要求手写推导，能指认链式法则即可）
- [ ] 至少完成 [`TUTORIAL.md`](TUTORIAL.md) 中 **一项 DIY**（噪声 / 样本数 / 预测加速度）
- [ ] （可选）运行 `demo_reference_end2end.py`，只改参数做对比实验，**不复制粘贴交作业**

## 与复试叙事

- [ ] 能在一分钟内说明：本实验与后续 **LQR / RL** 的分工（开环拟合 vs 闭环决策）
- [ ] 知道完整倒立摆模型在 `src/inverted_pendulum/model.py` 尚未实现，本支线用的是 **简化摆 ODE**

---

**下一预告**：Week 2 主线学 numpy 向量与 scipy ODE；可把本数据生成改成自己写的积分循环，与 `pendulum.py` 对照。
