# T01 · Python 语言基础

**章节 ID**：T01  
**预计用时**：3–5 天（配合 Week 1）

---

## 1.1 为什么机器人项目用 Python

- **快**：验证公式、画图、调参循环短。  
- **库**：NumPy / SciPy / Matplotlib 是数值仿真的标准组合。  
- **分工**：MCU 实物阶段用 **C** 做实时控制；主机用 Python 做仿真与学习（见 ROADMAP）。

你要达到的标准：**能读、能改、能写 50 行以内的小脚本**，而不是背遍标准库。

---

## 1.2 变量、类型与打印

Python 是动态类型语言：名字绑定到对象。

| 类型 | 例子 | 控制/仿真中的用途 |
|------|------|-------------------|
| `int` / `float` | `theta = 0.1` | 角度、时间步 |
| `bool` | `is_stable = False` | 标志位 |
| `str` | `"cart-pole"` | 日志、路径 |
| `list` | `[x, x_dot]` | 临时状态列表（后期多用 ndarray） |
| `dict` | `{"mass": 1.0}` | 参数字典 |

运行并阅读：`weeks/week01/ex01_syntax.py`。

**与平衡车的联系**：日志里打印 `theta`、`theta_dot`，就是以后调试 IMU 与编码器时的习惯。

---

## 1.3 条件与循环

- `if / elif / else`：根据误差符号决定电机方向（PID 的雏形是「误差大则大力矩」）。  
- `for`：遍历时间步、参数扫掠。  
- `while`：仿真主循环的语法形式（后期常用 `for t in t_array` 更清晰）。

---

## 1.4 函数

函数把「输入 → 输出」封装起来，便于测试。

阅读 [`weeks/week01/ex02_functions.py`](../../weeks/week01/ex02_functions.py)，关注：

- `clamp`：输出限幅，对应电机力矩饱和  
- 参数与返回值  
- 默认参数（例如仿真步长 `dt=0.001`）  
- 文档字符串 `"""..."""`（复试笔记里可引用）

**小练习（必做级）**：写函数 `square(x)` 返回平方，并对列表 `[1,2,3]` 用循环打印平方。

---

## 1.5 列表、字典与推导式

`weeks/week01/ex03_lists_dicts.py` 覆盖：

- 索引、切片  
- `dict` 存物理参数 `m, l, g`  
- 列表推导式 `[x**2 for x in range(5)]`

**与平衡车的联系**：参数字典 `params = {"m_cart": 1.0, "m_pole": 0.1}` 会在 `model.py` 里反复出现。

---

## 1.6 模块与 `if __name__ == "__main__"`

脚本结构建议：

```python
def main() -> None:
    ...

if __name__ == "__main__":
    main()
```

这样别人可以 `import` 你的函数而不自动跑仿真。`hello_sim.py` 已是范例。

---

## 1.7 常见坑（WSL 新手）

1. **缩进**：必须用空格（通常 4 格），混用 Tab 会报错。  
2. **路径**：运行脚本时在**项目根**执行 `python weeks/week01/...`，相对路径才一致。  
3. **虚拟环境**：终端提示符前有 `(.venv)` 或 `(pendulum)` 再 `pip install`。

---

## 必做

- [ ] 完成 `ex01_syntax.py`、`ex02_functions.py`、`ex03_lists_dicts.py`，能口述每段在做什么。  
- [ ] 修改 `ex01` 里 `score` 或循环范围，确认你理解输出从何而来。  
- [ ] 自写 ≤10 行：列表 `[1,2,3]`，for 循环打印平方。

## 选做

- [ ] 读 Python 官方教程「数据结构」一章（中文即可）。  
- [ ] 用 `type()` 打印五个变量的类型，写在笔记里。

---

**上一章**：[T00](T00-导读与环境.md) · **下一章**：[T02 · NumPy 与 Matplotlib](T02-NumPy与Matplotlib.md)
