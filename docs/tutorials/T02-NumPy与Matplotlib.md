# T02 · NumPy 与 Matplotlib

**章节 ID**：T02  
**预计用时**：5–7 天  
**示例**：[`weeks/week01/examples/hello_sim.py`](../../weeks/week01/examples/hello_sim.py)  
**练习**：继续巩固 T01 练习 + 改 `hello_sim` 中 `K, tau`  
**思路**：[`weeks/week01/answers/02_numpy_matplotlib.md`](../../weeks/week01/answers/02_numpy_matplotlib.md)

---

## 学习目标

把状态当成 **向量** 处理；能画 **阶跃/时间序列** 图，为 ODE 与 PID 响应图打底。

## 知识要点

| 块 | 要点 |
|----|------|
| `ndarray` | 形状、`dtype`、与 Python `list` 区别 |
| 创建与索引 | `np.array`、`np.linspace`、`np.zeros`、切片 |
| 向量化 | 避免 Python 双层循环算时间序列 |
| 广播 | 标量与数组运算规则 |
| 线性代数入门 | 点积、`@` 小矩阵（为 \(A x\) 预热） |
| Matplotlib | `plot`、`xlabel`、`legend`、`savefig`；无 GUI 用 Agg |

## 推荐读物

| 资源 | 范围 |
|------|------|
| [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html) | 全文 skim + 练数组创建 |
| [Matplotlib Pyplot 教程](https://matplotlib.org/stable/tutorials/pyplot.html) | 折线图、子图选读 |

## 与项目的联系

- 倒立摆状态 `x = [x, ẋ, θ, θ̇]` 将是 **长度 4 的向量**（T03–T04）。  
- `hello_sim` 的一阶阶跃 = 以后看 **闭环阶跃响应** 的同一套画图习惯。  
- 保存 PNG 到 `weeks/week01/examples/` 便于写进周复盘。

## 练习与验收

1. 跑 `hello_sim.py`，改 `tau` 观察趋近速度。  
2. 用 `np.linspace` 生成时间轴，**向量化**计算 `y = K(1-exp(-t/tau))`。  
3. 选做：子图对比两组 `tau`。

**必做**：[`weeks/week01/CHECKLIST.md`](../../weeks/week01/CHECKLIST.md) 中 `hello_sim` 项。

---

**上一章**：[T01](T01-Python语言基础.md) · **下一章**：[T03](T03-常微分方程与仿真直觉.md)
