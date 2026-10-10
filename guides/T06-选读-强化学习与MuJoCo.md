# T06 · 选读：强化学习与 MuJoCo

**预计**：选读 2–4 h · **实现**：寒假及以后 · **前置**：T04 经典主线

## 三句话

1. 寒假优先 **MuJoCo + LQR**，再考虑 RL。  
2. T05 的 MLP 是 **有标签的一步预测**；RL 是 **奖励驱动的策略**，没有逐步「正确力矩」标签。  
3. 复试能对比 PID / LQR / RL 的假设与可解释性，比只会调包更重要。

## 学什么（概念）

MDP \((S,A,P,R,\gamma)\)、策略 \(\pi(a|s)\)、与 T03 仿真循环的差别；MuJoCo 作为 **物理仿真器** 的角色。

## 推荐资源

| 资源 | 说明 |
|------|------|
| [MuJoCo 文档](https://mujoco.readthedocs.io/) | 安装与 MJCF 入门（寒假） |
| [Sutton & Barto](http://incompleteideas.net/book/the-book.html) | Ch 3–4 概念（选读） |
| [DeepMind Control Suite](https://github.com/google-deepmind/dm_control) | 以后对照环境（选读） |

本学期 **不把** MuJoCo / RL 库写入根 `requirements.txt`；01 月下旬起可按当周打卡试装。
