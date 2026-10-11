"""
仿真结果可视化（状态曲线、相平面、动画等）。
"""

from __future__ import annotations

import matplotlib.pyplot as plt


def configure_matplotlib_chinese() -> None:
    """
    Windows 下中文轴标签不乱码；Linux/WSL 无微软雅黑时会回退到 SimHei 等。
    绘图前调用一次即可。
    """
    plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False


def placeholder_plotting_doc() -> None:
    """占位：提醒此处将实现绘图工具，当前无实现。"""
    raise NotImplementedError("绘图模块尚未实现。")
