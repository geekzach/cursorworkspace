# 01 · Python 基础（控制向）

## 为什么学这个

平衡车固件里你会写 C 的 `if`、循环和函数；主机仿真里 **同一套逻辑用 Python 写更快试错**。复试不会考 Python 语法题，但会看你能否 **读仿真脚本、改参数、讲清控制量怎么算**。Week 1 的 `ex01`–`ex03` 就是为 `hello_sim.py` 和以后的 `u = pid(error)` 铺路。

---

## 1. 变量与类型

Python 变量 **不用声明类型**，但值有类型：

| 类型 | 例子 | 控制场景 |
|------|------|----------|
| `int` | `week = 1` | 循环计数、采样序号 |
| `float` | `tau = 0.5` | 时间常数、角度、力矩 |
| `str` | `name = "倒立摆"` | 日志、图标题 |
| `bool` | `is_ready = False` | 标志位（是否饱和等） |

**仓库对照**：[`weeks/week01/ex01_syntax.py`](../../weeks/week01/ex01_syntax.py) 开头几行。

**迷你例子**（可在交互式 Python 或临时脚本里试）：

```python
theta_deg = 2.5
theta_rad = theta_deg * 3.14159 / 180.0
print(theta_rad)  # 约 0.0436
```

**预期**：打印一个小于 0.1 的浮点数（小角度 rad）。

---

## 2. 条件与循环

- **`if / elif / else`**：根据传感器或误差分支，例如「误差大 → 大增益」。
- **`for i in range(a, b)`**：`i` 取 `a, a+1, …, b-1`（**不含 b**）。
- **`while`**：条件为真就重复；仿真里要小心别写成死循环。

**仓库对照**：`ex01_syntax.py` 里分数分级、`for` 求 1+…+5、`while` 倒计时。

**控制味例子**：限幅（饱和）——与 `ex02_functions.py` 的 `clamp` 同源思想：

```python
u_cmd = 15.0
u_max = 10.0
if u_cmd > u_max:
    u = u_max
elif u_cmd < -u_max:
    u = -u_max
else:
    u = u_cmd
print(u)  # 10.0
```

---

## 3. 函数

函数 = **有名字的一段计算**，可带参数和返回值。

```python
def greet(student_name: str) -> str:
    return f"你好，{student_name}！"
```

- `def` 定义；`return` 把结果交给调用者。
- **默认参数**：`def step_size(dt: float = 0.01)` —— 仿真步长常用默认 `0.01` s。
- **`if __name__ == "__main__"`**：只有「直接运行本文件」时才执行 `main()`，被 `import` 时不乱跑。

**仓库对照**：[`weeks/week01/ex02_functions.py`](../../weeks/week01/ex02_functions.py)。

**和 C 的对比**（帮助迁移）：

| C | Python |
|---|--------|
| `float clamp(float v, ...)` | `def clamp(value: float, ...) -> float` |
| 必须声明类型 | 类型注解可选，给人看 |
| `return` | 同样 |

---

## 4. 列表 `list`

有序、可变，用下标访问；**负下标**从末尾数：`a[-1]` 最后一个。

```python
angles_deg = [2.1, 1.8, 1.2, 0.5, -0.1]
print(angles_deg[0], len(angles_deg))
```

**列表推导式**（预习 numpy 向量化）：

```python
squares = [x * x for x in angles_deg]
```

**仓库对照**：[`weeks/week01/ex03_lists_dicts.py`](../../weeks/week01/ex03_lists_dicts.py)。

---

## 5. 字典 `dict`

键值对，适合 **物理参数表**：

```python
params = {
    "cart_mass_kg": 1.0,
    "rod_length_m": 0.5,
}
L = params["rod_length_m"]
```

后续 `PendulumParams` 会用 `dataclass`，本质也是「命名字段」，见 03、04 节。

---

## 6. `zip`：对齐时间序列

```python
times = [0.0, 0.1, 0.2]
values = [0.0, 0.63, 0.86]
for t, y in zip(times, values):
    print(f"t={t:.1f}s, y={y:.2f}")
```

仿真里常同时遍历 `t` 与状态分量。

---

## 常见踩坑

1. **`range(1, 6)` 没有 6** —— 想包含 6 用 `range(1, 7)`。
2. **缩进错误** —— Python 用缩进表示块，复制代码时混用 Tab/空格会报 `IndentationError`。
3. **浮点比较** —— 不要写 `if x == 0.1`，用 `abs(x - 0.1) < 1e-9` 或比较区间。
4. **修改 list 当参数** —— 函数里 `lst.append(...)` 会改外面的 list（引用语义）；初学先当「要注意」，OOP 以后再系统学。
5. **中文路径** —— 尽量仓库路径纯英文，WSL 下更省心。

---

## 本节练习

### 必做

1. 运行 `python weeks/week01/ex01_syntax.py`、`ex02_functions.py`、`ex03_lists_dicts.py` 各一遍，在笔记里各写 **一句** 你新学到的点。
2. 在 `ex02_functions.py` 里把 `raw_command = 15.0` 改成 `-20.0`，再运行，记录 `clamp` 后的输出。
3. **自己写**：新建 `weeks/week01/my_squares.py`（或放笔记里），用 `for` 对列表 `[1,2,3,4,5]` 打印每个数的平方；运行无报错。

### 选做

1. 写一个函数 `deg_to_rad(deg: float) -> float`，并在 `if __name__ == "__main__"` 里打印 `deg_to_rad(30)`（约 0.524）。
2. 读 `ex02` 里嵌套的 `step_size`，解释：**默认参数**在控制仿真里为什么有用（联系「常用 dt=0.01，偶尔要更小步长」）。

---

**参考思路**：[`answers/01_python_basics.md`](answers/01_python_basics.md)  
**下一节**：[02 NumPy 与 Matplotlib](02_numpy_matplotlib.md)
