# 02 NumPy / Matplotlib · 参考思路

## 必做 2（τ 与 63%）

一阶系统约在 \(t=\tau\) 时输出达到 \(0.632 \times K\)（对 \(K=1\) 即约 0.632）。  
τ=0.2 时更快接近稳态；τ=1.0 更慢。

## 必做 3（sin 曲线）

```python
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 100)
plt.plot(theta, np.sin(theta))
plt.xlabel("theta (rad)")
plt.ylabel("sin(theta)")
plt.grid(True, alpha=0.3)
plt.savefig("my_sin.png", dpi=120)
```

## 选做 2（随机数）

`rng.uniform(-1, 1, size=5)` 每次不同；`np.mean` 应接近 0 量级，`np.std` 约 0.3–0.6（仅 5 个点波动大）。
