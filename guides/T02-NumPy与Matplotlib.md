# T02 · NumPy 与 Matplotlib

**预计**：5–7 天 · **示例**：`code/week01/examples/hello_sim.py`

## 学什么

`ndarray`、切片、`linspace`、向量化运算、简单 `plot`/`savefig`（无 GUI 时保存 PNG）。

## 推荐资源

| 资源 | 范围 |
|------|------|
| [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html) | 数组创建与运算 |
| [Matplotlib Pyplot](https://matplotlib.org/stable/tutorials/pyplot.html) | 折线图、子图（选读） |

## 与项目

状态 `x` 将是长度 4 向量；阶跃响应图习惯与以后 PID 曲线相同。

**验收**：跑 `hello_sim` 并改 `tau`；用 `np.linspace` 向量化算一阶阶跃。
