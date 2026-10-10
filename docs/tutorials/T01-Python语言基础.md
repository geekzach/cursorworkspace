# T01 · Python 语言基础（零基础自学讲义）

**章节 ID**：T01  
**预计用时**：5–8 天（可拆成每天 1–1.5 小时 × 6 天）  
**配套脚本**：[`weeks/week01/ex01_syntax.py`](../../weeks/week01/ex01_syntax.py) · [`ex02_functions.py`](../../weeks/week01/ex02_functions.py) · [`ex03_lists_dicts.py`](../../weeks/week01/ex03_lists_dicts.py)

---

## 如何使用本章（必读）

你不是来「背语法表」的，而是要学会：**读得懂仓库里的脚本、改得动参数、能独立写出几十行仿真辅助代码**。推荐节奏（知乎/网课里常说的 **「先跑通再讲」**）：

1. **先跑**配套 `ex0x` 脚本，对照本节「仓库对照」看输出。  
2. **再抄**下面灰色代码块到终端或临时 `.py` 文件，**改一个数**看输出怎么变。  
3. **做**每节末尾「练习」；标 ⭐ 的为必做，标 🔶 的为进阶。  
4. 卡住时看「常见错误 vs 推荐」，不要跳过。

对照外部资料时，以 [Python 官方教程（中文）](https://docs.python.org/zh-cn/3/tutorial/) 第 1–5 章为主；本章把**和控制/仿真相关**的例子写密一些。

**本章结束时你应该能**：解释 `ex01`–`ex03` 每一段在干什么；自己写 `clamp`、循环累加、参数字典；**能读会写简单的 `class`（如 `PID` 控制器对象）**；为 T02 的 NumPy 数组打底。类与对象的**加练**见 [T01b · 类与对象入门](T01b-类与对象入门.md)。

---

## 1.1 为什么机器人项目用 Python（以及 C 在哪）

| 场景 | 用 Python | 用 C（ESP32/STM32） |
|------|-----------|---------------------|
| 推导检验、画曲线、扫 PID 参数 | ✅ 改两行即跑 | 每次改参要编译烧录 |
| 1 ms 级电机电流环 | ❌ 不适合硬实时 | ✅ |
| 复试展示「我会仿真」 | ✅ 笔记本即可 | 需硬件 |

本仓库 **大三上** 主机侧几乎全是 Python；**大三下** 实物控制在 MCU 上写 C。现在把 Python 练到 **「能读 50 行、能写 30 行」** 就够支撑后续 ODE 与 PID，不必先学装饰器、元类等进阶特性。

### 1.1.1 跑通：30 秒认识「状态变量」

在项目根目录（已 `source .venv/bin/activate`）：

```bash
python - <<'PY'
theta = 0.05       # 摆角 (rad)，先当普通小数
theta_dot = -0.2   # 角速度 (rad/s)
print("摆角", theta, "角速度", theta_dot)
PY
```

**练习 ⭐**：把 `theta` 改成 `0.12`，再运行，确认只有数字变、语法不变。

---

## 1.2 三种运行 Python 的方式

### 1.2.1 交互式解释器（REPL）

终端输入 `python` 回车，出现 `>>>`：

```python
>>> 1 + 2
3
>>> 10 / 4      # 真除法，结果是浮点
2.5
>>> 10 // 4     # 地板除，商
2
>>> 10 % 4      # 余数
2
>>> 2 ** 3      # 幂
8
>>> exit()
```

REPL 适合：**试一句算一句**。写长程序请用脚本文件。

### 1.2.2 脚本文件

```bash
python weeks/week01/ex01_syntax.py
```

规则：**当前工作目录最好是仓库根目录**，这样以后 `weeks/week02/` 等路径一致。

### 1.2.3 一行命令（本章常用）

```bash
python -c "print(1 + 1)"
```

**常见错误 vs 推荐**

| ❌ | ✅ |
|----|-----|
| 在 `weeks/week01/` 里 `python ex01_syntax.py`，以后写 `open("data.csv")` 路径全乱 | 始终在根目录 `python weeks/week01/ex01_syntax.py` |
| 没激活 venv 就 `pip install`，装到系统 Python | 先 `source .venv/bin/activate` 再 pip |

**练习 ⭐**：用 `python -c` 打印你的名字（字符串）。

---

## 1.3 注释、缩进与代码块

Python 用 **缩进（通常 4 个空格）** 表示「属于同一块」的代码，不用花括号 `{}`。

```python
# 这是整行注释
score = 85
if score >= 60:
    print("及格")      # 属于 if 块，必须缩进
    print("继续学")    # 同属 if 块
print("无论是否及格都会执行")  # 与 if 对齐，不在 if 里
```

```python
# ❌ IndentationError：if 下一行没缩进
# if True:
# print("错")

# ❌ Tab 和空格混用（WSL 下很常见）
# 在 VS Code 设置：Insert Spaces，Tab Size = 4
```

**练习 ⭐**：写 `if score >= 90: print("优秀")` 的单行合法形式（`:` 后换行缩进更常见）。

---

## 1.4 数字：int、float 与运算

仿真里 **时间、角度、力矩** 几乎都是浮点数；循环计数用整数。

```python
dt = 0.001          # float
n = 1000            # int
t = n * dt          # 1000 * 0.001 -> 1.0
print(t, type(t))
```

**运算符**（务必亲手在 REPL 试一遍）：

- `+ - * /`：加减乘除（`/ 总是浮点除）  
- `//` `%` `**`：整除、取余、幂  
- 比较：`== != < <= > >=`，结果是 `True` / `False`

```python
theta = 0.1
print(theta == 0.1)           # 可能 True
print(0.1 + 0.2 == 0.3)       # 常常是 False！浮点误差
print(abs(0.1 + 0.2 - 0.3) < 1e-9)
```

控制里判断「是否直立」要用 **容差**，不要 `theta == 0`。

**练习 ⭐**：`tau = 0.5`，计算 `1 - 2**(-1/tau)`（一阶阶跃在 \(t=1\) 的解析值，预习 T02）。  
**练习 🔶**：`range(0, 5)` 与 `range(1, 6)` 各生成什么列表？用 `list(...)` 打印。

---

## 1.5 字符串 str 与打印

```python
name = "东南大学复试准备"
week = 1
hours = 1.5
# 方式 1：逗号 print（自动加空格）
print("周次", week, "每天", hours, "小时")
# 方式 2：f-string（推荐）
print(f"周次 {week} 每天 {hours} 小时")
print(f"2位小数: {hours:.2f}")
```

`ex01_syntax.py` 里同时用了两种方式，你可以统一改成 f-string 练手。

**转义与多行**：

```python
path = "C:\\Users\\name"   # 反斜杠要转义；Linux 下多用 "/"
text = """第一行
第二行"""
```

**练习 ⭐**：用 f-string 打印 `theta=0.05` 保留 3 位小数：`f"{theta:.3f}"`。

---

## 1.6 布尔值 bool 与逻辑运算

```python
is_stable = False
has_imu = True
print(is_stable or has_imu)   # True
print(is_stable and has_imu)  # False
print(not is_stable)          # True
```

`if` 的条件可以是比较表达式或布尔变量：

```python
e = 0.0 - 0.05   # 误差 = 期望 - 测量
if abs(e) > 0.01:
    print("误差偏大，需要加大控制")
```

**练习 ⭐**：设 `score=85`，用 `if/elif/else` 输出「优秀/及格/需加强」（对照 `ex01`）。

---

## 1.7 条件分支 if / elif / else（细讲）

结构：

```text
if 条件1:
    语句块1
elif 条件2:
    语句块2
else:
    语句块3
```

**控制语境**：根据摆角符号决定「往哪边用力」（极简逻辑，还不是完整 PID）：

```python
theta = 0.1
if theta > 0:
    direction = "向左推车"
elif theta < 0:
    direction = "向右推车"
else:
    direction = "不动作"
print(direction)
```

**嵌套**（可读性变差时要考虑用函数拆分）：

```python
theta = 0.2
if abs(theta) < 0.5:
    if theta > 0:
        u = -1.0
    else:
        u = 1.0
else:
    u = 0.0   # 角太大先保护
print("u =", u)
```

**常见错误 vs 推荐**

```python
# ❌ C 语言习惯
# if (theta > 0) { ... }

# ✅ Python
if theta > 0:
    ...

# ❌ 比较链写错
# if 0 < theta < 0.5:   # 其实合法！但要理解这是链式比较
# 初学更直观：
if theta > 0 and theta < 0.5:
    ...
```

**练习 ⭐**：`score` 从 59、60、90 各跑一遍 `ex01` 的分支逻辑（改 `score` 变量）。  
**练习 🔶**：写三段分支：`|theta| < 0.05` 为「稳」，`0.05~0.3` 为「调」，`>0.3` 为「危险」。

---

## 1.8 for 循环与 range

`ex01` 核心片段：

```python
total = 0
for i in range(1, 6):   # i = 1,2,3,4,5
    total = total + i
    print("  加上", i, "后累计 =", total)
```

`range` 要点：

- `range(5)` → 0,1,2,3,4  
- `range(1, 6)` → 1..5（**不含**右端点 6）  
- `range(0, 10, 2)` → 0,2,4,6,8

**仿真雏形**：固定步长累加时间

```python
t = 0.0
dt = 0.1
for k in range(5):
    print(f"k={k} t={t:.1f}")
    t += dt
```

**遍历列表**

```python
angles = [2.1, 1.8, 1.2]
for a in angles:
    print(a)
for idx, a in enumerate(angles):
    print(idx, a)
```

**练习 ⭐**：用 `for` 计算 1 到 10 的和（答案 55）。  
**练习 🔶**：用 `zip(times, values)` 打印配对（见 `ex03` 末尾）。

---

## 1.9 while 循环

`ex01` 倒计时：

```python
countdown = 3
while countdown > 0:
    print("  还剩", countdown, "秒…")
    countdown = countdown - 1
```

`while` 适合「不知道要循环几次，直到条件满足」；数值仿真更常用 **`for k in range(n_steps)`**，因为步数已知。

**常见错误 vs 推荐**

```python
# ❌ 忘记更新条件 -> 死循环
# while countdown > 0:
#     print(countdown)

# ✅ 循环体内改变 countdown
```

**练习 ⭐**：`while` 把 `x=1.0` 每次乘 0.5，直到 `x < 0.1`，打印循环次数。

---

## 1.10 函数：定义、调用、返回值

函数 = 给一段逻辑起名，避免复制粘贴。

```python
def greet(student_name: str) -> str:
    return f"你好，{student_name}！"

print(greet("同学"))
```

- `student_name` 是**形参**；`"同学"` 是**实参**。  
- `-> str` 是类型注解，**不强制**，但读代码像说明书。  
- `return` 结束函数并给出结果；没有 `return` 则返回 `None`。

### 1.10.1 限幅 clamp（控制必会）

[`ex02_functions.py`](../../weeks/week01/ex02_functions.py)：

```python
def clamp(value: float, low: float, high: float) -> float:
    if value < low:
        return low
    if value > high:
        return high
    return value

raw = 15.0
safe = clamp(raw, -10.0, 10.0)
print(safe)   # 10.0
```

物理含义：电机指令不能超过驱动器允许范围 → **抗饱和** 的第一步。

### 1.10.2 默认参数

```python
def step_size(dt: float = 0.01) -> float:
    return dt

print(step_size())       # 0.01
print(step_size(0.001))  # 0.001
```

默认参数必须写在非默认参数后面：`def f(a, b=1)` ✅，`def f(a=1, b)` ❌。

### 1.10.3 可变默认参数陷阱（面试常问）

```python
def bad(x, bucket=[]):
    bucket.append(x)
    return bucket

print(bad(1))   # [1]
print(bad(2))   # [1, 2]  吓人！同一个默认列表被复用

def good(x, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(x)
    return bucket

print(good(1))  # [1]
print(good(2))  # [2]
```

**练习 ⭐**：自己实现 `mean_of_three(a,b,c)`（见 `ex02`）。  
**练习 ⭐**：写 `p_control(theta, Kp=1.0)` 返回 `-Kp*theta`（期望角为 0）。  
**练习 🔶**：写 `saturate(u, u_max)` 用 `clamp` 实现对称限幅 `[-u_max, u_max]`。

---

## 1.11 变量作用域（够用版）

```python
Kp = 1.0

def control(theta):
    u = Kp * (0.0 - theta)   # 可读外层 Kp
    return u

print(control(0.1))
```

函数内 **赋值** 给名字会创建局部变量，除非 `global`（初学仿真脚本几乎不需要 `global`，用参数传入更清晰）。

```python
def broken():
    Kp = 2.0   # 局部 Kp，与外层无关

Kp = 1.0
broken()
print(Kp)   # 仍是 1.0
```

---

## 1.12 列表 list（有序、可变）

`ex03` 摆角序列：

```python
angles_deg = [2.1, 1.8, 1.2, 0.5, -0.1]
print(angles_deg[0], angles_deg[-1], len(angles_deg))
angles_deg.append(0.0)
```

**切片**（预习 NumPy 切片）：

```python
xs = [0, 1, 2, 3, 4, 5]
print(xs[1:4])    # [1, 2, 3]
print(xs[:3])     # 前三个
print(xs[::2])    # 隔一个取一个
```

**列表推导**

```python
squares = [x * x for x in angles_deg]
evens = [x for x in range(10) if x % 2 == 0]
```

**常见错误 vs 推荐**

```python
# ❌ 下标越界
# angles_deg[100]

# ✅ 先 len 或 try
i = 2
if i < len(angles_deg):
    print(angles_deg[i])

# ❌ 复制列表
a = [1, 2, 3]
b = a
b.append(4)   # a 也变了

# ✅
b = a.copy()   # 或 list(a)
```

**练习 ⭐**：列表 `[3,1,4,1,5]` 用循环求和。  
**练习 🔶**：推导式生成 `[i*0.1 for i in range(6)]` 作为时间轴。

---

## 1.13 字典 dict（键值对、物理参数）

```python
params = {
    "cart_mass_kg": 1.0,
    "pendulum_mass_kg": 0.1,
    "rod_length_m": 0.5,
    "gravity_m_s2": 9.81,
}
print(params["rod_length_m"])
print(params.get("damping", 0.0))  # 无键则默认 0

for key, value in params.items():
    print(key, value)
```

键通常是字符串；值可以是数字、列表、甚至嵌套 dict。

**练习 ⭐**：给 `params` 增加 `"note": "Week1"`，再 `print`。  
**练习 🔶**：用 dict 存 `{"Kp": 1.0, "Ki": 0.0, "Kd": 0.1}`，函数 `pid_placeholder(e, params)` 只算 `Kp*e`。

---

## 1.14 类与对象（够用版：读懂 `PID` 类）

函数把**一次计算**包起来；**类**把 **数据 + 多步操作** 绑在同一个名字下。后面 T04 的离散 PID、`src/inverted_pendulum/controllers/pid.py` 都会用 **「控制器对象」** 在仿真循环里反复调用 `step(...)`。

**本节不讲**继承、多态、设计模式——只学到能写 **30–60 行** 的实用类。

### 1.14.1 对象是什么（直觉）

- **类（class）**：图纸，例如「PID 控制器」。  
- **对象（instance）**：按图纸造出来的一个具体控制器，有自己的 `Kp`、内部积分状态。  
- **属性（attribute）**：挂在对象上的变量，如 `self.integral`。  
- **方法（method）**：挂在对象上的函数，第一个参数通常是 `self`（指「这个对象自己」）。

```python
class MotorLimit:
    """示例：只存上下限，并提供限幅方法。"""

    def __init__(self, u_min: float, u_max: float) -> None:
        self.u_min = u_min
        self.u_max = u_max

    def clamp(self, u: float) -> float:
        if u < self.u_min:
            return self.u_min
        if u > self.u_max:
            return self.u_max
        return u


lim = MotorLimit(-10.0, 10.0)   # 构造对象
print(lim.clamp(15.0))          # 10.0
print(lim.clamp(-20.0))         # -10.0
```

**练习 ⭐**：把上限改成 `5.0`，对 `u=3` 和 `u=8` 各调用 `clamp`，口述结果。

### 1.14.2 构造函数 `__init__`

`__init__` 在 **创建对象时自动调用**，用来初始化属性：

```python
class POnly:
    def __init__(self, Kp: float) -> None:
        self.Kp = Kp

    def compute(self, error: float) -> float:
        return self.Kp * error


ctrl = POnly(Kp=2.0)
u = ctrl.compute(error=0.1)   # 0.2
print(u)
```

**常见错误 vs 推荐**

```python
# ❌ 忘记 self.
# def compute(error):
#     return Kp * error

# ✅ 实例属性必须 self.Kp
# def compute(self, error):
#     return self.Kp * error

# ❌ 用类名当对象调用实例方法
# POnly.compute(0.1)
# ✅ 先 ctrl = POnly(2.0)，再 ctrl.compute(0.1)
```

### 1.14.3 离散 PID 类（与 T04 同款结构）

下面是一个 **可放进仿真循环** 的极简 PID；T04 会在此基础上加抗积分饱和等细节。

```python
class PID:
    def __init__(
        self,
        Kp: float,
        Ki: float,
        Kd: float,
        u_min: float = -10.0,
        u_max: float = 10.0,
    ) -> None:
        self.Kp, self.Ki, self.Kd = Kp, Ki, Kd
        self.u_min, self.u_max = u_min, u_max
        self.integral = 0.0
        self.prev_error = 0.0

    def reset(self) -> None:
        """换一条轨迹或重新仿真前清零内部状态。"""
        self.integral = 0.0
        self.prev_error = 0.0

    def step(self, error: float, dt: float) -> float:
        self.integral += error * dt
        d_error = (error - self.prev_error) / dt if dt > 0 else 0.0
        u = self.Kp * error + self.Ki * self.integral + self.Kd * d_error
        u = max(self.u_min, min(self.u_max, u))
        self.prev_error = error
        return u


pid = PID(Kp=1.0, Ki=0.0, Kd=0.1)
dt = 0.01
for e in (0.1, 0.08, 0.05):
    print("e=", e, "u=", pid.step(e, dt))
```

**练习 ⭐**：`Kp=2, Ki=0, Kd=0`，只对 `e=0.1` 调一次 `step`，手算 `u` 再运行核对。  
**练习 ⭐**：连续调用 `step` 三次后调用 `reset()`，再 `step` 一次，说明 `integral` 为何要从 0 重新开始。

### 1.14.4 小系统类：把状态包起来

用类保存 **状态向量** 和 **一步更新**，比散落的全局变量清晰（仍用纯 Python float，T03 再换 NumPy）。

```python
class FirstOrderSystem:
    """dy/dt = (K - y) / tau  —— 与 T02 阶跃响应同一族。"""

    def __init__(self, tau: float, K: float, y0: float = 0.0) -> None:
        self.tau = tau
        self.K = K
        self.y = y0

    def step(self, dt: float, u: float = 0.0) -> float:
        """u 可选：把输入看成对 K 的扰动（示意用）。"""
        target = self.K + u
        self.y += dt * (target - self.y) / self.tau
        return self.y


plant = FirstOrderSystem(tau=0.5, K=1.0, y0=0.0)
pid = PID(Kp=0.8, Ki=0.2, Kd=0.0, u_min=-2.0, u_max=2.0)
dt = 0.05
r = 1.0
for k in range(30):
    e = r - plant.y
    u = pid.step(e, dt)
    y = plant.step(dt, u=0.0)   # 本例 plant 未接 u，仅演示两类对象协作
    if k % 10 == 0:
        print(f"k={k} y={y:.3f} u={u:.3f}")
```

**说明**：上例 `plant.step` 未真正把 `u` 接入动力学，只为展示 **两个对象在循环里分工**。完整闭环在 T03–T04 用正确的 \(f(x,u)\) 实现；加练见 [T01b](T01b-类与对象入门.md)。

### 1.14.5 `self` 到底是什么

```python
class Demo:
    def __init__(self, value: int) -> None:
        self.value = value

    def show(self) -> None:
        print("self is", self, "value=", self.value)


a = Demo(1)
b = Demo(2)
a.show()
b.show()   # 两个对象各自一份 self.value
```

`self` 只是约定俗成的名字（必须占第一个参数位）；调用 `a.show()` 时 Python 自动把 `a` 传给 `self`。

### 1.14.6 类 vs 字典 vs 函数（怎么选）

| 方式 | 适合 |
|------|------|
| 函数 + 全局变量 | 极短草稿（易乱） |
| `dict` 存 `Kp,Ki,Kd` + 函数 | 参数表、配置 |
| **class** | 有 **内部状态** 要跨多步保留（积分、上一拍误差） |

`ex03` 的 `params` 字典仍然有用：**类里也可以引用 dict** 存物理常数。

### 1.14.7 常见错误 vs 推荐（汇总）

```python
# ❌ 在类外直接改未定义的属性
# pid.integral = 0   # 若 pid 没有先 __init__ 会怪

# ❌ step 里忘记更新 prev_error / integral

# ❌ 每个时间步 new PID(...) —— 积分永远累加不上
# ✅ 循环外 pid = PID(...)，循环内 pid.step(...)

# ✅ 仿真重跑前 pid.reset()
```

### 1.14.8 本节练习（必做）

**练习 ⭐ A**：给 `MotorLimit` 增加方法 `is_saturated(u)`，当 `u` 被限幅时返回 `True`。  
**练习 ⭐ B**：给 `PID` 增加只读属性效果：在 `step` 后能用 `pid.integral` 打印当前积分。  
**练习 ⭐ C**：写 `class SimClock`，`__init__(dt)`，`tick()` 每次 `self.t += dt` 并返回 `self.t`。  
**练习 🔶 D**：阅读 `src/inverted_pendulum/controllers/pid.py` 骨架，找出将来会对应 `step` 的函数名（可尚未实现）。

---

## 1.15 元组 tuple、集合 set（了解）

```python
state_names = ("x", "x_dot", "theta", "theta_dot")  # 不可变，可当「常量配置」
unique_ids = {1, 2, 2, 3}   # {1, 2, 3}
```

仿真主状态以后会放进 **NumPy 数组**；tuple 常用于「不会变的名字列表」。

---

## 1.16 模块与 `if __name__ == "__main__"`

`ex02` / `ex03` 末尾：

```python
def main() -> None:
    ...

if __name__ == "__main__":
    main()
```

含义：别人 `import ex02_functions` 时不会自动跑 `main()`；你 `python ex02_functions.py` 才会跑。

**自己写脚本时也用这套结构**，复试项目里显得专业。

---

## 1.17 读错信息：异常与调试

```python
try:
    x = int("3.14")
except ValueError as err:
    print("转换失败:", err)
```

常见：

- `SyntaxError`：缩进、括号  
- `NameError`：变量未定义  
- `TypeError`：类型不对（如 `str + int`）  
- `KeyError`：dict 没有该键  
- `IndexError`：列表下标越界

**调试习惯**：在怀疑处 `print("debug theta=", theta)`；或用 VS Code 断点。学完 T02 可用 `matplotlib` 画图代替盯数字。

**练习 ⭐**：故意 `params["no_key"]` 触发 `KeyError`，改用 `.get`。

---

## 1.18 与仓库脚本逐段对照

### ex01_syntax.py

| 行段 | 知识点 |
|------|--------|
| 变量 `name, week, hours` | §1.4–1.5 |
| `if score` 分支 | §1.7 |
| `for i in range(1,6)` | §1.8 |
| `while countdown` | §1.9 |

**建议**：改 `score=59/60/90` 各运行一次；改 `range(1,6)` 为 `range(1,11)` 看 `total` 变化。

### ex02_functions.py

| 函数 | 在后续项目中的角色 |
|------|-------------------|
| `clamp` | 力矩/电压饱和 |
| `step_size` | 仿真 `dt` |
| `greet` | 纯语法示例 |

### ex03_lists_dicts.py

| 段 | 在后续项目中的角色 |
|----|-------------------|
| `angles_deg` | 传感器采样序列（将来是数组） |
| `params` | `model.py` 参数字典 |
| `zip(times, values)` | 画图前整理数据 |

---

## 1.19 渐进式综合练习（像作业一样做）

### 第 1 组：热身 ⭐

1. REPL 计算 `(1 + 0.1) ** 10`。  
2. 写 `if` 判断 `abs(theta) < 0.01` 打印「近似直立」。  
3. `for` 打印 0..4 的平方。

### 第 2 组：函数 ⭐

1. 实现 `euler_decay(y, tau, dt)`：`y_new = y + dt * (-y/tau)`。  
2. 从 `y0=1.0` 循环 20 次，`tau=0.5, dt=0.05`，打印最终 `y`。  
3. 用 `clamp` 限制 `u` 在 `[-5,5]`。

### 第 3 组：数据 🔶

1. `params` 字典存 `m, L, g`，函数 `gravity_pendulum_accel(theta)` 返回 `-g/L*sin(theta)` 的**小角度近似** `-g/L*theta`（先用近似）。  
2. 用列表存 10 步 `theta`，每步用上述加速度 + 朴素欧拉更新（预习 T03）。

### 第 4 组：类与对象 ⭐

1. 完成 §1.14.8 练习 A、B、C。  
2. 用 `PID` + `FirstOrderSystem` 跑 50 步闭环（需按 [T01b](T01b-类与对象入门.md) 把 `u` 接入 plant，或自己改 `step`）。  
3. 在笔记里写 3 行：`class` 相比「函数+全局变量」的好处。

### 第 5 组：小项目 🔶

新建 `weeks/week01/my_week1_mini_sim.py`（可不提交）：

- 状态 `theta, theta_dot`  
- 参数 `g/L=20`, `dt=0.01`, 共 200 步  
- 每步：`theta_dot += dt * (-20*theta)`，`theta += dt * theta_dot`  
- 每 50 步 `print` 一次  
- 对照：这是极简谐振子欧拉法，会**发散或漂**——T03 会解释为什么需要更小 `dt` 或 RK4

---

## 1.20 自测清单（章末）

能 **口头或笔头** 回答即过关：

1. `range(1,6)` 包含哪些整数？  
2. `clamp(15,-10,10)` 等于多少？为什么控制需要它？  
3. list 和 dict 分别适合存什么？  
4. 为什么 `0.1+0.2==0.3` 可能为 False？  
5. `if __name__ == "__main__"` 解决什么问题？  
6. `__init__` 何时调用？`self` 是什么？  
7. 为什么仿真循环里不要每步 `PID(...)` 新建对象？

---

## 必做（打卡用）

- [ ] 通读本章并完成 **所有标 ⭐ 的练习**（至少 10 处）。  
- [ ] 运行并修改 `ex01`–`ex03`，每文件至少改 1 处变量并预测输出。  
- [ ] 完成 **第 1、2、4 组**综合练习（含 §1.14 类与对象）。  
- [ ] 在当周 checklist 写一句：你今天独立写出的一段代码是什么。

## 选做

- [ ] Python 官方教程第 3–5 章通读 + 每章 3 个 REPL 实验。  
- [ ] 完成第 3、4 组综合练习。  
- [ ] 把 `ex01` 里所有 `print` 改成 f-string。

---

**上一章**：[T00](T00-导读与环境.md) · **下一章**：[T02 · NumPy 与 Matplotlib](T02-NumPy与Matplotlib.md)
