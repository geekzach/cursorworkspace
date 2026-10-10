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
