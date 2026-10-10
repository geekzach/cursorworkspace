# 01 Python 基础 · 参考思路

## 必做 2（clamp -20）

`clamp(-20, -10, 10)` → **-10.0**（下限饱和）。

## 必做 3（平方列表）

核心结构：

```python
nums = [1, 2, 3, 4, 5]
for n in nums:
    print(n * n)
```

或推导式：`print([n*n for n in nums])`。

## 选做 1（deg_to_rad）

```python
import math

def deg_to_rad(deg: float) -> float:
    return deg * math.pi / 180.0
```

`deg_to_rad(30)` ≈ **0.523599**。

## 选做 2（默认参数）

仿真常固定默认 `dt=0.01`；调试稳定性时可传更小 `dt` 而不改所有调用点。

---

## T01b 加练（闭环 50 步）

- **积分项**：`PID` 在 `for` 循环**外**创建一次；调参前调用 `reset()`，避免积分带着旧轨迹。  
- **一阶 plant**：`dy = (setpoint - y) / tau + ku * u`；`ku=0` 时只有开环趋近，闭环才靠 `u`。  
- **验收**：`Ki=0` 时稳态 `y` 往往 **仍低于** `r`（比例控制有余差）；适当加 `Ki` 可消余差。完整骨架见 [T01b](../T01b-类与对象入门.md) §B.4 `run_closed_loop`。
